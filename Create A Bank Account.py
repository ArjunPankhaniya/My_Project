banner=('====================\nwelcome to your bank\n====================\n')
print(banner)
try:
    name=input('Enter Your Name:')
    birthdate=input('Enter Your Birthdate:')
    mobile_number=int(input('Enter Your Mobile Number:'))
except ValueError:
    print('\n*Enter Correct Mobile Number*')
print('\n============================\nAccount Successfully Created\n============================\n')
total=0
print('Current Balance:',total)
flag=0
while True:
    input_value = int(input('\nMenu\n1. To Deposit\n2. To Withdraw\n3. To See Your Balance\n4. To Display Account Information\n\nEnter your choice: '))
    if input_value == 1:
        deposit=int(input('Enter Amount To Deposit:'))
        total += deposit
        print('Deposited Amount:',deposit)
        print('Current Balance:',total)
    elif input_value == 2:
        withdraw=int(input('Enter Amount To Withdraw:'))
        min_balance=float('500')
        min_balance = total - min_balance
        if withdraw>min_balance:
            print('\nInsufficient Balance!!\nBalance Must Be Rs. 500\n')
        else:
            total -=withdraw
            print('\nWithdrawed Amount:',withdraw)
            print('Current Balance:',total)
    elif input_value == 3:
        print('Current Balance:',total)
    elif input_value == 4:
        try:
            print('Name:',name)
            print('Birthdate:',birthdate)
            print('Mobile Number:',mobile_number)
            print('Current Balance:',total)
        except NameError:
            print('\n*Enter Correct Mobile Number*')
    else:
        print('\nTerminating season....')
        break
print('\nFinished.')
