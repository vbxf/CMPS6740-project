import ast
import random
import numpy as np
import gymnasium as gym
from gymnasium import spaces
from copy import deepcopy
from typing import (
    Dict, Optional, Tuple
)

from .base import CodeFrame
from ._ast_t import MutationVisitor

class ObfuscatorEnv(gym.Env):
    metadata = {"render.modes": ["human"]}
    _seed = None

    def __init__(
        self,
        code_frame: CodeFrame,
        max_insert_num: int = 1,
        max_lines_cap: int = 16,
        max_vars_cap: int = 8,
        code_window_cap: int = 512,
        invalid_penalty: float = 5.0,
    ) -> None:
        super().__init__()
        
        self.max_insert_num = int(max(1, max_insert_num))
        self.max_lines_cap = int(max(16, max_lines_cap))
        self.max_vars_cap = int(max(8, max_vars_cap))
        self.code_window_cap = int(max(512, code_window_cap))
        self.invalid_penalty = float(max(0.0, invalid_penalty))
        self._orig_serialized = deepcopy(code_frame.serialized_code)
        
        

        self._ops = ["+=", "-=", "*=", "/=", "**="]
        self._value_candidates = [random.randint(0, 10), random.randint(0, 10)]

        self.action_space = spaces.MultiDiscrete([4, len(self._ops), self.max_vars_cap, len(self._value_candidates)])
        self.observation_space = spaces.Dict(
            {
                "line_index": spaces.Discrete(self.max_lines_cap + 1),
                "inserts_left": spaces.Discrete(self.max_insert_num + 1),
                "var_mask": spaces.MultiBinary(self.max_vars_cap),
                "var_values": spaces.Box(low=-np.inf, high=np.inf, shape=(self.max_vars_cap,), dtype=np.float32),
                "code_window": spaces.Text(self.code_window_cap),
            }
        )
        
        self._reset_environment()
        self._reset_random_seed()
        self._reset_episode_state()
        
    def _reset_episode_state(self) -> None:
        self._orig_len = len(self.cf.main_code_lines)
        self._orig_ptr = 0
        self._inserts_done = 0
        self._edits_done = 0
        self._inserted_before_line = [0] * self._orig_len
        self._deleted_lines = [0] * self._orig_len
        self._last_error = None
        
    def _reset_environment(self) -> None:
        self.cf = CodeFrame(deepcopy(self._orig_serialized))
        self._true_result = self.cf.true_result
        self._true_vars = deepcopy(self.cf.true_vars)
        self._baseline_var_names = sorted(list(self._true_vars.keys()))[: self.max_vars_cap]
        
    def _reset_random_seed(self) -> None:
        self.np_random, _ = gym.utils.seeding.np_random(self._seed)
        
    def reset(self):
        self._reset_random_seed()
        self._reset_environment()
        self._reset_episode_state()

        obs = self._make_observation()
        info = {"error": None}
        return obs, info
    
    def _var_name_from_index(self, idx: int) -> Optional[str]:
        if 0 <= idx < len(self._baseline_var_names):
            return self._baseline_var_names[idx]
        return None
    
    def _build_invalid_return(
        self,
        info:dict,
        err:str,
        prev_lines:list[str],
    ):
        self.cf.main_code_lines = prev_lines
        self._last_error = err
        info["error"] = err
        return self._make_observation(), -10.0, True, False, info
    
    def _action_insert(
        self,
        current_index: int,
        prev_lines: list[str],
        info: dict,
        op_id: int,
        value_id: int,
        var_name: Optional[str],
    ) -> None:
        if var_name is None:
            return self._build_invalid_return(info, "Invalid var_index", prev_lines)
        op = self._ops[op_id]
        value_candidate = self._value_candidates[value_id]
        value = str(value_candidate)
        snippet = f"{var_name} {op} {value}"
        self.cf.main_code_lines.insert(current_index, snippet)
        valid, err = self._check_executable()
        if not valid:
            return self._build_invalid_return(info, err, prev_lines)
        self._inserts_done += 1
        self._inserted_before_line[self._orig_ptr] += 1
        self._orig_ptr += 1
        
    def _action_delete(
        self,
        current_index: int,
        prev_lines: list[str],
        info: dict,
    ):
        if 0 <= current_index < len(self.cf.main_code_lines):
            del self.cf.main_code_lines[current_index]
            valid, err = self._check_executable()
            if not valid:
                return self._build_invalid_return(info, err, prev_lines)
            self._deleted_lines[self._orig_ptr] = 1
            self._orig_ptr += 1
        else:
            self._orig_ptr += 1
    
    def _apply_ast_edit(
        self,
        code: str,
        op_id: int,
        var_name: Optional[str],
        value_id: int
    ) -> str:
        try:
            tree = ast.parse(code)
            op_str = self._ops[op_id]
            value_str = str(self._value_candidates[value_id])
            visitor = MutationVisitor(op_str, var_name, value_str)
            new_tree = visitor.visit(tree)
            if visitor.mutated: return ast.unparse(new_tree)
            return code
        except: return code
        
    def _action_edit(
        self,
        current_index: int,
        prev_lines: list[str],
        info: dict,
        op_id: int,
        value_id: int,
        var_name: Optional[str],
    ) -> None:
        if 0 <= current_index < len(self.cf.main_code_lines):
            line_code = self.cf.main_code_lines[current_index]
            new_code = self._apply_ast_edit(line_code, op_id, var_name, value_id)
            if new_code != line_code:
                self.cf.main_code_lines[current_index] = new_code
                valid, err = self._check_executable()
                if not valid:
                    return self._build_invalid_return(info, err, prev_lines)
                self._edits_done += 1
            self._orig_ptr += 1
        else:
            self._orig_ptr += 1

    def step(self, action: Tuple[int, int, int, int]):
        if self._orig_ptr >= self._orig_len:
            total_changes = self._inserts_done + self._edits_done + sum(self._deleted_lines)
            if total_changes == 0: self._orig_ptr = self._orig_len - 1
            else: return self._make_observation(), 0.0, True, False, {"error": None}

        action_type, op_id, var_idx, value_id = (int(a) for a in action)
        terminated, truncated, reward = False, False, 0.0
        info = {"error": None}
        op_id = max(0, min(op_id, len(self._ops) - 1))
        value_id = max(0, min(value_id, len(self._value_candidates) - 1))
        var_name = self._var_name_from_index(var_idx)
        
        current_index = \
            self._orig_ptr + \
            sum(self._inserted_before_line[: self._orig_ptr]) - \
            sum(self._deleted_lines[: self._orig_ptr])
        prev_lines = list(self.cf.main_code_lines)

        if action_type == 1 and self._inserts_done < self.max_insert_num:
            err = self._action_insert(current_index, prev_lines, info, op_id, value_id, var_name)
            if err is not None: return err
        elif action_type == 2:
            err = self._action_delete(current_index, prev_lines, info)
            if err is not None: return err
        elif action_type == 3:
            err = self._action_edit(current_index, prev_lines, info, op_id, value_id, var_name)
            if err is not None: return err
        else: self._orig_ptr += 1

        total_changes = self._inserts_done + self._edits_done + sum(self._deleted_lines)
        terminated = (self._orig_ptr >= self._orig_len) and (total_changes > 0)

        if terminated: reward = self._calculate_final_reward()
        obs = self._make_observation()
        return obs, reward, terminated, truncated, info

    def render(self):
        print("===== Current main code =====")
        print("\n".join(self.cf.main_code_lines))
        print("=============================")

    def close(self):
        pass

    def _make_observation(self) -> Dict[str, object]:
        code_text = "".join(self.cf.main_code_lines)
        if len(code_text) > self.code_window_cap:
            code_text = code_text[: self.code_window_cap]
        var_mask, var_values = self._var_info_at_current_position()
        return {
            "line_index": min(self._orig_ptr, self.max_lines_cap),
            "inserts_left": max(0, self.max_insert_num - self._inserts_done),
            "var_mask": var_mask,
            "var_values": var_values,
            "code_window": code_text,
        }

    def _var_info_at_current_position(self):
        mask = [0] * self.max_vars_cap
        values = np.zeros(self.max_vars_cap, dtype=np.float32)

        current_index = self._orig_ptr + sum(self._inserted_before_line[: self._orig_ptr]) - sum(self._deleted_lines[: self._orig_ptr])
        
        try:
            tmp = CodeFrame(self.cf.main_code_lines)
            tmp.reset()
            if current_index > 0:
                tmp.run()
            current_vars = tmp.vars
        except: current_vars = {}
        for i, name in enumerate(self._baseline_var_names):
            if i >= self.max_vars_cap: break
            if name in current_vars:
                mask[i] = 1
                val = current_vars[name]
                try: values[i] = float(val)
                except: values[i] = 0.0
            else:
                mask[i] = 0
                values[i] = 0.0
        return mask, values

    def _check_executable(self) -> Tuple[bool, Optional[str]]:
        try:
            self.cf.run()
            return True, None
        except Exception as e:
            return False, f"Execution error after insertion: {e}"

    def _calculate_final_reward(self) -> float:
        reward = 0.0
        total_changes = self._inserts_done + self._edits_done + sum(self._deleted_lines)
        reward += float(total_changes)
        try:
            output_changed = (self.cf.result != self._true_result)
            if output_changed: reward += -10.0
        except: reward += -10.0
        return reward

    @staticmethod
    def _same_visible_vars(
        now: Dict[str, object],
        baseline: Dict[str, object]
    ) -> bool:
        if set(now.keys()) != set(baseline.keys()):
            return False
        for k in baseline.keys():
            if now[k] != baseline[k]: return False
        return True
