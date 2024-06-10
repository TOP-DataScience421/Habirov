import random
from time import perf_counter
from utils import important_message
from data.vars import N
from data.questions import questions

def display_question(question):
    """
    Выводит вопрос и варианты ответов на экран.
    """
    print(question)
    options = list(questions[question].keys())
    random.shuffle(options)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def quiz_session():
    """
    Основная функция для прохождения викторины.
    """
    important_message("Началась викторина! Отвечайте на вопросы.")
    score = 0
    for _ in range(N):
        question = random.choice(list(questions.keys()))
        display_question(question)
        correct_answer = list(questions[question].keys()).index(
            next(filter(lambda x: questions[question][x], questions[question].keys()))
        ) + 1
        start_time = perf_counter()
        answer = input("Введите номер правильного ответа: ")
        end_time = perf_counter()
        elapsed_time = end_time - start_time
        if elapsed_time <= 5:
            if int(answer) == correct_answer:
                score += 1
        else:
            if int(answer) == correct_answer:
                score += 0.5
    print(f"Игра окончена! Ваш итоговый счет: {score}")

def main():
    """
    Точка входа в приложение.
    """
    quiz_session()

if __name__ == "__main__":
    main()