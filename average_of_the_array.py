n=int(input())
a = list(map(int,input().strip().split()))[:n]
s=sum(a)
b=s/n
print("{:.2f}".format(b))