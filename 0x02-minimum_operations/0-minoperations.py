#!/usr/bin/python3
'''
Finds the minimum number of operations needed to achive a certain outcome
'''


def minOperations(n):
    ''' Calculates minimum number of tasks needed to achieve a result'''
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
