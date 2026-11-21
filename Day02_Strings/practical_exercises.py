# =============================================================================
# Question 1: Reverse a Word and Check for a Palindrome
# =============================================================================

#   Write a program that reverses a word. Test it with "python" and "level".
#   For each word, print the original, the reversed word, and whether the word
#   is a palindrome (a word that reads the same forwards and backwards).

# Answer:
print("=== Question 1 ===")
word1= "python"
reverse1 = word1[::-1]
print(f"1. Word: {word1}- Reversed:{reverse1}")
print(f"Palindrome: {word1 == reverse1}")
word2 = "level"
reverse2 =word2[::-1]
print(f"1.Word:  {word2}- Reversed:{reverse2}")
print(f"Palindrome: {word2 == reverse2}")

# =============================================================================
# Question 2: Count the Vowels in a Sentence
# =============================================================================

#   Count the vowels (a, e, i, o, u) in the text "Education is Important".
#   Print how many times each vowel appears, the total number of vowels, the
#   total length of the text, and the percentage of the text that is vowels
#   (with 1 decimal place).

# Answer:
print("=== Question 2 ===")
text = "Education is Important"
lower_case = text.lower()

a_count=lower_case.count("a")
e_count=lower_case.count("e")
i_count=lower_case.count("i")
o_count=lower_case.count("o")
u_count=lower_case.count("u")

vowels_total=a_count+e_count+i_count+o_count+u_count
text_len=len(text)
percentage= vowels_total/text_len*100

print(f"a: {a_count}")
print(f"e: {e_count}")
print(f"i: {i_count}")
print(f"o: {o_count}")
print(f"u: {u_count}")
print(f"Total vowels: {vowels_total}")
print(f"Text length: {text_len}")
print(f"Vowel percentage: {percentage:.1f}%")

# =============================================================================
# Question 3: First Letter, Last Letter and Initials of a Name
# =============================================================================

#   A form gave you this messy full name:   "  mary jane watson  "
#   Write a program that:
#   - Cleans the name (remove outer spaces) and prints it in title case.
#   - Prints the first letter and the last letter of the cleaned name.
#   - Prints the initials in capital letters, like M.J.W

# Answer:
print("=== Question 3 ===")
raw_name = "  mary jane watson  "
clean_name = raw_name.strip().title()
print(clean_name)

first_letter = clean_name[0]
last_letter = clean_name[-1]
print(f"First letter: {first_letter}")
print(f"Last letter: {last_letter}")

name_part = clean_name.split()
initials = name_part[0][0]+"."+name_part[1][0]+"."+name_part[2][0]
print(f"Initials : {initials}")

# =============================================================================
# Question 4: Username and Email Generator
# =============================================================================

#   A school system receives the name "  John   SMITH  " and the birth year
#   as the text "1998". Create:
#   - A username in the form first.last in lowercase (john.smith).
#   - An email address by adding "@school.com" to the username.
#   - A student code made from the first 3 letters of the last name in
#     capitals, followed by the last 2 digits of the birth year (SMI98).
#   - A check that tells you whether the email starts with "john".
#   Print the username length too.

# Answer:
print("=== Practical Question 4 ===")
full_name = "  John   SMITH  "
birth_year = "1998"

parts=full_name.strip().lower().split()
username= ".".join(parts)
email= username +"@school.com"

last_name = parts[1]
student_code=last_name[:3].upper()+birth_year[-2:]

print(f"Username: {username}")
print(f"Email: {email}")
print(f"Student code: {student_code}")
print(f"Email starts with john: {email.startswith('john')}")
print(f"Username length: {len(username)}")

# =============================================================================
# Question 5: Text Analyzer Report
# =============================================================================

#   Analyze this text:
#   "  the QUICK brown fox jumps over the lazy dog. The dog sleeps.  "
#   Write a program that prints a small report:
#   - The cleaned text (outer spaces removed, all lowercase).
#   - The number of characters and the number of words in the cleaned text.
#   - How many times the word "the" appears.
#   - The position where "fox" starts.
#   - Whether the cleaned text starts with "the".
#   - A new version where "dog" is replaced by "cat".
#   - The first word and the last word in capital letters.
#   - The cleaned text with its words in reverse order, joined by spaces.

# Answer:
print("=== Practical Question 5 ===")
original = "  the QUICK brown fox jumps over the lazy dog. The dog sleeps.  "
clean_orginal= original.strip().lower()
words=clean_orginal.split()

print("----- Text Report -----")
print(f"Cleaned text: {clean_orginal}")
print(f"Characters: {len(clean_orginal)}")
print(f"Words: {len(words)}")
print(f"Times 'the' appears: {clean_orginal.count('the')}")
print(f"'fox' starts at index: {clean_orginal.find('fox')}")
print(f"Starts with 'the': {clean_orginal.startswith('the')}")
print(f"With cat: {clean_orginal.replace('dog', 'cat')}")
print(f"First word: {words[0].upper()}")
print(f"Last word: {words[-1].upper()}")
print(f"Reversed word order: {' '.join(words[::-1])}")