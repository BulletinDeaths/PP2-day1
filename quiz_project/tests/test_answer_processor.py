import unittest
from business_logic.answer_processor import AnswerProcessor


class TestAnswerProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = AnswerProcessor()
        self.test_question = {"correct_index": 2}

    def test_correct_answer(self):
        """Проверка правильного ответа."""
        result = self.processor.check_answer(self.test_question, "2")
        self.assertTrue(result)

    def test_incorrect_answer(self):
        """Проверка неправильного ответа."""
        result = self.processor.check_answer(self.test_question, "0")
        self.assertFalse(result)

    def test_invalid_input(self):
        """Проверка обработки некорректного ввода (не число)."""
        result = self.processor.check_answer(self.test_question, "два")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()