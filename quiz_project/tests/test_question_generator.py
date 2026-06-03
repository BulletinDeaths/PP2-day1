import unittest
from unittest.mock import patch, mock_open
import json
from business_logic.question_generator import QuestionGenerator


class TestQuestionGenerator(unittest.TestCase):
    """
    Набор тестов для класса QuestionGenerator.
    Проверяет корректность загрузки данных и генерации вопросов.
    """

    def setUp(self):
        """Создаем экземпляр класса перед каждым тестом."""
        self.generator = QuestionGenerator()

    @patch('builtins.open', new_callable=mock_open,
           read_data='[{"id": 1, "text": "Q1", "options": ["A"], "correct_index": 0, "points": 10}]')
    @patch('json.load')
    def test_load_questions_success(self, mock_json_load, mock_file):
        """
        Тест: Успешная загрузка вопросов из файла.
        Проверяем, что функция open была вызвана с правильными параметрами.
        """
        # Настраиваем mock_json_load, чтобы он возвращал наш тестовый список
        mock_json_load.return_value = [{"id": 1, "text": "Q1", "options": ["A"], "correct_index": 0, "points": 10}]

        # Вызываем метод (он вызывается в __init__, но вызовем явно для чистоты теста)
        self.generator.load_questions()

        # Проверяем, что файл был открыт в нужном месте с нужными параметрами
        mock_file.assert_called_once_with('data/questions.json', 'r', encoding='utf-8')
        # Проверяем, что список вопросов не пуст
        self.assertEqual(len(self.generator.questions), 1)

    @patch('builtins.open')
    def test_load_questions_file_not_found(self, mock_file):
        """
        Тест: Обработка ошибки, если файл questions.json не найден.
        Проверяем, что список вопросов остается пустым и выводится сообщение.
        """
        # Настраиваем mock так, чтобы он вызывал ошибку FileNotFoundError при попытке открыть файл
        mock_file.side_effect = FileNotFoundError

        # Перехватываем вывод в консоль
        with self.assertLogs() as captured:
            self.generator.load_questions()

        # Проверяем, что список вопросов пуст
        self.assertEqual(self.generator.questions, [])
        # Проверяем, что в логи или вывод попало сообщение об ошибке
        self.assertIn("Ошибка: файл questions.json не найден.", captured.output[0])

    @patch('business_logic.question_generator.random.choice')
    def test_get_random_question_success(self, mock_choice):
        """
        Тест: Успешное получение случайного вопроса.
        """
        # Подготавливаем данные в генераторе
        test_question = {"id": 99, "text": "Mock Question"}
        self.generator.questions = [test_question]

        # Настраиваем mock, чтобы он возвращал наш тестовый вопрос
        mock_choice.return_value = test_question

        # Вызываем метод
        result = self.generator.get_random_question()

        # Проверяем, что результат совпадает с ожидаемым
        self.assertEqual(result, test_question)

    def test_get_random_question_empty_list(self):
        """
        Тест: Попытка получить вопрос из пустого списка.
        Метод должен вернуть None.
        """
        # Очищаем список вопросов
        self.generator.questions = []

        # Вызываем метод
        result = self.generator.get_random_question()

        # Проверяем результат
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()