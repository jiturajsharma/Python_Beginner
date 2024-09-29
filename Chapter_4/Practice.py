#  Write a program to store seven fruits in a list entered by the user.
Fruits = []
Fru1 = input("Enter the First Fruit name : ")
Fruits.append(Fru1)
Fru2 = input("Enter the Second Fruit name : ")
Fruits.append(Fru2)
Fru3 = input("Enter the Third Fruit name : ")
Fruits.append(Fru3)
Fru4 = input("Enter the Fourth Fruit name : ")
Fruits.append(Fru4)
Fru5 = input("Enter the Five Fruit name : ")
Fruits.append(Fru5)
Fru6 = input("Enter the Six Fruit name : ")
Fruits.append(Fru6)
Fru7 = input("Enter the Seven Fruit name : ")
Fruits.append(Fru7)

print(Fruits)

# write a program to accept marks of 6 students nad display them in a sorted manner.

StudentMarks = []

Math = int(input('Enter the Marks Math : '))
StudentMarks.append(Math)
Biology = int(input('Enter the Marks Biology : '))
StudentMarks.append(Biology)
snk = int(input('Enter the Marks snk : '))
StudentMarks.append(snk)
english = int(input('Enter the Marks english : '))
StudentMarks.append(english)
hindi = int(input('Enter the Marks hindi : '))
StudentMarks.append(hindi)
social = int(input('Enter the Marks social : '))
StudentMarks.append(social)
java= int(input('Enter the Marks java : '))
StudentMarks.append(java)

StudentMarks.sort()
print(StudentMarks)

#  check that a tupple type  cannot be changed in python
a = (5,64)
# a[1] = "String"
print(a)

# Write a program to sum a list with four number
SumOfList = [43,645,75,34]
print(sum(SumOfList))

#  Write a program to count the nbumbe rof zeros in the following tupples.
a = (43, 0, 0, 0, 43,645,0, 0, 0)
print(a.count(0))