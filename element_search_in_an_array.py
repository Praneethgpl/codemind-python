n=int(input())
a = list(map(int,input().strip().split()))[:n]
b = int(input())
givencondition=False
for i in range(0,n):
    if a[i]==b:
        givencondition=True
        break
print(givencondition)