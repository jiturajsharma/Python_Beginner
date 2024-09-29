friend = ["rajesh", False, 'jitu', 5, 5.65]
print(friend)
friend[1] = True
print(friend)
print(friend[1:3])
# print(friend.append("AddedValue"))
friend.append("Added Value")
print(friend)

# short is a basically arrrage small to large value
ListTry = [12,45,75,43,34]
ListTry.sort()
print(ListTry)

ListTry.reverse()
print(ListTry)
ListTry.insert(2, "Jitu raj sharma")
print(ListTry)

# POP list detelet the element 
ListTry.pop(2)
print(ListTry)

# Remove methods
ListTry.remove(12)
print(ListTry)

