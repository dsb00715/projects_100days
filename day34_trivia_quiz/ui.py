from tkinter import *
from quiz_brain import QuizBrain

# constants
THEME_COLOR = "#375362"
SCORE_FONT = ("Arial", 10, "bold")
QUE_FONT = ("Arial", 20, "italic")
RIGHT_IMG = r"day34_trivia_quiz\images\true.png"
WRONG_IMG = r"day34_trivia_quiz\images\false.png"


class QuizGui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, highlightthickness=0)

        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            padx=20,
            pady=20,
            font=SCORE_FONT,
        )
        self.score_label.grid(row=0, column=1, sticky="EW")

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_label = self.canvas.create_text(
            150, 125, text="Question", fill=THEME_COLOR, font=QUE_FONT, width=280
        )

        right_image = PhotoImage(file=RIGHT_IMG)
        self.right_button = Button(
            image=right_image,
            highlightthickness=0,
            command=lambda: self.give_feedback("True"),
        )
        self.right_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file=WRONG_IMG)
        self.wrong_button = Button(
            image=wrong_image,
            highlightthickness=0,
            command=lambda: self.give_feedback("False"),
        )
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_label, text="You've reached the end of the quiz."
            )
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def give_feedback(self, user_ans):
        is_right = self.quiz.check_answer(user_answer=user_ans)
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, func=self.get_next_question)
