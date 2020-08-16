from time import sleep
from random import randint

def print_welcome_message():
    print("")
    print("     .-------.    ______                     ")
    print("    /   o   /|   /\     \                    ")
    print("   /_______/o|  /o \  o  \       Welcome     ")
    print("   | o     | | /   o\_____\        to        ")
    print("   |   o   |o/ \o   /o    /     dices.py!    ")
    print("   |     o |/   \ o/  o  /                   ")
    print("   '-------'     \/____o/                    ")
    print("")

def chose_number_of_faces():
    faces = int(input('\nNumber of faces: '))
    return faces

def random_number(faces):
    num = randint(1, faces)
    return num

def print_throwing_message(faces):
    return print(f'\nTHROWING A {faces} FACES DICE (D{faces})! WAIT...')

def print_countdown():
    time = '3...', '2...', '1...', ' '
    for countdown in (time):
        sleep(1)
        print(countdown)

def print_results(num):
    return print('The dice showed: |{:^10}|'.format(num))

def jogar(faces):
    num = random_number(faces)
    print_throwing_message(faces)
    print_countdown()
    print_results(num)

def play_again():
    play = str(input('\nDo you wish to play again? (Y/N): ')).strip().lower()
    print('')
    print('='*50)
    if play == 'y' or play == 'yes':
        return True
    else:
        return False 

def d20():
    print_welcome_message()
    faces = chose_number_of_faces()
    jogar(faces)
    while play_again() == True:
        jogar(faces)

if(__name__ == '__main__'):
    d20()
