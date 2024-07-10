# x = 30
# print(x)
# x = 40

#Variables can hold one value at a time 
my_List =[10,20,30,20,25,47]
#         0  1   2  3  4  5
print(my_List)

print(my_List[3])
print(my_List[5])

#List with diffrent types of values
my_list2 =[100,True,"Hello","20",25.678,47]
print(my_list2[2])
#Trying to print more than largest index
#print(my_List[8])     #list index out of range

#Negative Indexing
#         my_List =[10, 20, 30, 20, 25, 47]
#                   0    1   2   3   4   5
# Negaitive Index= -6   -5  -4  -3   -2  -1
print("Last index with Negative indexing :",my_List[-1])
print("Negative Indexing :",my_List[-4])


#Updating a particular item in the list
my_list2[2]="Hello World"
print(my_list2)


#Adding new item to the list
my_list2.append(500)
#we can only append one item at a time
#my_list2.append(50,300,"Wow!")



#Create a list to append multiple items at once
my_list3= [50,300,"Wow!"]
my_list2.append(my_list3)
print(my_list2)
print(len(my_list2))


#Appeding items at a specific index
my_list3.insert(1,2000)
my_list3.insert(3,"Hey!!!")
print(my_list3)


#Removing an item from the list
my_list3.remove(2000)
print(my_list3)

#remove an item from a particular index
#my_list2 =[100,True,"Hello World","20",25.678,47]
# my_list2.pop(1)
# my_list2.pop(1)
# print(my_list2)


#slicing of lists
print('''

----------------- Slicing in Python Lists ----------------------

''')
print("Complete Lists : ")
print(my_list2[0:])
print(my_list2[:8])
print(my_list2[:])

print("Specific slice")
print(my_list2[3:])
print(my_list2[3:6])
print(my_list2[0:3])

#Step in subslicing
print("--------------------- Steps in Python ------------------")
print(my_list2[0:3:1])
print(my_list2[0:8:2])

#Subsling with negative index
print(my_list2[-3:])
print(my_list2[-7:-3])
# print(my_list2[-3:-7])


#del my_list2
my_list2.clear()
print(my_list2)