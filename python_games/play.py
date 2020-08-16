import hangman.hangman
import guessing_game.guessing_game

def chose_game():
    print()
    print('*****************************************')
    print('******     CHOSE YOUR GAME!!!     *******')
    print('*****************************************')


    print("\n(1) - Hangman, (2) - Guessing Game")

    game = int(input("Wich game?: "))

    if (game == 1):
        print("\nPlaying HANGMAN!\n")
        hangman.hangman.play()
    if (game == 2):
        print("\nPlaying GUESSING GAME!\n")
        guessing_game.guessing_game.play()

if(__name__ == "__main__"):
    chose_game()
