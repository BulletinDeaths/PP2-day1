class ScoreManager:
    """
    Класс для управления текущим счетом игрока.
    """

    def __init__(self):
        self.score = 0  # Начальный счет равен нулю

    def add_points(self, points: int) -> None:
        """Добавляет очки к счету."""
        self.score += points

    def subtract_points(self, points: int) -> None:
        """Вычитает очки из счета."""
        self.score -= points

    def get_current_score(self) -> int:
        """Возвращает текущее значение счета."""
        return self.score
