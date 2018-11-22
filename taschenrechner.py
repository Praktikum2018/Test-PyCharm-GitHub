num1 = float(input("Erste Nummer: "))
op = input("Rechnungsart: ")
num2 = float(input("Zweite Nummer: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Falsches Rechnungszeichen!!!")

