# Initialize the list
lst = []

# Read the number of commands
n = int(input())

# Iterate through each command
for _ in range(n):
    command = input().split()
    
    # Command 1: insert i e
    if command[0] == 'insert':
        i = int(command[1])
        e = int(command[2])
        lst.insert(i, e)
    
    # Command 2: print
    elif command[0] == 'print':
        print(lst)
    
    # Command 3: remove e
    elif command[0] == 'remove':
        e = int(command[1])
        lst.remove(e)
    
    # Command 4: append e
    elif command[0] == 'append':
        e = int(command[1])
        lst.append(e)
    
    # Command 5: sort
    elif command[0] == 'sort':
        lst.sort()
    
    # Command 6: pop
    elif command[0] == 'pop':
        lst.pop()
    
    # Command 7: reverse
    elif command[0] == 'reverse':
        lst.reverse()