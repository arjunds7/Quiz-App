from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox

THEME_COLOR = "#34656D"


class QuizInterface:
    """The UI of the Quiz using Tkinter"""

    def __init__(self, quiz_brain: QuizBrain):
        """Graphical information of the APP Layout contains Buttons, Labels, Message Box"""
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("THD QUIZ APP")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score 0", fg="white", font=12, bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=350, height=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=300, text='q_text',
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True Button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        # False Button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        # Information Button
        info_image = PhotoImage(file="images/info1.png")
        self.info_button = Button(image=info_image, highlightthickness=0, command=self.infobox, height=25, width=25)
        self.info_button.grid(row=3, column=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        """Takes the Feedback and changes the User SCORE, changes the background again back to white for next question,
        Loads the next question,Disable the buttons once the last question is reached and displays the End Quiz message"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """Provides the feedback to check if the actual answer is 'True' or not"""
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """Provides the feedback to check if the actual answer is 'False' or not"""
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Provide feedback and changes the background color to Green if Correct and Red if Wrong"""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def infobox(self):
        """shows the infobox with information about the quiz"""
        messagebox.showinfo('Information', 'Click the Button with the hook or cross to give your answer.')
