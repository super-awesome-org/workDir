"""Console script for workDir"""
import argparse
import sys


def main():
    """Console script for python_boilerplate."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()
    print("Arguments: " + str(args._))
    return 0


if __name__ == "__main__":
    sys.exit(main())
