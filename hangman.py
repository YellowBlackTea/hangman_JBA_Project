import random

random.seed()


def hephen_print(num, char, word, hephen):
    for i in range(num):
        if char == word[i]:
            print(char)
            hephen = hephen[:i] + char + hephen[i + 1:]
    return hephen


def is_aplha(word):
    try:
        return word.encode('ascii').isalpha()
    except:
        return False


def check_input(word, hephen):
    b = True
    b1 = False
    while b:
        if b1:
            word = input()
            b1 = False
        if len(word) != 1:
            print("Please, input a single letter.")
            print(hephen)
            print("Input a letter:")
            b1 = True
        elif not word.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
            print(hephen)
            print("Input a letter:")
            b1 = True
        elif not is_aplha(word):
            print("Please, enter a lowercase letter from the English alphabet.")
            print(hephen)
            print("Input a letter:")
            b1 = True
        else:
            b = False

    if not b:
        return word


def hangman(word, keep_progress):
    i = 0
    attempts = 8
    list_already = []

    while i < attempts:
        print("Input a letter:")
        # guess = input()
        guess = check_input(input(), keep_progress)
        for c in word:
            if guess == 'v':
                for s in keep_progress:
                    if s == guess:
                        print("You've already guessed this letter.")

                if c == word[-1]:
                    print("That letter doesn't appear in the word.")
                    print(keep_progress)
                    i += 1
                    break

                keep_progress = hephen_print(len(word), guess, word, keep_progress)
                print(keep_progress)
                break

            if guess == c:
                for s in keep_progress:
                    if s == guess:
                        print("You've already guessed this letter.")
                        break
                keep_progress = hephen_print(len(word), c, word, keep_progress)
                print(keep_progress)
                break

            elif guess in list_already:
                print("You've already guessed this letter.")
                keep_progress = hephen_print(len(word), guess, word, keep_progress)
                print(keep_progress)
                break

            if c == word[-1]:
                print("That letter doesn't appear in the word.")
                print(keep_progress)
                i += 1
                break
            else:
                continue
        list_already.append(guess)
        # print(i)
        if keep_progress == word and i < attempts:
            return 1
    return 0


def play(won, lost):
    list_words = ["python", "java", "swift", "javascript"]
    word = list_words[random.randint(0, 3)]
    keep_progress = "-" * len(word)

    print(keep_progress)
    if hangman(word, keep_progress) == 1:
        print("You guessed the word", word + "!")
        print("You survived!")
        won += 1

    else:
        print("You lost!")
        lost += 1

    return won, lost


def menu():
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    return input()


def main():
    nb_win = 0
    nb_lost = 0
    print("H A N G M A N")
    print()

    while True:
        m = menu()
        if m == "play":
            nb_win, nb_lost = play(nb_win, nb_lost)
            print()

        if m == "results":
            print("You won:", nb_win, "times.")
            print("You lost:", nb_lost, "times.")
            print()

        if m == "exit":
            return


if __name__ == "__main__":
    main()