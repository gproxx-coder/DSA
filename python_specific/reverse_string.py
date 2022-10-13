# Reverse string without using slicing or any builtin function

def reverse_string(string):
    new_string = ''
    for char in string:
        new_string = char + new_string
    return new_string


string = "ABCDE"
print(reverse_string(string))
