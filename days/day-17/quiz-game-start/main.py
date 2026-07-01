from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# TODO 2 - Write a for loop to iterate over question_data.
#   Create a Question object from each entry in question data
#   Append each Question object to the question_bank

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)


# TODO - Use the while loop to show the next question until the end
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
print(
    f"You're final score was {quiz_brain.score}/{quiz_brain.question_number}")
