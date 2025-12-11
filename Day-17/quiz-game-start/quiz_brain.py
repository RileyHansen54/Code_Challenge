class QuizBrain:
    def __init__(self,list):
        self.question_number = 0
        self.question_list = list
        self.score = 0
        pass
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number +=1
        self.check_answer(input(f"Q.{self.question_number}: {self.current_question.text} (True or False)"))
    def still_has_questions(self):
        if self.question_number > len(self.question_list):
            return False
        else:
            return True
    def check_answer(self,inp):
        if inp != self.current_question.answer:
            print("You got it Wrong!")
            return False
        else:
            print("You got it Right!")
            print(f"the correct answer is {self.current_question.answer}")
            self.score+=1
            print(f"Your score is {self.score} / {self.question_number}\n")

            return True
