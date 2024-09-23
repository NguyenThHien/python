import math
def check(n):
   
    s = n[::-1]
    for i in range(1, len(n)):
        diff_s1 = abs(ord(n[i]) - ord(n[i - 1]))
        diff_s2 = abs(ord(s[i]) - ord(s[i - 1]))
        
        
        if diff_s1 != diff_s2:
            return "NO"
    
    return "YES"

        
T = int(input())
for _ in range(T):
    n = str(input())
    print(check(n))
