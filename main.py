import os
import random
import sys


class Game():
    def generate_word(self):
        with open("words.txt", "r", encoding="utf-8") as file:
            lines = file.read().splitlines()
            return random.choice(lines)

    def __init__(self):
        self.letters = set()
        self.letters_left = set("abcdefghijklmnopqrstuvwxyz")
        self.is_failed = False
        self.is_won = False
        self.tries = 7
        self.word = self.generate_word()

    def process_fail(self):
        self.is_failed = True
        os.system("clear")
        print(f"You were hanged! Answer was \"{self.word}\"")
        input("Press enter to continue")

    def process_error(self):
        self.tries -= 1
        if self.tries == 0:
            self.process_fail()

    def process_won(self):
        self.is_won = True
        os.system("clear")
        print(f"You won! Answer is \"{self.word}\"")
        input("Press enter to continue")

    def process_correct(self, letter):
        self.letters.add(letter)
        if self.letters == set(self.word):
            self.process_won()

    def add_letter(self, letter):
        skip_step = False
        if len(letter) > 1:
            input("You can enter only one letter. Press enter to continue")
            skip_step = True
        if not skip_step and letter not in self.letters_left:
            input("You entered this letter already. Press enter to continue")
            skip_step = True

        if not skip_step:
            self.letters_left.remove(letter)
            if letter in self.word:
                self.process_correct(letter)
            else:
                self.process_error()

    def print_current_answer(self):
        # print(self.word)
        print("Current answer: ", end='')
        for letter in self.word:
            if letter in self.letters:
                print(letter, end='')
            else:
                print(".", end='')
        print()
        print(f"Tries left: {self.tries}")
        print(f"Available letters: {''.join(sorted(self.letters_left))}")

    def play(self):
        while not (self.is_failed or self.is_won):
            os.system('clear')
            self.print_current_answer()
            next_letter = input('Enter letter: ')
            self.add_letter(next_letter)

def main():
    while True:
        os.system('clear')
        print('------ HANGMAN ------')
        print('1. Start new game')
        print('2. Exit')

        ans = input('Your answer: ')
        if ans == '1':
            os.system('clear')
            game = Game()
            game.play()
        elif ans == '2':
            os.system('clear')
            sys.exit()
        else:
            continue

if __name__ == "__main__":
    main()
