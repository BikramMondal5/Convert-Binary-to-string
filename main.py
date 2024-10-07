 def binary_to_string(binary_string):

    binary_values = binary_string.split()

    ascii_characters = [chr(int(b, 2)) for b in binary_values]

    return ''.join(ascii_characters)


binary_string = ""

output_string = binary_to_string(binary_string)

print(f"String representation of '{binary_string}': {output_string}")
