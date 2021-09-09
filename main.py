from question_model import Question
from data import question_data_dict
from quiz_brain import QuizBrain
from ui import QuizInterface, CategorySelectInterface

category_select_ui = CategorySelectInterface()
selected_category = category_select_ui.selected_category
print(selected_category)

question_bank = []
for question in question_data_dict[selected_category]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    print(question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
