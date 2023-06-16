import random
import time
import sys

class HangmanGame:
    def __init__(self):
        # Initialize the game with necessary variables
        self.words_to_guess = ["chocolates", "books", "photography", "cinema", "city", "peace", "magazines", "toys", "songs", "parents", "legos"]
        self.limit = 8 # Number of guesses allowed
        self.count = 0  # Current number of incorrect guesses
        self.already_guessed = []  # List to store already guessed letters
        self.word = ""    # Word to be guessed
        self.display = ""  # Displayed word with guessed letters

# Display a welcome message and get player's name
    def welcome(self):
        print("\nWelcome to the Ultimate Hangman game\n")
        self.name = input("Enter your name: ")
        print("Hello " + self.name + "! Best of Luck!")
        time.sleep(2)
        print("Game Starting!\n Let's play Hangman!")
        time.sleep(3)

# Randomly select a word from the list of words to guess
    def select_word(self):
        self.word = random.choice(self.words_to_guess)
        self.length = len(self.word)
        self.display = '_ ' * self.length

# Prompt the player to play again or exit the game
    def play_loop(self):
        play_game = input("Do you want to play again? (y = yes, n = no)\n").lower()
        while play_game not in ["y", "n"]:
            play_game = input("Do you want to play again? (y = yes, n = no)\n").lower()
# Reset game variables and select a new word            
        if play_game == "y":
            self.count = 0
            self.already_guessed = []
            self.select_word()
            self.play()
        else:
            print("Thanks For Playing! See you again!")
            sys.exit("Bye!") 

# Main game logic for guessing the word and determining the outcome
    def hangman(self):
        guess = input("This is the Hangman Word: " + self.display + " Enter your guess:\n").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input, Try a letter\n")
            self.hangman()
        elif guess in self.already_guessed:
            print("Try another letter.\n")
        else:
            self.already_guessed.append(guess)
            if guess in self.word:
                self.update_display(guess)
                print(self.display + "\n")
            else:
                self.count += 1
                self.print_hangman()

                if self.count == self.limit:
                    print("Wrong guess. You are hanged!!!")
                    print("The word was:", self.word)
                    self.play_loop()
                else:
                    print("Wrong guess. " + str(self.limit - self.count) + " guesses remaining\n")

# Update the display with the correctly guessed letter
    def update_display(self, guess):
        indices = [i for i, letter in enumerate(self.word) if letter == guess]
        self.display = ' '.join([letter if index in indices else self.display[index*2] for index, letter in enumerate(self.word)])

# Print the current stage of the hangman        
    def print_hangman(self):
        stages = [
            "       \n"
            "       \n"
            "       \n"
            "       \n"
            "        \n"
            "       \n"
            "       \n"
            "____\n",

            "        \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "__|__\n",

            "   _____ \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "  |      \n"
            "  |      \n"
            "  |     \n"
            "__|__\n",
            
            "   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "__|__\n",

            "   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |      \n"
            "  |      \n"
            "__|__\n",

            "   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |     | \n"
            "  |      \n"
            "__|__\n"
            
             "   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |    /| \n"
            "  |       \n"
            "__|__\n",
            
             "   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |    /|\ \n"
            "  |       \n"
            "__|__\n",
            
             "   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |    /|\ \n"
            "  |    /  \n"
            "__|__\n",
            
             "   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |    /|\ \n"
            "  |    / \ \n"
            "__|__\n"
        ]

        if self.count < len(stages):
            print(stages[self.count])
        else:
            print("Hanging stage not found.")

# Start the game by displaying the welcome message, selecting a word, and playing the hangman game
    def play(self):
        self.welcome()
        self.select_word()
        self.hangman()

        while True:
            if self.display.replace(" ", "") == self.word:
                print("Congrats! You have guessed the word correctly!")
                self.play_loop()
            else:
                self.hangman()

# Create an instance of the HangmanGame class and start the game
hangman_game = HangmanGame()
hangman_game.play()
