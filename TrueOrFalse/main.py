from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

quiz_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    quiz_bank.append(question)


quiz = QuizBrain(quiz_bank)
while quiz.question_number < len(quiz_bank):
    quiz.next_question()

print(f"Your final score: {quiz.score}/{len(quiz_bank)}")