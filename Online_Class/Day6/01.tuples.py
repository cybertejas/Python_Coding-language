myTuple = ("Hello","World","Python","Hello","Hello")

print(myTuple)

my_List =[10,20,30,20,25,47]

# print(myTuple.count("Hello"))
# print(myTuple.index("Python"))

secondTuple = ("Apple",)
# print(secondTuple)

# print(len(myTuple))

#Accessing a parrticular element 
#myTuple = ("Hello","World","Python","Hello","Hello")
# myTuple[2] = "Tuple is useless"
print(myTuple[2])
converted_tuple = list(myTuple)
print(converted_tuple)
converted_tuple.append("Are tuples useless?")
print(converted_tuple)
print(tuple(converted_tuple))


del secondTuple


#Unpacking of Tuples 
habits = ("Cricket","Sleeping","Eating","Maar Khana","Daant Khana")
# habits = ("Cricket","Sleeping","Eating")
# (useful, useless , notTomention)=habits
(useful, * useless, notTomention)=habits
# (useful, useless, * notTomention)=habits
print(useful)
print(useless)
print(notTomention)


tuple1 = (1,2,3,4,5)
tuple2 = (6,7,8,9,10)
print(tuple1 + tuple2)
print(tuple1*10)
# print(tuple1*100)