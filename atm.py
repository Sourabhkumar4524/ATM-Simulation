from utils import display_menu
class ATM:
    def __init__(self,account):
        self.account = account

    def login(self):
        account_number = int(input("Enter account number:"))
        pin = int(input("Enter pin:"))

        if(
            account_number == self.account.account_number
            and pin == self.account.pin
        ):
            print(f"Welcome, {self.account.account_holder}")
            self.menu()
        else:
            print("Invalid Account number and pin!")

    def menu(self):
        while True:
            display_menu()

            choice = int(input("Enter choice:"))    

            if(choice == 1):
                self.account.check_balance()
            elif(choice == 2):
                amount = float(input("Enter amount(Rs):"))
                self.account.withdraw(amount)
            elif(choice == 3):
                amount = float(input("Enter amount(Rs):"))
                self.account.deposit(amount)
            elif(choice == 4):
                self.account.statement()
            elif(choice == 5):
                old_pin = int(input("Enter old pin:"))
                new_pin = int(input("Enter new_pin:"))
                self.account.change_pin(old_pin, new_pin)
            elif(choice == 6):
                print("Thank you for using ATM.")
                break
            else:
                print("Invalid choice, please try again.")