# Sets - unordered , unchangeble , duplicates not allowed

myTuple = (2,2,2)
# print(myTuple)
# mySet = {2,2,2}
# print(len(mySet))
# print(mySet)

# True == 1 == 1.0 , False == 0 == 0.0
# set1= {True, 1 , 1.01 , 0 , False, 0.03}
# print(len(set1))
# print(set1)

#Accessing items in a set 
newSet = {"Hello",True, 123,145.67,False,"Coding"}
# for x in newSet:
#     print(x)

newSet.add("Python")
# for x in newSet:
#     print(x)

Set1= {1,2,3,5}   
Set2= {5,6,7}
# print(Set1.union(Set2))
# print(Set1.intersection(Set2))
# Union of Sets = {1,2,3,5,6,7}
# Intersection = {5}

# If thatb itme does not exist discard will not through an error
# Set1.discard(4)

#Set1.remove(4)

Set1.pop()
print(Set1)

# Set1.clear()
# print(Set1)
# del Set1
# print(Set1)