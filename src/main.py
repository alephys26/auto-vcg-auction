from auction import Auction
from argparse import ArgumentParser


def run(cases):
    auc = Auction()
    for case in cases:
        i, t = int(case[0]), case[1]
        print(f"Running Case: {i}, Auction Type: {t}")
        auc.run(i, t)


def parse_args():
    parser = ArgumentParser(
        description='Script to run the experiment. Provide a list of integer-string pairs for cases, or leave empty to run all cases.')
    parser.add_argument('cases', nargs='*', type=str, default=None,
                        help='List of cases to run. If left empty, all default cases will run.')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.cases is None or len(args.cases) == 0:
        print("No cases provided. Running all cases by default.")
        all_cases = [f'{i}v' for i in range(1,10)]+[f'{i}s' for i in range(1,10)]
        run(all_cases)
    else:
        run(args.cases)


if __name__ == "__main__":
    main()
