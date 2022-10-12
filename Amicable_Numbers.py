firstnumber=int(input())
secondnumber=int(input())
sumOffirst=0
sumOfsecond=0
for i in range(1,firstnumber):
    if firstnumber%i==0:
        sumOffirst+=i
for i in range(1,secondnumber):
    if secondnumber%i==0:
        sumOfsecond+=i
if sumOffirst==secondnumber and sumOfsecond==firstnumber:
    print("Amicable")
else:
    print("Not Amicable")
