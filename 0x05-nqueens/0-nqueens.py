#!/usr/bin/python3
'''
solving the nqueens problem using recurstion and backtracking
'''
import sys


def is_safe(board, row, col, n):
    '''Checks diagonals and columns are free of other queens'''
    # Check if theres is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row,n , solutions):
    '''core function that recursively looks for solutions and accmults them'''
    if row == n:      #  Base case
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, row, i, n):
            board[row][i] = 1
            solve_nqueens(board, row + 1, n, solutions)
            board[row][i] = 0
              

def nQueens(n):
    '''Sets up board, invokes core function solve_nqueens,returns all solns'''
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    return solutions


def print_solutions(solutions):
    '''lists all possibilities with all queens' positions in each as 2D Lst'''
    for solution in solutions:
        print(solution)

def main():
    '''Entry point for program'''
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

    solutions = nQueens(n)
    print_solutions(solutions)


if __name__ == '__main__':
    main()

