import prompt


def welcome_user():
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    return username
