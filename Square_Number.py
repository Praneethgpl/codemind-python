n=int(input())
value=False
for i in range(2,int(n**0.5)+1):
    if i**2==n:
        value=True
print(value)