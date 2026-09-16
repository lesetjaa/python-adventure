from tkinter import *  # type: ignore
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizeUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Trivia")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score
        self.score_label = Label(text="score: 0")
        self.score_label.config(bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            font=FONT,
            text="Questions go here",
            fill=THEME_COLOR,
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Images
        correct_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")

        # Buttons
        self.correct_btn = Button(
            image=correct_img, highlightthickness=0, command=self.correct_guess)
        self.correct_btn.grid(row=2, column=0)

        self.wrong_btn = Button(
            image=wrong_img, highlightthickness=0, command=self.wrong_guess)
        self.wrong_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You have reached the end of the quiz!\nThank You for Playing")
            self.wrong_btn.config(state="disabled")
            self.correct_btn.config(state="disabled")

    def correct_guess(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def wrong_guess(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
