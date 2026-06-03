import json
import random
from typing import Dict, Optional


class QuestionGenerator:
    """
    Класс для генерации случайных вопросов из файла.
    """
    def __init__(self):
        self.questions = []
        self.load_questions() # Загружаем вопросы при создании объекта

    def load_questions(self) -> None:
        """Загружает список вопросов из JSON-файла."""
        try:
            with open('data/questions.json', 'r', encoding='utf-8') as f:
                self.questions = json.load(f)
        except FileNotFoundError:
            print("Ошибка: файл questions.json не найден.")
            self.questions = [] # Если файла нет, создаем пустой список

    def get_random_question(self) -> Optional[Dict]:
        """
        Возвращает случайный вопрос из списка.
        :return: Словарь с данными вопроса или None, если список пуст.
        """
        if not self.questions:
            return None
        # Используем .copy(), чтобы случайно не изменить исходные данные в списке
        return random.choice(self.questions).copy()