from pathlib import Path

def list_files(inp_path: str) -> 'tuple[str] | None':
    """
    Функция принимает путь к каталогу в виде строки (str).
    Выполняет поиск файлов в указанном каталоге.
    Возвращает кортеж с именами найденных файлов или None, если каталог не существует.
    """
    
    # Преобразуем входной путь в объект Path
    path_to_parse = Path(inp_path)
    
    # Проверяем, существует ли каталог по указанному пути
    if not path_to_parse.is_dir():
        return None
    
    # Используем метод glob() для поиска всех файлов в указанном каталоге
    files = [file.name for file in path_to_parse.glob('*') if file.is_file()]
    
    # Возвращаем кортеж с именами найденных файлов
    return tuple(files)

# Пример ввода и вывода
if __name__ == "__main__":
    # Запрашиваем у пользователя путь к каталогу
    directory_path = input("Введите путь к каталогу: ")
    
    # Получаем имена файлов из указанного каталога
    files = list_files(directory_path)

    # Выводим найденные файлы
    if files is not None:
        print("Найденные файлы:")
        for file_name in files:
            print(file_name)
    else:
        print("Указанный каталог не существует.")

#     Пример ручного теста (cmd):
# D:\student\2023.05.28 > tree /f

# 2023.05.28
# │   7MD9i.chm
# │   conf.py
# │   E3ln1.txt
# │   F1jws.jpg
# │   le1UO.txt
# │   q40Kv.docx
# │   r62Bf.txt
# │   xcD1a.zip
# │
# ├───c14KE
# │       5vsIh.dat
# │       P2a91.dat
# │
# └───mXbd9
#         RoBjg.pt
#         z03EN.pt    

# D:\student\2023.05.28 > python -i 1.py
# >>> list_files(r'd:\student\2023.05.28\data')
# ('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'r62Bf.txt', 'xcD1a.zip')