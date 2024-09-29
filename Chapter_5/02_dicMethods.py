#  empty dictonary can be created as
a = {}
a.update({"jitu": 600})
print(type(a), a)
print(type(a))
marks = {
    "jitu" : 100,
    "Shubham": 65,
    "Rohan" : 32,
    0: "Tesing"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"jitu":300, "raj": 900})   # if we have value then update other wise added new key value
print(marks)
print(marks.get("jitu"))    # error
# print(marks.get("Jitu"))  #print none
print(marks["jitu"])
# print(marks["Jitu"])    # it is case sensative

# marks.clear()
# print(marks)

newValueCopy = marks.copy()
print(newValueCopy)


#  we can find out length of the dictatonary
print(len(a))