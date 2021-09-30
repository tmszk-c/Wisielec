import sys

# Dodaj właściwą walidacje, czy urzytkownik wpisuje tylko jedną literę
# nie pozwól żeby urzytkownik nie wpisał pora 2 tą samo literę
# lista sołów do losowania - zewnętrzna biblioteka


no_of_tries = 5
world = "tomasz"
used_letters = []
user_word = []

def show_state_of_game():
    print()
    print(user_word)
    print('pozostało prób: ', no_of_tries)
    print('urzyte litery: ', used_letters)
    print()

def find_indexes(world, letter):
    indexes = []

    for index, letter_in_word in enumerate(world):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

for _ in world:
    user_word.append('_')

while True:
    letter = input('Podaj literę: ')
    used_letters.append(letter)

    found_indexes = find_indexes(world, letter)

    if len(found_indexes) == 0:
        print('nie ma takiej litery')
        no_of_tries -= 1
        if no_of_tries == 0:
            print('koniec gry')
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter
    if "".join(user_word) == world:
        print('brawo to jest to słowo')
        sys.exit(0)

    show_state_of_game()
