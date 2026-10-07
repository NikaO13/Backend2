import secrets
import string


def generate_password(
    length: int = 12,
    use_lowercase: bool = True,
    use_uppercase: bool = True,
    use_digits: bool = True,
    use_special: bool = True,
) -> str:
    """Генерирует случайный сложный пароль.

    Args:
        length: Длина пароля.
        use_lowercase: Использовать ли строчные буквы.
        use_uppercase: Использовать ли заглавные буквы.
        use_digits: Использовать ли цифры.
        use_special: Использовать ли специальные символы.

    Returns:
        Сгенерированный пароль.

    """
    char_sets = []

    if use_lowercase:
        char_sets.append(string.ascii_lowercase)

    if use_uppercase:
        char_sets.append(string.ascii_uppercase)

    if use_digits:
        char_sets.append(string.digits)

    if use_special:
        char_sets.append(string.punctuation)

    if not char_sets:
        raise ValueError("Не выбран ни один тип символов.")

    if length < 1:
        raise ValueError("Длина пароля должна быть больше 0.")

    if length < len(char_sets):
        raise ValueError(
            "Длина пароля должна быть не меньше количества "
            "выбранных типов символов."
        )

    # Гарантируем наличие каждого выбранного типа символов.
    password = [
        secrets.choice(char_set)
        for char_set in char_sets
    ]

    all_chars = "".join(char_sets)

    # Заполняем оставшиеся позиции.
    for _ in range(length - len(password)):
        password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def ask_yes_no(question: str) -> bool:
    """Запрашивает у пользователя ответ «y» или «n».

    Args:
        question: Текст вопроса.

    Returns:
        True, если пользователь ответил «y», иначе False.
    """
    while True:
        answer = input(f"{question} [y/n]: ").strip().lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print("Введите «y» или «n».")


def get_length() -> int:
    """Запрашивает у пользователя длину пароля.

    Returns:
        Корректная длина пароля.
    """
    while True:
        value = input("Введите длину пароля: ").strip()

        if not value:
            return 12

        try:
            length = int(value)

            if length > 0:
                return length

            print("Длина должна быть больше 0.")

        except ValueError:
            print("Введите целое число.")


def show_settings(
    length: int,
    use_lowercase: bool,
    use_uppercase: bool,
    use_digits: bool,
    use_special: bool,
) -> None:
    """Выводит текущие настройки генератора.

    Args:
        length: Длина пароля.
        use_lowercase: Используются ли строчные буквы.
        use_uppercase: Используются ли заглавные буквы.
        use_digits: Используются ли цифры.
        use_special: Используются ли специальные символы.
    """
    print("\n" + "=" * 45)
    print("             НАСТРОЙКИ ПАРОЛЯ")
    print("=" * 45)

    print(f"Длина пароля:       {length}")
    print(
        f"Нижний регистр:     {'Да' if use_lowercase else 'Нет'}"
    )
    print(
        f"Верхний регистр:    {'Да' if use_uppercase else 'Нет'}"
    )
    print(f"Цифры:              {'Да' if use_digits else 'Нет'}")
    print(
        f"Спецсимволы:        {'Да' if use_special else 'Нет'}"
    )

    print("=" * 45)


def main() -> None:
    """Запускает консольный интерфейс генератора паролей."""
    print("\n" + "=" * 45)
    print("          ГЕНЕРАТОР СЛОЖНЫХ ПАРОЛЕЙ")
    print("=" * 45)

    length = get_length()

    print("\nВыберите символы для пароля:")

    use_lowercase = ask_yes_no("Использовать нижний регистр?")
    use_uppercase = ask_yes_no("Использовать верхний регистр?")
    use_digits = ask_yes_no("Использовать цифры?")
    use_special = ask_yes_no("Использовать спецсимволы?")

    if not any(
        (
            use_lowercase,
            use_uppercase,
            use_digits,
            use_special,
        )
    ):
        print("\nНеобходимо выбрать хотя бы один тип символов.")
        return

    show_settings(
        length,
        use_lowercase,
        use_uppercase,
        use_digits,
        use_special,
    )

    input("\nНажмите Enter, чтобы сгенерировать пароль...")

    try:
        password = generate_password(
            length=length,
            use_lowercase=use_lowercase,
            use_uppercase=use_uppercase,
            use_digits=use_digits,
            use_special=use_special,
        )

        print("\n" + "=" * 45)
        print("              ВАШ ПАРОЛЬ")
        print("=" * 45)
        print(f"\n  {password}\n")
        print("=" * 45)

    except ValueError as error:
        print(f"\nОшибка: {error}")


if __name__ == "__main__":
    main()
