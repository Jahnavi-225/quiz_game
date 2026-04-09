import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        random.shuffle(self.questions)

        for question in self.questions:
            question.display_question()

            while True:
                try:
                    user_answer = int(input("Enter your choice (1-4): "))
                    if 1 <= user_answer <= len(question.options):
                        break
                    else:
                        print("Please enter a valid option (1-4).")
                except ValueError:
                    print("Invalid input! Please enter a number.")

            if question.check_answer(user_answer):
                print(" Correct!\n")
                self.score += 1
            else:
                print(" Incorrect!\n")

        print(f"\n Final Score: {self.score}/{len(self.questions)}")