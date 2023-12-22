
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

def main():
    balance = deposit()

main()