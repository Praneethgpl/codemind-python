a,b=map(int,input().split())
if a>b:
    a,b=b,a
lcm=b
while True:
    if lcm%a==0 and lcm%b==0:
        print(lcm)
        break
    else:
        lcm=lcm+1