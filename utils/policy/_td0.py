import numpy as np
from collections import defaultdict

def encode_state(obs):
    return (int(obs["line_index"]), int(obs["inserts_left"]), tuple(int(x) for x in obs["var_mask"]))
    
def encode_action(action, num_ops, num_vars, num_values):
    # action: (action_type, op_id, var_idx, value_id)
    # action_type range: [0, 3] (Next, Insert, Delete, Edit)
    action_type, op_id, var_idx, value_id = action
    return (action_type * num_ops * num_vars * num_values + 
            op_id * num_vars * num_values + 
            var_idx * num_values + 
            value_id)

def decode_action(a_int, num_ops, num_vars, num_values):
    size_v = num_values
    size_var = num_vars * size_v
    size_op = num_ops * size_var
    
    action_type = a_int // size_op
    a_int %= size_op
    
    op_id = a_int // size_var
    a_int %= size_var
    
    var_idx = a_int // size_v
    value_id = a_int % size_v
    
    return (action_type, op_id, var_idx, value_id)

def TD0_policy(
    env,
    num_episodes: int = 200,
    alpha: float = 0.3,
    gamma: float = 0.9,
    epsilon: float = 0.1,
    **kwargs
):
    num_ops = len(env._ops)
    num_values = len(env._value_candidates)
    # Action space size: 4 types * num_ops * 64 vars * num_values
    Q = defaultdict(lambda: np.zeros(4 * num_ops * 64 * num_values))
    
    last_episode_actions = 0
    
    for episode in range(num_episodes):
        obs, info = env.reset()
        state = encode_state(obs)
        done = False
        
        while not done:
            num_vars = len(obs["var_mask"])
            num_actions = 4 * num_ops * num_vars * num_values
            
            if np.random.rand() < epsilon:
                a_int = np.random.randint(num_actions)
            else:
                a_int = np.argmax(Q[state][:num_actions])
            
            action = decode_action(a_int, num_ops, num_vars, num_values)
            
            next_obs, reward, terminated, truncated, info = env.step(action)
            next_state = encode_state(next_obs)
            next_num_vars = len(next_obs["var_mask"])
            next_actions = 4 * num_ops * next_num_vars * num_values
            
            td_target = reward + gamma * np.max(Q[next_state][:next_actions])
            td_error = td_target - Q[state][a_int]
            Q[state][a_int] += alpha * td_error
            
            obs = next_obs
            state = next_state
            done = terminated or truncated
        
        if episode == num_episodes - 1:
            # Count all valid actions (Insert, Edit, Delete)
            last_episode_actions = env._inserts_done + env._edits_done + sum(env._deleted_lines)
            
    return env.cf