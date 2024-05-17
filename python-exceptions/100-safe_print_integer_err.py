#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as error:
        sys.stderr = error
        print("Exception: {}".format(sys.stderr))
        return False
