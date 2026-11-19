# =============================================================================
# QUESTION 1: Student Profile Card
# =============================================================================
# Task:
#   Create variables for a student: name, age, grade level, height in metres
#   and whether the student is enrolled. Print them as a neat profile card.
#   Also print the data type of the age and the height.

# Answer 
print("=== Question 1 ===")
name = "Kala"
age = 16
grade_level = 11
height = 1.63
is_enrolled = True

print("----- Student Profile -----")
print(f"Name : {name}")
print(f"Age : {age}")
print(f"Grade Level : {grade_level}")
print(f"Height : {height}")
print(f"Enrolled : {is_enrolled}")
print("---------------------------")
print(f"Age type: {type(age)}")
print(f"Height type : {type(height)}")

# =============================================================================
# QUESTION 2: Shop Bill Calculator
# =============================================================================
# Task:
#   A shop sells pens at 1.50 each and notebooks at 3.25 each. A customer
#   buys 4 pens and 2 notebooks. The tax rate is 10 percent (0.10).
#   Calculate and print the subtotal, the tax and the total, using 2 decimal
#   places.

# Answer
print("=== Question 2 ===")
pen = 1.50
notebook = 3.25
tax_percentage = 0.10

subtotal = (pen*4)+(notebook*2)
tax = subtotal*tax_percentage
total = subtotal + tax
print(f"Subtotal : {subtotal:.2f}")
print(f"Tax : {tax:.2f}")
print (f"Total : {total:.2f}")


# =============================================================================
# QUESTION 3: Temperature Converter
# =============================================================================
# Task:
#   Convert 30 degrees Celsius to Fahrenheit.
#   Then convert 100 degrees Fahrenheit to Celsius (show 1 decimal place).
#   Formulas:
#       fahrenheit = celsius * 9 / 5 + 32
#       celsius = (fahrenheit - 32) * 5 / 9

# Answer
print("=== Question 3 ===")
celsius = 30
cel_to_fahr = celsius * 9 / 5 + 32
print(f"{celsius} C = {cel_to_fahr} F")

fahrenheit = 100
fahr_to_cel = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} F = {fahr_to_cel:.1f} C")

# =============================================================================
# QUESTION 4: BMI Calculator
# =============================================================================
# Task:
#   A person weighs 60 kg and is 1.65 m tall.
#   BMI = weight / (height * height)
#   Print the BMI with 2 decimal places. Also store in a boolean variable
#   whether the BMI is in the healthy range (18.5 or more, but less than 25)
#   and print it.

# Answer
print("=== Question 4 ===")
weight=60
height=1.65
bmi= weight / (height * height)
print(f"BMI = {bmi:.2f}")
is_healthy = bmi>=18.5 and bmi<25
print(f"Is BMI in the healthy range? {is_healthy}")

# =============================================================================
# QUESTION 5: Restaurant Tip and Bill Splitter
# =============================================================================
# Task:
#   A restaurant bill is 85.50. You leave a 10 percent tip. Three friends
#   share the total equally. Print the tip, the total and the amount each
#   person pays (2 decimal places).

# Answer
print("=== Question 5 ===")
bill =85.50 
tip_percent = 10
people=3

tip=bill*tip_percent/100
total_with_tip= tip+bill
each_pay = total_with_tip/people

print(f"Tip: {tip:.2f}")
print(f"Total with tip: {total_with_tip:.2f}")
print(f"Each person pays: {each_pay:.2f}")

# =============================================================================
# QUESTION 6: Seconds Converter
# =============================================================================
# Task:
#   Convert 3725 seconds into hours, minutes and seconds.

# Answer
print("=== Question 6 ===")
total_seconds = 3725

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{total_seconds} seconds = {hours} hour(s), {minutes} minute(s), {seconds} second(s)")

# =============================================================================
# QUESTION 7: Marks Average and Pass or Fail
# =============================================================================
# Task:
#   A student scored 78 in Maths, 85 in Science and 69 in English.
#   Calculate the total and the average (2 decimal places). The pass mark is
#   50 on average. Store the pass result in a boolean and print it.

# ANSWER
print("=== Question 7 ===")
maths = 78
science = 85
english = 69
pass_mark = 50

total_marks = maths + science + english
average = total_marks / 3
has_passed = average >= pass_mark

print(f"Total marks: {total_marks}")
print(f"Average: {average:.2f}")
print(f"Passed: {has_passed}")
print(f"Type of has_passed: {type(has_passed)}")

# =============================================================================
# QUESTION 8: Fix the Broken Program (Debugging)
# =============================================================================
# Task:
#   This program has two bugs because of data types:
#
#       name = "Sam"
#       age = "14"
#       print("Next year, " + name + " will be " + age + 1)
#
#       price = "20"
#       quantity = 3
#       print(price * quantity)
#
#   Bug 1 crashes with a TypeError. Bug 2 does not crash but prints the wrong
#   answer (202020 instead of 60). Fix both bugs.

# ANSWER
print("=== Question 8 ===")
name = "Sam"
age = int("14")
print("Next year, " + name + " will be " + str(age + 1))

price = int("20")
quantity = 3
print(price * quantity)
