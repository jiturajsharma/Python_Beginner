s = set()  # no repetition allowed
print(type(s))

s.add(54)       # if we put same value again and again and print them so print only one
s.add(54)
s.add(57)
s.add(55)
print(s)
print(len(s))
#  we can remove the value what ever you want 
s.remove(54)
print(len(s))

#  pop() remove an arbitray element from the set and return the element removed which is remove random only
s.pop()
print(len(s))

#  if we have two set then we  can combine two set 'union'
r = {1,2,45, 3}
b = {4,5,3,3}
print(type(r))
UnionValue = r.union(b)
print(UnionValue)


#  Intersection of two set
t = {2,3,5}
y = {3,5,6}

IntersectionValue = t.intersection(y)
print(IntersectionValue)