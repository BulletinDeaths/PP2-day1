import unittest
from business_logic.score_manager import ScoreManager


class TestScoreManager(unittest.TestCase):
    def test_initial_score(self):
        """Начальный счет должен быть равен 0."""
        manager = ScoreManager()
        self.assertEqual(manager.get_current_score(), 0)

    def test_add_points(self):
        """Тест добавления очков."""
        manager = ScoreManager()
        manager.add_points(10)
        self.assertEqual(manager.get_current_score(), 10)

    def test_subtract_points(self):
        """Тест вычитания очков."""
        manager = ScoreManager()
        manager.subtract_points(5)
        self.assertEqual(manager.get_current_score(), -5)


if __name__ == '__main__':
    unittest.main()