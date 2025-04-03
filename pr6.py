def check_access():
    try:
        age = int(input("Введіть ваш вік: "))
        if age < 18:
            print("Доступ заборонено!")
            return
        print("Доступ дозволено!")
    except ValueError:
        print("Помилка: введіть число!")


def check_stock():
    stock = 20
    try:
        quantity = int(input("Введіть кількість товару: "))
        if quantity <= 0:
            print("Помилка: некоректна кількість!")
            return
        if quantity > stock:
            print("На складі недостатньо товару!")
            return
        print("Ваше замовлення прийнято!")
    except ValueError:
        print("Помилка: введіть число!")


def check_password():
    password = input("Введіть пароль: ")
    if len(password) < 8:
        print("Пароль надто короткий!")
        return
    if password in ("password", "12345678"):
        print("Пароль занадто простий!")
        return
    print("Вхід дозволено!")


def check_temperature():
    try:
        temp = float(input("Введіть температуру приміщення: "))
        if temp < 16:
            print("Температура занизька! Увімкніть обігрівач.")
            return
        if temp > 28:
            print("Температура зависока! Увімкніть кондиціонер.")
            return
        print("Температура комфортна.")
    except ValueError:
        print("Помилка: введіть число!")


def check_top_up():
    try:
        amount = float(input("Введіть суму поповнення: "))
        if amount < 10:
            print("Мінімальна сума поповнення – 10 грн!")
            return
        if amount > 3000:
            print("Сума поповнення занадто велика!")
            return
        print(f"Поповнення на суму {amount} грн виконано успішно!")
    except ValueError:
        print("Помилка: введіть число!")


if __name__ == "__main__":
    while True:
        print("\nОберіть завдання:")
        print("1 - Перевірка доступу")
        print("2 - Перевірка наявності товару")
        print("3 - Перевірка пароля")
        print("4 - Перевірка температури")
        print("5 - Перевірка поповнення рахунку")
        print("0 - Вийти")
        
        choice = input("Ваш вибір: ")
        if choice == "1":
            check_access()
        elif choice == "2":
            check_stock()
        elif choice == "3":
            check_password()
        elif choice == "4":
            check_temperature()
        elif choice == "5":
            check_top_up()
        elif choice == "0":
            break
        else:
            print("Некоректний вибір, спробуйте ще раз.")
