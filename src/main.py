# Star Wars Game

class Character:
    def __init__(self, name, power):
        self.name = name
        self.power = power

characters = [
    Character(name='Marrick', power=20),
    Character(name='Eeva', power=20),
    Character(name='Su-Awk', power=20)
]

def choose_character():
    print('Choose a character')
    counter = 1
    for character in characters:
        print(f'{counter}. {character.name}')
        counter += 1
    user_selection = int(input('Selection: '))
    return characters[user_selection - 1]


def start_game():
    print("Star Wars!!!")
    user_character = choose_character()
    print(f'Welcome to Mos Eisley, {user_character.name}!')

def main():
    start_game()


if __name__ == "__main__":
    main()