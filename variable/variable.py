#rule of defining variables in python
#1. variable name should start with a letter or underscore(_)
#2. variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#3. variable name are case-sensitive (age, Age and AGE are three different variables)
#4. variable name should not be a reserved word (like python keywords)
#5. variable name should be meaningful  
#6. you cannot use special symbols like !, @, #, $, % etc in variable names
#7. you cannot use spaces in variable names, instead use underscore(_) to separate words in a variable name
#8. you cannot use numbers to start a variable name, but can use numbers after the first letter (like age1 is valid but 1age is not valid)
age = 25
name = "John"
is_student = True
height_in_meters = 1.75
weight_in_kg = 70.5
#you can also assign multiple variables in one line
x, y, z = 10, 20, 30
#you can also assign the same value to multiple variables in one line
a = b = c = 100
#you can also use variables to assign values to other variables
d = a + b + c
print(age)
print(name)
print(is_student)
print(height_in_meters)
print(weight_in_kg)
print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
print(d)
print("Hello, World!");
print(abs(-5));
print(max(1, 5, 3, 9, 2));
print(min(1, 5, 3, 9, 2));
print(pow(2, 3));
print(round(3.6));
print(sum([1, 2, 3, 4, 5]));
