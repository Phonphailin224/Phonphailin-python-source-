# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw") ถอนเท่าไหร่
        print("3. Deposit") ฝากเท่าไหร่
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice ==4:
            print("Thank you for use our ATM")
            break
        if choice == "1":
            print("Now ,you have: ", balance)

        if choice == "2":
            banana =float(input("Whitdraw amout : ")) 
            balance = balance - banana
            print("Now, you have: ", balance)

            if choice == "3":
                deposit =float(input("Deposit amount: "))
                balance = balance - deposit
                print("Now, you have: ", balance)


else:
    print("Invalid PIN")
