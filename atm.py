def atm():
   
   balance=10000

   while True:
      print("\n welcome to bank of Zeshan")
      print("1. check balance ")
      print("2. withdraw money")
      print("3. deposit money")
      print("4. exit")
    
      choice=input("enter your choice: ")

      if choice=="1":
         print("your current balance is: ",balance)
      elif choice=="2":
         amount=float(input("enter the amount to withdraw: "))
         if amount>balance:
            print("insufficient balance")
         else:
            balance -= amount
            print("your withdrawal is successful. Remaining balance: ",balance)
      elif choice=="3":
         deposit=float(input("enter the amount you want to deposit: "))
         balance += deposit
         print("Deposit successful.  Your new balance is: ",balance)
      elif choice=="4":
         print("thank you for using our ATM")
         break
      else:
         print("invalid choice")
         
atm()

         
         