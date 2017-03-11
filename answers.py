def get_answer(question):
	answers={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
	question=str.lower(question)
	return answers.get(question)

if __name__ == '__main__':
	print(get_answer('Как дела'))