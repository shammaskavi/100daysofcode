class QuizBrain:
    def __init__(self, q_list):
        self.qno = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.qno != len(self.q_list) 
        # return self.qno < len(self.q_list) 

    def next_question(self):
        curr_question = self.q_list[self.qno]
        self.qno += 1
        user_answer = input(f"Q.{self.qno}: {curr_question.text} (True/False): ")
        self.check_answer(user_answer, curr_question.answer)

    def check_answer(self, user_answer, correct_ans):
        if user_answer.lower() == correct_ans.lower():
            self.score+=1
            print(f"You got it right!")
        else:
            print("Thats' wrong")
        print(f"The correct answer was {correct_ans}")
        print(f"Your score is {self.score}/{self.qno}")
        print("\n")