import random

def check_winners(scores: list[int], student_score: int) -> None:
    """Проверяет, вошёл ли студент в тройку лидеров олимпиады, и выводит результат.

    Args:
        scores: Список баллов всех участников олимпиады.
        student_score: Количество баллов, заработанное Стасом.
    """
    top_three = sorted(scores, reverse=True)[:3]
    if student_score in top_three:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")

scores_list = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
stas_score =  random.choice(scores_list)
check_winners(scores_list, stas_score)
