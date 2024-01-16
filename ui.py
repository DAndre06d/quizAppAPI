from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.score = quiz.score
        self.question_number = 0
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.score = Label(text=f"Score: {self.score}", bg=THEME_COLOR, font=("Arial", 15, "bold"), fg="white")
        self.score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,125, text="Some Question", font=("Arial",16, "italic"),
            fill=THEME_COLOR, width=280
        )
        self.true = PhotoImage(file="images/true.png")
        self.wrong = PhotoImage(file="images/false.png")
        self.right_button = Button(image=self.true, command=self.left_but)
        self.wrong_button = Button(image=self.wrong, command=self.right_but)
        self.right_button.grid(column=0, row=2)
        self.wrong_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def left_but(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def right_but(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



