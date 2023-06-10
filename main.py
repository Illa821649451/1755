import math


def calculator():
    while True:
        print("Виберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Обчислення відсотка")
        print("6. Обчислення за формулою дискримінанта")
        print("7. Обчислення периметра квадрата")
        print("8. Обчислення периметра трикутника")
        print("9. Обчислення периметра кола")
        print("10. Вийти з програми")

        choice = input("Ваш вибір: ")

        if choice == "10":
            print("До побачення!")
            break

        num1 = float(input("Введіть перше число: "))

        if choice != '5' and choice != '6' and choice != '7' and choice != '9':
            num2 = float(input("Введіть друге число: "))

        if choice == '1':
            result = num1 + num2
            print("Результат:", result)
        elif choice == '2':
            result = num1 - num2
            print("Результат:", result)
        elif choice == '3':
            result = num1 * num2
            print("Результат:", result)
        elif choice == '4':
            if num2 == 0:
                print("Помилка: Ділення на нуль неможливе")
            else:
                result = num1 / num2
                print("Результат:", result)
        elif choice == '5':
            percent = float(input("Введіть відсоток: "))
            result = (percent / 100) * num1
            print("Відсоток:", result)
        elif choice == '6':
            if num1 == 0:
                print("Помилка: a не може бути рівним нулю")
            else:
                b = float(input("Введіть значення b: "))
                c = float(input("Введіть значення c: "))
                discriminant = b ** 2 - 4 ** num1 ** c
                if discriminant < 0:
                    print("Дискримінант менший за нуль. Рішень немає.")
                elif discriminant == 0:
                    x = -b / (2 * num1)
                    print("Один корінь: x =", x)
                else:
                    x1 = (-b + math.sqrt(discriminant)) / (2 * num1)
                    x2 = (-b - math.sqrt(discriminant)) / (2 * num1)
                    print("Два корені: x1 =", x1, "x2 =", x2)
        elif choice == '7':
            perimeter = 4 * num1
            print("Периметр квадрата:", perimeter)
        elif choice == '8':
            perimeter = 3 * num1
            print("Периметр трикутника:", perimeter)
        elif choice == '9':
            perimeter = 2 * math.pi * num1
            print("Периметр кола:", perimeter)
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


calculator()