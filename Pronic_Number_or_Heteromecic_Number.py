n=int(input())
givencondition=False
for i in range(1,n//2):
    if i*(i+1)==n:
        givencondition=True
        break
if givencondition==True:
    print("YES")
else:
    print("NO")
