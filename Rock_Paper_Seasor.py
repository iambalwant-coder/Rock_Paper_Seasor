import random
while True:

        # Rock Paper Scissors ASCII Art

    # Rock
    game_sings=[("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)

    """),

    # Paper
    ("""
        ________
    ---'    ____)_
            ______)
            _______)
            _______)
    ---.__________)

    """),

    # Scissors
    ("""
        _______
    ---'   ____)____
            ________)
        __________)
        (______)
    ---.__(__)

    """)]


    user_choice = int(input("""
    Enter your Choice :-
    0. For Rock
    1. For Paper
    2. For Scissors
    ==========================
    """))

    if user_choice < 0 or user_choice >=3: 
        print('Wrong Choice, Enter valid choice.')

    else:
        choice = ['ROCK', 'PAPER', 'SCISSORS']
        print(f'User Choosen {choice[user_choice]} = {game_sings[user_choice]}')

        computer_choice = random.randint(0, 2) 
        print(f'Coputer Choosen {choice[computer_choice]} = {game_sings[computer_choice]}')

        if user_choice == computer_choice: # Condition if user and computer choice are same 
            print('-: Game Draw :- ')

        elif user_choice == 0 and computer_choice == 2:
            print("-: You Win :-")

        elif user_choice == 2 and computer_choice == 0:
            print("-: You Lose :-")

        elif user_choice < computer_choice:
            print("-: You Lose :-")

        elif user_choice > computer_choice:
            print("-: You Win :-")
        
        print('-------------------------------------')


    exit = int(input('''
    Do you want continue :-
    1. For YES
    2. For exit
    '''))

    if exit == 2:
        print('-:EXIT:-')
        break

