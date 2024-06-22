#!/usr/bin/python3
'''
Script that parses though an input simulating logs and processes the data
'''
import sys
import signal

total_size = 0
status_counts = {
                 200: 0,
                 301: 0,
                 400: 0,
                 401: 0,
                 403: 0,
                 404: 0,
                 405: 0,
                 500: 0
                }
line_count = 0


def print_stats():
    '''Prints collected statistics'''
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f'{status}: {status_counts[status]}')


def signal_handler(sig, frame):
    '''Handles keyboard interrupt signal'''
    print_stats()
    sys.exit(0)


def main():
    '''Entry point function calling the others'''
    global total_size, line_count
    signal.signal(signal.SIGINT, signal_handler)
    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) != 9:
                continue

            method = parts[4]
            status, size = parts[-2], parts[-1]
            if method != '"GET':
               continue
            try:
                status = int(status)
                size = int(size)
            except ValueError:
                continue

            if status in status_counts:
                status_counts[status] += 1
            total_size += size
            line_count += 1

            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)

    print_stats()


if __name__ == "__main__":
    main()
