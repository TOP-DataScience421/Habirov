from utils import load_file  

def ask_for_file():
    # Бесконечный цикл для повторного запроса пути файла в случае ошибки
    while True:
        # Получение пути файла от пользователя 
        file_path = input("Введите путь к файлу: ")  
        try:
            # Вызов функции load_file для загрузки файла
            copy = load_file(file_path)
            # Возврат загруженного модуля, если файл успешно загружен  
            return copy  
        except FileNotFoundError:
            # Вывод сообщения об ошибке, если файл не найден
            print("! По указанному пути отсутствует необходимый файл !") 

if __name__ == "__main__":
    # Вызов функции ask_for_file при выполнении скрипта как главного файла
    config_module = ask_for_file()  