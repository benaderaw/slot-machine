MAX_LINES = 3

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

# get the number of lines user wants to be on
def get_number_of_line():
    while True:
        lines = input(f'Enter the number of lines to bet on (1-{str(MAX_LINES)}). ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print('Enter a valid number of lines.')

        else:
            print('Please enter a number.')
    
    return lines



def main():
    balance = deposit()
    bet_lines = get_number_of_line()

    print(balance, bet_lines)

main()