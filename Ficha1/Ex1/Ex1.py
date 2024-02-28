#QUEM QUER SER MILIONARIO
import csv
from random import choice


class Question:
    def __init__(self, number, question, optionA, optionB, optionC, optionD, correct):
        self.number = number
        self.question = question
        self.optionA = optionA
        self.optionB = optionB
        self.optionC = optionC
        self.optionD = optionD
        self.correct = correct



def load_questions_from_csv(file_path):
    questions = []
    with open("./Questions") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            questions.append(Question(row[0], row[1], row[2], row[3],row[4],row[5], row[6]))
    return questions
def main():
    file_path = "./Questions"
    questions = load_questions_from_csv(file_path)
    game(questions)

def fifty(question):
    wrong  = 0

    match question.correct:
        case "a":
            wrong = choice([2, 3, 4])
            print(question.optionA)
        case "b":
            wrong = choice([1, 3, 4])
            print(question.optionB)
        case "c":
            wrong = choice([1, 2, 4])
            print(question.optionC)
        case "d":
            wrong = choice([1, 2, 3])
            print(question.optionD)
    match wrong:
        case 1:
            print(question.optionA)
        case 2:
            print(question.optionB)
        case 3:
            print(question.optionC)
        case 4:
            print(question.optionD)


def game(questions):
    score = 0
    print("Welcome to the game WHO WANTS TO BE A MILIONARE")
    for question in questions:
        print(question.question, question.optionA,
            question.optionB, question.optionC, question.optionD)
        response = input("Resposta: ")
        if response == question.correct:
            score += 1000
        if response == "skip":
            continue
        if response == "50/50":
            fifty(question)
            response = input("Resposta: ")
    print(f"O teu score passou para: {score}")



            


if __name__ == "__main__":
    main()





