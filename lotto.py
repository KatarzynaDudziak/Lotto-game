import random
import time
import os


class Config:
    def __init__(self, start, stop, to_draw, difficulty, money):
        self.start = start
        self.stop = stop
        self.to_draw = to_draw
        self.difficulty = difficulty
        self.money = money


# Ask user about level
def get_level_from_console(configs):
    print('Choose difficulty level:')
    i = 0

    for element in configs:
        print(f'{i} - {element.difficulty}')
        i += 1

    try:
        used_config = int(input())
        return used_config
    except ValueError:
        print("Error")
        exit()


# Checking the correctness of the level selection
def choose_level(configs) -> int:
    used_config = get_level_from_console(configs)

    if used_config < 0 or used_config >= len(configs):
        print('There is no such level!')
        exit()

    print(f'Selected level: {configs[used_config].difficulty}')
    return used_config


# Data input
def get_numbers(config: Config):
    print(f'Enter your {config.to_draw} unique numbers (from {config.start} to {config.stop})'
          f' separated by a comma:')
    input_numbers = input()

    given_numbers = set()

    for element in input_numbers.split(","):
        try:
            given_numbers.add(int(element))
        except ValueError:
            print('ERROR: numbers must be separated by only one comma!')
            exit()

    if len(given_numbers) != config.to_draw:
        print('Invalid data entered!!')
        exit()

    for element in given_numbers:
        if element < config.start or element > config.stop:
            print('The numbers do not belong to the given range!')
            exit()
    return given_numbers


# Draw numbers
def draw_numbers(config: Config):
    print('We start the draw:')
    time.sleep(1)

    random_numbers = set()

    while len(random_numbers) < config.to_draw:
        random_number = random.randint(config.start, config.stop)
        if random_number not in random_numbers:
            print(random_number)
            time.sleep(1)
        random_numbers.add(random_number)
    return random_numbers


# Win check
def check_winnings(numbers1, numbers2):
    numbers_hit = set(numbers1) & set(numbers2)

    hit = ', '.join(str(x) for x in numbers_hit)

    if len(numbers_hit):
        print(f'The numbers hit: {hit}')
    else:
        print('Try again!')
    return numbers_hit


# A function that assigns a winning amount
def winnings_money(config: Config, numbers_hit):
    win_money = 0

    if len(numbers_hit) > 1:
        print(f'You win {config.money}!')
        win_money += config.money
    else:
        print('Next time you will win!')
    time.sleep(1)
    return win_money


# choosing to continue playing or ending it
def to_keep_playing():
    print('Do you want to keep playing?')
    choice = ['yes', 'no']
    i = 0

    for element in choice:
        print(f'{i} - {element}')
        i += 1

    try:
        user_choice = int(input())
        return user_choice
    except ValueError:
        print('Incorrect data!')
        return 1


def main():
    configs = [
        Config(1, 10, 3, 'easy', 10),
        Config(1, 50, 6, 'normal', 20),
        Config(1, 100, 8, 'hard', 30)]

    win_money = 0
    user = 0

    while user == 0:
        os.system('cls')
        level = choose_level(configs)
        used_config = configs[level]
        numbers = get_numbers(used_config)
        selected_numbers = draw_numbers(used_config)
        win_numbers = check_winnings(selected_numbers, numbers)
        win_money += winnings_money(used_config, win_numbers)
        print(f'You have {win_money} money!')
        user = to_keep_playing()
    print('See you next time! :)')


if __name__ == '__main__':
    main()
