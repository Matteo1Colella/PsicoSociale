import json
import random


def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions


def get_random_questions(questions, num_questions=30):
    return random.sample(questions, num_questions)


def ask_question(question):
    print("\033[1;34m" + question['domanda'] + "\033[0m")
    options = question['altre_risposte'] + [question['risposta_corretta']]
    random.shuffle(options)
    for i, option in enumerate(options):
        print(f"\033[1;33m{i + 1}. {option}\033[0m")
    print("\033[1;31m" + "-" * 50 + "\033[0m")
    return options


def main():
    questions = load_questions('domande.json')
    selected_questions = get_random_questions(questions)

    score = 0
    for question in selected_questions:
        options = ask_question(question)
        answer = int(input("Answer: "))
        if options[answer - 1] == question['risposta_corretta']:
            score += 1
            print("\033[1;32mCorrect!\033[0m")
        else:
            print(f"\033[1;31mWrong Answer, The right one was: {question['risposta_corretta']}\033[0m")
        print()
    percentage = (float)((score / len(selected_questions)) * 100)
    print(
        f"\033[1;36mYou got {score} correct answers out of {len(selected_questions)}. You got a percentage of {percentage}%\033[0m")


if __name__ == "__main__":
    main()