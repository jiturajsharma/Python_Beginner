ListValue = ('jitu', 543, 435.64, True, 'Sharma')
print(ListValue)

# Count is counting how much value is given in orignal tupple
HowmuchValue = ListValue.count('jitu')
print(HowmuchValue)

# Find indexes in original tupple 
c = ListValue.index('jitu')  # it is find only first time if we got first then it code stoped
print(c)

# multiplying the value
MultiplyingValue = ListValue * 3
print(MultiplyingValue)

# finding value in orignal tuppe in value will be true or false
print('jitu' in ListValue)
print(True in ListValue)
print(False in ListValue)

# find in length
print(len(ListValue))