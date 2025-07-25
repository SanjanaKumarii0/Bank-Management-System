# read about json
# input sara dump hota hai json me aur load maytlab json se code me leke aaana 
# json me string use hota hai bas  
import json
from pathlib import Path
import random
import string
from turtle import back
class bank:
    data=[]
    __database="data.json"
    try:
        if Path (__database).exists():
            with open(__database,"r") as fs:
                data= json.load(fs.read())
    except Exception as err:
        print(f"An error occured as {err}")   
    @classmethod
    def __updatedata(cls) :
        with open(cls.__database,"w") as fs:
            fs.write(json.dumps(cls.data))
    @classmethod
    def __generate_account_number(cls): 
        alpha=random.choices(string.ascii_letters,k=5)
        numbers=random.choices(string.digits,k=5)
        id=alpha+numbers
        random.shuffle(id) #shuffle karne woo data ko 2 list me convert kar deta hai isliye usko wapas join kar deta hai .
        return "".join(id)


    def createaccount(self):
        info = {
             "name": input("Tell your name:-"),
               "age": int(input("tell your age:-")),
               "gender": input("tell your gender:-"),
               "email":input("tell your email:-"),
               "phone":int(input("tell your phone number")),
               "Accountno.": bank.__generate_account_number() ,
               "pin":int(input("tell your pin:-")),
               "balance":0
                }
        if info['age'] <18:
            print("sorry you can not cretae the account")
        elif  not len(str(info["phone"])) == 10:
            print("invalid phonr number")  
        elif not len(str(info["pin"])) ==4: 
            print("invalid pin") 
                
        else:
            bank.data.append(info)
            bank.__updatedata()
        print(f"your account number is {info['Accountno.']},donot forget id")      
    def deposite_money(self):
        account_no=input("tell your account number:-")
        pin=int(input("tell your pin:-")) 
        # for i in bank.data:
        #     if i["Accountno."] ==account_no and i ['pin'] ==pin:
        #         userdata=i
        #         break
        #     print("no such data found") 
        # print(userdata)
        user_data=[i for i in bank.data if i ["Accountno."]==account_no and i["pin"] ==pin] 
        if user_data==False:
            print("no such user found")
        else:
            amount=int(input("how much you want to deposite")) 

            if amount<0:
                print("sorry you cannot deposti negative amount")
            elif amount>20000:
                print("sorry you cannot deposti more than 20000rs")
            else:
                user_data[0]["balance"] += amount 
                bank.__updatedata() 
                print("amount deposited successfully")  
    def withdraw_money(self):
        account_no=input("tell your account number:-")
        pin = int(input("no such user found"))
        user_data=[i for i in bank.data if i ["Accountno."]==account_no and i["pin"] ==pin] 
        if user_data==False:
            print("no such user found")
        else:
            amount=int(input("how much you want to withdraw")) 
            if amount>20000:
                print("sorry you cannot withdraw more than 200000 amount")
            elif amount>user_data[0]["balance"]:
                print("insufficient balance")
            else:
                user_data[0]["balance"] -= amount 
                bank.__updatedata() 
                print("amount withdraw successfully")  
    def account_details(self):
        account_no=input("tell your account number:-")
        pin = int(input("no such user found"))
        user_data=[i for i in bank.data if i ["Accountno."]==account_no and i["pin"] ==pin] 
        if user_data==False:
            print("no such user found")
        else:
            for i in user_data[0]:
                print(f"{i} : {user_data[0][i]}")
    def update_details(self): 
        account_no=input("tell your account number:-")
        pin = int(input("no such user found"))
        user_data=[i for i in bank.data if i ["Accountno."]==account_no and i["pin"] ==pin] 
        if user_data==False:
            print("no such user found")
        else:
            print(" you cannot change your account number")   
            print("now update your details  enter to skip ")  
        newdata ={
              "name": input("tell your name:-"),
              "age": input("please tell your age"),
              "email": input("tell your phone number:-"),
              "phone": input("tell your phone number:-")
              }   
        if newdata['name'] =="":
            newdata['name']== user_data[0]['nmae']
        if newdata['age']=="":
            newdata['age'] ==user_data[0]['age']
        if newdata['email'] == "":
                newdata['email'] = user_data[0]['email']
        if newdata['phone'] == "":
                newdata['phone'] = user_data[0]['phone']
        if newdata['pin'] == "":
                newdata['pin'] = user_data[0]['pin']

        newdata["AccountNo."] = user_data[0]["AccountNo."]
        newdata["balance"] = user_data[0]["balance"]

        for i in user_data[0]:
                if user_data[0][i] == newdata[i]:
                    continue
                else:
                    if newdata[i].isnumeric():
                        user_data[0][i] = int(newdata[i])  
                    else:
                        user_data[0][i] = newdata[i]
            
            
        bank.__updatedata()
    print("updated successfully")
def delete_account(self):
        account_no = input("Tell your account number :- ")
        pin = int(input("Tell your pin :- "))

        user_data = [i for i in bank.data if i["AccountNo."] == account_no and i['pin'] == pin]

        if user_data == False:
            print("no such user found")
        else:
            bank.data.remove(user_data[0])
            bank.__updatedata()
            print("account deleted successfully")




            
        while True:

           print("""" press the following for your task:-
        
        press 1 for creating the bank account.
        press 2 for depositing money in your bank account.
        press 3 for withdrawing the money from your account.
        press 4 for account details.
        press 5 for updating your details.
        press 6 for deleting the account.
        press 0 to exit.""")
user = bank()
check=input("tell your response:-")
    

if check =="1":
        user.createaccount()
if check=="2":
    user.deposite_money()
if check=="3":
    user.withdraw_money()
if check=="4":
    user.account_details() 
if check=="5":
    user.update_details()  
if check =="6":
    user.delete_account()
if check =="0":
    exit( )           



#withdraw money ka section create karna hai     



