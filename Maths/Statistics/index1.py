
### Example 1 ###
numbers = [1,2,3,4,5]
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered)

### Example 2 ###
"""A dictionary is a list of key-value pairs, with unique keys (mutable). From Python 2.7/3.1, {} can also represent a set of unique values (mutable)."""
my_dict = {x: x*2 for x in range(10)
           if x % 2 == 0}
print(my_dict)




