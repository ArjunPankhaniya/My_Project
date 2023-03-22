print("  /------------------------------------/")
print(" / Welcome To The Phonebook Directory /")
print("/------------------------------------/")

filename = "Contacts.txt"
myfile = open(filename, "a+")
myfile.close()    

def main_menu():
    print("\nMAIN MENU\n")
    print("1. Show All Contacts")
    print("2. Create New Contact")
    print("3. Search The Existing Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        myfile = open(filename, "r+")
        filecontents = myfile.read()
        if len(filecontents) == 0:
            print("  /-------------------------------------/")
            print(" / There is no Contact in Contact List./")
            print("/-------------------------------------/")
            main_menu()
        else:
            print(filecontents)
        myfile.close()
        enter = input("Press Enter to continue ...")
        main_menu()
    
    elif choice == "2":
        newContact()
        enter = input("Press Enter to continue ...")
        main_menu()
    
    elif choice == "3":
        searchContact()
        enter = input("Press Enter to continue ...")
        main_menu()
    
    elif choice == "4":
        DeleteContact()
        enter = input("Press Enter to continue ...")
        main_menu()
    
    elif choice == "5":

        print("\nThank you for using Phonebook Directory.")
        exit()
    
    else:
        print("\nPlease provide a valid input!\n")
        enter = input("Press Enter to continue ...")
        main_menu()

def searchContact():
    try:
        print('Press 1 to search name wise:')
        print('Press 2 to search number wise:')
        select=int(input('Enter a number:'))
        if select==1:
            searchname = input( "Enter Name for Searching In Contact List: ")
            remname = searchname[1:]
            firstchar = searchname[:0]
            Search = firstchar.upper() + remname
            myfile = open(filename, "r+")
            filecontents = myfile.readlines()
            found = False
            
            for line in filecontents:
                if Search in line:
                    print("Your Found Contact is:", end = " ")
                    print(line)
                    found = True
                    continue
            if found == False:
                print( "The Contact""'",searchname,"'""does not Exist in the Phonebook Directory.")
            myfile.close()
        if select==2:
            print('Feature Coming Soon........')

        else:
            raise Exception('Error')
    except :
        print("\nPlease Enter Valid Input.\n")
        searchContact()

def DeleteContact():
    searchname = input( "Enter Name for Searching In Contact List: ")
    remname = searchname[1:]
    firstchar = searchname[:0]
    Search = firstchar.upper() + remname
    myfile = open(filename, "r+")
    filecontents = myfile.readlines()
    found = False
    
    for line in filecontents:
        if Search in line:
            #print("Are You Sure About To Delete This Contact?", end = " ")
            print(line,"Feature Coming Soon...")
            #print("contact deleted sucessfully...")
            
            found = True
            
            continue
    if found == False:
        print( "The Contact""'",searchname,"'""does not Exist in the Phonebook Directory.")
    myfile.close()


def newContact():
    try:
        fname = input("Enter Contact Name: ")
        Mobile = input("Enter Mobile Number:")
        ContactDetails = ("["+ fname +"," + Mobile +"]\n")
        myfile = open(filename, "a")
        myfile.write(ContactDetails)
        print("This Following Contact:\n"+ ContactDetails + "has been stored successfully!")
        myfile.close()
    except ValueError:
        print("\nPlease Enter Valid Input.\n")



main_menu()







