# =============================================================================
# Question 1: Fix a Typo and Capitalize Using Slicing
# =============================================================================

#   A student typed the text "pythen is fun". It has two problems:
#   1. The word "pythen" has a typo. The letter at index 4 must be "o".
#   2. The first letter should be a capital letter.
#   Fix both problems WITHOUT using replace(). Use slicing, +, upper() and
#   reassignment. Print the text before and after. Also print the last 3
#   letters and the text reversed.

# Answer:
print("=== Question 1 ===")
text = "pythen is fun"
print("Before : ",text )

text = text[:4] + "o" + text[5:]
text = text[0].upper() + text[1:]
print("After : ", text)

print(text[-3:])
print(text[::-1])

# =============================================================================
# Question 2: Replace and Count Inside a Sentence
# =============================================================================

#   Store this sentence in a variable called sentence:
#       "I like apples. Apples are red. apples are tasty."
#   - Count how many times "apples" appears (exact lowercase match).
#   - Count again after converting the whole sentence to lowercase.
#   - Create a new sentence where "apples" is replaced by "mangoes" (in the
#     lowercase version).
#   - Print the original sentence to show it did not change.
#   - Print how many letters "a" are in the lowercase sentence.

# Answer:
print("=== Question 2 ===")
sentence ="I like apples. Apples are red. apples are tasty."
print(f"1. {sentence.count("apples")}")

lower_case=sentence.lower()
print(f"2. {lower_case.count("apples")}")

new_sentence = lower_case.replace("apples","mangoes")
print(f"3. {new_sentence}")
print(f"4. {sentence}")
print(f"5. {lower_case.count("a")}")

# =============================================================================
# Question 3: Find a Position, Check the Start, and Slice Around It
# =============================================================================

#   A file is called "report_2024.pdf". Using find(), startswith() and
#   slicing:
#   - Print the position of "_" and the position of ".".
#   - Print the result of searching for the letter "x" (it is missing).
#   - Check if the file name starts with "report" and with "Report".
#   - Extract the name part (before "_"), the year (between "_" and "."), and
#     the file type (after ".").


# Answer:
print("=== Question 3 ===")
file_name = "report_2024.pdf"

underscore_pos = file_name.find("_")
dot_pos = file_name.find(".")
print(f"1. underscore position : {underscore_pos}, dot position : {dot_pos}")
print(f"2. {file_name.find("x")}")

print(f"4. {file_name.startswith("report")}")
print(f"4. {file_name.startswith("Report")}")

name_part = file_name[:underscore_pos]
year = file_name[underscore_pos + 1:dot_pos]
file_type = file_name[dot_pos + 1:]
print(name_part)
print(year)
print(file_type)

# =============================================================================
# Question 4: Split a Sentence and Join It Back
# =============================================================================

#   Store "the quick brown fox" in a variable called sentence.
#   - Split it into words and print the list of words.
#   - Print how many words there are, the first word and the last word.
#   - Join the words with a dash "-" between them.
#   - Join the words with a space and print the result in title case.
#   Then split the text "apple,banana,cherry" using a comma and join the
#   pieces with " and ".

# Answer:
print("=== Question 4 ===")
sentence = "the quick brown fox"
words = sentence.split()
print(words)

print(len(words))
print(words[0])
print(words[-1])
print("-".join(words))
print(" ".join(words).title())

fruits = "apple,banana,cherry"
fruit_list = fruits.split(",")
print(fruit_list)
print(" and ".join(fruit_list))

# =============================================================================
# Question 5: Clean and Transform Messy Text (Chaining Methods)
# =============================================================================

#   A user typed:   "   hELLO, wORLD! welcome TO python   "
#   Store it in messy. Then:
#   - Create clean_text by removing the outer spaces and converting
#     everything to lowercase in ONE line (method chaining).
#   - Create a title version of clean_text.
#   - Replace "world" with "everyone" in clean_text and print it.
#   - Print the first 5 letters, the last 6 letters, and every second
#     character of clean_text.
#   - Print messy to show it never changed.

# Answer:
print("=== Intermediate Question 5 ===")
messy = "   hELLO, wORLD! welcome TO python   "

clean_text = messy.strip().lower()
print(clean_text)
print(clean_text.title())
print(clean_text.replace("world", "everyone"))

print(clean_text[:5])
print(clean_text[-6:])
print(clean_text[::2])
print("[" + messy + "]")