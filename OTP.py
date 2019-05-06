import random
def opt_match():
   fname = input("\nPlease Enter Your First Name:\n")
   lname = input("\nPlease Enter Your Last Name:\n")
   ran = random.randint(1,5)
  # print("Your Otp For Transaction Is = ",ran)
   attempts = 4

   while True:
       try:
           x = int(input("\nPlease Enter the number Here:\n"))
           if x > 5:
               print ("\nWrong Input, Please Try Again")
           if x==ran:
               print ("\nSuccesfull OTP\n"); break
           if x!=ran:
               if attempts == 1:
                   print("\nWrong Input"),("\nSORRY PROGRAM CRASHED\n");
                   break
               print("\nERROR!!! ENTER THE OTP AGAIN")
               print ("You are left with only", (attempts)-1),("attempts to get right OTP\n")

               attempts = attempts-1

               try_again = input("To continue type yes and to quit press no\n")
               if try_again.lower()=="yes":
                   continue
               if try_again.lower()=="no":
                   print("\nThanks for your attempt\n");
               break
       except:
           print("\nYou did not type in the correct format, good bye\n"); break

opt_match()