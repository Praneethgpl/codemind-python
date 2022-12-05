n=int(input())
l=list(map(int,input().split(" ")))
onecount=0
for i in range(n):
    if l[i]==0:
        print("0",end=' ')
    else:
        onecount+=1
for i in range(onecount):
    print("1",end=' ')