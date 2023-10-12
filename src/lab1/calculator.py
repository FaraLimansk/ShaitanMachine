def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: division by zero"

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Выберите номер (1/2/3/4): ")

num1 = float(input("Введите 1 число: "))
num2 = float(input("Введите 2 число: "))

if choice == '1':
    print(num1, "+", num2, "=", addition(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtraction(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiplication(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", division(num1, num2))

else:
    print("Error: invalid operation input")
