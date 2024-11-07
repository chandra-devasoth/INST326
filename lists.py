# Create a list of strings
fruits = ["apple", "banana", "cherry"]

# Print the original list
print("Original List:", fruits)

# Indexing: Access a specific element
print("First Fruit:", fruits[0])

# Slicing: Get a subset of elements
print("First Two Fruits:", fruits[:2])

# Append: Add an element to the end
fruits.append("date")
print("List after appending 'date':", fruits)

# Insert: Add an element at a specific position
fruits.insert(1, "elderberry")
print("List after inserting 'elderberry' at index 1:", fruits)

# Remove: Remove the first occurrence of an element
fruits.remove("banana")
print("List after removing 'banana':", fruits)

# Sort: Sort the list in-place
fruits.sort()
print("Sorted List:", fruits)

# Reverse: Reverse the list in-place
fruits.reverse()
print("Reversed List:", fruits)

# Find the index of an element
print("Index of 'cherry':", fruits.index("cherry"))

# Check if an element is in the list
print("Is 'apple' in the list?", "apple" in fruits)

# Get the length of the list
print("Length of the list:", len(fruits))

# Clear the list
fruits.clear()
print("List after clearing:", fruits)