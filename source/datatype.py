# integer data type
d = -20
e = 20
print(d+e)

#
# float data type
a = 10.2
b = 20.1
print(a+b)

# Example of float data type usage
c = 3.14
d = 2.71
print(c * d)

# More float operations
x = 5.5
y = 2.2
print(x / y)

# Using float with a function
def calculate_area(radius):
    return 3.14159 * radius * radius

print(calculate_area(5.0))

#
#string data type
# Example of string data type
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)

# Multiline string
multiline_string = """This is a string that spans
multiple lines within triple quotes."""
print(multiline_string)

#
# Boolean
# Boolean data type examples
is_active = True
has_license = False

# Printing boolean values
print("Is active:", is_active)
print("Has license:", has_license)

# Using boolean in conditional statements
if is_active:
    print("The account is currently active.")
else:
    print("The account is not active.")

# Combining boolean values with logical operators
print("Active and has license:", is_active and has_license)
print("Active or has license:", is_active or has_license)
print("Not active:", not is_active)

#
# Example of list data type
numbers = [1, 2, 3, 4, 5]
print("List of numbers:", numbers)

# Accessing list elements
print("First number:", numbers[0])
print("Last number:", numbers[-1])

# List operations
numbers.append(6)  # Adding an element
print("List after appending 6:", numbers)

numbers.remove(3)  # Removing an element
print("List after removing 3:", numbers)

# Slicing a list
sub_numbers = numbers[1:4]
print("Sublist from index 1 to 4:", sub_numbers)

# List comprehension
squares = [x * x for x in numbers]
print("Squares of numbers:", squares)

#
# Example of tuple data type
example_tuple = (10, 20, 30, 40, 50)
print("Tuple of numbers:", example_tuple)

# Accessing tuple elements
print("First element of tuple:", example_tuple[0])
print("Last element of tuple:", example_tuple[-1])

# Tuple cannot be changed (immutable), trying to change will raise an error
# Uncommenting the following line will raise an error
# example_tuple[0] = 60

# Tuple slicing
sub_tuple = example_tuple[1:4]
print("Subtuple from index 1 to 4:", sub_tuple)

# Tuple unpacking
a, b, c, d, e = example_tuple
print("Unpacked tuple:", a, b, c, d, e)

# Using tuple in a function
def min_max(numbers):
    return min(numbers), max(numbers)

min_num, max_num = min_max(example_tuple)
print("Minimum and maximum numbers in the tuple:", min_num, max_num)

#
# Example of dictionary data type
example_dict = {"name": "John", "age": 30, "city": "New York"}
print("Dictionary:", example_dict)

# Accessing dictionary elements
print("Name:", example_dict["name"])
print("Age:", example_dict["age"])

# Adding a new key-value pair
example_dict["email"] = "john@example.com"
print("Dictionary after adding email:", example_dict)

# Removing a key-value pair
del example_dict["city"]
print("Dictionary after removing city:", example_dict)

# Dictionary comprehension
squared_numbers = {x: x*x for x in range(6)}
print("Dictionary of squared numbers:", squared_numbers)

# Iterating through a dictionary
for key, value in example_dict.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "name" in example_dict:
    print("Name is a key in the dictionary")

# Getting the length of a dictionary
print("Number of items in the dictionary:", len(example_dict))

#
# Example of set data type
example_set = {1, 2, 3, 4, 5}
print("Set:", example_set)

# Adding elements to a set
example_set.add(6)
print("Set after adding an element:", example_set)

# Removing elements from a set
example_set.discard(2)
print("Set after removing an element:", example_set)

# Set operations
another_set = {4, 5, 6, 7, 8}
intersection_set = example_set.intersection(another_set)
print("Intersection of sets:", intersection_set)

union_set = example_set.union(another_set)
print("Union of sets:", union_set)

difference_set = example_set.difference(another_set)
print("Difference of sets:", difference_set)

# Checking if an element is in a set
if 1 in example_set:
    print("1 is in the set")

# Set comprehension
squared_set = {x * x for x in range(10)}
print("Squared set:", squared_set)

# Example of type conversion using built-in functions
initial_value = 10
converted_to_float = float(initial_value)
print("Original integer:", initial_value, "Converted to float:", converted_to_float)
