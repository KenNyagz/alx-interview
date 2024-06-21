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


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 9:
            continue
        # 222.66.161.46 - [2024-06-21 20:08:45.501464] "GET /projects/260 HTTP/1.1" 404 530
        ip, dash, date, time, method, path, protocol, status, size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8]
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
        #print(f'{status}: {size}')

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
