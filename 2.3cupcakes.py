def print_pack_report(cakes_count: int) -> None:
    """Выводит отчет о возможности фасовки пирожных по коробочкам.

    Перебирает все целые числа в порядке убывания от `cakes_count` до 1
    и выводит информацию о фасовке каждого.

    Args:
        cakes_count: Целое число, обозначающее начальное
                        количество пирожных для проверки.
    """
    for count in range(cakes_count, 0, -1):
        if count % 3 == 0 and count % 5 == 0:
            print(f"{count} - расфасуем по 3 или по 5")
        elif count % 5 == 0:
            print(f"{count} - расфасуем по 5")
        elif count % 3 == 0:
            print(f"{count} - расфасуем по 3")
        else:
            print(f"{count} - не заказываем!")


cakes_number = int(input("Введите количество пирожных: "))
print_pack_report(cakes_number)
