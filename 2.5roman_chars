def int_to_roman(number: int) -> str:
    """Конвертирует целое число в римское представление.

    Args:
        number: Целое число от 1 до 3999.

    Returns:
        Строковое представление числа в римской системе.
    """
    if not 1 <= number <= 3999:
        raise ValueError("Число должно быть от 1 до 3999.")

    roman_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = []

    for value, symbol in roman_map:
        while number >= value:
            result.append(symbol)
            number -= value

    return "".join(result)


def roman_to_int(roman: str) -> int:
    """Конвертирует римское число в целое.

    Args:
        roman: Строка с римским числом.

    Returns:
        Целое число от 1 до 3999.
    """
    roman = roman.upper().strip()

    if not roman:
        raise ValueError("Число не может быть пустым.")

    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    for char in roman:
        if char not in roman_values:
            raise ValueError(
                f"Недопустимый символ: {char}"
            )

    total = 0
    previous_value = 0

    for char in reversed(roman):
        value = roman_values[char]

        if value < previous_value:
            total -= value
        else:
            total += value

        previous_value = value

    if int_to_roman(total) != roman:
        raise ValueError(
            f"Некорректная запись римского числа: {roman}"
        )

    return total


def main() -> None:
    user_input = input(
        "Введите ваше число: "
    ).strip()

    if not user_input:
        print("Ввод не может быть пустым.")
        return

    try:
        if user_input.isdigit():
            number = int(user_input)
            result = int_to_roman(number)

            print(f"Результат конвертации в римские: {result}")
        else:
            result = roman_to_int(user_input)

            print(f"Результат конвертации в арабские: {result}")

    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
