from prompt import string
from brain_games.cli import welcome_user


MAX_ROUND = 3


def engine(module):
    username = welcome_user()
    print(module.RULE)
    current_round = 0
    while current_round < MAX_ROUND:
        current_value, correct_value = module.make_logic()
        print(f"Question: {current_value}")
        answer = string("Your answer: ")
        if answer != str(correct_value):
            print(f'"{answer}" is wrong answer ;(\nCorrect answer was "{correct_value}".')
            print(f"Let's try again, {username}!")
            return
        print("Correct")
        current_round += 1
    print(f"Congratulations, {username}!")
