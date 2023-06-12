import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a four-digit number with each digit unique. Can you guess it?")
    print("You have 12 tries to guess the number correctly.\n")

    digits = list(range(10))
    random.shuffle(digits)
    number = ''.join(map(str, digits[:4]))

    tries = 0
    while tries < 12:
        print("Try #", tries + 1, sep="")
        guess = input("Enter your guess (a four-digit number with all unique digits): ")

        if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4:
            print("Invalid input. Please enter a unique four-digit number.\n")
            continue

        tries += 1

        count = 0
        position = 0

        for i in range(4):
            if guess[i] == number[i]:
                position += 1
            if guess[i] in number:
                count += 1

        print("Number of correctly guessed digits:", count)
        print("Number of digits in the correct position:", position, "\n")

        if guess == number:
            print("Congratulations! You guessed the number correctly!")
            return

        print("Try again!\n")

    print("You have reached the maximum number of tries.")
    print("The number I was thinking of was:", number)

# Play the game
play_game()
