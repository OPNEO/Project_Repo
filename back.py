import random
def read_file():
    with open('diceoutput/single_dict.txt','r') as fileread:
        fileread.readlines()
        fileread.close()
    with open('diceoutput/dual_dice.txt','r') as fileread:
        fileread.readlines()
        fileread.close()
history_of_single_dice=list()
history_of_dual_dice=list()
print('Welcome to Dice Games')
def single_dice_show_history(dice):
    for i,x in enumerate(dice,1):
        print(f'{i}.{x}')
def multiple_dice_history(dice):
    for i,x in enumerate(dice,1):
        print(f'{i}.{x}')
def roll_dice():
    numbers=random.randint(1,6)
    return numbers
while True:
    print('#'*25)
    continue_output=int(input('vroo wanna play  \n1.Yes\n2.No\n3.History\n4.save_history_to_file:\n'))
    if continue_output==1:
        option=int(input('1.Dice or 2.Dice'))
        if option==1:
            roll_input=roll_dice()
            roll_output=f'Single Dice number is {roll_input} \n'
            print(roll_output)
            history_of_single_dice.append(roll_output)
        elif option==2:
            roll1input=roll_dice()
            roll2input=roll_dice()
            dual_dice_history=f'Dual Dice Number is {roll1input},{roll2input} \n'
            print(dual_dice_history)
            history_of_dual_dice.append(dual_dice_history)
    elif continue_output==2:
        print('Goodbye! Thanks for playing.')
        break
    elif continue_output==3:
        dice_history_option=int(input('1.Single Dice History \n2.Dual Dice History'))
        if dice_history_option==1:
            print('#'*5,'Single Dice Histoy','#'*5)
            single_dice_show_history(history_of_single_dice)
        else:
            print('#'*5,'Dual Dice Histoy','#'*5)
            multiple_dice_history(history_of_dual_dice)
    elif continue_output==4:
        with open('diceoutput/single_dict.txt', 'w') as file:
            file.writelines(history_of_single_dice)
            file.close()
        with open('diceoutput/dual_dice.txt', 'w') as file:
            file.writelines(history_of_dual_dice)
            file.close()
    else:
        print('Choose A Valid option Between 1 2 3')
