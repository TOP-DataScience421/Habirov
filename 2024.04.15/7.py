list_of_dicts = [
    {
        'Волгоград': 4,
        'Воронеж': 2,
        'Екатеринбург': 2,
        'Иркутск': 5,
        'Махачкала': 1,
        'Новокузнецк': 4,
        'Омск': 1,
        'Ростов-на-Дону': 6,
        'Санкт-Петербург': 3,
        'Челябинск': 6
    },
    {
        'Иркутск': 4, 
        'Новокузнецк': 9, 
        'Омск': 6, 
        'Ульяновск': 9, 
        'Челябинск': 6
    },
    {
        'Екатеринбург': 4,
        'Ижевск': 3,
        'Новокузнецк': 3,
        'Новосибирск': 1,
        'Омск': 4,
        'Ростов-на-Дону': 8,
        'Самара': 3,
        'Тольятти': 3
    },
    {
        'Иркутск': 4,
        'Казань': 3,
        'Кемерово': 3,
        'Краснодар': 6,
        'Красноярск': 9,
        'Ростов-на-Дону': 1,
        'Санкт-Петербург': 8,
        'Тюмень': 3,
        'Ярославль': 9
    }
]

# Создаём пустой словарь для объединения
merge_dict = {}

# Проходим через каждый словарь в списке
for i in list_of_dicts:
    for key, value in i.items():
        if key in merge_dict:
            # Добавляем значение в существующее множество
            merge_dict[key].add(value)
        else:
            # Создаём новое множество с текущим значением
            merge_dict[key] = {value}

# Выводим результат в требуемом формате
for key in sorted(merge_dict.keys()):
    print(f"'{key}': {merge_dict[key]},")

# Пример вывода:
#     'Барнаул': {5},
#     'Краснодар': {9, 4},
#     'Красноярск': {9, 1},
#     'Липецк': {1},
#     'Махачкала': {5},
#     'Москва': {1},
#     'Новосибирск': {7},
#     'Пермь': {9, 3},
#     'Ростов-на-Дону': {5, 6},
#     'Самара': {2},
#     'Санкт-Петербург': {4, 6},
#     'Тольятти': {9},
#     'Тула': {2, 3},
#     'Тюмень': {5},
#     'Ульяновск': {4, 7},
#     'Хабаровск': {7},
#     'Ярославль': {9}