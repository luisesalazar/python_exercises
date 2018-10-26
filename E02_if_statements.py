num=5

if num:
    print("Num has a value")

text= "Hello"

if text:
    print("text has a value")

if text and num:
    print("Text and num have a value")

if num > 5:
    print("The given number is grater than 5")
else:
    print("The given number is less than 5 ")
#
val= "The given number is grater than 5" if num > 5 else "The given number is less than 5 "
print(val)
