import random

print("banking operation")
OTP = random.randint(1,5)
print(OTP)
userdata = {}
userdata["Balance"]=1000


user = int(input("enter OTP"))
k = 0
if user!= OTP:
    while k<2:  # Infinite loop or incorrect otp , k is useless here

        print("sorry i didn't understand")

        user = int(input("enter correct OTP"))
        k +=1
        if user == OTP:
            break;


        if k==2:
            raise  SystemExit

print("Banking Options")
Banking = int(input("1.Existing Account:\n2.New Account:"))


if Banking == 1:
    ano = int(input("Enter Account no."))

elif Banking == 2:
    print("Press 'Yes' to create new account \n 'No' for exit")
    choice=input()
    if choice == "yes":
        print("Enter Details")
        name = input("enter your name")

        while True:
            age0 = int(input("enter your age"))
            age=0
            if age0 >=1 and age0 <=100:
                age = age0
                break
            else:
                print("Wrong input")





        address = input("enter adress:")
        phone = int(input("enter phone no."))
        gender = input("gender")
        balance =int(input("balance"))

        ano=random.randint(100,1000)



        userdata["Name"] = name
        userdata["Age"] = age
        userdata["Address"]= address
        userdata["Phone"] = phone
        userdata["Gender"] = gender
        userdata["Balance"] = balance

        print("ACCOUNT CREATED")
        print("\bDetails\n:")

        print("\bYour account number:",ano)

        print("\b name:",name)
        print("\b Age:",age)
        print("\b Address:",address)
        print("\b Phone:", phone)
        print("\b Gender:", gender)
        print("\b Bank balance:", balance)



    else:
        print("You Entered the wrong choice\n\n Try Again")
        raise SystemExit

else:
    raise SystemExit





while True:
    print("\n\nEnter Choice\n")
    transaction = int(input("\n1.withdraw\n2.deposit\n3.balance enquiry\n4.demand draft\n5.Exit\n\nchoose option\n"))
    if transaction == 1:
        amount = int(input("enter the amount you want to withdraw"))  # what it gets 1 and user will withdraw 100

        print(userdata["Balance"])

        # it is withdrawing but from which account
        if amount >= 100 and amount <= userdata["Balance"]:
            userdata["Balance"] = userdata["Balance"] - amount
            print('here is your money')  # it is not  processed with related account
            print("Balance is :", userdata["Balance"])
        else:
            print("Insufficient fund or voilation of minimum limit ")

    elif transaction == 2:
        print("your current balance is:", userdata["Balance"])
        #  It is also an independent transaction ,no account associated
        amount = int(input("enter the amount you want to deposit"))

        if amount <= 50000:
            print("amount is deposited")
            userdata["Balance"] = userdata["Balance"] + amount
            print("your new balance is", userdata["Balance"])
        else:
            print("enter the correct amount")
        continue

    elif transaction == 3:
        print("enter any one of the following")
        a = int(input("\n1.Total amount\n2.outstanding balance\n3.minimum Due amount"))
        if a == 1:
            print("your total amount is: ", userdata["Balance"])
            continue
        elif a == 2:
            print("your outstanding balance is", random.randint(1, 5000))
            continue
        elif a == 3:
            a = userdata["Balance"] - userdata["Balance"]
            print("your due balance is ", a)
            continue

    elif transaction == 4:
        print("enter following details")
        bank_name = input("name of the bank")
        accountholder = input("name of account holder")
        branch = input("name of branch")
        amount = int(input("enter amount"))
        userdata["Balance"]=userdata["Balance"]-amount
        print("Available balance=",userdata["Balance"])
        continue

    elif transaction == 5:
        print("thank you")
        raise SystemExit
    else:
        print("enter the right choice")

print("Process Again")
