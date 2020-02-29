'''Steps
1. Input
2. Check if number is even/odd
3. Find nearest prime numbers
4. Output

'''

import math
from functools import lru_cache

@lru_cache(maxsize = 1000)

def isPrime(n):
    maxNum = math.ceil(n ** 0.5) + 2
    if n == 3: return True
    for x in range(3, maxNum, 2):
        if not n % x: return False 
    return True

#Input
t = int(input())
nums = [int(input()) for x in range(t)]

output = []

for num in nums:
    for x in range(3, num, 2):
        num2 = num + (num - x)
        if isPrime(x) and isPrime(num2):
            output.append((x, num2))
            break
    
for x in output:
    print(x[0], x[1])
        
    
        
        