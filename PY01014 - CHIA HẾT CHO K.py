a,k,n = map(int,input().split()) 
b = [] 
s_b = k -(a%k) 
end = n - a 
while s_b<=end: 
    b.append(str(s_b)) 
    s_b+=k 
if(len(b)==0): 
    print(-1) 
else: print(' '.join(b))