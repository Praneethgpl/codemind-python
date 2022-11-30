s=input()
n=int(s)
l=list(s)
sum1=0
j=1
for i in l:
    sum1+=int(i)**j
    j+=1
if sum1==n:
    print("True")
else:
    print("False")