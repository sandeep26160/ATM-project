print("***                               ***")
print("***    Welcome to Bank            ***")
print("***                               ***")
print("*************************************")
pin = 7890
chances = 3
balance = 5000
total_balance = 5000
mobile_nos = [9335210335, 9988776655]

while chances != 0:
    user_pin = int(input("Please Enter Four Digit Pin:\n"))
    if user_pin != pin:
        chances -= 1
        print("Wrong pin Number")
        print(f"You have {chances} chances left")
        if chances == 0:
            print("Your ATM card is blocked for 24 hours")
            exit()
    else:
        print("######### Select option using uppercase #####")
        user_choice = input(''' B: Balance inquiry
 D: Deposite
 W: Cash Withdraw
 C: Change your PIN
 O: Other services\n''')

        if user_choice == "B":
            print(f"Your total balance is RS.{balance}")
        elif user_choice == "D":
            deposit_user = int(input("Enter the amount that you want to deposit:\n"))
            total_balance = deposit_user + balance
            balance = total_balance
            print(f"You have deposited Rs.{deposit_user}")
            print(f"Your total balance is Rs.{total_balance}")
        elif user_choice == "W":
            withdraw_user = int(input("Enter the amount you want to withdraw:\n"))
            if withdraw_user > balance:
                print("     SORRY\n     ")
                print("Your Account has insufficient balance.")
                exit()
            else:
                total_balance = balance - withdraw_user
                print(f"You have withdrawn RS.{withdraw_user}")
                print(f"Your total balance is RS.{total_balance}")
        elif user_choice == "C":
            user_pin = int(input("Please Enter Your Four Digit Pin:\n"))
            if user_pin != pin:
                chances -= 1
                print("You typed the wrong PIN number.")
                print(f"You have {chances} chances left")
                if chances == 0:
                    exit()
            else:
                print("Enter your new PIN number:")
                new_pin = int(input())
                print("Confirm your new PIN:")
                new_pin_again = int(input())
                if new_pin == new_pin_again:
                    print("Your new Pin is Set!!!")
                    pin = new_pin
                else:
                    print("PINs do not match. Please try again.")
        elif user_choice == "O":
            print("!!! Select option using uppercase !!!")
            service = input(" M: Mobile top-up\n")
            if service == "M":
                mobile_no = int(input("Enter your mobile no.\n"))
                mob_n_a = int(input("Confirm your mobile number:\n"))
                if mobile_no == mob_n_a:
                    if mobile_no in mobile_nos:
                        E_top = int(input("Enter amount you want to top-up:\n"))
                        if E_top > balance:
                            print("    :-(SORRY  :-(   ")
                            print("You do not have enough balance")
                            print("!!! Thank you for using our services !!!")
                            exit()
                        else:
                            balance -= E_top
                            print("Transaction successful")
                            print("Thank you for using our service")
                    else:
                        print("This mobile number does not exist")
                        print("Thank you")
                        exit()
            user_exit = input("Would You like to exit ?\n Y:Yes\n N:No\n")
            if user_exit == "Y":
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("!!!                        !!!")
                print("!!!  Thank you for using Bank !!!")
                print("!!!                        !!!")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                exit()
            else:
                continue
