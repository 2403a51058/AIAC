
# The issue is that the list contains both integers and strings, which cannot be directly compared in Python 3.
# To fix this, we can convert all items to strings before sorting for consistent sorting.

def sort_list_consistent(data):
    return sorted(data, key=str)

items = [3, "apple", 1, "banana", 2]
print(sort_list_consistent(items))

