n=input()
l=list(map(int,input().split(" ")))
binaryArray=True
for i in l:
    if i==0 or i==1:
        binaryArray=True
    else:
        binaryArray=False
print(binaryArray)        