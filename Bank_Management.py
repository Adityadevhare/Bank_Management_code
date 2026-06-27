''' Bank Management '''

import json
import random
import string
from pathlib import Path


class Bank :
    database='data.json'
    data=[]

    try :
        if Path(database).exists():
            with open(database) as fs :
                data = json.loads(fs.read()) 
        else:
            print(f'No such file exists.')
 
    except Exception as err : 
        print(f" An exception occured as : {err}")
    
    
    @classmethod
    def __update(cls):
        with open(cls.database ,'w') as fs :
            fs.write(json.dumps(Bank.data))

    @classmethod 
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters , k=3)
        num = random.choices(string.digits , k= 3)
        spchar = random.choices("!@#$%^&*" , k =1)
        id = alpha + num + spchar 
        random.shuffle(id)
        return "".join(id) 
    
    
    def createaccount(self):
        info ={
            "name":input(f"Tell you name : "),
            "age": int(input(f"Enter your age : ")),
            "email":input("Tell your email : "),
            "pin":int(input("Tell your 4 number pin : ")),
            "accountNo.":Bank.__accountgenerate(),
            "balance":0
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print(f"Sorry you can't create your account . ")
        else:
            print(f"Account has been created successfully .")

            for i in info :
                print(f"{i} : {info[i]}")
            print(f'Please note down your account number . ')

            Bank.data.append(info)

            Bank.__update()
    
    def dopositemoney(self):
        accnumber = input(f"Please enter your account number :  ")
        pin = int(input(f"Please enter  your pin number : "))

        userdata=[i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print(f"Sorry no data found .")

        else:
            amount = int(input(f'How much you wnat to deposite : ')) 
            if amount > 10000 or amount < 0:
                print(f"Sorry the amount is too much you can only deposite below Rs. 10000 and above 0. ")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print(f'Amount is deposited sucessfully. ') 




    def withdrawmoney(self):
        accnumber = input(f"Please enter your account number :  ")
        pin = int(input(f"Please enter  your pin number : "))

        userdata=[i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print(f"Sorry no data found .")

        else:
            amount = int(input(f'How much you wnat to withdraw :  ')) 
            if userdata[0]['balance'] < amount :
                print(f"Sorry the amount is too much you can only withdraw below Rs. 10000  and above 0.")
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print(f'Amount is withdrawn sucessfully. ') 




    def showdetails(self):
        accnumber = input(f"Please enter your account number :  ")
        pin = int(input(f"Please enter  your pin number : "))
        userdata=[i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print(f"Your information are : \n \n " )
        print(f'-------------------------')
        for i in userdata[0]:
            print(f'{i} : {userdata[0][i]}')
        print(f'-------------------------')


    def updatedetails(self):
        accnumber = input(f"Please enter your account number :  ")
        pin = int(input(f"Please enter  your pin number : "))
        userdata=[i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print(f' No such User found !!')
        else:
            print(f'You cannot change your balance , age , account nummber .')
            print(f'-------------------------- \n \n ')
            print(f"Please enter the details you want to change or leave it empty if you don't want to change :")

            new_data={
                "name": input(f'Please enter yor new name (or press "enter" to skip) : '),
                "email": input(f'Please enter your new email (or press "enter " to skip ) : '),
                "pin":input(f'Please enter your new pin (or press "enter " to skip ) : ')
            }

            if new_data["name"] =="":
                new_data["name"] == userdata[0]["name"] 

            if new_data["email"]=="":
                new_data["email"] == userdata[0]["email"]

            if new_data["pin"] == "":
                new_data["pin"] == userdata[0]["pin"]

            new_data["age"] = userdata[0]["age"]
            new_data["accountNo."] = userdata[0]["accountNo."]
            new_data["balance"] = userdata[0]["balance"]

            if type(new_data["pin"]) == str:
                new_data["pin"] = int(new_data["pin"])
            

            for i in new_data:
                if new_data[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = new_data[i]
            

            Bank.__update()
            print(f"Details are updated sucessfully . ")

user = Bank()
print("Press the following to start : ")
print(f' 1. Create an account.')
print(f' 2. Depositing the money.')
print(f' 3. Withdrawing the money.')
print(f' 4. Deatils.')
print(f' 5. Updationg the the deatils.')
print(f' 6. Delete the account.')

check = int(input(f" Enter you choice :- "))

if check == 1:
    user.createaccount()

if check == 2:
    user.dopositemoney() 

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()