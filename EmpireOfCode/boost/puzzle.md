### Exchange Symbols

Given a string, return a new string where the first and last chars have been exchanged.

**Input:** String.

**Output:** Changed string.

**Example:**
````
sym_exchange("az") === "za"
sym_exchange("aiiiiiz") === "ziiiiia"
sym_exchange("length") === "hengtl"
````

-------------------------------
### Count Inversion

In computer science and discrete mathematics, an [inversion](https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics)) is a pair of places in a sequence where the elements in these places are out of their natural order. So, if we use ascending order for a group of numbers, then an inversion is when the order is reversed and larger numbers appear before lower number in a sequence.

Check out this example sequence: (1, 2, 5, 3, 4, 7, 6) and we can see here three inversions:

- 5 and 3;
- 5 and 4; 
- 7 and 6.

You are given a sequence of unique numbers and you should count the number of inversions in this sequence.

**Input:** A sequence as a tuple of integers.

**Output:** The inversion number as an integer.

**Example:**
````
count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3
count_inversion((0, 1, 2, 3)) == 0
````
**Precondition:**
````
2 < |sequence| < 200
All elements of a sequence are unique.
````

**How it is used:**

In this mission you will experience the wonder of nested loops, that is of course supposing you don't use advanced algorithms or black magic.

---------------------------------
### Even Last

You are given an array of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...) then multiply this summed number and the final element of the array together. Don't forget that the first element has an index of 0.

For an empty array, the result will always be 0 (zero).

**Input:** A list of integers.

**Output:** The number as an integer.

**Example:**
````
even_last([0, 1, 2, 3, 4, 5]) == 30
even_last([1, 3, 5]) == 30
even_last([6]) == 36
even_last([]) == 0
````
**Precondition:**
````
0 ≤ |array| ≤ 20
````
**How it is used:**

Indexes and slices are important elements of coding in python and other languages. This will come in handy down the road!

---------------------------
### Median

A median is a numerical value separating the upper half of a **sorted** array of numbers from the lower half. In a list where there are an odd number of entities, the median is the number found in the middle of the array. If the array contains an even number of entities, then there is no single middle value, instead the median becomes the average of the two numbers found in the middle.

For this mission, you are given a non-empty array of natural numbers (X). With it, you must separate the upper half of the numbers from the lower half and find the median.

**Input:** An array as a list or a tuple of integers.

**Output:** The median as a float or an integer.

**Example:**
````
median([1, 2, 3, 4, 5]) == 3
median([3, 1, 2, 5, 3]) == 3
median([1, 300, 2, 200, 1]) == 2
median((3, 6, 20, 99, 10, 15)) == 12.5
````
**Precondition:**
````
1 < |data| ≤ 1000
````
**How it is used:**

The median has usage for Statistics and Probability theory, it has especially significant value for skewed distribution. Here's an example: we want to know the average income of people from a set of data and 100 people earn $100 in month while 10 people earn $1,000,000. If we average it out we get $91,000. This is weird value and does nothing to show us the real picture.
In this case the median would give to us more useful value and a better picture. [The Article at Wikipedia](https://en.wikipedia.org/wiki/Median).

--------------------------
### Secret Message

You are given a chunk of text. Gather all of the capital letters in one word in the order that they appear in the text.

For example: text = "**H**ow are you? **E**h, ok. **L**ow or **L**ower? **O**hhh.", if we collect all of the capital letters, we get the message "HELLO".

**Input:** A text as a string.

**Output:** The secret message as a string or an empty string.

**Example:**
````
find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
find_message("hello world!") == ""
````
**Precondition:**
```
0 < |text| ≤ 1000
```
**How it is used:**

This type of communication has been used to send secret messages, or even tell jokes. But the skills behind it show you how to find specific types of information or patterns hidden within larger chunks of data that would be difficult to find by hand.

--------------------------
### Three Words

You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end" contains three words in succession.

**Input:** A string with words.

**Output:** The answer as a boolean.

**Example:**
````
three_words("Hello World hello") == True
three_words("He is 123 man") == False
three_words("1 2 3 4") == False
three_words("bla bla bla bla") == True
three_words("Hi") == False
````
**Precondition:**

The input contains words and/or numbers. There are no mixed words (letters and digits combined).
````
0 < |words| < 100
````
**How it is used:**

This teaches you how to work with strings and introduces some useful functions.

--------------
### Flatten List

There is a list which contains integers or other nested lists which may contain yet more lists and integers which then… you get the idea. You should put all of the integer values into one flat list. The order should be as it was in the original list with string representation from left to right.

**Input:** A nested list with lists or integers.

**Output:** The one-dimensional list with integers.

**Example:**
````
flat_list([1, 2, 3]) == [1, 2, 3]
flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]
````
**Precondition:**
````
depth < 10
````
**How it is used:**

This concept is useful for parsing and analyzing files with complex structures and the task challenges your creativity in writing short code.

------------
### Pearl Box

Let's play with pearls. To start the game, robots put several black and white pearls in one of the boxes. For each move, the robots take a pearl out of the box and put one of the opposite color back. The winner is the one who pulls the white pearl on the **Nth** step.

Our robots don't like indeterminacy and want to know the probability of a white pearl on the Nth step. The probability is a value between 0 (0% chance or will not happen) and 1 (100% chance or will happen). The result is a float from 0 to 1 with two digits precision (±0.01).

You are given a start set of pearls as a string that contains "b" (black) and "w" (white) and the number of the step (N). The order of the pearls does not matter.

**Input:** The start sequence of the pearls as a string and the step number as an integer.

**Output:** The probability for a white pearl as a number.

**Example:**
````
probability('bbw', 3) == 0.48
probability('wwb', 3) == 0.52
probability('www', 3) == 0.56
probability('bbbb', 1) == 0
probability('wwbb', 4) == 0.5
probability('bwbwbwb', 5) == 0.48
````
**Precondition:**
````
0 < N ≤ 20

0 < |pearls| ≤ 20
````
**How it is used:**

This task introduces you to the basics of probability theory and statistics. Fun fact: regardless of the initial state, as the number of steps increases, the probability approaches 0.5!

-----------
### Bird Language

The bird converts words by two rules:

- after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
- after each vowel letter the bird appends two of the same letter (a ⇒ aaa);

**Vowels letters == "aeiouy".**

You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by one whitespace). The bird does not know how to punctuate its phrases and only speaks words as letters. All words are given in lowercase. You should translate this phrase from the bird language to something more understandable.

**Input:** A bird phrase as a string.

**Output:** The translation as a string.

**Example:**
````
translate("hieeelalaooo") == "hello"
translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
translate("aaa bo cy da eee fe") == "a b c d e f"
translate("sooooso aaaaaaaaa") == "sos aaa"
````
**Precondition:**

A `phrase` satisfies regexp `"\A([a-z]+\ ?)+(<!\ )\Z"`.

A phrase always has the translation.

**How it is used:**

This a similar cipher to those used by children when they invent their own "bird" language. Now you will be ready to crack the code.

---------------
### Common Words

You are given two string with words separated by commas. Try to find what is common between these strings. The words are not repeated in the same string.

Your function should find all of the words that appear in both strings. The result must be represented as a string of words separated by commas in **alphabetical order**.

**Input:** Two arguments as strings.

**Output:** The common words as a string.

**Example:**
````
common_words("hello,world", "hello,earth") == "hello"
common_words("one,two,three", "four,five,six") == ""
common_words("one,two,three", "four,five,one,two,six,three") == "one,three,two"
````
**Precondition:**

Each string contains no more than 10 words.

All words separated by commas.

All words consist of lowercase latin letters.

**How it is used:**

This mission simply teaches you how to work with strings and sets, knowledge which can be useful in linguistic analysis.

-----------
### Hamming Distance

The Hamming distance between two binary integers is the number of bit positions that differs ( [read more about the Hamming distance on Wikipedia](https://en.wikipedia.org/wiki/Hamming_distance)). For example:

````
117 = 0 1 1 1 0 1 0 1
 17 = 0 0 0 1 0 0 0 1
  H = 0+1+1+0+0+1+0+0 = 3
 ````
You are given two positive numbers (N, M) in decimal form. You should calculate the Hamming distance between these two numbers in binary form.

**Input:** Two arguments as integers.

**Output:** The Hamming distance as an integer.

**Example:**
````
hamming(117, 17) == 3
hamming(1, 2) == 2
hamming(16, 15) == 5
````
**Precondition:**
````
0 < n < 1000000

0 < m < 1000000
````
**How it is used:**

This is a basis for Hamming code and other linear error-correcting programs. The Hamming distance is used in systematics as a measure of genetic distance. On a grid (ie: a chessboard,) the Hamming distance is the minimum number of moves it would take a rook to move from one cell to the other.

-----------
### Landing Holes

The system looks like numbered pipes arranged in a circular manner. There is a rotating mechanism behind these pipes, and the cannons are attached to the end. This system is incredibly ancient and some of the cannons are broken. The loading automaton has a program with the pipe numbers which indicate where it should place projectiles. These numbers cannot be changed as they are engraved into the pipes. We can, however, rotate the backend mechanism to change the correspondence between pipes and cannons. We should find each combination that we can rotate the backend mechanism so that all loaded projectiles will be loaded into the still-working cannons. The loading automaton will load all of the projectiles simultaneously.

The pipes are numbered from 0 to **N-1**. The initial positions of the backend mechanism are represented as an array with 1 and/or 0. Each element describes a cannon behind the pipe; the 0th element describe 0th pipe. 1 is a working cannon and 0 is a broken cannon.

You know the pipe numbers where the automaton will load projectiles (sometimes it loads several projectiles into one cannon). Your goal is to find all the combinations that you can rotate the backend mechanism in a clockwise manner so that all of the projectiles will be loaded into the working cannons. Rotation is described as an integer - how many units you should rotate clockwise. The result should be represented as a list of integers (variants) in the ascending order. The case when you don't need to rotate are described as 0 (but don't forget about other variants). If it's not possible to find a solution, then return \[\].

For example, the initial state is \[1,0,0,0,1,1,0,1,0,0,0,1\] and pipes numbers are \[0,1\]. If you rotate the mechanism by 1 or 8 units, then all projectiles which are be placed in the 0th and 1st pipes will be in cannons.

**Input:** Two arguments. A initial state as a list with 1 and/or 0 and pipe numbers for projectiles as a list of integers.

**Output:** The rotating variants as a list of integers or an empty list.

**Example:**
````
rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8]
rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == []
rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0]
rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5]
````
**Precondition:**
````
3 ≤ |state| < 100

∀ x ∈ pipe_numbers: 0 ≤ x < |state|
````
**How it is used:**

This concept will acquaint you with circular data structures.