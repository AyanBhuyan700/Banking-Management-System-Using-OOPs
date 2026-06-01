import json
import random
import string
from pathlib import Path 

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No data file was found.")
    except Exception as err:
        print(f"{err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountGenerate(cls):
        alpha = random.choices(string.ascii_letters, k = 3)
        num = random.choices(string.digits, k = 4)
        spchar = random.choices("@#$%^&*!", k = 3)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)


    def createAccount(self):
        info = {
            "name": input("Please enter your full name: "),
            "age": int(input("Please enter your age: ")),
            "email": input("Please enter your email address: "),
            "pin": int(input("Please enter a 4-digit PIN: ")),
            "accountNo": Bank.__accountGenerate(),
            "balance": 0
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("Sorry, you are not eligible to create an account.")

        else:
            print("Account created successfully!")
            print("\nAccount Details:")
            for i in info:
                print(f"{i} : {info[i]}")
            print("\nPlease write down your account number for future reference.")
            Bank.data.append(info)
            Bank.__update()

    def depositMoney(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))

        userData = [i for i in Bank.data if i["accountNo"] == accountNumber and i["pin"] == pin]

        if userData == False:
            print("Sorry, no account was found with the provided details.")

        else:
            amount = int(input("Enter the amount you want to deposit: "))
            if amount > 10000 or amount < 0:
                print("You cannot deposit more than 10,000 or less than 1.")
            else:
                userData[0]["balance"] += amount
                Bank.__update()
                print("Amount deposited successfully.")


    def withdrawMoney(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))

        userData = [i for i in Bank.data if i["accountNo"] == accountNumber and i["pin"] == pin]

        if userData == False:
            print("Sorry, no account was found with the provided details.")

        else:
            amount = int(input("Enter the amount you would like to withdraw: "))
            if amount > userData[0]["balance"] or amount < 0:
               print("You cannot withdraw more than your available balance or less than 1.")
            else:
                userData[0]["balance"] -= amount
                Bank.__update()
                print("Amount withdrawn successfully.")

    def viewUserDetail(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))

        userData = [i for i in Bank.data if i["accountNo"] == accountNumber and i["pin"] == pin]

        if userData == False:
            print("Sorry, no account was found with the provided details.")
         
        else:
            print("\nAccount Details:")
            for i in userData[0]:
                print(f"{i} : {userData[0][i]}")

    def updateUserDetail(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))

        userData = [i for i in Bank.data if i["accountNo"] == accountNumber and i["pin"] == pin]

        if userData == False:
            print("Sorry, no account was found with the provided details.")

        else:
            print("You cannot update your age, account number, or account balance.")

            print("Enter the details you would like to update, or press Enter to keep the current values.")
            newData = {
                "name": input("Enter your full name (or press Enter to skip): "),
                "email": input("Enter your email address (or press Enter to skip): "),
                "pin": input("Enter your new PIN (or press Enter to skip): "),
                }
            if newData["name"] == "":
                newData["name"] = userData[0]['name']
            if newData["email"] == "":
                newData["email"] = userData[0]['email']
            if newData["pin"] == "":
                newData["pin"] = userData[0]['pin']
                
                newData["age"] = userData[0]["age"]
                newData["accountNo"] = userData[0]["accountNo"]
                newData["balance"] = userData[0]["balance"]
                
                if type(newData["pin"]) == str:
                    newData["pin"] = int(newData["pin"])
                    
                    for i in newData:
                        if newData[i] == userData[0][i]:
                            continue
                        else:
                            userData[0][i] = newData[i]
                            Bank.__update()
                            print("Account details updated successfully.")


    def deleteAccount(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))

        userData = [i for i in Bank.data if i["accountNo"] == accountNumber and i["pin"] == pin]

        if not userData:
            print("Sorry, no account was found with the provided details.")

        else:
            check = input("Press Y to delete your account or N to cancel: ")

            if check == "n" or check == "N":
                print("Account deletion cancelled.")
            else:
                index = Bank.data.index(userData[0])
                Bank.data.pop(index)
                print("Account deleted successfully.")
                Bank.__update()


user = Bank()

print("===== BANKING SYSTEM MENU =====")
print("1. Create Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. View Account Details")
print("5. Update Account Details")
print("6. Delete Account")

check = int(input("Please select an option: "))

if check == 1:
    user.createAccount()

if check == 2:
    user.depositMoney()

if check == 3:
    user.withdrawMoney()

if check == 4:
    user.viewUserDetail()

if check == 5:
    user.updateUserDetail()

if check == 6:
    user.deleteAccount()
