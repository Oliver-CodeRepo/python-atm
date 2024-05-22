global balance
global pin 
global logged_in

balance = 0
pin = '1234'
logged_in = False

def deposit(amount):
  balance += amount
  return balance


def withdraw(amount):
  # check if balance is enough to make withdrawal
  if balance >= amount:
    balance -= amount
    return balance
  else:
    print('Cannot complete transaction. Balance to low')


def change_pin(old_pin, new_pin):
  if (old_pin == pin):
    pin = new_pin
    print('Pint changed Successfully')
    return
  else:
    print('Your Old Pin is wrong')
    return
  
def Authentitcate_user(user_pin):
  if (user_pin == pin):
    logged_in = True
    print('\nWelcome back!! \n')
    return logged_in
  else:
    logged_in = False
    print('Wrong Pin')
    return logged_in
  

def initiate():
  pin = input("Enter your pin: ")
  auth = Authentitcate_user(pin)
  if auth:
    print("Your Balance is: ", balance)
    option = input("What do you want to do: \n \
          1. Deposit \n\
          2. Withdraw \n\
          3. Check Balance\n\
          Enter the [1, 2, 3]: \n \
          ")
    
    if option == "1":
      amount = input('Enter Amount to Deposit: ')
      try:
          amount = float(amount)
          depositor = deposit(amount)
          print("Your Balance is: ", depositor)
      except ValueError:
          print("This is not a number")
    
    elif option == "2":
      amount = input('Enter Amount to Withdraw: ')
      try:
          amount = float(amount)
          depositor = withdraw(amount)
          print("Your Balance is: ", depositor)
      except ValueError:
          print("This is not a number")
    
    elif option == "3":
        print("Your Balance is: ", balance)
    
    else:
       print("invalid choice")



if __name__ == "__main__":
  initiate()

