from typing import Iterable, List, Callable, TypeVar
from numbers import Number
from collections.abc import Iterable as IterableType
import numpy as np
import operator as op

RawRow = Iterable[Number]
RawMatrix = Iterable[RawRow]
Self = TypeVar("Self", bound="Matrix")


class Matrix:
    def __init__(self, raw_matrix: RawMatrix):
        # Преобразуем входную матрицу в список списков и проверяем ее допустимость
        processed_matrix = list(map(list, raw_matrix))
        # Если матрица действительна, сохраняем ее и размеры
        if self.is_valid(processed_matrix):
            self.__rows = processed_matrix
            # количество строк
            self.n = len(processed_matrix)
            # количество столбцов
            self.m = len(processed_matrix[0])
        else:
            # В случае недопустимой матрицы выбрасываем исключение
            raise ValueError("Недопустимый формат матрицы")

    @staticmethod
    def is_valid(processed_matrix: List[List[Number]]) -> bool:
        # Проверяем, что матрица является итерируемой и что все элементы являются числами
        if not isinstance(processed_matrix, IterableType):
            return False
        if not all(isinstance(row, IterableType) for row in processed_matrix):
            return False
        return all(isinstance(num, Number) for row in processed_matrix for num in row)

    def __getitem__(self, index: int) -> List[Number]:
        # Метод для доступа к элементам матрицы по индексу
        return self.__rows[index]

    def __element_wise_operation(self, other: Self | Number, operation: Callable) -> Self:
         # Приватный метод для выполнения поэлементных операций над матрицей
        if isinstance(other, Matrix):
            # Если операция выполняется между двумя матрицами
            if self.n != other.n or self.m != other.m:
                raise ValueError("Матрицы должны иметь одинаковые размеры для операций по элементу")
            # Создаем новую матрицу, применяя операцию к соответствующим элементам двух матриц
            return Matrix([[operation(a, b) for a, b in zip(row_self, row_other)] for row_self, row_other in zip(self.__rows, other.__rows)])
        elif isinstance(other, Number):
            # Если операция выполняется между матрицей и числом
            # Создаем новую матрицу, применяя операцию к каждому элементу матрицы
            return Matrix([[operation(a, other) for a in row] for row in self.__rows])
        else:
            # Если операнд не поддерживается, выбрасываем исключение
            raise ValueError("Неподдерживаемый тип операнда")

    def __getitem__(self, key: int) -> list[Number]:
        return self.__rows[key]
    
    def __add__(self, other: Self | Number) -> Self:
        return self.__element_wise_operation(op.add, other)
    
    def __radd__(self, other: Self | Number) -> Self:
        return self.__element_wise_operation(op.add, other)
        
    def __sub__(self, other: Self | Number) -> Self:
        return self.__element_wise_operation(op.sub, other)
    
    def __rsub__(self, other: Self | Number) -> Self:
        result = self.__element_wise_operation(op.neg)
        return result.__element_wise_operation(op.add, other)
        
    def __mul__(self, other: Self | Number) -> Self:
        if isinstance(other, Matrix):
            raise NotImplementedError('умножение матриц будет реализовано в будущем')
        return self.__element_wise_operation(op.mul, other)
    
    def __rmul__(self, other: Self | Number) -> Self:
        return self.__element_wise_operation(op.mul, other)
        
    def __neg__(self) -> Self:
        return self.__element_wise_operation(op.neg)
        
    def __repr__(self) -> str:
        output: str = ''
        max_elem_width: int = 0
        
        for row in self.__rows:
            for elem in row:
                max_elem_width = max(max_elem_width, len(str(elem)))
        
        for row in self.__rows:
            for elem in row:
                output += str(elem).rjust(max_elem_width) + ' '
            output = output + '\n' 
        
        return output.rstrip('\n')  


# Определяем матрицы
matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix2 = np.array([[7, 8, 9], [10, 11, 12]])

# Сложение матриц
result = matrix1 + matrix2
result1 = matrix1 * matrix2
result2 = matrix1 / matrix2

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nResult of Matrix 1 + Matrix 2:")
print(result)
print("\nResult of Matrix 1 * Matrix 2:")
print(result1)
print("\nResult of Matrix 1 / Matrix 2:")
print(result2)

# Написанный класс необходимо протестировать.
# Пример теста:
# >>> 
# >>> Matrix(1, 2, 3, 4, 5, n=2, m=3)
# ...
# ValueError: невозможно сконструировать матрицу
# >>> 
# >>> from itertools import repeat
# >>> 
# >>> m1 = Matrix(*repeat(1, 15), n=3, m=5)
# >>> m2 = Matrix(*range(1, 16), n=3, m=5)
# >>> 
# >>> m1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# >>>
# >>> m2
#     1  2  3  4  5
#     6  7  8  9 10
# 11 12 13 14 15
# >>>
# >>> m1[0][0]
# ...
# TypeError: 'Matrix' object is not subscriptable
# >>>
# >>> m2.transpose
#     1  6 11
#     2  7 12
#     3  8 13
#     4  9 14
#     5 10 15
# >>>
# >>> m1 + m1
# 2 2 2 2 2
# 2 2 2 2 2
# 2 2 2 2 2
# >>>
# >>> m2 - m1
#     0  1  2  3  4
#     5  6  7  8  9
# 10 11 12 13 14
# >>>
# >>> m1 * m2
# ...
# NotImplementedError: умножение матриц будет реализовано в будущем
# >>>
# >>> 3 + m1
# 4 4 4 4 4
# 4 4 4 4 4
# 4 4 4 4 4
# >>> 
# >>> m2.transpose - 10
# -9 -4  1
# -8 -3  2
# -7 -2  3
# -6 -1  4
# -5  0  5
# >>>
# >>> -1.5 - m1
# -2.5 -2.5 -2.5 -2.5 -2.5
# -2.5 -2.5 -2.5 -2.5 -2.5
# -2.5 -2.5 -2.5 -2.5 -2.5
# >>>
# >>> m3 + m1
# ...
# ValueError: сложение и вычитание возможно только для матриц одной размерности
# >>> 
# >>> m3 = Matrix(*range(1, 5), n=2, m=2)
# >>> 
# >>> m3
# 1 2
# 3 4
# >>> 
# >>> m3 * 4.5
#     4.5  9.0
# 13.5 18.0
# >>>
# >>> -m3
# -1 -2
# -3 -4
# >>>
# >>> m3 - [4, 3, 2, 1]
# ...
# TypeError: алгебраические операции возможны только с матрицами и числами
