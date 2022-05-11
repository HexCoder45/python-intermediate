#Creating a List
list_of_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'Saturday' ]

#Printing a list
print(list_of_days)

#Printing Particular elements of list
print(list_of_days[1])

# Print number of elements in the list 
print(len(list_of_days))

# Itering over List
for item in list_of_days:
	print(item)

#Appending to the list 
list_of_days.append('rishabhday')

print(list_of_days)

#Removing item from list 
list_of_days.remove('rishabhday')

print(list_of_days)

#Removing item at a particular index
list_of_days.append('abhinavday')
print(list_of_days)
del list_of_days[7]
print(list_of_days)

# Negative Indexing 
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Aug', 'September', 'October', 'November', 'December']
print(months[-1])


#Change a particular element
months[7] = 'August'
print(months)


#Check if an item exists in a list or not
myMonth = "March"

if myMonth in months:
	print(f'Yes, {myMonth} is contained in the list')



#Copy One list to another
orignal_shopping_list = ['Coke', 'Chips', 'Chocolate']
duplicate_shopping_list = orignal_shopping_list.copy()

duplicate_shopping_list[1] = "Nachos"

print(duplicate_shopping_list)
print(orignal_shopping_list)

#Without using copy
list1 = ['A', 'B', 'C']
list2 = list1
print(list2)
list2[1] = 'X'
print(list2)
print(list1)























