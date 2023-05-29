#!/usr/bin/python3

def safe_print_integer(value):
    """Print an int
    Args:
        value (int): int to print
    Returns:
        true if not value or type error
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
