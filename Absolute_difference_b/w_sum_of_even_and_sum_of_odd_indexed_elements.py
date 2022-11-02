n=int(input())
a = list(map(int,input().strip().split()))[:n]
oddsum=0
evensum=0
for i in range(0,n):
    if i%2==0:
        oddsum+=a[i]
    else:
        evensum+=a[i]
if oddsum>evensum:
    print(oddsum-evensum)
else:
    print(evensum-oddsum)