- strings are immutable

- sorted() can be used to sort string. Use ''.join to create the new sorted string

- Counter from collections module - to count occurrences of elements in a list
Example:
 from collections import Counter
 my_list = [1,2,2,3,3,3]
 count = Counter(my_list)
 print(count)  # Output: Counter({3: 3, 2: 2, 1: 1})

 - float('inf') and float('-inf') can be used to represent positive and negative infinity respectively.

 - Use [] when: You don’t know the size in advance and **will append items**.

 - Use [value] * n when: You know the final size and want to **assign by index**.