#QUEM QUER SER MILIONARIO
import csv

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
    print("OLAAAAAAAA")
    file_path = "./Questions"
    questions = load_questions_from_csv(file_path)
    game(questions)

def game(questions):
    score = 0
    for question in questions:
        print(question.question, question.optionA,
            question.optionB, question.optionC, question.optionD)
        response = input("Resposta: ")
        if response == question.correct:
            print("TA CERTO vais aumentar mil")
            score += 1000
            print(f"O teu score aumentou para: {score}")
            


if __name__ == "__main__":
    main()





