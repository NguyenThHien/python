T= int(input())
for _ in range(T):
    n, k = map(int, input().split())
    m = list(map(int, input().split()))
    res = -10**9
    index = 0
    for i in range(n):
        if m[i] > res:
            res = m[i]
            index = i
    m.insert(index, k)
    m_duong = [i for i in m if i >= 0]
    m_am = [i for i in m if i < 0]
    m = m_am + m_duong
    print(" ".join(map(str, m)))