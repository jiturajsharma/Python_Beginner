# Write a program to point multiplication table of a given number using for loop.
n = int(input("Enter a number : "))
for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")

#  Write a program to get all the person names stored a [list] and which starts with S.

ListofStudent = ["Jitu", "Sohan", "Honda", "Heros"]

for name in ListofStudent:
    if(name.startswith("H")):
        print(f"Hello {name}")

# 

n = int(input("Enter a number : "))

i =1
while(i<11):
    print(f'{n} X {i} = {n * i}')
    i +=1

n = int(input("Enter a number : "))

for i in range(2, n):
    if(i%n==0):
        print("Number is not prime: ")
        break
else: 
    print("Number is prime")


#  Write a program to find the sum of first the sum of first natural numbers using while loop.

num = int(input("Enter the number:"))
i = 1
sum = 0
while(i<num):
    sum += i
    i+=1

print("Sum of digit :", sum)

# Write a program to calculate the factorial of a given number listing for loop.
num = int(input("Enter the number : "))
product = 1
for i in range(1, n+1):
    product = product * 1

print(f"The factorial of {n} is {product}")


# write a program to follow the start pattern
