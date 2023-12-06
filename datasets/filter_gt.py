import re
import string
import argparse

def filter_gt(args):

    batch_max_length = 25
    character  = string.printable[:-6] #'0123456789abcdefghijklmnopqrstuvwxyz'
    out_of_char = f'[^{character}]'
    filtered_gt = open(f'{args.out}/filtered_gt.txt', 'w')
    with open(f'{args.path_to_gt}', 'r') as f:
        lines = f.readlines()
        words = [line.strip().split(' ',1)[1] for line in lines]
        image_names = [line.strip().split(' ',1)[0] for line in lines]

        for image_name, word in zip(image_names, words):

            if re.search(out_of_char, word.lower()) is not None:
                print(word)

            if not len(word) > batch_max_length and re.search(out_of_char, word.lower()) is None:
                filtered_gt.write(f'{image_name} {word}\n')

    filtered_gt.close()

def parse_args():
    parser = argparse.ArgumentParser(description="Argument parser")

    parser.add_argument(
        "--path_to_gt",
        required=True,
        help="Path to gt.txt.")

    parser.add_argument(
        "--out",
        required=True,
        help="Prefix of the directory to contain output.")

    parser.add_argument(
        "--verbose",
        type=int,
        default=0,
        required=False,
        help="Print debug info. 0 - important messages only, 1 - more details, Default: 0.")

    args = parser.parse_args()
    if args.verbose >= 1:
        print(f"Parsed arguments: {args}")

    return args

if __name__ == '__main__':
    args = parse_args()
    filter_gt(args)
