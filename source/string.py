# String repetition
repeat_string = "Python! " * 3
print(repeat_string)

# Accessing string characters
sample_string = "Hello World"
first_letter = sample_string[0]
print("First letter:", first_letter)
last_letter = sample_string[-1]
print("Last letter:", last_letter)


# String length
string_length = len(sample_string)
print("Length of string:", string_length)

# String methods
lowercase_string = sample_string.lower()
print("Lowercase:", lowercase_string)
uppercase_string = sample_string.upper()
print("Uppercase:", uppercase_string)

# String formatting
age = 30
info = "My name is {} and I am {} years old.".format(name, age)
print(info)

# f-string (available from Python 3.6+)
info_fstring = f"My name is {name} and I am {age} years old."
print(info_fstring)