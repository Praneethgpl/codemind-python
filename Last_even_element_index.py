n=int(input())
a = list(map(int,input().strip().split()))[:n]
ind=0
for i in range(0,n):
    if a[i]%2==0:
        ind=i
print(ind)