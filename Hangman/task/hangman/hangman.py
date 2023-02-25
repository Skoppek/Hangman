from random import choice


def game() -> bool:
    words: list[str] = ["python", "java", "swift", "javascript"]
    guess_word: str = choice(words)
    masked_word: str = "-" * len(guess_word)
    guessed_letters = set()

    left_attempts: int = 8

    while left_attempts > 0 and masked_word != guess_word:
        print(masked_word)
        letter: str = input("Input a letter: ")

        if len(letter) != 1:
            print("Please, input a single letter.\n")
            continue

        if not letter.islower() or not letter.isalpha():
            print("Please, enter a lowercase letter from the English alphabet.\n")
            continue

        if letter in guessed_letters:
            print("You've already guessed this letter.\n")
            continue

        guessed_letters.add(letter)

        if guess_word.find(letter) >= 0:

            positions: list[int] = []
            for position, character in enumerate(guess_word):
                if character == letter:
                    positions.append(position)
            for position in positions:
                mask_list = list(masked_word)
                mask_list[position] = guess_word[position]
                masked_word = ''.join(mask_list)
        else:
            print("That letter doesn't appear in the word.")
            left_attempts -= 1

        print()

    if left_attempts > 0:
        print(f"You guessed the word {guess_word}!")
        print("You survived!")
        return True
    else:
        print("You lost!")
        return False


won_games: int = 0
lost_games: int = 0

print("H A N G M A N\n")

while True:
    option: str = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if option == "play":
        if game():
            won_games += 1
        else:
            lost_games += 1
    elif option == "results":
        print(f"You won: {won_games} times.")
        print(f"You lost: {lost_games} times.")
    elif option == "exit":
        break
