for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = [0]*n
    stack = []
    for i in range(n):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        if stack:
            res[i] = i - stack[-1]
        else:
            res[i] = i+1
        stack.append(i)
    print(" ".join(map(str, res)))
    
