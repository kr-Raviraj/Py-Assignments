import random

fname = input("\nPlease Enter Your First Name:\n")
lname = input("\nPlease Enter Your Last Name:\n")
ran = random.randint(1,10)

#print("Your Otp For Transaction Is =   ", ran)
otp=int(input("Enter OTP to proceed = "))
if ran==otp:

	print("\n\n Main Menu\t ")

	bank_data = {}
	user_data = {}

	while True:
		ch = int(input("""
		1. New Account
		2. Existing Customer
		3. Exist

		Enter choice:"""))

		if ch == 1:
			name = input("Enter Name:")
			city = input("Enter City")
			age = int(input("Enter Age:"))
			acc_type = input("Enter account type:")
			amt = int(input("enter initial amount:"))
			acc_no = int(input("Enter account no:"))

			user_data["name"]=name
			user_data["city"]=city
			user_data["age"]=age
			user_data["acc_type"]=acc_type
			user_data["amount"]=amt
			bank_data["account_number"]=acc_no
			bank_data["detail"]=user_data

			print("\n  Account Created Successfully  ")

		elif ch == 2:
			acc_no = int(input("Enter account number:"))

			if acc_no == bank_data["account_number"]:
				print("\n  Account Exist ")

				while True:
					print("\t\t    User Portal  ")

					u_ch = int(input("\n1.Check Balance\n2.Withdraw\n3.Deposit\n4.Cancel\n5.Balance Inquiry\n6.Demand Draft\nEnter chooice:"))

					if u_ch == 1:
						print("Your Currant Balance:",bank_data["detail"],user_data["amount"])

					elif u_ch == 2:
						w_amt = int(input("Enter withdraw amout: "))
						bank_data["detail"],user_data["amount"]= bank_data["detail"],user_data["amount"]-w_amt
						print("     Amount withdraw   ",user_data["amount"])
					elif u_ch == 3:
						d_amt = int(input("Enter deposit amout: "))

						bank_data["detail"],user_data["amount"]= bank_data["detail"],user_data["amount"]+d_amt
						print("    Amount deposited    ",user_data["amount"])
					elif u_ch == 5:
						bank_data["detail"],user_data["amount"]= bank_data["detail"],user_data["amount"]
						print("   Total Amount   ",user_data["amount"])

					elif u_ch == 4:
						break

					else:
						print("\n Invalid input")
			else:
				print("\n   Account not Exit  ")
		elif ch == 3:
			break

		else:
			print("\n Invalid input ")
else:
	print("Wrong OTP, Try again")



























