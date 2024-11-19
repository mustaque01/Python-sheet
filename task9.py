def check_weirdness(n):
    if n % 2 != 0:  # If n is odd
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:  # If n is even and in the range 2 to 5
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:  # If n is even and in the range 6 to 20
        print("Weird")
    elif n % 2 == 0 and n > 20:  # If n is even and greater than 20
        print("Not Weird")

# Example usage
check_weirdness(3)   # ➞ Weird
check_weirdness(4)   # ➞ Not Weird
check_weirdness(18)  # ➞ Weird
check_weirdness(22)  # ➞ Not Weird
