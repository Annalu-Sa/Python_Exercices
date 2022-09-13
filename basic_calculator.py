#Building a Basic Calculator in Python
def Calculator(a, b, opertn):
    return
    {
        '+': a + b
        '-': a - b
        '/': a / b
        '*': a * b

    }.get(oprtn)

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
operator = input("Choose the operation")

print("The result is: ", Calculator(num1, num2, operator))

