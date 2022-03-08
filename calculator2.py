symbol = input("Which symbol would you like to use?" )
x = input("x: ")
y = input("y: ")
x = float(x)
y= float(y)
if symbol == "+":
    print(float(x) + float(y))
elif symbol == "-":
    print(float(x) - float(y))
elif symbol == "*":
    print(float(x) * float(y))
elif y == 0 and symbol == "/":
    print("kan niet delen door 0")
else:
    print(float(x) / float(y))