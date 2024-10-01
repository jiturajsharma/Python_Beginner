a = int(input("Enter Your age: "))

if(a>=18):
    print("You are avobe the age of consent")
    print("Oh You are under age of consent")
elif(a<0):
    print("You are entered negative age")
elif(a==0):
    print("You are entering 0 age which is not valid") 
else:
    print("You are below the age of consent")

print("End of the Code execution")