import re

for _ in range(int(input())):
    s = input()
    
    res = re.findall(r'\d+', s)
    
    
    if res:
       
        numbers = [int(num) for num in res]
        print(max(numbers))