class ChessKing:
    # Словарь для соответствия буквенного представления вертикали доски и числового индекса
    files = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    # Словарь для соответствия строкового представления горизонтали доски и числового индекса
    ranks = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8}

    # Конструктор класса, инициализирует атрибуты экземпляра
    def __init__(self, color='white', square=None):
        self.color = color
        # Если поле не указано, устанавливаем начальную позицию в зависимости от цвета фигуры
        if square is None:
            self.square = 'e1' if color == 'white' else 'e8'
        else:
            self.square = square

    # Возвращает машиночитаемое строковое представление экземпляра класса
    def __repr__(self):
        return f"{self.color[0].upper()}K: {self.square}"

    # Возвращает человекочитаемое строковое представление экземпляра класса
    def __str__(self):
        return f"{self.color.upper()}K: {self.square}"

    # Проверяет, возможен ли ход короля на указанное новое поле
    def is_turn_valid(self, new_square):
        # Вычисляем разницу по горизонтали и вертикали между текущим и новым положением
        file_diff = abs(self.files[self.square[0]] - self.files[new_square[0]])
        rank_diff = abs(self.ranks[self.square[1]] - self.ranks[new_square[1]])
        # Ход короля возможен, если разница по горизонтали и вертикали не превышает 1 и хотя бы одна из них не равна 0
        return file_diff <= 1 and rank_diff <= 1 and file_diff + rank_diff > 0

    # Выполняет ход короля на указанное новое поле
    def turn(self, new_square):
        # Проверяем, возможен ли ход
        if self.is_turn_valid(new_square):
            # Если возможен, обновляем положение короля
            self.square = new_square
        else:
            # Если ход невозможен, выбрасываем исключение
            raise ValueError("Invalid move")

# Пример тестирования
if __name__ == "__main__":
    wk = ChessKing()
    print(wk.color)  # 'white'
    print(wk.square)  # 'e1'
    wk.turn('e2')
    print(wk)  # 'WK: e2'
    try:
        wk.turn('d4')
    except ValueError as e:
        print(e)  # Invalid move
    bk = ChessKing('black')
    print(bk)  # 'BK: e8'

# Написанный класс необходимо протестировать.
# Пример теста:
# >>> wk = ChessKing()
# >>> wk.color
# 'white'
# >>> wk.square
# 'e1'
# >>>
# >>> wk.turn('e2')
# >>> wk
# 'WK: e2'
# >>>
# >>> wk.turn('d4')
# ... 
# ValueError
# >>> 
# >>> bk = ChessKing('black')
# >>> print(bk)
# BK: e8