def get_answer(question):
    answers={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    question=str.lower(question)
    return answers.get(question,'Задайте вопрос привет, как дела или пока')

print(get_answer(question=input('Введите свой вопрос: ')))