import os
from colorama import Fore, Style, init
init(autoreset=True)

version = "0.0.1beta"
password = ""
attempts = 0


while password != "betatest" and attempts != 3:
    password = input("Enter password... ")
    attempts = attempts + 1
    print (f"Attempt {attempts}/3")
if attempts == 3:
    print("Access denied")
    input("Press Enter to close...")
    exit()
    
print ("Access allowed")

running = True
while running:
    os.system("cls")
    print('\033[92m                  CYCLOPHAN UTILITY (VISUAL) DEVELOPER BETA by Morpheus                     ')
    print("                                                                                                    ")
    print("[1.] Enter data                                            [2.] Send data to local LLM")
    print("[3.] About                                                                   [4.] Exit")
    print("                                                                                                    ")
    print("                                                                                                    ")
    print("                                                                                                    ")
    print(f'\033[92mDeveloper Beta by Morpheus v{version}\033[0m') 
    choice = input("Enter an option... (1-4) ")
    if choice == "1":
        os.system("cls")
        surname = input("Enter full surname... ")
        name = input("Enter FIRST letter of your name with dot in format (V.)... ")
        reason = input("Enter reason (Посещение врача / Семейные обстоятельства)... ")
        sign = input("Enter teacher's name... ")
        date = input("Enter date (DD.MM.YY)... ")
        print ("Completed!")
        os.system("cls")
        print("Check written data...")
        print(f"Surname: {surname}")
        print(f"Name: {name}")
        print(f"Reason: {reason}")
        print(f"Sign: {sign}")
        print(f"Date: {date}")
        yn = input("Is written data correct? (y/n) ")
        if yn == "y":
            print("Completed!")
        elif yn == "n":
            print("Rewrite the data again. Use first step again to complete.")
        else:
            print("Unknown answer, returning to menu...")

    elif choice == "2":
        os.system("cls")
        print('\033[91mUnexpected error, no LLM found\033[0m')


    elif choice == "3":
        os.system("cls")
        print("What is Cyclophan project?")
        print("")
        print("рус                             ")
        print("Cyclophan - утилита, которая позволяет ...,")
        print("отправляя данные, заполненные в пункте 1, в локальную LLM на вашем   ")
        print("компьютере, в уже подготовленный промпт для заполнения бланка введен-")
        print("ными данными.                                                        ")
        print("")
        print("eng")
        print("Cyclophan is a utility that lets you ...;            ")
        print("It takes the information entered in the first step and feeds it into ")
        print("a pre-con figured prompt for a local LLM running on your computer, which")
        print("then fills out the form with the provided details.") 
        print("")
        print('\033[91mWarning: the is visual beta and currently doesnt work\033[0m')
        print('\033[91mВАЖНО: Данная программа пока что является лишь визуалом и ничем более \033[0m')
        print("")

    elif choice == "4":
        os.system("cls")
        confirmation = input("Are you sure you wanna exit? (y/n): ")
        if confirmation.lower() == "y":
            running = False
        elif confirmation.lower() == "n":
            print("Returning to menu...")
        else:
            print("Unknown answer, returning to menu...")

    else:
        print("Invalid option!")

    if running:
        input("\nPress enter to continue...")
