#!/usr/bin/python3
'''
sadsd asdasd
'''

def isWinner(x, nums):
    '''adda adasda''' 
    # Function to generate primes up to max_n using Sieve of Eratosthenes
    def sieve_of_eratosthenes(max_n):
        is_prime = [True] * (max_n + 1)
        p = 2
        while p * p <= max_n:
            if is_prime[p]:
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = []
        for p in range(2, max_n + 1):
            if is_prime[p]:
                primes.append(p)
        return primes
    
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        # Track which numbers are still available
        available = [True] * (n + 1)
        current_player = 0  # 0 for Maria, 1 for Ben
        prime_index = 0
        
        while prime_index < len(primes) and primes[prime_index] <= n:
            prime = primes[prime_index]
            if available[prime]:
                # Remove the prime and its multiples
                for multiple in range(prime, n + 1, prime):
                    available[multiple] = False
                # Switch player
                current_player = 1 - current_player
            prime_index += 1
        
        if current_player == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

