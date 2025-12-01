def random_policy(env, **kwargs):
    obs, info = env.reset()
    done = False
    total_reward = 0.0
    while not done:
        action_type = env.np_random.integers(0, 4)
        op_id = env.np_random.integers(0, 5)
        value_id = env.np_random.integers(0, 3)
        mask = obs["var_mask"]
        choices = [i for i, m in enumerate(mask) if m == 1]
        var_idx = int(env.np_random.choice(choices)) if choices else 0
        obs, reward, terminated, truncated, info = env.step((action_type, op_id, var_idx, value_id))
        total_reward += reward
        done = terminated or truncated
    return env.cf