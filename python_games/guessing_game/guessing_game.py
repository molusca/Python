from random import randint

def play():
    print()
    print('*****************************************')
    print('******* Welcome to GUESSING GAME! *******')
    print('*****************************************')

    secret_number = randint(1, 101)
    points = 1000


    print("\nDIFICULTIES")
    print("(1) - Easy, (2) - Medium, (3) - Hard")
    dificulty = int(input("Chose a dificulty: "))
    if(dificulty == 1):
        attempts = 10
    elif(dificulty == 2):
        attempts = 6
    elif(dificulty == 3):
        attempts = 3


    for round in range(1, attempts +1):
        print(f'\nTry {round} of {attempts}')
        guess = int(input('\nType a number between 1 and 100: '))
        print(f'Your guess is {guess}!\n')

        corret_guess = secret_number == guess
        higher_guess = guess > secret_number
        lower_guess = guess < secret_number

        if(guess < 1 or guess > 100):
            print("ERROR! You should type a number between 1 AND 100!")
            continue

        if (corret_guess):
            print(f'Correct answer. You got {points} points!')
            print('You won!\n')
            break
        else:
            if (higher_guess):
                print(f'Incorrect guess! The secret number is lower than {guess} !\n')
            elif (lower_guess):
                print(f'Incorrect guess! The secret number is higher than {guess} !\n')
            lost_points = abs(secret_number - guess)
            points -= lost_points
        print('='*40)

if(__name__ == "__main__"):
    play()