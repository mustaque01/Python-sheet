def split_and_join(string):
    return "-".join(string.split(" "))

# Example usage
input_string = "this is a test"
result = split_and_join(input_string)
print(result)  # ➞ "this-is-a-test"
