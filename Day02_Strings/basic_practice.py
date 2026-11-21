# =============================================================================
# Question 1: Strings, Positive Indexing and Negative Indexing
# =============================================================================

#   Store the word "Python" in a variable called word. Then:
#   - Print the type of word.
#   - Print how many characters it has.
#   - Print the first letter and the third letter using positive indexes.
#   - Print the last letter and the second-to-last letter using negative
#     indexes.

# Answer:
print("=== Question 1 ===")
word ="Python"
print(f"1. {type(word)}")
print(f"2. {len(word)}")
print(f"3. {word[0]} , {word[2]}")
print (f"4. {word[-1]}, {word[-2]}")

# =============================================================================
# Question 2: String Immutability and Reassignment
# =============================================================================

#   The word "cat" is stored in a variable called pet. You want to change the
#   first letter to "b" to make "bat". Show that you cannot change a string
#   directly, then create the new word using slicing and reassignment.

# Answer:
print("=== Question 2 ===")
pet = "cat"

# pet[0] = "b"  # TypeError: 'str' object does not support item assignment

new_letter = "b"+pet[1:]
print(pet)
print(new_letter)
pet = "b" + pet[1:]
print(pet)

# =============================================================================
# Question 3: Basic Slicing with Start and End
# =============================================================================

#   Store the word "Programming" in a variable called text. Use slicing to
#   print:
#   - The first 4 letters.
#   - Everything from index 3 to the end.
#   - Everything from the start up to (but not including) index 7.
#   - The last 4 letters.
#   - The letters from index 2 up to index 8.
#   - A full copy of the string.

# Answer:
print("=== Question 3 ===")
text = "Programming"
print(f"1. {text[0:4]}")
print(f"2. {text[3:]}")
print(f"3. {text[:7]}")
print(f"4. {text[-4:]}")
print(f"5. {text[2:8]}")
print(f"6. {text[:]}")

# =============================================================================
# Question 4: Slicing with a Step and Reversing a String
# =============================================================================

#   Store the letters "abcdefghij" in a variable called letters. Use slicing
#   with a step value to print:
#   - Every second letter starting from the beginning.
#   - Every second letter starting from index 1.
#   - Every third letter.
#   - Letters from index 2 up to 8, moving 2 steps each time.
#   - The whole string reversed.

# Answer:
print("=== Question 4 ===")
letters="abcdefghij"
print(f"1. {letters[::2]}")
print(f"2. {letters[1::2]}")
print(f"3. {letters[::3]}")
print(f"4. {letters[2:8:2]}")
print(f"5. {letters[::-1]}")

# =============================================================================
# Question 5: Case Methods, strip() and len()
# =============================================================================

#   A user typed this messy text:   "  hello python world  "
#   Store it in a variable called raw. Then:
#   - Print its length before cleaning.
#   - Remove the extra spaces with strip() and print its new length.
#   - Print the cleaned text in uppercase, lowercase and title case.
#   - Print the original raw text again to prove it did not change.

# Answer:
print("=== Question 5 ===")
raw = "  hello python world  "
print(f"1. {len(raw)}")

clean= raw.strip()
print(f"2. {len(clean)}")

print(f"3. Upper case : {clean.upper()}")
print(f"3. Lower case : {clean.lower()}")
print(f"3. Title case : {clean.title()}")

print(f"4. {raw}")