symbol = input("Which symbol would you like to use?" )
if symbol not in "+/-*%":
    print("No function")
    exit()
    print(symbol)
x = input("x: ")
y = input("y: ")
try:
    x = float(x)
    y = float(y)
except ValueError:
    print("Kan niet")
    exit()
print("symbol")
if symbol == "+":
    print(float(x) + float(y))
elif symbol == "-":
    print(float(x) - float(y))
elif symbol == "%" and(float(x) % float(y) == 0) :
    print(float(x) % float(y))
elif symbol == "*":
    print(float(x) * float(y))
elif y == 0 and symbol == "/":
    print("kan niet delen door 0")
else:
    print(float(x) / float(y))
