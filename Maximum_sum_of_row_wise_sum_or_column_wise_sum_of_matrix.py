n,m=map(int,input().split(" "))
matrix=[]
for i in range(n):
    a=list(map(int,input().split(" ")))
    matrix.append(a)
maxrowwisesum=0
maxcolumnwisesum=0
sum=0
for i in range(n):
    sum=0
    for j in matrix[i]:
        sum+=j
    if sum>maxrowwisesum:
        maxrowwisesum=sum
for i in range(m):
    sum=0
    for j in range(n):
        sum+=matrix[j][i]
    if sum>maxcolumnwisesum:
        maxcolumnwisesum=sum
if maxcolumnwisesum>maxrowwisesum:
    print(maxcolumnwisesum)
else:
    print(maxrowwisesum)