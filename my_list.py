#Creating an empty list
my_list = []
print("This is an empty list: ", my_list)

# Appending 10, 20, 30 and 40 to the list
my_list.extend([10, 20, 30, 40])
print("This is the list after appending 10, 20, 30 and 40: ", my_list)

#Inserting 15 at the second position of the list
my_list.insert(1,15)
print("This is the list after inserting 15 at the second position: ", my_list)

#Extending the list with another list [50, 60]
my_list.extend([50,60])
print("This is the list after extending it with [50, 60]: ", my_list)

#Removing the last element from the list
my_list.pop()
print("This is the list after removing the last element: ", my_list)

#Sorting the list in ascending order
my_list.sort()
print("This is the list after sorting it in ascending order: ", my_list)

#Finding and printing the index of 30
print("The index of 30 is: ", my_list.index(30))