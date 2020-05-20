import time  # import time to sleep some times
import random  # import random to select random objects
# Confugre List Of Objects
# Confugre List Of Objects
Places = ['Forest', 'Desert', 'House']
Weapons = ['Sword', 'Knife', 'Gun', 'Rock']
Forest_Monsters = ['Bear', 'Rabbit', 'Lion', 'Wolf', 'Monkey']
Desert_Monsters = ['Alien', 'Giant Monster', 'Snake', 'Dog']
House = ['Eat', 'Drink', 'Sleep', 'Wach Movie']
Game_Result = ['Win', 'Lose']
UserResponse = ['yes', 'no', 'y', 'n']
Monster = ''
# End Configuration
# Define Function To print Messagess


def GetUserChoise(Input):
    if (Choise.lower() == 'Forest'.lower() or
        Choise.lower() == 'F'.lower() or
            Choise == '1'):
        return 'Forest'
    elif (Choise.lower() == 'Desert'.lower() or
          Choise.lower() == 'D'.lower() or
          Choise == '2'):
        return 'Desert'
    elif (Choise.lower() == 'House'.lower() or
          Choise.lower() == 'H'.lower() or
          Choise == '3'):
        return 'House'
    else:
        return ''


def GetUserMonster(UserChoise):
    if UserChoise == 'Forest':
        print(random.choice(Forest_Monsters))
    if UserChoise == 'Desert':
        print(random.choice(Desert_Monsters))
    if UserChoise == 'House':
        print(random.choice(House))


def PrintSleep(msg, seconds):
    print(msg + '\n')
    time.sleep(seconds)


def ChangeWeapon():
    changerequest = input('would you like to change weapon\n')
    if changerequest == 'yes':
        weaponchoosed = random.choice(Weapons)
        print(weaponchoosed)


# Game Will Start
RetryGame = 'y'
while RetryGame == 'y':
    PrintSleep('Welcome to the game of adventures fun game ', 2)
    PrintSleep('takes you to another world of fun and thrill', 2)
    PrintSleep(
        'We will help you during the game choices'
        'but you have to think well before each selection so you can win',
        2)
    name = input('Please Enter Your Name To Start Game \n')
    time.sleep(1)
    print('Please Choose Witch Place you want to play \n')
    time.sleep(1)
    for place in Places:
        print(place)
        time.sleep(1)
    Choise = ''
    while Choise not in Places:
        msg = 'Give me your choise for forest write f or forest'\
            'or 1\n for desert write desert or d or 2 \nfor'\
            'house write house or h or 3\n'
        Choise = input(msg)
        Choise = GetUserChoise(Choise)
    time.sleep(2)
    print('you have a weapon ')
    weaponchoosed = random.choice(Weapons)
    print(weaponchoosed)
    ChangeWeapon()
    print('\nyou now in ' + Choise + ' and you have a weapon ' + weaponchoosed)
    time.sleep(1)
    print('now you see fornt of you ')
    GetUserMonster(Choise)

    time.sleep(2)
    PrintSleep('Use weapon to kill monster', 2)
    if (weaponchoosed == 'Rock' or weaponchoosed == 'Sword' or weaponchoosed ==
            'Gun' or weaponchoosed == 'Knife') and Monster == 'Rabbit':
        print('you Win')
        time.sleep(2)
        print('Game Over')
    elif Choise == 'House':
        print('you Win')
        time.sleep(2)
        print('Game Over')
    else:
        print('you ' + random.choice(Game_Result))
        time.sleep(2)
        print('Game Over')
    RetryGame = input(
        'Would You Like to try again for yes write y for no write n')
    while RetryGame not in UserResponse:
        print('Invalid input please choose yes or no or y or n')
        RetryGame = input(
            'Would You Like to try again for yes write y for no write n\n')
