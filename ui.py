from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.label.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='Some question', font=FONT, width=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        true_img = PhotoImage(file='images/true.gif')
        self.true_button = Button(image=true_img, border=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        false_img = PhotoImage(file='images/false.gif')
        self.false_button = Button(image=false_img, border=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='Yo\'ve reached the and of the quiz')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    # def call_check_answer(self) -> str:
    #     is_correct = self.quiz.check_answer()
    #     if is_correct:
    #         print('You are right!')
    #         return 'True'
    #     else:
    #         print('You are wrong!')
    #         return 'False'

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)


class CategorySelectInterface:
    def __init__(self):
        self.selected_category = 'General'

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=5, pady=170)

        self.label = Label(text='Select a category', bg=THEME_COLOR, fg='white', font=FONT)
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        
        self.select_button_general = Button(text='General', width=15, border=0, command=self.general_selected)
        self.select_button_general.grid(row=1, column=0, padx=20, pady=20)

        self.select_button_cs = Button(text='Computer Science', width=15, border=0, command=self.cs_selected)
        self.select_button_cs.grid(row=1, column=1, padx=20, pady=20)

        self.select_button_history = Button(text='History', width=15, border=0, command=self.history_selected)
        self.select_button_history.grid(row=2, column=0, padx=20, pady=20)

        self.select_button_music = Button(text='Music', width=15, border=0, command=self.music_selected)
        self.select_button_music.grid(row=2, column=1, padx=20, pady=20)

        self.window.mainloop()

    def general_selected(self):
        self.selected_category = 'General'
        self.window.destroy()

    def cs_selected(self):
        self.selected_category = 'Cs'
        self.window.destroy()

    def history_selected(self):
        self.selected_category = 'History'
        self.window.destroy()

    def music_selected(self):
        self.selected_category = 'Music'
        self.window.destroy()
