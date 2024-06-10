import shutil
from pathlib import Path
import os

def important_message(text: str) -> str:
    # Получаем ширину окна терминала
    terminal_width = shutil.get_terminal_size().columns - 1
    
    # Определяем ширину рамки
    frame_width = terminal_width
    
    # Генерируем верхнюю границу рамки
    top_border = '#' * (frame_width + 2)
    
    # Генерируем нижнюю границу рамки
    low_border = '#' * (frame_width + 2)
    
    # Определяем ширину текста
    text_width = frame_width - 4
    
    # Разбиваем текст на строки и выравниваем по центру
    center_text = [line.center(text_width) for line in text.split('\n')]
    
    # Объединяем текст с отступами
    framed_text = '\n'.join(['#  {}  #'.format(line) for line in center_text])
    
    # Формируем окончательное сообщение
    message = f"{top_border}\n#  {' ' * ((frame_width - len(' '.join(center_text[0].split()))) // 2)}  #\n{framed_text}\n#  {' ' * ((frame_width - len(' '.join(center_text[-1].split()))) // 2)}  #\n{low_border}"
    
    return message

def load_file(file_path: Path) -> Path:
    # Создание пути для нового файла в основном каталоге
    destination = Path(__file__).parent / Path("conf.py").name 
     # Копирование файла по указанному пути в основной каталог 
    shutil.copy2(file_path, destination) 
    # Возврат пути к созданной копии файла
    return destination 

def search_context(*keywords: str, context: int = 0):
    results = []
    
    # Определяем расширение файла и формируем список всех текстовых файлов
    text_files = [file for file in os.listdir('data') if file.endswith('.txt')]
    
    # Проходим по каждому текстовому файлу
    for filename in text_files:
        with open(os.path.join('data', filename), 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            # Проходим по каждой строчке в файле
            for i, line in enumerate(lines, start=1):
                # Проверяем наличие хотя бы одного ключевого слова в текущей строчке
                if any(keyword.lower() in line.lower() for keyword in keywords):
                    start_index = max(0, i - context - 1)
                    end_index = min(len(lines), i + context)
                    context_lines = lines[start_index:end_index]
                    
                    # Формируем словарь для текущего совпадения
                    result = {
                        'keyword': keywords,
                        'filename': filename,
                        'line': i,
                        'context': context,
                        'text': ''.join(context_lines).strip()
                    }
                    results.append(result)
    
    return results

def important_message(message):
    """
    Выводит важное сообщение с разделителями.
    """
    print("=" * 50)
    print(message)
    print("=" * 50)