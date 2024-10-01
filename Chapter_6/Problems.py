#  Write a program to find the greatest of four numbers entered  by the user .







# Write a program to find out whether a studenet hs passed oir failed if it required a total of 40% and at least 33% in each subject to pass. Assume 3 subject and take makrs as an input from the user
marks1 = int(input("Enter the marks 1: "))
marks2 = int(input("Enter the marks 2: "))
marks3 = int(input("Enter the marks 3: "))

#  check for total percentage 
total_percentage = (100 *(marks1+marks2+marks3))/300
if(total_percentage >=40 and marks1>33 and marks2 >33 and marks3>33):
        print("You are pass", total_percentage)
else: 
        print("You failed, try again next year")

# A spam comment is defined as a text containing following keywords: 
#  Marks a lot of money, buy now, subscribe this click this Write a program to detect these spams.

spamName1 = "Make a lot of money"
spamName2 = "buy now"
spamName3 = 'subscribe this'
spamName4 = 'click this'

message = input("Enter your comment")

if((spamName1 in message) or (spamName2 in message) or (spamName3 in message)):
            print('This comment is spam')
else: 
        print("This comment is not a spam")


# Write a program to find whether a given username contains less than 10
username = input("Enter your name : ")
if(len(username)<10):
            print("Your username is less than ten ")
else:
        print("Your usermae is greater than ten")

# Write a program which finds out whether a given name is present in a list or not 
listName = ['Anjali', 'Puja', 'Subham', 'Divya']
nameInput = input("Enter the name which you find: ")
if(nameInput in listName):
            print("Your name is available in list ")
else: 
        print("Your name is not in this list")
    

#  Write a program to calculate the greate of a student from his marks from the following shceme:
makrs = int(input("Enter you marks :"))
if(marks<=100 and marks>=90):
        grade = 'Ex'
elif(marks<90 and makrs>=80):
        grade = "A"
elif(marks<80 and makrs>=70):
        grade = "B"
elif(marks<70 and makrs>=60):
        grade = "C"
elif(marks<60 and makrs>=50):
        grade = "D"
elif(marks<50):
        grade = 'F'
print("Your grade is : ", grade)

