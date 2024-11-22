def modify_string(string, index, new_char):
    # Convert the string to a list of characters
    string_list = list(string)
    
    # Modify the character at the given index
    string_list[index] = new_char
    
    # Join the list back into a string
    return "".join(string_list)

# Example usage
original_string = "hello"
index_to_modify = 1
new_character = "a"
modified_string = modify_string(original_string, index_to_modify, new_character)
print(modified_string)  # ➞ "hallo"
