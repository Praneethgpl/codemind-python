word = input()
lowerword=word.lower()
reversedword=""
for char in lowerword:
    reversedword=char+reversedword
if lowerword==reversedword:
    print("True")
else:
    print("False")