from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for dict in question_data[0]["results"]:
   x = Question(dict["question"],dict["correct_answer"])
   question_bank.append(x)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
   quiz.next_question()
   

   
