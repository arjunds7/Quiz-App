import html


class QuizBrain:
    """This class contains the logic/brain of the quiz"""

    def __init__(self, q_list):
        """The Quiz is initiliased with question number and score"""
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Check if there is still more questions to be loaded"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Display the next question from the database(API)"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """Checks if the user answer is same as the actual answer of the question"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False