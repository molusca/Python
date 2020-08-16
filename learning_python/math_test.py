'''
Take a math test for children who are learning to add integers numbers lesser than 50.
Choose random numbers between 0 and 50, and display the question: "What is the value of a + b?" Where a and b are
random numbers. Ask for the answer. Ask each student 5 questions, show them the questions, correct answers and how many times the student got it right.
'''
from random import randint

def ask_for_answer(question, random_number1, random_number2):
    answer = int(input(f'{question} - How much is: {random_number1} + {random_number2}?: '))
    return answer

def generate_random_number():
    number1 = randint(0, 50)
    number2 = randint(0, 50)
    return number1, number2

def calculate_results(random_number1, random_number2):
    results = random_number1 + random_number2
    return results

def answer_is_correct(student_answer, correct_answer):
    if student_answer == correct_answer:
        return True

print('\nMATH TEST\n')

total_of_correct_answers = 0

for question in range(1,6):
    random_number1, random_number2 = generate_random_number()

    student_answer = ask_for_answer(question, random_number1, random_number2)
    correct_answer = calculate_results(random_number1, random_number2)

    if answer_is_correct(student_answer, correct_answer):
        print(f' Congracts! The correct answer is {correct_answer} !\n')
        total_of_correct_answers += 1

    else:
        print(f' Ops... wrong answer! The correct answer is {correct_answer} !\n')

print(f'YOU ANSWERED CORRECTLY {total_of_correct_answers} TIMES!')

if total_of_correct_answers == 0 or total_of_correct_answers == 1:
    print('You need to practice!!! Let\'s start again? \n')
elif total_of_correct_answers > 1 and total_of_correct_answers <= 3:
    print('You are in the right way! Just a few more tries :) \n')
elif total_of_correct_answers == 4:
    print('ALMOST!!! Just a few more tries and you will ace :) \n')
elif total_of_correct_answers == 5:
    print('NICE!!! YOU ARE THE BEST :D\n')
