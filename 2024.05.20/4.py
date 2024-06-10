import csv
from pathlib import Path

class CountableNouns:
    db_path = Path('words.csv')  # Путь к файлу базы данных

    # Словарь, хранящий соответствие между существительными и их словоформами
    words = {}

    def __init__(self):
        # Метод __init__ вызывается при создании объекта класса
        with open(self.db_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                self.words[row[0]] = tuple(row[1:])

    @classmethod
    def pick(cls, number: int, word: str) -> str:
        # Метод pick выбирает правильную словоформу существительного в зависимости от переданного числа
        if word in cls.words:
            return cls.words[word][0] if number == 1 else cls.words[word][1]
        else:
            cls.save_words(word)  # Если существительное отсутствует в базе, вызываем метод save_words
            return word

    @classmethod
    def save_words(cls, word1: str = None) -> None:
        # Метод save_words запрашивает у пользователя словоформы для существительного и сохраняет их в базу данных
        if word1:
            word2 = input(f'Введите слово, согласующееся с числительным "пять": ')
            cls.words[word1] = (input(f'Введите слово, согласующееся с числительным "два": '), word2)
        else:
            # Если метод вызывается без аргумента, запрашиваем все три словоформы
            word1 = input(f'Введите слово, согласующееся с числительным "один": ')
            word2 = input(f'Введите слово, согласующееся с числительным "два": ')
            word3 = input(f'Введите слово, согласующееся с числительным "пять": ')
            cls.words[word1] = (word2, word3)

        # Добавляем новое слово в файл базы данных
        with open(cls.db_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([word1, cls.words[word1][0], cls.words[word1][1]])

# Пример использования и тестирования
print(CountableNouns.words)
print(CountableNouns.pick(22, 'год'))
print(CountableNouns.pick(365, 'день'))
print(CountableNouns.pick(21, 'попугай'))
print(CountableNouns.pick(22, 'попугай'))
print(CountableNouns.words)
CountableNouns.save_words()
print(CountableNouns.db_path.read_text(encoding='utf-8'))

# Написанный класс необходимо протестировать.
# Пример теста:
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
# >>> 
# >>> CountableNouns.pick(22, 'год')
# 'года'
# >>> CountableNouns.pick(365, 'день')
# 'дней'
# >>> 
# >>> CountableNouns.pick(21, 'попугай')
# 'попугай'
# >>> CountableNouns.pick(22, 'попугай')
# существительное "попугай" отсутствует в базе
#     введите слово, согласующееся с числительным "два": попугая
#     введите слово, согласующееся с числительным "пять": попугаев
# >>>
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'попугай': ('попугая', 'попугаев')}
# >>>
# >>> CountableNouns.save_words()
#     введите слово, согласующееся с числительным "один": капля
#     введите слово, согласующееся с числительным "два": капли
#     введите слово, согласующееся с числительным "пять": капель
# >>>
# >>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
# год,года,лет
# месяц,месяца,месяцев
# день,дня,дней
# попугай,попугая,попугаев
# капля,капли,капель