from auction import Auction
from argparse import ArgumentParser


def run(cases):
    print(f"Cases to run: {cases}")
    auc = Auction()


def parse_args():
    parser = ArgumentParser(
        description='Script to run the experiment. Provide a list of integers for cases, or leave empty to run all cases.')
    parser.add_argument('cases', nargs='*', type=int, default=None,
                        help='List of integers representing cases to run. If left empty, all cases will run.')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    # If no cases are provided, we can define a default behavior (e.g., run all cases)
    if args.cases is None or len(args.cases) == 0:
        print("No cases provided. Running all cases by default.")
        # Example: Replace with actual default cases
        all_cases = [1, 2, 3]
        run(all_cases)
    else:
        run(args.cases)


if __name__ == "__main__":
    main()
