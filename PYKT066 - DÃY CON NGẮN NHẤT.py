import math
from sys import stdin, stdout

def find_smallest_subarray_with_gcd_k(a, k):

    
    min_length = 1001
    
    for start in range(n):
        current_gcd = 0
        for end in range(start, n):
            current_gcd = math.gcd(current_gcd, a[end])
            if current_gcd == k:  # Since elements are already divided by `k`, we need GCD to be 1
                min_length = min(min_length, end - start + 1)
                
    
    return min_length if min_length != 1001 else -1

# Reading input and executing the function for multiple test cases
input = stdin.read
data = input().split()

index = 0
T = int(data[index])
index += 1
results = []

for _ in range(T):
    n = int(data[index])
    k = int(data[index + 1])
    index += 2
    a = list(map(int, data[index:index + n]))
    index += n
    
    result = find_smallest_subarray_with_gcd_k(a, k)
    results.append(result)

for i in results:
    print(i)