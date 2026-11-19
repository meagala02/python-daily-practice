# =============================================================================
# QUESTION 1: Converting Between Strings and Integers
# =============================================================================

# Task:
#   The text "15" is stored in age_text. Convert it to an integer, add 1 and
#   print the result. Then convert the number 100 into a string and join it
#   with the word " points". Print the types of all three variables.

# Answer 
print("=== Question 1 ===")
age_text = "15"
age_number = int(age_text)
print(age_number + 1 )

number = 100 
text_number = str(number)
print(text_number +" points")

print(type(age_text))
print(type(age_number))
print(type(text_number))

# =============================================================================
# QUESTION 2: Converting Between Floats and Integers
# =============================================================================

# Task:
#   Convert 9.99 to an integer and print it. Then print round(9.99). Convert
#   7 to a float. Convert the text "3.5" to a float and add 1. Finally print
#   int(-2.7).

# Answer 
print("=== Question 2 ===")
price = 9.99
price_as_int = int(price)
print(price_as_int)         # 9
print(round(price))         # 10

whole = 7
whole_as_float = float(whole)
print(whole_as_float)       # 7.0

print(float("3.5") + 1)     # 4.5
print(int(-2.7))            # -2

# =============================================================================
# QUESTION 3: Converting to Boolean
# =============================================================================

# Task:
#   Print bool() of these values: 0, 1, -5, 0.0, "" (empty string),
#   "hello", "False" and None. Then print int(True), int(False) and
#   True + True.

# ANSWER
print("=== Question 3 ===")
print(bool(0))
print(bool(1))
print(bool(-5))
print(bool(0.0))
print(bool(""))
print(bool("hello"))
print(bool("False"))
print(bool(None))

print(int(True))
print(int(False))
print(True + True)

# =============================================================================
# QUESTION 4: Arithmetic Operators
# =============================================================================

# Task:
#   Store a = 17 and b = 5. Print the result of addition, subtraction,
#   multiplication, division, floor division, remainder (modulus) and b to
#   the power of 2.

# ANSWER
print("=== Question 4 ===")
a = 17
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Remainder:", a % b)
print("Power:", b ** 2)

# =============================================================================
# QUESTION 5: What Type Does the Answer Have?
# =============================================================================

# Task:
#   Print the type of 5 + 3, 5 + 3.0, 10 / 2 and 10 // 2. Also print the
#   values of 10 / 2, 10 // 2, 2 * 2.5 and 7 // 2.0.

# ANSWER
print("=== Question 5 ===")
print(type(5 + 3))
print(type(5 + 3.0))
print(10 / 2)
print(type(10 / 2))
print(10 // 2)
print(type(10 // 2))
print(2 * 2.5)
print(7 // 2.0)

# =============================================================================
# QUESTION 6: Working with Strings
# =============================================================================

# Task:
#   Using word = "Python", print it in uppercase, lowercase, its length,
#   with "!" added at the end, and repeated twice. Also print "hello world"
#   with every word starting with a capital letter, and remove the spaces
#   around "  hi  ". Finally print word again to see if it changed.

# ANSWER
print("=== Question 6 ===")
word = "Python"
print(word.upper())
print(word.lower())
print(len(word))
print(word + "!")
print(word * 2)
print("hello world".title())
print("[" + "  hi  ".strip() + "]")
print(word)

# =============================================================================
# QUESTION 7: f-Strings (Formatted Strings)
# =============================================================================

# Task:
#   Store name = "Lee", age = 14, height = 1.6 and price = 19.5.
#   Use f-strings to print:
#   - A sentence with the name and age.
#   - The height with the unit "m".
#   - The price with exactly 2 decimal places.
#   - A sentence that shows the age next year (age + 1).

# ANSWER
print("=== Question 7 ===")
name = "Lee"
age = 14
height = 1.6
price = 19.5

print(f"My name is {name} and I am {age} years old.")
print(f"Height: {height} m")
print(f"Price: {price:.2f}")
print(f"Next year I will be {age + 1}.")

# =============================================================================
# QUESTION 8: Comparison Operators Create Booleans
# =============================================================================

# Task:
#   Store a = 10 and b = 20. Print the results of a == b, a != b, a < b and
#   a >= b. Store the result of a < b in a variable called result and print its
#   type. Then compare "apple" with "apple", "apple" with "Apple", 10 with
#   10.0, and "10" with 10.

# ANSWER
print("=== Question 8 ===")
a = 10
b = 20
print(a == b)
print(a != b)
print(a < b)
print(a >= b)

result = a < b
print(result)
print(type(result))

print("apple" == "apple")
print("apple" == "Apple")
print(10 == 10.0)
print("10" == 10)

# =============================================================================
# QUESTION 9: Float Precision and Rounding
# =============================================================================

# Task:
#   Print 0.1 + 0.2. Then print it rounded to 2 decimal places. Check whether
#   0.1 + 0.2 == 0.3 and whether round(0.1 + 0.2, 2) == 0.3. Finally round
#   3.14159 to 2 decimal places.

# ANSWER
print("=== Question 9 ===")
print(0.1 + 0.2)
print(round(0.1 + 0.2, 2))
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 2) == 0.3)
print(round(3.14159, 2))

# =============================================================================
# QUESTION 10: The None Value
# =============================================================================

# Task:
#   Create a variable middle_name with the value None. Print it, print its
#   type, and check if it is None. Then give it the value "Alex" and check
#   again.

# ANSWER
print("=== Question 10 ===")
middle_name = None
print(middle_name)
print(type(middle_name))
print(middle_name is None)

middle_name = "Alex"
print(middle_name is None)

# =============================================================================
# QUESTION 11: Common Mistake - Joining a String and a Number
# =============================================================================
# Task:
#   You want to print: I am 15 years old.
#   The code "I am " + age + " years old." causes an error when age is 15.
#   Show three correct ways to fix it.

# ANSWER
print("=== Question 11 ===")
age = 15


print("I am " + str(age) + " years old.")
print("I am", age, "years old.")
print(f"I am {age} years old.")

# =============================================================================
# QUESTION 12: More Common Beginner Mistakes
# =============================================================================
# Task:
#   Show the correct version of these common mistakes:
#   1. Using the wrong capital letters in a variable name.
#   2. Joining numbers written as text ("10" + "5").
#   3. Mixing up = and ==.
#   4. Using invalid variable names.
#   5. Using a variable before creating it.
#   6. Mixing up / and //.

# ANSWER
print("=== Question 12 ===")

# Mistake 1: Names are case sensitive.
score = 50
# print(Score)       <- WRONG: NameError, because Score is not score
print(score)

# Mistake 2: Numbers inside quotes are text.
print("10" + "5")
print(10 + 5)
print(int("10") + int("5"))

# Mistake 3: = stores a value, == compares two values.
x = 5
print(x == 5)

# Mistake 4: Invalid names. All of these lines would cause errors:
#   2nd_place = 2      <- starts with a number
#   my score = 10      <- has a space
#   class = "A"        <- class is a reserved Python word
#   my-name = "Sam"    <- has a minus sign
second_place = 2
my_score = 10
class_name = "A"
print(second_place, my_score, class_name)

# Mistake 5: Use a variable only after you have created it.
# print(lives)       <- WRONG: NameError, lives does not exist yet
lives = 3
print(lives)

# Mistake 6: / gives a float, // gives the whole-number part.
print(7 // 2)
print(7 / 2)