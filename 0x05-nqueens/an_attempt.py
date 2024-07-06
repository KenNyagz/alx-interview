#!/usr/bin/python3
'''
solving the nqueens problem using recurstion
'''
import sys


def is_safe(board, row, col, n):
    '''function one'''
    for c in range(col, -1, -1):
        if board[row][c] == 1:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][i] == 1:
            return False
        i += 1
        j -= 1
    return True


def nQueens(board, col, n):
    '''Function two'''
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if nQueens(board,  col + 1, n):
                return True
            board[i][col] = 0
    return False


def main():
    '''main fn'''
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("ValueError: Please enter a number")
        sys.exit(1)
    if n < 4 :
        print("n must be an integer greater than 4")
        sys.exit(1)

    board = [[0 for j in range(n)] for i in range(n)]
    if nQueens(board, 0, n) == True:
        combns = []
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=' ')
            print()
    else:
        print('error')



if __name__ == '__main__':
    main()

