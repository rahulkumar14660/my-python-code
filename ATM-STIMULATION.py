message = '''Please choose your option
1-> Check balance
2-> Deposit amount
3-> Withdarwal'''
print(message)

task = int(input('Enter your option '))
available_amount = 5000

if(task>=1) and (task<=3):
    # 1 balance
    if task == 1:
        check_message = f"Your available balance is {available_amount}"
        print(check_message)

        #balance checked
        
    # 2 deposit
    elif task == 2:
        #deposit
        deposit_amount = int(input('Please enter your depsoit amount '))
        if deposit_amount > 0:
            available_amount += deposit_amount
            print('Your have successfully deposited your amount')
            check_message = f"Your available balance is {available_amount}"
            print(check_message)
            
            
        else:
            print('Please give your valuable amount')

    else:
        withdrawal_amount = int(input('Please enter your withdrawal amount '))
        if withdrawal_amount <= available_amount:
            available_amount -= withdrawal_amount
            print('Your have successfully withdrawal your amount')
            check_message = f"Your available balance is {available_amount}"
            print(check_message)
        else:
            print('Insufficient balance')        
else:
    print('Please corret option')