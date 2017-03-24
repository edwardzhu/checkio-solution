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
--------------------------------------
### String Length

Define a function that computes the length of a given string.

**Input:** String.

**Output:** It's length.

**Example:** 
````
str_length("") == 0
str_length("mo") == 2
str_length("length") == 6
````
---------------------------------------
### Rotate List

Write a function that rotates a list by k elements. For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2]. Try solving this without creating a copy of the list.

**Input:** Two arguments. List of elements and positive integer

**Output:** Converter list of elements

**Example:**
````
rotate_list([1, 2, 3, 4, 5, 6], 2) === [3, 4, 5, 6, 1, 2]
rotate_list([1, 2, 3, 4, 5, 6], 3) === [4, 5, 6, 1, 2, 3]
````
---------------------------------------
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

--------------------------------------
### Number Base

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
### Two Monkeys

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
### Most Numbers
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
### Non Unique
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

-------------------------------------
### Robot Sort

You are given the size and initial order of the ingots as an array of numbers. Indexes are their position, values are their sizes. You should order this array from the smallest to the largest in size.

For each action a Robot can swap two neighboring elements. Each action should be represented as a string with two digits - indexes of the swapped elements (ex, "01" - swap 0th and 1st ingots). The result should be represented as a string that contains the sequence of actions separated by commas. If the array does not require sorting, then return an empty string.

And you can swap only **N\*(N-1)/2** times, where N - is a quantity of ingots.

Initial   6 ============ 
position  4   ========   
          2     ====     

Swap      4   ========
0 - 1     6 ============ 
          2     ====
          
Swap      4   ========
1 - 2     2     ==== 
          6 ============
          
Swap      2     ====
0 - 1     4   ======== 
          6 ============

**Input:** An array as a tuple of integers.

**Output:** The sequence of actions as a string.

**Example:**
````
swap_sort((6, 4, 2)) == "01,12,01"
swap_sort((1, 2, 3, 4, 5)) == ""
swap_sort((1, 2, 3, 5, 3)) == "43"
````

**Precondition:**

1 ≤ |array| ≤ 10

**How it is used:**

This mission will show you how to work the simplest sorting algorithms. It also models one of the game mechanics in the classic puzzle game "Tetris Attack".

-----------------------------------
### Clock Angle

Analog clocks display time with an analog clock face, which consists of a round dial with the numbers 1 through 12, the hours in the day, around the outside. The hours are indicated with an hour hand, which makes two revolutions in a day, while the minutes are indicated by a minute hand, which makes one revolution per hour. In this mission we will use a clock without second hand. The hour hand moves smoothly and the minute hand moves step by step.

You are given a time in 24-hour format and you should calculate a lesser angle between the hour and minute hands in degrees. Don't forget that clock has numbers from 1 to 12, so 23 == 11. The time is given as a string with the follow format "HH:MM", where HH is hours and MM is minutes. Hours and minutes are given in two digits format, so "1" will be writen as "01". The result should be given in degrees with precision ±0.1.

**Input:** A time as a string.

**Output:** The lesser angle as an integer or a float.

**Example:**
````
clock_angle("02:30") == 105
clock_angle("13:42") == 159
clock_angle("01:43") == 153.5
````
**Precondition:**

Input time matches by regexp expression `"\A((2[0-3])|([0-1][0-9])):[0-5][0-9]\Z"`

**How it is used:**

Simple mathematics and skill to built a model for various things from real world.

----------------------------------
### Triangle Angles

You are given the lengths for each side of a triangle. You need to find all three of the angles for this triangle. If the given side lengths cannot form a triangle (or form a degenerated triangle), then you must return all angles as 0 (zero). The angles should be represented as a list of integers in **ascending** order. Each angle is measured in degrees and rounded to the nearest integer number using standard mathematical rounding.

**Input:** The lengths of the sides of a triangle as integers.

**Output:** Angles of a triangle in degrees as sorted list of integers.

**Example:**
````
angles(4, 4, 4) == [60, 60, 60]
angles(3, 4, 5) == [37, 53, 90]
angles(2, 2, 5) == [0, 0, 0]
````
**Precondition:**
````
0 < a ≤ 1000
0 < b ≤ 1000
0 < c ≤ 1000
````
**How it is used:**

This is a classical geometry problem. With this concept you can measure an angle without the need for a protractor for use in fields such as topography or architecture.

--------------------------------
### Vault Password

The password will be considered strong enough if its length is greater than or equal to 10 characters, it contains at least one digit, as well as at least one uppercase letter and one lowercase letter. The password may only contain ASCII latin letters or digits, no punctuation symbols.

You are given a password. We need your code to verify if it meets the conditions for a secure password.

In this mission the main goal to make your code as short as possible. The shorter your code, the more points you earn. Your score for this mission is dynamic and directly related to the length of your code.

**Input:** A password as a string.

**Output:** A determination if the password safe or not as a boolean, or any data type that can be converted and processed as a boolean. When the results process, you will see the converted results.

**Example:**
````
golf('A1213pokl') == False
golf('bAse730onE') == True
golf('asasasasasasasaas') == False
golf('QWERTYqwerty') == False
golf('123456123456') == False
golf('QwErTy911poqqqq') == True
````
**Precondition:**

0 < "password| ≤ 64

password matches by regexp expression `"[a-zA-Z0-9]+"`

**Scoring:**

Scoring in this mission is based on the number of characters used in your code (comment lines are not counted).

*Rank1:*

Any code length.

*Rank2:*

Your code should be shorter than 200 characters.

*Rank3:*

Your code should be shorter than 100 characters.

**How it is used:**

If you are worried about the security of your app or service, you can use this handy code to personally check your users' passwords for complexity. You can further use these skills to require that your users passwords meet or include even more conditions, punctuation or unicode.

-----------------------------
### Boolean Algebra

In mathematics and mathematical logic, [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra#Basic_operations) is a sub-area of algebra in which the values of the variables are true or false, typically denoted with 1 or 0 respectively. Instead of elementary algebra where the values of the variables are numbers and the main operations are addition and multiplication, the main operations of Boolean algebra are the conjunction (denoted ∧), the disjunction (denoted ∨) and the negation (denoted ¬).

In this mission you should implement some boolean operations:

- **"conjunction"** denoted x ∧ y, satisfies x ∧ y = 1 if x = y = 1 and x ∧ y = 0 otherwise.

- **"disjunction"** denoted x ∨ y, satisfies x ∨ y = 0 if x = y = 0 and x ∨ y = 1 otherwise.

- **"implication"** (material implication) denoted x → y and can be described as ¬ x ∨ y. If x is true then the value of x → y is taken to be that of y. But if x is false then the value of y can be ignored; however the operation must return some truth value and there are only two choices, so the return value is the one that entails less, namely true.

- **"exclusive"** (exclusive or) denoted x ⊕ y and can be described as (x ∨ y)∧ ¬ (x ∧ y). It excludes the possibility of both x and y. Defined in terms of arithmetic it is addition mod 2 where 1 + 1 = 0.

- **"equivalence"** denoted x ≡ y and can be described as ¬ (x ⊕ y). It's true just when x and y have the same value.

Here you can see the truth table for these operations:

x	y	x∧y	x∨y	x→y	x⊕y	x≡y
0	0	0	0	1	0	1
1	0	0	1	0	1	0
0	1	0	1	1	1	0
1	1	1	1	1	0	1

You are given two boolean values **x** and **y** as 1 or 0 and you are given an operation name as described earlier. You should calculate the value and return it as 1 or 0.

**Input:** Three arguments. X and Y as 0 or 1. An operation name as a string.

**Output:** The result as 1 or 0.

**Example:**
````
boolean(1, 0, "conjunction") == 0
boolean(0, 1, "exclusive") == 1
````
**Precondition:**
````
x in (0, 1)
y in (0, 1)
operation in ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
````

**How it is used:**

Fixing our defense bot's logic modules gets you working with boolean values and operators, a core concept in many programming languages.

----------------------------
### List Combitation

Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].

**Input:** Two lists

**Output:** List - combination of two

**Example:**
````
list_combination([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]
list_combination([1, 1, 1, 1], [2, 2, 2, 2]) == [1, 2, 1, 2, 1, 2, 1, 2]
````

--------------------------