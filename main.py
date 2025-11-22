from check_password import is_valid_password, password_regex

# Главная функция программы
def main():
    # Бесконечный цикл
    while True:
        print("\nВыберите действие")
        print("1 — Проверить введённый пароль")
        print("2 — Найти надёжные пароли в файле")
        print("3 — Выход")

        choice = input().strip()

        # Блок с проверкой надёжности введённого пароля
        if choice == "1":
            password = input("Введите пароль: ")

            # Проверка надёжности пароля с помощью функции, написанной в файле check_password
            if is_valid_password(password):
                print("Пароль является надёжным")
            else:
                print("Пароль не соответствует критериям надёжности")

        # Блок с считыванием данных из файла и проверкой надёжности паролей из него
        elif choice == "2":
            filename = input("Введите путь к файлу или его имя: ")

            # Блок try/except для открытия файла и ловли исключения при ошибке
            try:
                with open(filename, "r", encoding="utf-8", errors="ignore") as file:
                    lines = file.read().splitlines()

                # Список найденных надёжных паролей
                found_good_passwords = [line for line in lines if password_regex.match(line)]

                if found_good_passwords:
                    print('\nНайденные надежные пароли:')

                    # Вывод всех паролей с нумерацией
                    for i in range(len(found_good_passwords)):
                        print(f'{i + 1}. {found_good_passwords[i]}\n')

                else:
                    print(f'В файле нет надёжных паролей')

            # Исключение для случая, если файл окажется не найден
            except FileNotFoundError:
                print(f"Ошибка: файл '{filename}' не найден!")

        # Выход из бесконечного цикла
        elif choice == "3":
            print("Выход...")
            break

        # Обработка для случая ввода других символов
        else:
            print("Некорректный ввод. Попробуйте снова.")
            return ""


# Запуск главной функции
if __name__ == "__main__":
    main()