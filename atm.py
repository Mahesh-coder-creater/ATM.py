print("Welcome to ABC Bank !!")
pin = 2996
chances = 3
balance = 50000
while chances !=0:
    user_pin = int(input("Please enter the four digit pin"))
    if user_pin !=pin :
        chances -= 1
        print("Wrong pin number")
        print(f" You have {chances} chances left")
    else:
        user_choice = input("B : balance, D : deposit, W : withdraw")
        if user_choice == "B":
            print(f" Your total balance is Rs.{balance}")
            
        if user_choice == "D":
            deposit_user = int(input("Enter the amount that you would like to deposit : "))
            total_balance = deposit_user + balance
            print(f"You have deposited Rs.{deposit_user}")
            print(f"Your total balance is Rs.{total_balance}")
            
        if user_choice == "W":
            withdraw_user = int(input("Enter the amount you want to withdraw :"))
            total_balance = balance - withdraw_user
            print(f"You have withdrawn Rs.{withdraw_user}")
            print(f"Your total balance is Rs.{total_balance}")
            
    user_exit = input("Would like to exit? Yes/No")
    if user_exit == "Yes":
        print("Thankyou for using ABC bank !!")
        break
    else:
        continue
