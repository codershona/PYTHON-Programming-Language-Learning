# Python Lists
# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

# List
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

# Example
# Create a List:

# thislist = ["apple", "banana", "cherry"]
# print(thislist)



thislist = ["apple", "banana", "cherry"]
print(thislist)



# Access Items  :
# You access the list items by referring to the index number:

# Example
# Print the second item of the list:

# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[1])



# Negative Indexing :
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.

# Example
# Print the last item of the list:

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])



thislist = ["apple", "banana", "cherry"]
print(thislist[-1])





# Range of Indexes :
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.

# Example
# Return the third, fourth, and fifth item:

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])





thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included




# Note: The search will start at index 2 (included) and end at index 5 (not included).

# Remember that the first item has index 0.

# By leaving out the start value, the range will start at the first item:

# Example
# This example returns the items from the beginning to "orange":

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])




thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This will return the items from index 0 to index 4.

#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included



# By leaving out the end value, the range will go on to the end of the list:

# Example
# This example returns the items from "cherry" and to the end:

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This will return the items from index 2 to the end.

#Remember that index 0 is the first item, and index 2 is the third





# Range of Negative Indexes :


# Specify negative indexes if you want to start the search from the end of the list:

# Example
# This example returns the items from index -4 (included) to index -1 (excluded)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,







# Change Item Value :
# To change the value of a specific item, refer to the index number:
# Example
# Change the second item:

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)



# Loop Through a List  :
# You can loop through the list items by using a for loop:

# Example
# Print all items in the list, one by one:

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)



thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)



# Check if Item Exists :
# To determine if a specified item is present in a list use the in keyword:

# Example
# Check if "apple" is present in the list:

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")



thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")





# List Length :
# To determine how many items a list has, use the len() function:

# Example
# Print the number of items in the list:

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))



thislist = ["apple", "banana", "cherry"]
print(len(thislist))




# Add Items  :

# To add an item to the end of the list, use the append() method:

# Example
# Using the append() method to append an item:

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)


thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)



# To add an item at the specified index, use the insert() method:

# Example
# Insert an item as the second position:

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)





# Remove Item  :
# There are several methods to remove items from a list:

# Example
# The remove() method removes the specified item:

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)



# Example
# The pop() method removes the specified index, (or the last item if index is not specified):

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)



# Example
# The del keyword removes the specified index:

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)




thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)





# Example
# The del keyword can also delete the list completely:

# thislist = ["apple", "banana", "cherry"]
# del thislist



thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".




# Example
# The clear() method empties the list:

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
















































