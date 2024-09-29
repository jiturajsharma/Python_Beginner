# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

HindiWorld = {
    'Fan': 'Pankha',
    'Book' : 'Kitab',
    'Girl': 'ladhaki',
    'School': 'Vidyalaya'
}
# word = input('Enter the world in english : ')

# print(HindiWorld[word])


#  Write a program to input eight numbers from the user and display all the unique number(once)

UniqueNumbers = set()

# Number1 = int(input("Enter the number one  : "))
# UniqueNumbers.add(Number1)
# Number2 = int(input("Enter the number two : "))
# UniqueNumbers.add(Number2)
# Number3 = int(input("Enter the number three : "))
# UniqueNumbers.add(Number3)
# Number4 = int(input("Enter the number four : "))
# UniqueNumbers.add(Number4)
# Number5 = int(input("Enter the number five: "))
# UniqueNumbers.add(Number5)
# Number6 = int(input("Enter the number six: "))
# UniqueNumbers.add(Number6)
# Number7 = int(input("Enter the number  seven: "))
# UniqueNumbers.add(Number7)
# Number8 = int(input("Enter the number eight: "))
# UniqueNumbers.add(Number8)
# Number9= int(input("Enter the number nine: "))
# UniqueNumbers.add(Number9)
# print(UniqueNumbers)


#  Can we have a set with 18(int) and '18' (str) as a value in it?
a = {32,54,675, "18", 18}
print(a)

#  what will be the length of following set s:
s = set()
s.add(20)
s.add(20.99)
s.add('20.99')
print(len(s))

#  What is the  type of 's'?
s = {}
b = {6,4,4,43}
print(type(s))
print(type(b))

#  Create an empty dictionary. Allow 4 frinds to enter their favorite language as value and use key as their names. Assume that the names are unique.
FriendList = {}

Friend1 = input("Enter the name Friend One  : ")
language1 = input("Enter the language : ")
FriendList.update({Friend1: language1})

Friend2 = input("Enter the name Friend Two  : ")
language2 = input("Enter the language : ")
FriendList.update({Friend2: language2})

Friend3 = input("Enter the name Friend One  : ")
language3 = input("Enter the language : ")
FriendList.update({Friend3: language3})

Friend4 = input("Enter the name Friend One  : ")
language4 = input("Enter the language : ")
FriendList.update({Friend4: language4})

print(FriendList)


E = {8, 7, 12, "Harry", [1,2]}
E.update("Harry")
print(type(E), E)