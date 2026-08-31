# Percentage of Correct Answers 
# Input total questions and correct answers, and calculate the percentage score.

questions = int(input("Enter total number of questions: "))

correct_answers = int(input("Enter total number of correct answers: "))

percentage_score = (correct_answers / questions) * 100

print(f"Percentage score is: {percentage_score}")