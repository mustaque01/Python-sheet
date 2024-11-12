# Read the integer n
n = int(input())

# Read the space-separated integers, convert them to a list and then to a tuple
t = tuple(map(int, input().split()))

# Compute the hash of the tuple
print(hash(t))
