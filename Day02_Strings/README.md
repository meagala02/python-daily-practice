# 02 - Strings (Deep)

Practice exercises for **Day 2: Strings (Deep)**.
This folder has 3 files with 5 questions each (15 questions in total).

## What This Topic Covers

**1. Strings and immutability**
- What a string is
- Why strings cannot be changed directly
- Making a modified string with slicing and reassignment

**2. String slicing**
- Positive and negative indexing
- Slicing with start and end
- Slicing with a step
- Reversing a string with `[::-1]`

**3. Common string methods (only these 11)**
`upper()`, `lower()`, `title()`, `strip()`, `len()`, `replace()`, `split()`, `join()`, `find()`, `startswith()`, `count()`

**4. Small string programs**
- Reverse a word
- Count vowels
- Find the first letter of a word
- Find the last letter of a word

## Files

| File | Section | Questions | Main ideas |
|------|---------|-----------|------------|
| `basic_practice.py` | Basic | 5 | Indexing, immutability, slicing, step, case methods, `strip()`, `len()` |
| `intermediate_practice.py` | Intermediate | 5 | Fixing text with slices, `replace()`, `count()`, `find()`, `startswith()`, `split()`, `join()`, method chaining |
| `practical_exercises.py` | Practical | 5 | Reverse a word, count vowels, first and last letters, username generator, text report |

## Topic Coverage Map

| Topic | Where it is practised |
|-------|-----------------------|
| What are strings, `len()` | Basic Q1, Q5 |
| Immutability and reassignment | Basic Q2, Intermediate Q1, Q2, Q5 |
| Positive and negative indexing | Basic Q1, Practical Q3 |
| Slicing with start and end | Basic Q3, Intermediate Q1, Q3 |
| Slicing with a step | Basic Q4, Intermediate Q5 |
| Reversing with slicing | Basic Q4, Intermediate Q1, Practical Q1, Q5 |
| `upper()`, `lower()`, `title()` | Basic Q5, Practical Q2, Q3, Q4 |
| `strip()` | Basic Q5, Practical Q3, Q4, Q5 |
| `replace()` | Intermediate Q2, Q5, Practical Q5 |
| `split()` and `join()` | Intermediate Q4, Practical Q3, Q4, Q5 |
| `find()` | Intermediate Q3, Practical Q5 |
| `startswith()` | Intermediate Q3, Practical Q4, Q5 |
| `count()` | Intermediate Q2, Practical Q2, Q5 |
| Reverse a word | Practical Q1 |
| Count vowels | Practical Q2 |
| First letter and last letter | Practical Q3 |

## How to Practise

1. Open a file and read the question comment.
2. Write your own answer first in a scratch file.
3. Run your code, then compare it with the answer and the expected output below.
4. Read the explanation comments to understand why it works.
5. Tick the checklist.

Run a file from this folder:

```bash
python basic_practice.py
```

On some computers the command is `python3` instead of `python`.

## Expected Output

Every question prints a heading like `=== Basic Question 1 ===`. Your output should match the blocks below exactly.

### Section 1 - Basic Practice (`basic_practice.py`)

**Question 1: Strings, Positive Indexing and Negative Indexing**

```text
<class 'str'>
6
P
t
n
o
```

**Question 2: String Immutability and Reassignment**

```text
cat
bat
hat
```

**Question 3: Basic Slicing with Start and End**

```text
Prog
gramming
Program
ming
ogramm
Programming
```

**Question 4: Slicing with a Step and Reversing a String**

```text
acegi
bdfhj
adgj
ceg
jihgfedcba
```

**Question 5: Case Methods, strip() and len()**

```text
22
18
HELLO PYTHON WORLD
hello python world
Hello Python World
[  hello python world  ]
```

### Section 2 - Intermediate Practice (`intermediate_practice.py`)

**Question 1: Fix a Typo and Capitalize Using Slicing**

```text
Before: pythen is fun
After: Python is fun
fun
nuf si nohtyP
```

**Question 2: Replace and Count Inside a Sentence**

```text
2
3
i like mangoes. mangoes are red. mangoes are tasty.
I like apples. Apples are red. apples are tasty.
6
```

**Question 3: Find a Position, Check the Start, and Slice Around It**

```text
6
11
-1
True
False
report
2024
pdf
```

**Question 4: Split a Sentence and Join It Back**

```text
['the', 'quick', 'brown', 'fox']
4
the
fox
the-quick-brown-fox
The Quick Brown Fox
['apple', 'banana', 'cherry']
apple and banana and cherry
```

**Question 5: Clean and Transform Messy Text (Chaining Methods)**

```text
hello, world! welcome to python
Hello, World! Welcome To Python
hello, everyone! welcome to python
hello
python
hlo ol!wloet yhn
[   hELLO, wORLD! welcome TO python   ]
```

### Section 3 - Practical Exercises (`practical_exercises.py`)

**Question 1: Reverse a Word and Check for a Palindrome**

```text
Word: python
Reversed: nohtyp
Palindrome: False
Word: level
Reversed: level
Palindrome: True
```

**Question 2: Count the Vowels in a Sentence**

```text
a: 2
e: 1
i: 3
o: 2
u: 1
Total vowels: 9
Text length: 22
Vowel percentage: 40.9%
```

**Question 3: First Letter, Last Letter and Initials of a Name**

```text
Mary Jane Watson
First letter: M
Last letter: n
Initials: M.J.W
```

**Question 4: Username and Email Generator**

```text
Username: john.smith
Email: john.smith@school.com
Student code: SMI98
Email starts with john: True
Username length: 10
```

**Question 5: Text Analyzer Report**

```text
----- Text Report -----
Cleaned text: the quick brown fox jumps over the lazy dog. the dog sleeps.
Characters: 60
Words: 12
Times 'the' appears: 3
'fox' starts at index: 16
Starts with 'the': True
With cat: the quick brown fox jumps over the lazy cat. the cat sleeps.
First word: THE
Last word: SLEEPS.
Reversed word order: sleeps. dog the dog. lazy the over jumps fox brown quick the
```

## Progress Checklist

### Section 1 - Basic Practice
- [ ] Q1 Strings, positive indexing and negative indexing
- [ ] Q2 String immutability and reassignment
- [ ] Q3 Basic slicing with start and end
- [ ] Q4 Slicing with a step and reversing a string
- [ ] Q5 Case methods, `strip()` and `len()`

### Section 2 - Intermediate Practice
- [ ] Q1 Fix a typo and capitalize using slicing
- [ ] Q2 Replace and count inside a sentence
- [ ] Q3 Find a position, check the start, and slice around it
- [ ] Q4 Split a sentence and join it back
- [ ] Q5 Clean and transform messy text (chaining methods)

### Section 3 - Practical Exercises
- [ ] Q1 Reverse a word and check for a palindrome
- [ ] Q2 Count the vowels in a sentence
- [ ] Q3 First letter, last letter and initials of a name
- [ ] Q4 Username and email generator
- [ ] Q5 Text analyzer report

### Final Self-Check
- [ ] I can explain why `word[0] = "x"` gives an error
- [ ] I can explain the difference between `[:4]`, `[4:]` and `[::-1]`
- [ ] I know that the end index in a slice is not included
- [ ] I know that `find()` gives `-1` when the text is not found
- [ ] I know string methods return a new string and do not change the original
- [ ] I solved at least one question without looking at the answer

## Suggested Git Commit Messages

```text
Add Day 2 basic string practice: indexing, slicing and immutability
Add Day 2 intermediate string practice: replace, find, split and join
Add Day 2 practical exercises: reverse word, count vowels and text report
Add Day 2 README with expected output and checklist
Update main README: add Day 2 strings progress
Complete Day 2 basic practice (Q1-Q5)
Complete Day 2 intermediate practice (Q1-Q5)
Complete Day 2 practical exercises (Q1-Q5)
Fix typo in Day 2 explanation
```

## Dates

- Started: 21 / 11 / 2026
- Finished: 21 / 11 / 2026