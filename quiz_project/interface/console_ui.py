from business_logic.question_generator import QuestionGenerator
from business_logic.answer_processor import AnswerProcessor
from business_logic.score_manager import ScoreManager


class ConsoleUI:
    """
    Класс для реализации консольного интерфейса викторины.
    """
    def __init__(self, q_gen, ans_proc, score_mgr):
        # Принимаем готовые объекты (инъекция зависимостей)
        self.q_gen = q_gen
        self.ans_proc = ans_proc
        self.score_mgr = score_mgr

    def display_question(self, question_data: dict) -> None:
        """Выводит текст вопроса и варианты ответов на экран."""
        print("\n" + "=" * 40)
        print(question_data['text'])
        for i, option in enumerate(question_data['options']):
            print(f"{i}. {option}")

    def start_game(self) -> None:
        """Запускает основной цикл игры."""
        total_questions = len(self.q_gen.questions)
        current_q_num = 1

        while current_q_num <= total_questions and self.q_gen.questions:
            question_data = self.q_gen.get_random_question()
            self.display_question(question_data)

            user_input = input("Ваш выбор (введите номер): ")

            is_correct = self.ans_proc.check_answer(question_data, user_input)
            points = question_data['points']

            if is_correct:
                self.score_mgr.add_points(points)
                print(f"Верно! +{points} очков.")
            else:
                self.score_mgr.subtract_points(points)
                correct_idx = question_data['correct_index']
                print(f"Неверно! -{points} очков. Правильный ответ был: {correct_idx}")

            current_q_num += 1

        final_score = self.score_mgr.get_current_score()
        print("\nИгра окончена!")
        print(f"Ваш итоговый результат: {final_score} очков.")