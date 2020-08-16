from random import randrange
import os

def print_welcome_message():
    print()
    print('*****************************************')
    print('********* Welcome to Hangman!!! *********')
    print('*****************************************')

def carregar_secret_word(): 
    words = []

    script_dir = os.path.dirname(__file__)
    rel_path = "hangman_dictionary.txt"
    abs_file_path = os.path.join(script_dir, rel_path)

    archive = open(abs_file_path , 'r')

    for row in archive:
        row = row.strip()
        words.append(row)
    archive.close()

    word_number = randrange(0, len(words))
    secret_word = words[word_number].lower()

    return secret_word

def start_correct_letters(secret_word):
    return ["_" for letra in secret_word]

def ask_for_guess():
    guess = str(input('\nWich letter?: ')).strip().lower()
    return guess

def keep_correct_guess(guess, correct_letters, secret_word):
    index = 0

    for letra in secret_word:
        if guess == letra:
            print(f'I found the letter "{letra}" in position {index}!')
            correct_letters[index] = letra
        index += 1
    
def keep_incorrect_guess(mistakes):
    print('\nINCORRECT!!!\n')

def draw_gallows(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    print(" |            ")
    print("_|___         ")
    print()

def print_winner_message():
    print("Congracts, you won!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_loser_message(secret_word):
    print("You got hanged!")
    print("The correct word was \"{}\"".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print()
    
def play():

    print_welcome_message()
    secret_word = carregar_secret_word()
    
    correct_letters = start_correct_letters(secret_word)

    hanged = False
    correct_answer = False
    mistakes = 0
        
    while(not hanged and not correct_answer):
        draw_gallows(mistakes)
        print(correct_letters)
        guess = ask_for_guess()
        
        if guess in secret_word:
            keep_correct_guess(guess, correct_letters, secret_word)
        else:
            keep_incorrect_guess(mistakes)
            mistakes += 1

        hanged = mistakes == 5
        correct_answer = '_' not in correct_letters

    if correct_answer:
        print_winner_message()
    else:
        print_loser_message(secret_word)

if(__name__ == '__main__'):
    play()