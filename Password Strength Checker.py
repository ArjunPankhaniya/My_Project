print("Passsword Strength Checker Using Python")
print("by")
print("Yash Vasoya     (216200316002)")
print("Darshan Lathiya (216200316005)")
print("Arjun Pankhaniya(216200316012)\n ")
lower, upper, special, digit = 0, 0, 0, 0
flag=0
try:
    while True:
        print("Press 1 To Enter password:")
        print("Press 2 To Exit:")
        choice=int(input("\nEnter your choice:"))
        if choice==1:
            print("\n*password must be 8 character long,must contain "
                "1 uppercase,1 lowercase,1 special character,1 integer*\n")
            password=input("Enter Password:")
            if (len(password) >= 8):
                for i in password:
                    for word in password.split():
                        if(i.isupper()):
                            upper += 1
                        if(i.islower()):
                            lower += 1
                        if(i.isdigit()):
                            digit += 1
                        if(i == '@' or i == '$' or i == '_' or i == '#'):
                            special += 1
                if(lower<1):
                    print("*lower case charecter is missing in password)\n")
                if(upper<1):
                    print("(*Upper case charecter is missing in password)\n")
                if(special<1):
                    print("(*Special charecter is missing in password)\n")
                if(digit<1):
                    print("(*Integer charecter is missing in password)\n")
                if(lower >= 1 and upper >= 1 and special >= 1 and digit >= 1):
                    print("\n**Strong Password**\n")
            else:
                print("\nWeak Password (*password must be 8 character long*)\n")
        elif choice==2:
            print("\n**Terminating Program.....**")
            print("**Program End**")
            exit()
        else:
            print("\n**Wrong Input**")
            print("**Terminating Program.....**")
            print("**Program End**")
            exit()
except ValueError:
    print("\n**Please Enter Choice In Integer Only**")
    print("**Terminating Program.....**")
    print("**Program End**")