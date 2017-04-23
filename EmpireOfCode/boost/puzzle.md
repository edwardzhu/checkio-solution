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