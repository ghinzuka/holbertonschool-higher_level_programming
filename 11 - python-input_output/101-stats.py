#!/usr/bin/python3
import sys


def print_stats(file_size, status_counts):
    """
    Prints the file size and status counts.

    Args:
            file_size (int): The size of the file.
            status_counts (dict): A dictionary containing the status counts.

    Returns:
            None
    """
    print("File size: {}".format(file_size))
    for status in sorted(status_counts.keys()):
        print("{}: {}".format(status, status_counts[status]))


file_size = 0
status_counts = {}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 9:
            continue
        size = int(parts[-1])
        status_code = parts[-2]

        file_size += size
        if status_code not in status_counts:
            status_counts[status_code] = 0
        status_counts[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats(file_size, status_counts)

except KeyboardInterrupt:
    print_stats(file_size, status_counts)
    raise
