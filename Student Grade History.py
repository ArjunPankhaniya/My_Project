import turtle
try:
    menu = turtle.Turtle()
    menu.speed(5)
    turtle.color('blue')
    style = ('Courier', 10, 'normal')
    turtle.write('Python Micro Project\nBy\nPankhaniya Arjun Harjibhai (216200316012)', font=style,)
    turtle.hideturtle()
    a = 0
    b = 0
    for x in range(5):
        if(b == 0):
            a=1
        else:
            a=0
        for y in range(5):
            menu.penup()
            menu.goto(60*y,60*x*(-1))
            menu.pendown()
            if(a==0):
                a=1
            else:
                a=0
            for z in range(4):
                menu.fd(60)
                menu.right(90)
        if(b==0):
            b=1
        else:
            b=0
    turtle.exitonclick()
except:
    print("\nClosing turtle...\n")


# printing the heading of the program
from xmlrpc.client import boolean

print("  /-----------------------------------------/")
print(" / Welcome To The Student Record Directory /")
print("/-----------------------------------------/")
# creating a .txt file to store Student details
filename = "Student_Record.txt"
myfile = open(filename, "a+")
myfile.close()

# defining main menu
def main_menu():
    print("\nMAIN MENU\n")
    print("1. Show All Existing Student")
    print("2. Add A New Student")
    print("3. Search The Existing Student")
    print("4. Top Students")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        myfile = open(filename, "r+")
        filecontents = myfile.read()
        if len(filecontents) == 0:
            print("  /--------------------------------------------/")
            print(" / There is no Student in the Student Record. /")
            print("/--------------------------------------------/")
        else:
            print(filecontents)
        myfile.close()
        enter = input("Press Enter to continue ...")
        main_menu()
    
    elif choice == "2":
        newStudent()
        enter = input("Press Enter to continue ...")
        main_menu()
    
    elif choice == "3":
        searchStudent()
        enter = input("Press Enter to continue ...")
        main_menu()
    
    elif choice == "4":
        topstudent()
        enter = input("Press Enter to continue ...")
        main_menu()
    
    elif choice == "5":

        print("\nThank you for using Student Record.")
    
    else:
        print("\nPlease provide a valid input!\n")
        enter = input("Press Enter to continue ...")
        main_menu()

# defining search function
def searchStudent():
    searchname = input( "Enter Name for Searching Student Record: ")
    remname = searchname[1:]
    firstchar = searchname[:0]
    Search = firstchar.upper() + remname
    myfile = open(filename, "r+")
    filecontents = myfile.readlines()
    found = False
    
    for line in filecontents:
        if Search in line:
            print("Your Required Student Record is:", end = " ")
            print(line)
            found = True
            continue
    if found == False:
        print( "The Student is not available in the Student Record Called:",searchname)
    myfile.close()

# Defining Top Students
def toppers():
    myfile = open(filename, "r+")
    filecontents = myfile.readlines()
    student_list = []
    
    for i in filecontents:
        i = i[1:-2]
        l = i.split(',')
        l[1] = int(l[1])
        l[2] = int(l[2])
        student_list.append(l)
    student_list = sorted(student_list,key=lambda x: x[-1], reverse=True)
    return student_list
    myfile.close()

# Toppers
def topstudent():
    top_students = toppers()

    for i in top_students:
        print(i)

# Storing The New Student Details
def newStudent():
    try:
        name = input("Enter Full Name Of Student: ")
        roll = input("Enter Roll No Of Student: ")
        age = input("Enter Age Of student:")
        Gender = input("Enter Gender: ")
        percentage = input("Enter Percentage: ")
        StudentDetails = ("["+ name +","+ roll +"," + age +","+ Gender +","+ percentage +"]\n")
        myfile = open(filename, "a")
        myfile.write(StudentDetails)
        print("The following Student Details:\n"+ StudentDetails + "\nhas been stored successfully!")
        myfile.close()
    except ValueError:
        print("\nPlease Enter Valid Input.\n")

main_menu()
print("\nProgram Terminated.")