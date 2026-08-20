from account import Account
from atm import ATM

account = Account(
    account_number = 123456789,
    account_holder = "Sourabh Kumar",
    pin = 1234,
    balance = 100000
)

atm = ATM(account)
atm.login()