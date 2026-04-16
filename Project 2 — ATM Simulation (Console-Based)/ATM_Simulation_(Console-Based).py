a=int(input("Enter 4-digit PIN: "))
Balance=10000
if len(str(a)) == 4:
    while True:
        print("1. Balance: ")
        print("2. Deposit: ")
        print("3. Withdraw: ")
        print("4. Exit: ")
        
        b=int(input("Select an option 1 - 4: "))
        
        if b==1:
            print("Your current balance is this: $", Balance)
        elif b==2:
            c=int(input("Enter amount for deposit: "))
            Balance=Balance+c
            print("Deposited Amount: ", c)
            print("Now your current balance is: ", Balance)
        elif b==3:
            d=float(input("Enter amount for withdraw: "))
            if Balance>0 and Balance>d:
                Balance=Balance-d
                print("Withdraw amount: ", d)
                print("Current Balance: ", Balance)
            else:
                print("Insufficient fund: ")
        elif b==4:
            print("Exiting, Thank you!")
            break
        else:
            print("Invalid Choice, Please Select 1-4: ")
            break
else:
    print("Wrong PIN\nPlease Enter Valid PIN: ")