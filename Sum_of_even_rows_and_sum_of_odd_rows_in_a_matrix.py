rows,column=map(int,input().split(" "))
oddsum=0
evensum=0
matrix=[]
for i in range(1,rows+1):
    a=list(map(int,input().split(" ")))
    matrix.append(a)
    if i%2==0:
        for j in range(column):
            evensum+=matrix[i-1][j]
    else:
        for j in range(column):
            oddsum+=matrix[i-1][j]
print(oddsum,evensum,sep=" ")