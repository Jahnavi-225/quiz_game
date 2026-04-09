from quiz import Quiz
from questions import Question

# List of questions
questions = [
    Question(
        "What is the capital of France?",
        ["London", "Paris", "Berlin", "Rome"],
        2
    ),
    Question(
        "Which planet is known as the Red Planet?",
        ["Earth", "Mars", "Jupiter", "Saturn"],
        2
    ),
    Question(
        "What is 2 + 2?",
        ["3", "4", "5", "6"],
        2
    ),
    Question(
        "Who wrote 'To Kill a Mockingbird'?",
        ["Harper Lee", "Jane Austen", "J.K. Rowling", "Stephen King"],
        1
    ),
    Question(
        "Who made the Harry Potter films?",
        ["J.K. Rowling", "Warner Bros", "Marvel", "Potterhead"],
        2
    )
]

# Run quiz
quiz = Quiz(questions)
quiz.run_quiz()