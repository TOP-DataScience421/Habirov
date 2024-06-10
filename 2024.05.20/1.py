class Tetrahedron:
    def __init__(self, edge: float):
        # Конструктор класса Tetrahedron. Принимает длину ребра правильного тетраэдра.
        self.edge = edge

    def surface(self) -> float:
        # Метод для вычисления площади поверхности правильного тетраэдра.
        return (3 ** 0.5) * self.edge ** 2

    def volume(self) -> float:
        # Метод для вычисления объёма правильного тетраэдра.
        return (self.edge ** 3) / (6 * (2 ** 0.5))

# Тестирование
if __name__ == "__main__":
    t1 = Tetrahedron(5)
    print(t1.edge)              
    print(t1.surface())          
    print(t1.volume())           

    t1.edge = 6
    print(t1.surface()) 

# Написанный класс необходимо протестировать.
# Пример теста:
# >>> t1 = Tetrahedron(5)
# >>> t1.edge
# 5.0
# >>> t1.surface()
# 43.30127018922193
# >>> t1.volume()
# 14.731391274719739
# >>> 
# >>> t1.edge = 6
# >>> t1.surface()
# 62.35382907247958