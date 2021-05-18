import random


def find_duplicates(seq):  # hledani duplicit
    a = []
    for _ in seq:
        if _ not in a:
            a.append(_)
    if len(a) == 4:
        return True
    else:
        return False


def bullsncows(player, comp):  # hledani bulls a cows
    bulls = 0
    cows = 0
    index = 0
    for i in player:
        if i == comp[index]:
            bulls += 1
            index += 1
        elif i != comp[index] and i in comp:
            cows += 1
            index += 1
        else:
            index += 1
    print("Bulls: ", bulls, ", Cows: ", cows)


ODDELOVAC = ("-" * 30)

riddle = str(random.randint(1000, 10000))       # generovani 4 mistneho cisla
while not find_duplicates(riddle):              # v pripade, ze cislo obsahuje duplicity, vygeneruje nove cislo
    riddle = str(random.randint(1000, 10000))

print("Hi there!")
print(ODDELOVAC)
print("I've generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
print(ODDELOVAC)

game = True  # hra bezi
counter = 1  # pocitadlo

while game:
    guess = str(input("Enter the number: "))  # hadej cislo
    while not find_duplicates(guess) or not guess.isnumeric() or guess[0] == "0":   # kontrola vhodnosti vstupu
        guess = str(input("Wrong input, try again: "))

    if guess == riddle:  # uhodnuti hadanky
        print("Correct, you've guessed the right number in", counter, "guesses!")
        game = False

    elif guess != riddle:  # neuhodnuti hadanky
        bullsncows(guess, riddle)  # hledani bulls and cows
        print(ODDELOVAC)
        counter += 1  # pocitadlo pokusu
