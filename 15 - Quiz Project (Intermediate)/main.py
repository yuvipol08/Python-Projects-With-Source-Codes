from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list of Question objects from the question data
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create a QuizBrain instance with the question bank
quiz = QuizBrain(question_bank)

# Loop through the questions in the quiz until there are no more questions
while quiz.still_has_questions():
    quiz.next_question()

# Display the final score after completing the quiz
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
