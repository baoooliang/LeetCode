from collections import deque

primes = set()
for a in range(2, 1000):
    if all(a % p != 0 for p in primes):
        primes.add(a)

def split_primes(input_str: str) -> int:
    def is_prime(string):
        return not string.startswith('0') and int(string) in primes
    
    def check_all_primes(breakpoints):
        prev = 0
        for i in breakpoints:
            if not is_prime(input_str[prev:i+1]):
                return False
            prev = i+1
        return is_prime(input_str[prev:len(input_str)])
    
    def helper(i, breakpoints):
        if i >= len(input_str) - 1:
            if check_all_primes(breakpoints):
                return 1
            return 0
        breakpoints += [i]
        v1 = helper(i+1,breakpoints)
        breakpoints.pop()
        v2 = helper(i+1,breakpoints)
        return v1 + v2
    
    return helper(0, [])