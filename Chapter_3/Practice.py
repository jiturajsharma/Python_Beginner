#  Write a python program to disply a user entered name followed by Good Afternoon using inpout() function

boy = input("Student  message: ")
print(f"Teacher says {boy}")

#  Write a program to fill in a letter templete given below with name and date
letter = '''
                Dear <|Name|>,
                You are selected!
                <|Date|>
'''
print(letter.replace("<|Name|", "Jitu").replace("<|Date|>", "28 september 2025"))


#  write a program to detect double spaces in a string
d = "jitu is a very     smart boy he is understand       verything"
f = d.find("  ");
print("space is detected", f)
e = d.replace("  ", "_");
print(e)
print( e)
        

#  Replace the doubel spaces from problesm 3 with single spaces.
d = "jitu is a very smart boy he is understand   verything"
print(d.replace("  ", ""))
print(d)             # Strings are immutable which means that you cannot change them by running functions on them



# Write a program to format the following letter using escape sequence charactyers.
Letter = "Dear Jitu, \nYou are learning python \tcourses is nice. \nThanks!"
print(Letter)
