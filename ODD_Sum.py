n=int(input())
a = list(map(int,input().strip().split()))[:n]
oddsum=0
for i in range(0,n):
    if a[i]%2!=0:
        oddsum+=a[i]
print(oddsum)
