balance=7.52
print("Hi, Welcome to the Atm.")
print("no need for pin numbers, we already know who you are")
print("please selection one of the options given beneath")
print("""
    D = Deposit
    W = Withdrawal
    T = Transfer
    B = Balance check
    Q = Quick cash of 20$
    E = Exit
    Please select in the next line.   
""")
option=input("which option would you like?:")
if option==("D"):
    print("How much would you like to deposit?")
    amount=(int(input("amount:")))
    total=amount+balance
elif option ==("W"):
    print("How much would you like to withdrawl?")
    withdrawl=int(input("how much would you like to take out:?"))
    if balance<withdrawl:
        print("Error, insufficent funds")
        print("please try again")
elif option == "T":
    print("don't worry about the technicalities, we already know who you're 0transferring to")
    transfer =int(input("How much would you like to transfer:?"))
    print("you now have", balance-transfer,"dollars in your bank")
elif option=="B":
    print("you currently have",balance,"dollars.")
elif option=="Q":
    print("processing transaction, please await approval")
    quicky=balance-20
    if balance<quicky:
         print("processing transaction, please await approval")
    print("Error, You're broke.:(")
elif option=="E":
      print("Thanks for checking with the Atm")
      print("press the enter key to exit")