from itertools import product
from argparse import ArgumentParser

DEFAULT_CONFIG = {
    "LENGTH": 8,
    "CHARSET": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    "OUTPUT": "wordlist.txt"
}

parser = ArgumentParser(description="Generates a wordlist based on the given configuration.")
parser.add_argument("-l", "--length", type=int, help="The length of the words to generate.")
parser.add_argument("-c", "--charset", type=str, help="The charset to use for the words.")
parser.add_argument("-o", "--output", type=str, help="The output file to write the wordlist to.")


def main():
    """
    The main function.
    """
    # Parse the arguments
    args = parser.parse_args()

    # Generate the configuration
    config = DEFAULT_CONFIG
    if args.length:
        config["LENGTH"] = args.length
    if args.charset:
        config["CHARSET"] = args.charset
    if args.output:
        config["OUTPUT"] = args.output

    # Generate the wordlist
    generate_wordlist(config)


def generate_wordlist(config):
    """
    Generates a wordlist based on the given configuration.
    """
    # Generate all possible combinations of the given length
    combinations = product(config["CHARSET"], repeat=config["LENGTH"])

    # Write all combinations to the output file
    with open(config["OUTPUT"], "w") as file:
        for combination in combinations:
            file.write("".join(combination) + "\n")


if __name__ == "__main__":
    main()
