n=int(input())
count=0
for i in range(0,n):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        if j%10==2 or j%10==3 or j%10==9:
            count+=1
    print(count)
    count=0
            