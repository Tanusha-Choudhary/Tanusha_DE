class Quiz:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list= q_list
        self.score = 0
    def stil_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer1 = input(f"Could you answer the question\n{self.question_number}:{current_question.question} True/False:")
        self.check_answer(answer1,current_question.answer)

    def check_answer(self,answer1,answer2):
        if answer1.lower() == answer2.lower():
            print("Correct")
            self.score+=1
        else:
            print("Incorrect")
        print("the correct answer is ",answer2)
        print(f"Your current score is:{self.score}/{len(self.question_list)}")
        print("\n")

# Q=Quiz()
# Q.next_question()
