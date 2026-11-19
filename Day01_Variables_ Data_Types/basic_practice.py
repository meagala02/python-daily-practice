# =============================================================================
# QUESTION 1: Create Your First Variables
# =============================================================================

# Task:
#   Create two variables. One called name that stores a name, and one called
#   age that stores an age. Then print both values.

# ANSWER
print("=== Question 1 ===")
name = "Meagala"
age = 23
print(name)
print(age)

# =============================================================================
# QUESTION 2: Naming Variables the Right Way
# =============================================================================

# Task:
#   Create variables using good Python names:
#   first_name, last_name, student_age, city and _secret_code.
#   Print them to show they all work.

# ANSWER
print("=== Question 2 ===")
first_name = "Kavya"
last_name = "Sivakumar"
student_age = 12
city = "Vavuniya"
_secret_code = 4821
print(first_name, last_name)
print(student_age)
print(city)
print(_secret_code)

# =============================================================================
# QUESTION 3: Variable Assignment and Using Variables in Calculations
# =============================================================================

# Task:
#   You buy 5 apples. Each apple costs 20 rupees. Store these values in
#   variables, calculate the total cost, and print it with a label.

# ANSWER
print("=== Question 3 ===")
apples = 5
price_per_apple = 20
total_cost = apples * price_per_apple
print("Total cost:", total_cost)

# =============================================================================
# QUESTION 4: Integers (int)
# =============================================================================

# Task:
#   Create three integer variables: students (25), temperature (-4) and
#   population (1000000). Print them, check the type of students, and print
#   the sum of students and temperature.

# ANSWER
print("=== Question 4 ===")
students = 25
temperature = -4
population = 1_000_000
print(students)
print(temperature)
print(population)
print(type(students))
print(students + temperature)

# =============================================================================
# QUESTION 5: Floating-Point Numbers (float)
# =============================================================================

# Task:
#   Create float variables: price (19.99), height (1.75) and pi_value
#   (3.14159). Print them, check the type of price, print price multiplied by
#   2, and show that 10.0 is also a float.

# ANSWER
print("=== Question 5 ===")
price = 19.99
height = 1.75
pi_value = 3.14159
print(price)
print(height)
print(pi_value)
print(type(price))
print(price * 2)
whole_float = 10.0
print(type(whole_float))

# =============================================================================
# QUESTION 6: Strings (str)
# =============================================================================

# Task:
#   Create two strings: "Hello" using double quotes and 'Python' using single
#   quotes. Join them with a space between to make one sentence. Print the
#   sentence, its length, "Hello" repeated 3 times, and the type of sentence.
#   Also store the text It's fun in a variable and print it.

# ANSWER
print("=== Question 6 ===")
first_word = "Hello"
second_word = 'Python'
sentence = first_word + " " + second_word
print(sentence)
print(len(sentence))        # characters count (with space)
print(first_word * 3)
print(type(sentence))
message = "It's fun"
print(message)

# =============================================================================
# QUESTION 7: Booleans (bool)
# =============================================================================

# Task:
#   Create two boolean variables: is_raining (True) and is_sunny (False).
#   Print them and the type of is_raining. Then print the result of 10 > 5
#   and 10 == 5.

# ANSWER
print("=== Question 7 ===")
is_raining = True
is_sunny = False
print(is_raining)
print(is_sunny)
print(type(is_raining))
print(10 > 5)
print(10 == 5)

# =============================================================================
# QUESTION 8: Checking Data Types with type()
# =============================================================================

# Task:
#   Print the data type of each of these values:
#   42, 3.14, "42", True, 4.0 and "True".

# ANSWER
print("=== Question 8 ===")
print(type(42))
print(type(3.14))
print(type("42"))
print(type(True))
print(type(4.0))
print(type("True"))

# =============================================================================
# QUESTION 9: Multiple Variable Assignment
# =============================================================================

# Task:
#   1. Assign the values 1, 2 and 3 to the variables x, y and z in ONE line.
#   2. Give a, b and c the same value 0 in ONE line.
#   3. Create name, age and height in one line using a string, an int and a
#      float. Print everything.

# ANSWER
print("=== Question 9 ===")
x, y, z = 1, 2, 3
print(x, y, z)

a = b = c = 0
print(a, b, c)

name, age, height = "Lee", 14, 1.60
print(name, age, height)

# =============================================================================
# QUESTION 10: Variable Reassignment
# =============================================================================

# Task:
#   Create a variable score with the value 0. Change it to 10, then add 5 to
#   it, then add 5 more using +=. Finally, change score to the text "Winner".
#   Print the value after every change, and the type at the end.

# ANSWER
print("=== Question 10 ===")
score = 0
print("Start score:", score)

score = 10
print("After changing to 10:", score)

score = score + 5
print("After adding 5:", score)

score += 5
print("After += 5:", score)

score = "Winner"
print("Now score is:", score)
print(type(score))

# =============================================================================
# QUESTION 11: Swapping Two Variables
# =============================================================================

# Task:
#   Swap the values of first = "apple" and second = "banana".
#   Do it once with a temporary variable. Then swap x = 1 and y = 2 using
#   the Python shortcut.

# ANSWER
print("=== Question 11 ===")
first = "apple"
second = "banana"

temp = first
first = second
second = temp
print(first, second)

x = 1
y = 2
x, y = y, x
print(x, y)

# =============================================================================
# QUESTION 12: Student Profile (Putting It All Together)
# =============================================================================

# Task:
#   Create four variables: student_name (a string), student_age (an int),
#   student_height (a float) and is_enrolled (a boolean). Print each value
#   together with its data type.

# ANSWER
print("=== Question 12 ===")
student_name = "Lee"
student_age = 14
student_height = 1.6
is_enrolled = True

print("Name:", student_name, "| type:", type(student_name))
print("Age:", student_age, "| type:", type(student_age))
print("Height:", student_height, "| type:", type(student_height))
print("Enrolled:", is_enrolled, "| type:", type(is_enrolled))