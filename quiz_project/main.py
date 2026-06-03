import sys
from interface.console_ui import ConsoleUI
from business_logic.question_generator import QuestionGenerator
from business_logic.answer_processor import AnswerProcessor
from business_logic.score_manager import ScoreManager
from interface.web_ui import app as web_app


def run_console():
    """Функция запуска консольной версии викторины."""
    # Создаем объекты бизнес-логики
    q_gen = QuestionGenerator()
    ans_proc = AnswerProcessor()
    score_mgr = ScoreManager()
    # Создаем объект интерфейса, передавая ему зависимости
    ui = ConsoleUI(q_gen, ans_proc, score_mgr)
    ui.start_game()


if __name__ == "__main__":
    # Проверяем аргументы командной строки
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'web':
        print("Запуск веб-сервера... Откройте http://127.0.0.1:5000 в браузере.")
        web_app.run(debug=True) # Запускаем Flask-приложение
    else:
        print("Запуск консольной версии...")
        run_console()