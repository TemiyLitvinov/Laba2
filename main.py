from check_password import is_valid_password, password_regex

def main():
    while True:
        print("\nВыберите действие")
        print("1 — Проверить введённый пароль")
        print("2 — Найти надёжные пароли в файле")
        print("3 — Выход")

        choice = input().strip()
        if choice == "1":
            password = input("Введите пароль: ")
            if is_valid_password(password):
                print("Пароль является надёжным")
            else:
                print("Пароль не соответствует")

        elif choice == "2":
            filename = "example_passwords.txt"
            try:
                with open(filename, "r", encoding="utf-8", errors="ignore") as file:
                    lines = file.read().splitlines()

                found_good_passwords = [line for line in lines if password_regex.match(line)]

                if found_good_passwords:
                    print('\nНайденные надежные пароли:')
                    for i in range(len(found_good_passwords)):
                        print(f'{i + 1}. {found_good_passwords[i]}\n')

                else:
                    print(f'В файле нет надёжных паролей')

            except FileNotFoundError:
                print(f"Ошибка: файл '{filename}' не найден!")
                return ""

        elif choice == "3":
            print("Выход...")
            break

        else:
            print("Некорректный ввод. Попробуйте снова.")
            return ""


if __name__ == "__main__":
    main()