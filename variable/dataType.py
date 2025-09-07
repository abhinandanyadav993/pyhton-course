# Python supports several built-in data types:

# 1. Integer (int): Whole numbers, positive or negative, without decimals.
age = 25
print("Integer example:", age, type(age))

# 2. Float: Numbers with decimal points.
height = 1.75
print("Float example:", height, type(height))

# 3. String (str): Sequence of characters, enclosed in single or double quotes.
name = "John"
message = 'Hello, World!'
print("String example:", name, type(name))
print("Another string:", message, type(message))

# 4. Boolean (bool): Represents True or False.
is_student = True
has_graduated = False
print("Boolean example:", is_student, type(is_student))
print("Another boolean:", has_graduated, type(has_graduated))

# 5. List: Ordered, mutable collection of items, enclosed in square brackets.
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
print("List example:", fruits, type(fruits))
print("Another list:", numbers, type(numbers))

# 6. Tuple: Ordered, immutable collection of items, enclosed in parentheses.
coordinates = (10, 20)
colors = ("red", "green", "blue")
print("Tuple example:", coordinates, type(coordinates))
print("Another tuple:", colors, type(colors))

# 7. Dictionary (dict): Unordered collection of key-value pairs, enclosed in curly braces.
person = {"name": "Alice", "age": 30, "city": "New York"}
grades = {"math": 90, "science": 85}
print("Dictionary example:", person, type(person))
print("Another dictionary:", grades, type(grades))

# 8. Set: Unordered collection of unique items, enclosed in curly braces.
unique_numbers = {1, 2, 3, 4, 5}
letters = {"a", "b", "c"}
print("Set example:", unique_numbers, type(unique_numbers))
print("Another set:", letters, type(letters))

# Additional examples:
# Complex number (complex): For mathematical computations.
complex_num = 3 + 4j
print("Complex example:", complex_num, type(complex_num))

# NoneType: Represents the absence of a value.
result = None
print("NoneType example:", result, type(result))
