class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.list = q_list
        self.score = 0

    def check_answer(self,user_answer, actual_answer):
        return user_answer.lower() == actual_answer.lower()

    def next_question(self):
        current_question = self.list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} {current_question.answer}(True/False): ")
        if self.check_answer(user_answer,current_question.answer):
            self.score +=1
            print(f"Correct. Your current score is: {self.score}\n")
        else:
            print(f"Wrong Answer. Your score is: {self.score}\n")





