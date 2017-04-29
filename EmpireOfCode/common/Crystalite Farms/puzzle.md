### Fizz Buzz

To get them ready for storage, we need the worker-bots to sort crystals by 3 or 5 or divide them by the number of edges. To make things easier, we will base our program on the ancient human word game "Fizz buzz".

Our goal is to write a function that will receive a positive integer and return:

The phrase **"Fizz Buzz"** if the number is divisible by 3 and by 5,

The word **"Fizz"** if the number is divisible by 3,

The word **"Buzz"** if the number is divisible by 5,

The number as a string for all other cases.

**Input:** A number as an integer.

**Output:** The answer as a string.

**Example:**
````
fizz_buzz(15) == "Fizz Buzz"
fizz_buzz(6) == "Fizz"
fizz_buzz(5) == "Buzz"
fizz_buzz(7) == "7"
````

**Precondition:**

0 < number ≤ 1000

**How it is used:**

Here you can learn how to write simple functions and work with if-else statements.

---------------
### Digits Multiplication

You are given a positive integer. Your function should calculate the product of the digits **excluding any zeroes**.

For example: The number given is 123405. The result will be 1\*2\*3\*4\*5=120.

In this mission the main goal to make your code as short as possible. The shorter your code, the more points you earn. Your score for this mission is dynamic and directly related to the length of your code.

**Input:** A positive integer.

**Output:** The product of the digits as an integer.

**Example:**
````
golf(123405) == 120
golf(999) == 729
golf(1000) == 1
golf(1111) == 1
````
**Precondition:**
````
0 < number < 10^6
````
**Scoring:**

Scoring in this mission is based on the number of characters used in your code (comment lines are not counted).

**Rank1:**

Any code length.

**Rank2:**

Your code should be shorter than 100 characters.

**Rank3:**

Your code should be shorter than 70 characters.

**How it is used:**

This mission teaches you to work with simple data type conversions to solve a problem.

-----------------
### Friendly Numbers

You should write a function for converting a **number** into a string following several rules. First of all, you will need to cut the number with a given base (**base** argument; default 1000). The value is a float number with decimal after the point (**decimals** argument; default 0). For the value, use the rounding to zero rule (5.6⇒5, -5.6⇒-5) if the decimal = 0, otherwise use the standard rounding procedure. If the number of decimals is greater than the current number of digits after dot, trail the value with zeroes. The number should be a value with letters designating the power. You will be given a list of power designations (**powers** argument; default \['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'\]). If you are given suffix (**suffix** argument; default ‘’), then you must append it. If you don’t have enough powers, stay at the maximum.

Zero is always zero without powers, but with a suffix.

Let's look at some examples:

- n=102; result: "102", the base is default 1000 and 102 is lower this base.
- n=10240; result: "10k", the base is default 1000 and rounding down.
- n=12341234, decimals=1; result: "12.3M", one digit after the dot.
- n=12000000, decimals=3; result: "12.000M", trailing zeros.
- n=12461, decimals=1; result: "12.5k", standard rounding.
- n=1024000000, base=1024, suffix='iB'; result: '976MiB', the different base and the suffix.
- n=-150, base=100, powers=\['', 'd', 'D'\]; result: '-1d', the negative number and rounding towards zero.
- n=-155, base=100, decimals=1, powers=\['', 'd', 'D'\]; result: '-1.6d', the negative number and standard rounding.
- n=255000000000, powers=\['', 'k', 'M'\]; result: '255000M', there is not enough powers.

**Input:** A number as an integer. The keyword argument "base" as an integer, default 1000. The keyword argument "decimals" as an integer, default 0. The keyword argument "powers" as a list of string, default \['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'\].

**Output:** The converted number as a string.

**Example:**
````
friendly_number(102) == '102'
friendly_number(10240) == '10k'
friendly_number(12341234, decimals=1) == '12.3M'
friendly_number(12000000, decimals=3) == '12.000M'
friendly_number(12461, decimals=1) == '12.5k'
friendly_number(1024000000, base=1024, suffix='iB') == '976MiB'
friendly_number(-150, base=100, powers=['', 'd', 'D']) == '-1d'
friendly_number(-155, base=100, decimals=1, powers=['', 'd', 'D']) == '-1.6d'
friendly_number(255000000000, powers=['', 'k', 'M']) == '255000M'
````
**Precondition:**
````
1 < base <= 10 ** 32
-10 * 32 < number <= 10 ** 32
0 <= decimals <= 15
0 < len(powers) <= 32
````
**How it is used:**

In physics and IT we work with many varying numbers. Sometimes we need to make them simpler and easier to read. For example: when you talk about the number of gigabytes in a hard drive, sometimes you don’t need to know the exact number bytes or kilobytes.

--------------------------------------
### Max of Two

Define a function that takes two numbers as arguments and returns the largest of them.

**Input:** Two arguments as numbers.

**Output:** Maximum of two.

**Example:**
````
my_max(3, 3) == 3
my_max(0, 1) == 1
my_max(3, 2) == 3
````

------------------
### Crystal Row

Because crystals are such an important resource, systems must be put in place to check the crystal quality during the growth and harvest periods. For our initial tests, we use random spot checks on the atomic lines composing each of the crystals. This crystal type contains two atoms composed of the elements "X" (Xenatom) and "Z" (Zorium). In a well grown crystal, these atoms should alternate down the atomic line.

You are given a random atomic line from a sample crystal lattice as a sequence of the letters "X" and "Z". A good line should have the periodic arrangement (one by one) looking like ["X", "Z", "X", "Z"]. If any atoms neighbor another of the same element, then this crystal is of no use to us and should be discarded.
````
X - Z - X - Z - X - Z Good
Z - X - Z - X - Z - X Good
Z - X - X - Z - X - Z Bad
Z - X - Z - Z - Z - X Bad
````
**Input:** Atomic lines as a list of strings.

**Output:** The crystal quality as a boolean.

**Example:**
````
checkLine(["X", "Z", "X"]) == true
checkLine(["X", "Z", "X", "X"]) == false
````
**Precondition:**
````
1 < |line| ≤ 1000
∀ x ∈ line: x='X' OR x='Z'
````
**How it is used:**

This is first simple data structure and here you can learn how to work with a list. It's a simple concept which you can solve by just pausing to think.

---------------
### Crystal Grid

The initial crystal quality check phase (link) is not enough to satisfactorily pass a crystal for use. As such, we need to work to improve the process. Since we've checked random atomic lines/rows, perhaps it would be best to perform checks on random slices of the crystal. This crystal type contains two atoms composed of the elements "X" (Xenatom) and "Z" (Zorium). In a well grown crystal, these atoms should alternate down each row and column.

You are given a slice of crystal lattice as a grid (2D array) of the atoms "X" and "Z". A well grown grid should have proper periodic arrangements both horizontally and vertically. If one atom is found next to another atom of its element, the crystal is unusable. For example:
````
[["X", "Z"],
 ["Z", "X"]] is good

[["X", "Z", "X"],
 ["Z", "X", "Z"],
 ["X", "Z", "X"]] is good

[["X", "Z", "X"],
 ["Z", "Z", "Z"],
 ["X", "Z", "X"]] is bad
````
**Input:** Atomic grid as a list of lists with strings.

**Output:** The crystal quality as a boolean.

**Example:**
````
check_grid([["X", "Z"], ["Z", "X"]]) == True
check_grid([["X", "X"], ["X", "X"]]) == False
````
**Precondition:**
````
1 < |grid| ≤ 12

∀ row ∈ grid: 1 < |row| ≤ 12

All rows have the same length and contains only "X"/"Z"
````

**How it is used:**

In this mission we will use more complex structure as list of list. This structure often use as tables or grids or land maps.

-------------------
### Structure Pattern

You are given a pattern as a positive integer and you are also given a row structure as a word. For comparison, the recognition system should convert the integer pattern into binary form. It needs to append zeros to left to match the structure length and compare this combination with the structure.

**1 is a letter and 0 is a digit.**

If the pattern and the structure match, then return True, else return False. If the pattern is longer than a given structure, then they are not a match (Example: 8 = 1000 and "a").

Here's an example: the given pattern is 42 and the structure is "12a0b3e4". 42 == 101010 in binary form, but this is not long enough to match the structure. Append zeroes to the left to get "00101010". Now compare the two:
````
      42 == 00101010
12a0b3e4 == DDLDLDLD
--------------------
    True    VVVVVVVV
````
Here's one more example -- 101 and "ab23b4zz":
````
     101 == 01100101
ab23b4zz == LLDDLDLL
--------------------
   False    XVXVXXXV
````
**Input:** A pattern as a positive integer and a command as a string. The third argument is optional with default value defines a level of patterns.

**Output:** Determination if the pattern matches the command as a boolean.

**Example:**
````
check_structure(42, "12a0b3e4") == True
check_structure(101, "ab23b4zz") == False
````
**Precondition:**

`structure` matches by `"\A[A-Za-z0-9]{1, 32}\Z"` regexp expression.

`pattern_level = 2`

**Rank 2:**

In default pattern level (level = 2) we using binary form. If the patter level equals 3, then convert the integer pattern into ternary numeral system (base 3). **0 is a digit, 1 is a lowercase letter, 2 is an uppercase letter.**

*Precondition rank 2:*

`structure` matches by `"\A[a-zA-Z0-9]{1, 32}\Z"` regexp expression.

`pattern_level ∈ {2, 3}`

**Rank 3:**
 
 If the pattern level equals 4, then convert the integer pattern into Quaternary numeral system (base 4). **0 is a digit, 1 is a lowercase letter, 2 is an uppercase letter, 3 is a whitespace.**

*Precondition rank 3:*

`structure` matches by `"\A[ a-zA-Z0-9]{1, 32}\Z"` regexp expression.

`pattern_level ∈ {2, 3, 4}`

**How it is used:**

In this mission you learn how to store complex data in simple numbers and how to work with simple patterns. You can expand this concept to take on more complex patterns with different or more complex numbering systems.

--------------------------------------
### Speech Module

You are given a number as an integer and must convert it to word form in English. All the words in the string must be separated by exactly one space character. Be careful with the spaces, it's hard to see if you might have placed two spaces instead of only one.

For example, 143 => 'one hundred forty three'.

**Input:** A number as an integer.

**Output:** The word representation of the number as a string.

**Example:**
````
tell_number(4) == 'four'
tell_number(143) == 'one hundred forty three'
tell_number(12) == 'twelve'
tell_number(101) == 'one hundred one'
tell_number(212) == 'two hundred twelve'
tell_number(40) == 'forty'
````
**Precondition:**

0 < number < 1000

**Optional goal**

**Rank 2:** A number can be zero and negative. For a negative number, append "minus" in front of it.

-1000 < number < 1000

**Rank 3:** A number can be more than 1000.

-1000000 < number < 1000000

**How it is used:**

This concept may be useful for the speech synthesis software or automated report systems. The system could also be used when writing a chatbot by assigning words or phrases numerical values and having a system retrieve responses based on those values.

----------------
### Good Radix

You are given some number 'n' written as a string with a radix equal to `k (1 < k < 37)`. We know that our number is divisible by `(k - 1)` without a remainder. You should find the smallest possible `k` if it exists, or return `0` in the case where it doesn't.

For example: where `n = 18`, `k` should be greater than 8.

If `k == 9`, then `n = 17` in the decimal system and `17 % 8 == 1`. This is the wrong radix.

If `k == 10`, then `n = 18` in the decimal system and `18 % 9 == 0`. We found the answer.

**Input:** A number as a string.

**Output:** The radix k as an integer.

**Example:**
````
good_radix(u"18") == 10
good_radix(u"1010101011") == 2
good_radix(u"222") == 3
good_radix(u"A23B") == 14
good_radix(u"IDDQD") == 0
````
**Precondition:**

Input number string matches at `"[A-Z1-9][A-Z0-9]{0, 9}"` regular expression.

**How it is used:**

Let's familiarize ourselves with numeral systems and examine the radix. Many devices are built to accept numbers in decimal representation and display the results in decimal. Often such devices convert from decimal to some internal radix on input, do all internal operations in that radix, and then convert the results from the internal radix to decimal on output. Such devices could in principle use any radix internally. The people who design such computing devices sometimes wonder what would be the "best" radix to use internally for the radix economy.

The octal, hexadecimal and base-64 systems are often used in computing because of their ease as shorthand for binary.

-----------
### Hidden Word

You are given a rhyme (a multiline string), in which lines are separated by "newline" (\n). Casing does not matter for your search, but whitespaces should be removed beforehand. You should find the word inside the rhyme in the horizontal (from left to right) or vertical (from up to down) lines. For this you need envision the rhyme as a matrix (2D array). Find the coordinates of the word in the cut rhyme (without whitespaces).

The result must be represented as a list -- **\[row_start,column_start,row_end,column_end\]**, where

- **row_start** is the line number for the first letter of the word.
- **column_start** is the column number for the first letter of the word.
- **row_end** is the line number for the last letter of the word.
- **column_end** is the line number for the last letter of the word.
- Counting of the rows and columns start from 1.

**Input:** Two arguments. A rhyme as a string and a word as a string (lowercase).

**Output:** The coordinates of the word as a list/tuple.

**Example:**
````
find_word(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", u"ten") == [2, 14, 2, 16]

find_word("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
````
**Precondition:**
````
0 < len(word) < 10
0 < len(rhyme) < 300
````
**How it is used:**

This task shows the variance of the positional ciphers. With this cipher you can hide a message within a book which allows you and receiver to send these coded messages.

-------------
### Monkey Typing

You are given some text which possibly contains sensible words. You should count how many words are included in the given text. A word should be whole and may be a part of another word. Letter case does not matter. Words are given in lowercase and don't repeat. If a word appears several times in the text, it should be counted only once.

For example, text - "How are sjfhdskfhskd you?", words - ("how", "are", "you", "hello"). The result will be 3.

**Input:** Two arguments. A text as a string and words as a set of strings.

**Output:** The number of words in the text as an integer.

**Example:**
````
count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {"sum", "hamlet", "infinity", "anything"}) == 1
````
**Precondition:**
````
0 < |text| ≤ 256

All words are given in lowercase.
````
**How it is used:**

Python is a useful and powerful language for text processing. This mission is only a simple example of the kind of text searching tools you could build.

------------
### Digit Stack

We will emulate the stack process with Python. You are given a sequence of commands:

- "PUSH X" -- add **X** in the stack, where **X** is a digit.
- "POP" -- look and remove the top position. If the stack is empty, then it returns 0 (zero) and does nothing.
- "PEEK" -- look at the top position. If the stack is empty, then it returns 0 (zero). The stack can only contain digits.

You should process all commands and sum all digits which were taken from the stack ("PEEK" or "POP"). The initial value of the sum is 0 (zero).

Let's look at an example, here’s the sequence of commands:
````
["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]
````
````
| Command | Stack | Sum 
|---------|-------|-----
| PUSH 3  | 3     | 0
| POP     |       | 0+3
| POP     |       | 3+0
| PUSH 4  | 4     | 3
| PEEK    | 4     | 3+4
| PUSH 9  | 4,9   | 7
| PUSH 0  | 4,9,0 | 7
| PEEK    | 4,9,0 | 7+0
| POP     | 4,9   | 7+0
| PUSH 1  | 4,9,1 | 7
| PEEK    | 4,9,1 | 7+1=8
````
In this mission the main goal to make your code as short as possible. The shorter your code, the more points you earn. Your score for this mission is dynamic and directly related to the length of your code.

**Input:** A sequence of commands as a list of strings.

**Output:** The sum of the taken digits as an integer.

**Example:**
````
golf(("PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK")) == 8
golf(("POP", "POP")) == 0
golf(("PUSH 9", "PUSH 9", "POP")) == 9
golf(()) == 0
````
**Precondition:**
````
0 ≤ |commands| ≤ 20
````
All commands match at `"\APUSH \d\Z"` regular expression or equal by `"POP"` or equal by `"PEEK"`.

**Scoring:**

Scoring in this mission is based on the number of characters used in your code (comment lines are not counted).

**Rank1:**

Any code length.

**Rank2:**

Your code should be shorter than 250 characters.

**Rank3:**

Your code should be shorter than 150 characters.

**How it is used:**

Stacks have numerous applications. We see stacks in everyday life, from the books in our library, to the blank sheets of paper in our printer tray. All of them follow the Last In First Out (LIFO) logic, that is when we add a book to a pile of books, we add it to the top of the pile, whereas when we remove a book from the pile, we generally remove it from the top of the pile. After all, taking one from the middle just makes a mess.

-----------------------
### Most Wanted Letter

You are given a text which contains different English letters and punctuation symbols. You must find the most frequent letter in the given text. The letter returned must be in lower case.

While checking for the most wanted letter, casing does not matter. For the purpose of your search, "A"=="a". Make sure you do not count punctuation symbols, digits and white spaces, only letters.

If you have two or more letters with the same frequency, then return any of them.

**Input:** Some text for analysis as a string. The second argument is optional with the default value. It's used for "Rank 3".

**Output:** The most frequent letter in lower case as a string.

**Example:**
````
most_letter("Hello World!") in "l"
most_letter("How do you do?") == "o"
most_letter("One") in "one"
most_letter("Oops!") == "o"
most_letter("AAaooo!!!!") in "ao"
most_letter("abe") in "abe"
````
**Precondition:**

A text contains only ASCII symbols.
````
0 < |text| ≤ 10^5
````

**Optional goals**

**Rank 2:**

If you have **two or more letters with the same frequency**, then return the letter which comes first in the alphabet. For example -- "one" contains "o", "n", "e" only once for each and since it comes first, we choose "e".

**Rank 3:**

If the second argument "all_letters" is True, then your function should return all letters from the text in lowercase as a string. Letters must be sorted in descending order by frequency and same frequency letters by alphabetical order. For example -- "Hello" ⇒ "leho". "l" is the first because appears twice and other letters are sorted by alphabet.

**How it is used:**

For most decryption tasks you need to know the frequency of occurrence for various letters in a section of text. With this information we can easily crack a simple addition or substitution cipher. This is interesting stuff for language experts!