list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# Iterate over list1 in original order and list2 in reverse order
for item1, item2 in zip(list1, reversed(list2)):
    print(item1, item2)
