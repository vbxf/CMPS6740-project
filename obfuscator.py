from utils import ProgramDataset, ObfuscatorEnv
from utils.policy import default_policy_pool
import argparse

def print_code_block(codeframe, title='Original Code'):
    print(title)
    print("===================================================")
    print("\n".join(codeframe.main_code_lines))
    print("===================================================")
    print(f"Result: {codeframe.true_result}")
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Python Obfuscator")
    parser.add_argument(
        "dataset",
        type=str,
        default="./dataset",
        help="The sample ID of the dataset.",
    )
    parser.add_argument(
        "sample_id",
        type=int,
        default=0,
        help="The path to the code dataset."
    )
    parser.add_argument(
        "policy",
        choices=[
            "montecarlo",
            "random",
            "gpro",
            "td0"
        ],
        default="montecarlo",
        help="The policy name for obfuscator."
    )
    parser.add_argument(
        "max_edits",
        type=int,
        default=4,
        help="The maximum number of modifications."
    )
    args = parser.parse_args()

    policy = default_policy_pool[args.policy]
    pd_dataset = ProgramDataset(args.dataset)
    codeframe = pd_dataset[args.sample_id].codeframe
    env = ObfuscatorEnv(codeframe, max_insert_num=args.max_edits)

    print_code_block(codeframe, 'Original Code')
    print(f"Running {args.policy} Policy...")
    modified_cf = policy(env)
    if modified_cf.result is None:
        modified_cf.run()
    print_code_block(modified_cf, 'Obfuscated Code')
    