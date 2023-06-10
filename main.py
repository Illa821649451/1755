def calculator():
    while True:
        print("Виберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Обчислення відсотка")
        print("6. Вийти з програми")

        choice = input("Ваш вибір: ")

        if choice == '6':
            print("До побачення!")
            break

        num1 = float(input("Введіть перше число: "))

        if choice != '5':
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
        else:
            print("Неправильний вибір. Спробуйте ще раз.")



calculator()