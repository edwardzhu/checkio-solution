###Max of Two

Define a function that takes two numbers as arguments and returns the largest of them.

**Input:** Two arguments as numbers.

**Output:** Maximum of two.

**Example:**

my_max(3, 3) == 3
my_max(0, 1) == 1
my_max(3, 2) == 3
--------------------------------------
###String Length

Define a function that computes the length of a given string.

**Input:** String.

**Output:** It's length.

**Example:**

str_length("") == 0
str_length("mo") == 2
str_length("length") == 6
---------------------------------------
###Rotate List

Write a function that rotates a list by k elements. For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2]. Try solving this without creating a copy of the list.

**Input:** Two arguments. List of elements and positive integer

**Output:** Converter list of elements

**Example:**

rotate_list([1, 2, 3, 4, 5, 6], 2) === [3, 4, 5, 6, 1, 2]
rotate_list([1, 2, 3, 4, 5, 6], 3) === [4, 5, 6, 1, 2, 3]
---------------------------------------
###Fizz Buzz

To get them ready for storage, we need the worker-bots to sort crystals by 3 or 5 or divide them by the number of edges. To make things easier, we will base our program on the ancient human word game "Fizz buzz".

Our goal is to write a function that will receive a positive integer and return:

The phrase **"Fizz Buzz"** if the number is divisible by 3 and by 5,

The word **"Fizz"** if the number is divisible by 3,

The word **"Buzz"** if the number is divisible by 5,

The number as a string for all other cases.

**Input:** A number as an integer.

**Output:** The answer as a string.

**Example:**

fizz_buzz(15) == "Fizz Buzz"
fizz_buzz(6) == "Fizz"
fizz_buzz(5) == "Buzz"
fizz_buzz(7) == "7"

**Precondition:**

0 < number ≤ 1000

**How it is used:**

Here you can learn how to write simple functions and work with if-else statements.

--------------------------------------
###Number Base

Sometimes the robots mix up their coordinates and use other [Numeral systems](https://en.wikipedia.org/wiki/Numeral_system). Let's try to sort this out and see what could be going on.

You are given a positive number as a string along with the radix for it. Your function should convert it into decimal form. The radix is less than 37 and greater than 1. The task uses digits and the letters A-Z for the strings.

Watch out for cases when the number cannot be converted. For example: "1A" cannot be converted with radix 9. For these cases your function should return -1.

**Input:** Two arguments. A number as string and a radix as an integer.

**Output:** The converted number as an integer.

**Example:**
````
convert("AF", 16) == 175
convert("101", 2) == 5
convert("101", 5) == 26
convert("Z", 36) == 35
convert("AB", 10) == -1
````
**Precondition:**
````
re.match("\A[A-Z0-9]\Z", str_number)
0 < len(str_number) <= 10
2 <= radix <= 36
````
**How it is used:**

Here you will learn how to work with the various numeral systems and handle exceptions.

--------------------------------------
###Two Monkeys

We have two monkeys, a and b, and the parameters asmile and bsmile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

**Input:** Two arguments as numbers.

**Output:** Maximum of two.

**Example:**
````
two_monkeys(True, True) == True
two_monkeys(False, False) == True
two_monkeys(True, False) == False
two_monkeys(False, True) == False
````

--------------------------------------
###Most Numbers
You are given an array of numbers from which you must find the difference between the maximum and minimum elements. Your function should be able to handle an undefined amount of arguments. For an empty argument list, the function should return 0.

Floating-point numbers are represented in computer hardware as base 2 (binary) fractions, since this is the case, we should check that the result is within 0.001 precision.

**Input:** An arbitrary number of arguments as numbers (int, float).

**Output:** The difference between the maximum and minimum as a number (int, float).

**Example:**
````
most_difference(1, 2, 3) == 2
most_difference(5, -5) == 10
most_difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4
most_difference() == 0
````
**Precondition:**

0 ≤ |arguments| ≤ 20

**How it is used:**

The important concept to learn from this mission is about passing an undefined amount of arguments to functions.

-------------------------------------
###Non Unique
You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the non-unique elements in this list. To do so you will need to remove all unique elements (elements which are contained in a given list only once). When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements so the result will be [1, 3, 1, 3].

**Input:** A list of integers.

**Output:** The list of integers.

**Example:**
````
non_unique([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
non_unique([1, 2, 3, 4, 5]) == []
non_unique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
non_unique([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
````
**Precondition:**

0 < |data| < 1000

**Optional Goals**

**Rank 2:**

An array can contain Latin letters. Letters are counted as case insensitive, so "a" == "A", so in ["d", "D", "A"] only one unique element - "A".

*Precondition Rank 2*

data contains only numbers or letters (one symbol string).

**How it is used:**

This mission will help you to understand how to use manipulate arrays, giving you a foundation for solving more complex tasks. The concept can be easily generalized for real world tasks. For example; it allows you to clarify data by removing low frequency elements (noise).