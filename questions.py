class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    def display_question(self):
        print("\n" + self.prompt)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

    def check_answer(self, user_answer):
        return user_answer == self.answer