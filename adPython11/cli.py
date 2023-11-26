"""Console script for adPython11."""
import argparse
import sys

import fancydata
import fancyfunction


def display_fancy_data() -> None:
    """Display fancy data."""
    fancydata.print_a_named_tuple()
    fancydata.compare_stack_and_queue()


def display_fancy_function() -> None:
    """Display fancy function."""
    fancyfunction.show_location("China", "Beijing")


def main():
    """Console script for adPython11."""
    parser = argparse.ArgumentParser()
    parser.add_argument("_", nargs="*")
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("hello, python world")

    display_fancy_data()
    display_fancy_function()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
