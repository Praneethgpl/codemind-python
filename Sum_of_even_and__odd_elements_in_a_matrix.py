r,c=map(int,input().split(" "))
evensum=0
oddsum=0
for i in range(r):
    l=list(map(int,input().split(" ")))
    for j in range(c):
        if l[j]%2==0:
            evensum+=l[j]
        else:
            oddsum+=l[j]
print(evensum,oddsum,sep=" ")