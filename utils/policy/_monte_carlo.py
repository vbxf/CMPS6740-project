from typing import Dict, Tuple
from utils import ProgramDataset

def monte_carlo_policy(
    env,
    num_episodes: int = 200,
    max_steps: int = 256,
    insert_bias: float = 0.75,
    **kwargs
) -> Tuple[float, Dict[str, object] | None]:
    best_reward = float("-inf")
    best_episode = None
    for rollout_idx in range(num_episodes):
        obs, info = env.reset()
        total_reward = 0.0
        terminated = False
        truncated = False
        actions = []
        steps = 0
        while not (terminated or truncated) and steps < max_steps:
            mask = obs["var_mask"]
            viable_vars = [i for i, flag in enumerate(mask) if flag == 1]
            
            if env.np_random.random() < insert_bias:
                options = [2, 3]
                if obs["inserts_left"] > 0 and viable_vars:
                    options.append(1)
                action_type = int(env.np_random.choice(options))
            else: action_type = 0

            op_id = int(env.np_random.integers(0, len(env._ops)))
            value_id = int(env.np_random.integers(0, len(env._value_candidates)))
            if not viable_vars:
                if action_type == 1: action_type = 0
                var_idx = 0
            else:
                var_idx = int(env.np_random.choice(viable_vars))
            
            action = (action_type, op_id, var_idx, value_id)
            actions.append(action)
            obs, reward, terminated, truncated, info = env.step(action)
            total_reward += reward
            steps += 1
            if info.get("error"): break
        if total_reward > best_reward:
            best_reward = total_reward
            best_episode = {
                "reward": total_reward,
                "actions": list(actions),
                "code": list(env.cf.main_code_lines),
                "result": env.cf.result,
                "error": info.get("error"),
                "codeframe": env.cf
            }
    return best_episode['codeframe']
