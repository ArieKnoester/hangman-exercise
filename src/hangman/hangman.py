import random
from hangman.words import word_list
from hangman.art import logo, stages
from hangman.util.screen import screen_clear
from hangman.util.exceptions import DuplicateGuessException


class Hangman:

    def __init__(self):
        self.chosen_word = random.choice(word_list)
        self.end_of_game = False
        self.lives = 6
        self.display = [ '_' for letter in self.chosen_word ]

        print(logo)


    def reveal_word(self):
        print(self.chosen_word)


    def _check_guess(self, guess):

        self._check_duplicate_guess(guess)

        for position in range(len(self.chosen_word)):
            letter = self.chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                self.display[position] = letter

        # Check if user is wrong.
        if guess not in self.chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            self.lives -= 1
            self._check_lives()


    def _check_lives(self):
        if self.lives == 0:
            self.end_of_game = True
            print("You lose.")


    def _check_duplicate_guess(self, guess):
        if guess in self.display:
            message = f"You've already guessed {guess}"
            print(message)
            raise DuplicateGuessException(message)


    def _display_game_state(self):
        print(f"{' '.join(self.display)} (lives left: {self.lives})")
        print(stages[self.lives])


    def _check_win_condition(self):
        if "_" not in self.display:
            self.end_of_game = True
            print("You win.")


    def run_game(self):

        while not self.end_of_game:
            guess = input("Guess a letter: ").lower().strip()
            screen_clear()

            try:
                self._check_guess(guess)
            except DuplicateGuessException:
                continue

            self._display_game_state()
            self._check_win_condition()