- del - 

- .count method - 

 .items, .keys, .values

 - reversed() function

- strings are immutable

- sorted() can be used to sort string. Use ''.join to create the new sorted string

- Enumerate - to get both index and element

- There is no "null" in python. If you want to initialise a null value use "None"

- list[::-1] reverses the list but it doesn't modify the list, instead creates a copy

- Counter from collections module - to count occurrences of elements in a list
Example:
 from collections import Counter
 my_list = [1,2,2,3,3,3]
 count = Counter(my_list)
 print(count)  # Output: Counter({3: 3, 2: 2, 1: 1})

 - float('inf') and float('-inf') can be used to represent positive and negative infinity respectively.