from typing import Dict


class AnswerProcessor:
    """
    Класс для обработки и проверки ответов пользователя.
    """
    def check_answer(self, question_data: Dict, user_answer: str) -> bool:
        """
        Проверяет, совпадает ли ответ пользователя с правильным индексом.
        :param question_data: Данные вопроса, включая правильный индекс ('correct_index').
        :param user_answer: Ответ пользователя (строка).
        :return: True, если ответ верный, иначе False.
        """
        try:
            # Преобразуем строку от пользователя в целое число
            answer_index = int(user_answer)
            return answer_index == question_data.get('correct_index')
        except ValueError:
            # Если пользователь ввел что-то, что нельзя преобразовать в int
            return False