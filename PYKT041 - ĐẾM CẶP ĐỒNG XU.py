def count_pairs(count):
    return (count * (count - 1)) // 2
n = int(input())
a = []
for _ in range(n):
    s = input()
    a.append(s)
count_row = [0]*n
count_col = [0]*n
for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            count_col[j]+=1
            count_row[i]+=1
total_pairs = sum(count_pairs(count) for count in count_col)
total_pairs += sum(count_pairs(count) for count in count_row)
print(total_pairs)