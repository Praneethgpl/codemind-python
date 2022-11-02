n=int(input())
a = list(map(int,input().strip().split()))[:n]
evensum=0
for i in range(0,n):
    if i%2==0:
        evensum+=a[i]
print(evensum)
