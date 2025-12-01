import numpy as np
from typing import Dict, Tuple

class GRPOAgent:
    def __init__(self, env, learning_rate=0.1):
        self.env = env
        self.lr = learning_rate
        
        self.theta_action_type = np.zeros(4)
        self.theta_op = np.zeros(5)
        self.theta_var = np.zeros(64)
        self.theta_value = np.zeros(2)
        
    def get_action_probs(self, obs):
        p_action_type = self.softmax(self.theta_action_type)
        p_op = self.softmax(self.theta_op)
        mask = obs["var_mask"]
        masked_logits = np.where(mask == 1, self.theta_var, -1e9)
        p_var = self.softmax(masked_logits)
        p_value = self.softmax(self.theta_value)
        
        return p_action_type, p_op, p_var, p_value

    def softmax(self, x):
        e_x = np.exp(x - np.max(x))
        return e_x / (e_x.sum() + 1e-10)

    def sample_action(self, obs):
        p_action_type, p_op, p_var, p_value = self.get_action_probs(obs)
        
        a_action_type = np.random.choice(len(p_action_type), p=p_action_type)
        a_op = np.random.choice(len(p_op), p=p_op)
        a_var = np.random.choice(len(p_var), p=p_var)
        a_value = np.random.choice(len(p_value), p=p_value)
        
        return (a_action_type, a_op, a_var, a_value), (p_action_type, p_op, p_var, p_value)

    def update(self, rollouts):
        
        rewards = np.array([r for r, _ in rollouts])
        mean_r = np.mean(rewards)
        std_r = np.std(rewards) + 1e-8
        advantages = (rewards - mean_r) / std_r
        
        grad_action_type = np.zeros_like(self.theta_action_type)
        grad_op = np.zeros_like(self.theta_op)
        grad_var = np.zeros_like(self.theta_var)
        grad_value = np.zeros_like(self.theta_value)
        
        for idx, (r, traj) in enumerate(rollouts):
            adv = advantages[idx]
            for obs, action, probs in traj:
                a_action_type, a_op, a_var, a_value = action
                p_action_type, p_op, p_var, p_value = probs
                
                d_action_type = -p_action_type
                d_action_type[a_action_type] += 1
                grad_action_type += d_action_type * adv
                
                d_op = -p_op
                d_op[a_op] += 1
                grad_op += d_op * adv
                
                d_var = -p_var
                d_var[a_var] += 1
                grad_var += d_var * adv
                
                d_value = -p_value
                d_value[a_value] += 1
                grad_value += d_value * adv
                
        N = len(rollouts)
        self.theta_action_type += self.lr * grad_action_type / N
        self.theta_op += self.lr * grad_op / N
        self.theta_var += self.lr * grad_var / N
        self.theta_value += self.lr * grad_value / N

def gpro_policy(
    env,
    iterations: int = 10,
    group_size: int = 10,
    max_steps: int = 256,
) -> Tuple[float, Dict[str, object] | None]:
    agent = GRPOAgent(env)
    
    best_reward = float("-inf")
    best_episode = None
    
    for _ in range(iterations):
        rollouts = []
        for g in range(group_size):
            obs, info = env.reset()
            terminated, truncated, total_reward, trajectory, steps = False, False, 0.0, [], 0
            
            while not (terminated or truncated) and steps < max_steps:
                action, probs = agent.sample_action(obs)
                next_obs, reward, terminated, truncated, info = env.step(action)
                
                trajectory.append((obs, action, probs))
                total_reward += reward
                obs = next_obs
                steps += 1
                if info.get("error"): break
            
            rollouts.append((total_reward, trajectory))
            
            if total_reward > best_reward:
                best_reward = total_reward
                best_episode = {
                    "reward": total_reward,
                    "actions": [x[1] for x in trajectory],
                    "code": list(env.cf.main_code_lines),
                    "result": env.cf.result,
                    "error": info.get("error"),
                    "codeframe": env.cf
                }
        
        agent.update(rollouts)
        
    return best_episode['codeframe']