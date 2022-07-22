num1 = int(input("Enter a number:\n"))

num2 = int(input("Enter a second number:\n"))

menu = int(input("""What do you want to do?

1. Add
2. Subtract
3. Multiply
4. Divide

"""))

if menu == 1:
    print(num1 + num2)

if menu == 2:
    print(num1 - num2)