def find_maximum(lst):
    return max(lst)

# Read 3 elements from the user
elements = []
for i in range(3):
    num = float(input(f"Enter element {i+1}: "))
    elements.append(num)

maximum = find_maximum(elements)
print("The maximum element is:", maximum)