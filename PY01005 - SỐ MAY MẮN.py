n = str(input())
cnt_4 = n.count('4')
cnt_7 = n.count('7')
if cnt_4 + cnt_7 == 4 or cnt_7 + cnt_4 == 7 :
    print("YES")
else:
    print("NO") 
