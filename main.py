
import getpass
import random


# USER ACCOUNTS AND PASS
accounts = ['farha', 'talib', 'john']
pins = ['1234', '2288', '1111']
amounts = ['1000', '12000', '20000']
count = 0

print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome to OSHWAL COLLEGE ATM              *")
print("*                                                                          *")
print("****************************************************************************")


#def login():
while True:




         name = input("/nENTER ACCOUNT NAME")

        # TRANFORMS THE NAME INTO LOWERCASE
         name.lower()

         if name in accounts:
            if name == accounts[0]:
                n = 0
                break


            elif name == accounts[1]:
                n = 1
                break

            else:
                n = 2
                break

         else:
              print("INVALID USERNAME")


count = 0
while True:
        # print('------------------')
      pin = input('PLEASE ENTER PIN: ')

      if pin.isdigit():
        if name == 'farha':
            if pin == pins[0]:
              print("*                   WELCOME BACK FARHa *")

              break

        else:
            count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            print()

        if name == 'talib':
            if pin == pins[1]:
                break

        else:
            count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            print()

        if name == 'john':
            if pin == pins[2]:
                break

        else:
            count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            print()


def statement(n):
        print('---------------------------------------------')
        print('*********************************************')
        print(str.capitalize(accounts[n]), 'YOU HAVE ', amounts[n], 'EURO ON YOUR ACCOUNT.')

def withdraw(n):
    print('---------------------------------------------')
    print('*********************************************')
    cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
    print('*********************************************')
    print('---------------------------------------------')
    if cash_out % 10 != 0:
        print('------------------------------------------------------')
        print('******************************************************')
        print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 EURO NOTES')
        print('******************************************************')
        print('------------------------------------------------------')
    elif cash_out > amounts[n]:
        print('-----------------------------')
        print('*****************************')
        print('YOU HAVE INSUFFICIENT BALANCE')
        print('*****************************')
        print('-----------------------------')
    else:
        amounts[n] = amounts[n] - cash_out
        print('-----------------------------------')
        print('***********************************')
        print('YOUR NEW BALANCE IS: ', amounts[n], 'EURO')
        print('***********************************')
        print('-----------------------------------')



def deposit(n):
    print()
    print('---------------------------------------------')
    print('*********************************************')
    cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
    print('*********************************************')
    print('---------------------------------------------')
    print()
    if cash_in % 10 != 0:
        print('----------------------------------------------------')
        print('****************************************************')
        print('AMOUNT YOU WANT TO DEPOSIT MUST TO MATCH 10 EURO NOTES')
        print('****************************************************')
        print('----------------------------------------------------')
    else:
        amounts[n] = amounts[n] + cash_in
        print('----------------------------------------')
        print('****************************************')
        print('YOUR NEW BALANCE IS: ', amounts[n], 'EURO')
        print('****************************************')
        print('----------------------------------------')


def new_pin(n):
    print('-----------------------------')
    print('*****************************')
    new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
    print('*****************************')
    print('-----------------------------')
    if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
        print('------------------')
        print('******************')
        new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
        print('*******************')
        print('-------------------')
        if new_ppin != new_pin:
            print('------------')
            print('************')
            print('PIN MISMATCH')
            print('************')
            print('------------')
        else:
            pins[n] = new_pin
            print('NEW PIN SAVED')
    else:
        print('-------------------------------------')
        print('*************************************')
        print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
        print('*************************************')
        print('-------------------------------------')

def quit(n):
    print(f"""
                    printing receipt..............
              ******************************************
                  Transaction is now complete.                         
                  Transaction number: {random.randint(10000, 1000000)}                   
                  Account name: {accounts[n]}                
                  Available balance: ksh{amounts[n]}                    

                  Thanks for choosing us as your bank                  
              ******************************************
              """)








def main_menu():
    while True:
       response = input(
         'SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nDEPOSIT(d)  \nChange PIN_(P)  \nQuit_______(Q) \nType The Letter Of Your Choices: ').lower()

       response.lower()

       if response =='s':
           statement(n)
       elif response =='w':
           withdraw(n)
       elif response =='d':
           deposit(n)
       elif response =='p':
           new_pin(n)
       elif response =='q':
           quit(n)
           break





main_menu()