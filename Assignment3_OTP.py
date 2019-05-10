import random
OTP= random.randint(1,5)
print(OTP)

FirstName= input('enter your first name - ')
LastName= input('enter your last name - ')

number= int(input('enter any number between 1 to 5- '))


if number>5:
    print("wrong input, Please try again")


if number != OTP:
    for i in range(3):
        print("ERROR!!! ENTER THE OTP AGAIN")
        a = input("Enter yes/no to continue - ")
        if a == "yes":

            number = int(input('enter any number between 1 to 5- '))
            i -= 1
            if number == OTP:
                print("OTP SUCCESSFULLY MATCHED")

                break
        else:
            print("Thank you for visit")
            raise SystemExit
else:
    print("OTP SUCCESSFULLY MATCHED")



