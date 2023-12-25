import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3



def play():
    symbol_count = {
        "🍒" : 3,
        "🍊" : 6,
        "🫒" : 9,
        "⬜️" : 12,
    }

    # press play/bet
    fruits = []
    selected_fruits  = []

    # append the symbol_count keys in the fruits list based on the values of each key
    for symbol in symbol_count:
        for _ in range(0, symbol_count[symbol]):
            fruits.append(symbol)

    # copy fruits
    fruits_copy = fruits[:]

    # get a random number and append 3 unique numbers into the selected list
    for _ in range(0, 100):
        # shuffle fruits
        random.shuffle(fruits_copy)

        # get a random num
        random_num = random.randrange(0, len(fruits_copy))

        # if random number already in selected list print message
        if random_num in selected_fruits :
            break
        # if selected already has 3 values stop the loop and print message
        elif len(selected_fruits ) == 3:
            # print('selected num is full') 
            break
        # if random number is not in the selected list and selected length isn't 3 ann the random number to the selected list
        else:
            selected_fruits.append(fruits_copy[random_num])  
            del fruits_copy[random_num]
            # print(len(fruits_copy), fruits_copy)

    print(selected_fruits)   
    return selected_fruits    






# collect user deposit
def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print('Amount must be greater then 0.')

        else:
            print('Please enter a number.')

    return amount

# get the number of lines user wants to bet on
def get_number_of_line():
    while True:
        lines = input(f'Enter the number of lines to bet on (1-{MAX_LINES}). ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print('Enter a valid number of lines.')

        else:
            print('Please enter a number.')
    
    return lines

# get the bet amount per line selected
def get_bet_amount_per_line(balance, lines):
    while True:
        max_bet_per_line = balance / lines
        bet_amount = input(f'How much do you want to bet on each line, maximum bet per line is ${max_bet_per_line}?  ')
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if bet_amount <= max_bet_per_line:
                break
            else: 
                print(f'Total bet exceeds current balance of ${balance}, please enter a valid bet amount per line (must be ${max_bet_per_line} or less). ')

        else:
            print('Please enter a number.')
    
    return bet_amount 


def main():
    balance = deposit()
    bet_lines = get_number_of_line()
    bet_per_line = get_bet_amount_per_line(balance, bet_lines)
    total_bet_amount = bet_per_line * bet_lines

    print(f'You are betting ${bet_per_line} per line. Your total bet is ${total_bet_amount}.')
    play()
    

main()