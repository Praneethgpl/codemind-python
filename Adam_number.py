def reverse(number):
    reversednumber=0
    while number>0:
        rem=number%10
        reversednumber=(reversednumber*10)+rem
        number//=10
    return reversednumber
adamnumber=False
n=int(input())
square=n**2
revnumber=reverse(n)
if reverse(revnumber**2)==square:
    adamnumber=True
print(adamnumber)