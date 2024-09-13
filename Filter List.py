import timeit

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Code snippet using filter
filter_code = """
newList = list(filter(lambda x: x % 2 == 0, myList))
"""

# Code snippet using list comprehension
list_comp_code = """
newList = [x for x in myList if x % 2 == 0]
"""

# Measure the execution time of each code snippet
filter_time = timeit.timeit(filter_code, globals=globals(), number=100000)
list_comp_time = timeit.timeit(list_comp_code, globals=globals(), number=100000)

print(f"Filter function time: {filter_time}")
print(f"List comprehension time: {list_comp_time}")