from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for quesiton in question_data:
    question_text = quesiton['question']
    question_answer = quesiton["correct_answer"]
    new_ques = Question(question_text, question_answer)
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've Completed the quiz")
print(f"You're final score was {quiz.score}/{quiz.qno}")