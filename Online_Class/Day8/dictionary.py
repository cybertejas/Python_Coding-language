# 

myDt = {
    "Name":"Amazing Guide",
    "Year":2020,
    "Field":"Education"
}
# print(myDt)
# print(type(myDt))

# Accessing one specific item from the list 
# print(myDt["Name"])

#Using get() method
# print(myDt.get('Field'))


myDt2 = {
    "Name":"Amazing Guide",
    # 123_:2020,
    "Name":"The Amazing Guide",
    "Field":"Education"
}
# print(myDt2)
# print(len(myDt2))

# To get all the keys 
# print(myDt2.keys())

# To get all the values
# print(myDt2.values())

# both keys and values 
# print(myDt.items())

# Update a dictionary item
myDt3 = {
    "Name":"The Amazing Guide",
    "Field":"Education"
}
myDt3.update({"Field":"Technical Education"})
# print(myDt3)

myDt3['Year']= 2020
myDt3['Team']= 20
# print(myDt3)
#Removes a specific item
# myDt3.pop("Year")

#removes last inserted item
# myDt3.popitem()
# print(myDt3)

del myDt3
