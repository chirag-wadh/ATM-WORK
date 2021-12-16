print("welcome to SAITM ATM")
print("1.withdraw money")
print("2.update passowrd")
print("3.exit")
ask_user=int(input())
if ask_user ==1:
    print("how much money you want to withdraw")
    print("Available notes 2000 and 500 only")
    a=int(input())
    print("collect your money")
    b=input("Do you want to see your total balance")
    if b =="yes":
        print("340000 clear balance")
    else:
            print("exit")
elif ask_user ==2:
    print("enter your current password")
    d=int(input())
    if d == 8876:
     print("your password is match")
    else:
     print("your password is wrong")
else:
    ask_user ==3
    print("thank you for visiting SAITM ATM")
