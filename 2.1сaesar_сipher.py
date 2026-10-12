"""Модуль для шифрования и дешифрования текста с помощью шифра Цезаря."""


def detect_language(text: str) -> str:
    """Определяет язык входного текста (русский или английский).

    Args:
        text (str): Входной текст для анализа.

    Returns:
        str: Код языка ('ru' или 'en').
    """
    russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    english_alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in text.lower():
        if char in russian_alphabet:
            return "ru"
        elif char in english_alphabet:
            return "en"

    return "ru"


def caesar_char(char: str, shift: int, alphabet: str) -> str:
    """Сдвигает один символ по заданному алфавиту на определенный шаг.

    Args:
        char (str): Символ для сдвига.
        shift (int): Шаг сдвига.
        alphabet (str): Алфавит в нижнем регистре.

    Returns:
        str: Зашифрованный или расшифрованный символ.
    """
    if char.islower():
        current_alphabet = alphabet.lower()
    else:
        current_alphabet = alphabet.upper()

    if char.lower() not in alphabet.lower():
        return char

    index = current_alphabet.find(char)
    new_index = (index + shift) % len(current_alphabet)

    return current_alphabet[new_index]


def process_text(text: str, shift: int, mode: str) -> str:
    """Обрабатывает весь текст: шифрует или дешифрует его.

    Args:
        text (str): Исходный текст.
        shift (int): Величина сдвига.
        mode (str): Режим работы ('encrypt' или 'decrypt').

    Returns:
        str: Результирующий обработанный текст.
    """
    russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    english_alphabet = "abcdefghijklmnopqrstuvwxyz"

    if mode == "decrypt":
        shift = -shift

    result = []

    for char in text:
        if char.lower() in russian_alphabet:
            result.append(caesar_char(char, shift, russian_alphabet))
        elif char.lower() in english_alphabet:
            result.append(caesar_char(char, shift, english_alphabet))
        else:
            result.append(char)

    return "".join(result)


def get_shift() -> int:
    """Запрашивает у пользователя корректное целое число для сдвига.

    Returns:
        int: Введенный пользователем шаг сдвига.
    """
    while True:
        try:
            return int(input("Введите шаг сдвига: "))
        except ValueError:
            print("Ошибка! Введите целое число.")


def main() -> None:
    """Главная функция программы для взаимодействия с пользователем."""
    text = input("Введите текст: ")

    if not text:
        print("Текст не может быть пустым.")
        return

    shift = get_shift()
    language = detect_language(text)

    if language == "ru":
        print("Язык - русский")
    else:
        print("Язык - английский")

    print("Выберите действие:")
    print("1 — Зашифровать")
    print("2 — Расшифровать")

    while True:
        choice = input("Ваш выбор: ")

        if choice == "1":
            result = process_text(text, shift, "encrypt")
            print(f"\nЗашифрованный текст: {result}")
            break

        elif choice == "2":
            result = process_text(text, shift, "decrypt")
            print(f"\nРасшифрованный текст: {result}")
            break

        else:
            print("Выберите 1 или 2")


if __name__ == "__main__":
    main()
