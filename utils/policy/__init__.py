from ._random import random_policy
from ._monte_carlo import monte_carlo_policy
from ._td0 import TD0_policy
from ._gpro import gpro_policy

default_policy_pool = dict(
    random = lambda env:random_policy(env),
    montecarlo = lambda env:monte_carlo_policy(
        env,
        num_episodes=120,
        max_steps=192,
        insert_bias=0.8,
    ),
    grpo = lambda env:gpro_policy(
        env,
        iterations=10,
        group_size=12,
        max_steps=192,
    ),
    td0 = lambda env:TD0_policy(
        env,
        num_episodes=200,
        alpha=0.3,
        gamma=0.9,
        epsilon=0.1
    )
)