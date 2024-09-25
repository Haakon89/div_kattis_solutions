number_of_questions = int(input())
score = 0
List_of_answers = []
for i in range(number_of_questions):
    List_of_answers + input()


for i in range(number_of_questions-1):
    current_answer = input()
    if(previous_answer == current_answer):
        score += 1
print(score)