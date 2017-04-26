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

````
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
````
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

````
x	y	x∧y	x∨y	x→y	x⊕y	x≡y
0	0	0	0	1	0	1
1	0	0	1	0	1	0
0	1	0	1	1	1	0
1	1	1	1	1	0	1
````

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
### Index Power
You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.

Let's look at a few examples:

- array = [1, 2, 3, 4] and N = 2, then the result is 32 == 9;
- array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.

**Input:** An array as a list of integers and a number as an integer.

**Output:** The result as an integer.

**Example:**
````
index_power([1, 2, 3, 4], 2) == 9
index_power([1, 3, 10, 100], 3) == 1000000
index_power([0, 1], 0) == 1
index_power([1, 2], 3) == -1
````

**Precondition:**
````
0 < |array| ≤ 10
0 ≤ N
∀ x ∈ array: 0 ≤ x ≤ 100
````

**How it is used:**

This mission teaches you how to use basic arrays and indexes in combination with simple mathematics.

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

----------------
### Simple Area
You should write a function to calculate the area of simple figures: circles, rectangles and triangles. You are given an arbitrary number of arguments which the function should use to calculate the area for the different figures.

- One argument -- The diameter of a circle and you need calculate the area of the circle.
- Two arguments -- The side lengths of a rectangle and you need calculate the area of the rectangle.
- Three arguments -- The lengths of each side on a triangle and you need calculate the area of the triangle.

The result should be given with two digit precision like so: +-0.01

**Input:** One, two or three arguments as floats or as integers.

**Output:** The area of the circle, the rectangle or the triangle as a float.

**Example:**
````
simple_areas(3) == 7.07
simple_areas(2, 2) == 4
simple_areas(2, 3) == 6
simple_areas(3, 5, 4) == 6
simple_areas(1.5, 2.5, 2) == 1.5
````
**Precondition:**
````
0 < len(args) <= 3
all(0 < x <= 1000 for x in args)
For the "triangle" cases, the sum of the lengths of any two sides always exceeds the length of the third side.
````
**How it is used:**

Python can be an useful tool for mathematics and science due to its simplicity, readability and ease of use.

-----------------
### Daily Report
Ingots in each consignment are numbered in the row from A1 to Z9 as A1, A2,..., A9, B1, B2, ..., Z9. Each consignment are marked by the last ingots in it. So you can define the quantity of ingots by marks. Each daily report written as consignments of marks in string separated by commas. So you can count the total quantity of ingots for a day.

The full report contain daily reports for several days. Each report is given with a date in the next format: YYYY-MM-DD, where YYYY is year, MM is month, DD is day. Date and report are separated by whitespace. Each date-report are placed on separated lines.

You are given a full report as a multiline text and two dates. You should calculate the total quantity ingots for the days between given dates **(including)**.

For example you are given the next full report and dates:
````
2015-01-01 A1,B2
2015-01-05 C3,C2,C1
2015-02-01 B4
2015-01-03 Z9,Z9

From: 2015-01-01
To:   2015-01-31
````

For these dates we see three "good" days: 2015-01-01, 2015-01-03, 2015-01-05.

- 2015-01-01 == 1 + 11 == 12
- 2015-01-03 == 21 + 20 + 19 == 60
- 2015-01-05 == 234 + 234 == 468

So the result is 540.

**Input:** Three arguments. A full report as a multiline string. A start and end date as strings.

**Output:** The total quantity of ingots for daily reports between these days as an integer.

**Example:**
````
count_reports("2015-01-01 A1,B2\n"
              "2015-01-05 C3,C2,C1\n"
              "2015-02-01 B4\n"
              "2015-01-03 Z9,Z9",
              "2015-01-01", "2015-01-31") == 540,
````
**Precondition:**

All report lines are correct.

**How it is used:**

String date representation often appears in various reports and documents. This concept is useful for parsing and process documents.

-----------
### Place Queens
Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and denoted with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. Each square of the chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", "d6"). For this mission we only need to concern ourselves with Queens. The Queen can move any number of squares along the rank, file, or diagonal axis.

You should place eight chess Queens on an 8×8 chessboard so that no two Queens threaten each other. For this challenge, we have already placed one or more Queens on the board, so you will need to finish the placement. In addition, each Queen may be considered as part of it’s army, meaning every Queen could possible be a threat to every other Queen on the board.

You are given a set of square coordinates where we have placed Queens already. You should finish this set and return the full set of the coordinates for all eight Queens. If it's not possible -- return an empty set. Be careful - an initial position could possibly threaten another Queen right off the bat.

**Input:** Placed Queens coordinates as a set of strings.

**Output:** Eight Queens coordinates as a set of strings or an empty set.

**Example:**
````
place_queens({"b2", "c4", "d6", "e8"})  # {"b2", "c4", "d6", "e8", "a5", "f3", "g1", "h7"}
place_queens({"b2", "c4", "d6", "e8", "a7", "g5"}) == set()
````
**Precondition:**

An input strings satisfies regexp `"[a-h][1-8]"`.

`0 < |placed| < 8`

**How it is used:**

This is a classical puzzle and combinatorial constraints problem. It can be useful if you need make a schedule for teachers and classes, or for sport games occurring in several different stadiums.

-----------
### Count Ingots

Ingots in each consignment are numbered in the row from A1 to Z9 as A1, A2,..., A9, B1, B2, ..., Z9. Each consignment is marked with the number of the last ingot in it. So you can define the quantity of ingots by the number of marks.

You are given a report of daily consignments as number marks written in a string separated by commas. Count the total quantity of ingots. Take the report "A2,B1" for example. Here we can see two consignments with 2 (A2) and 10 (B1) ingots, giving us a result of 12.

**Input:** A daily report as a string.

**Output:** The total quantity of ingots as an integer.

**Example:**
````
count_ingots("A2,B1") == 12
count_ingots("A1,A1,A1") == 3
count_ingots("Z9,X8,Y7") == 672
count_ingots("C1,D1,B1,E1,F1") == 140
````
**Precondition:**

report match with regexp expression `"[A-Z][1-9](,[A-Z][1-9])*"`

**How it is used:**

This concept uses a modified numeral system and provides you with a basis for working with strings.

-----------
### Stair Steps

There is a staircase with N steps and two platforms; one at the beginning of the stairs and the other at the end. On each step a number is written (ranging from -100 to 100 with the exception of 0.) Zeros are written on both platforms. You start going up the stairs from the first platform, to reach the top on the second one. You can move either to the next step or to the next step plus one. You must find the best path to maximize the sum of numbers on the stairs on your way up and return the final sum.

````
                         __
                   __   /  |
         ______   /  | | _____
        /      | |  _____|  0
   __  /      _____|  2 
  /  ||  _____| -1
 |  _____| -3
____|  5
  0 
````

**Input:** Numbers on stairs as a tuple of integers.

**Output:** The final sum for the best path as an integer.

**Example:**
````
golf((5, -3, -1, 2)) == 6
golf((5, 6, -10, -7, 4)) == 8
golf((-11, 69, 77, -51, 23, 67, 35, 27, -25, 95)) == 393
golf((-21, -23, -69, -67, 1, 41, 97, 49, 27)) == 125
````
**Precondition:**
````
0 < |steps| ≤ 10
∀ x ∈ steps: -100 < x < 100
````

**Scoring:**

In this mission the main goal to make your code as short as possible. The shorter your code, the more points you earn. Your score for this mission is dynamic and directly related to the length of your code.

Scoring in this mission is based on the number of characters used in your code (comment lines are not counted).

**Rank1:**
Any code length.

**Rank2:**
Your code should be shorter than 250 characters.

**Rank3:**
Your code should be shorter than 150 characters.

**How it is used:**

This is a classical example of an optimization problem. It can show you the difference between the various methods of programming; such as dynamic programming and recursion.

--------------
### Broken Reports

Ingots in each consignment are numbered in the row from A1 to Z9 as A1, A2,..., A9, B1, B2, ..., Z9. Each consignment is marked with the number of the last ingot in it. This lets you define the quantity of ingots by the number of marks.

Our daily report is broken. For some reason all of the commas separating values were removed or replaced with a junk data. We need to figure out which are the good marks in todays report. Each mark will look a little like "LD", where "L" is a capital english letter and "D" is a digit ranging from 1 to 9 (zero indicates junk data).

You are given a report as a chunk of text. Your code needs to find all consignment marks and count the total quantity of ingots. Take the report "ASDA1,BB22D01C1" for example. Here we can find three marks: A1, B2 and C1, so the result is 31.

**Input:** A broken report as a string.

**Output:** The total quantity of ingots as an integer.

**Example:**
````
golf("ASDA1,BB22D01C1") == 31
````
**Precondition:**

report can contains only ASCI letters, digits and commas.

**Scoring:**

In this mission the main goal is to make your code as short as possible. The shorter your code, the more points you earn. Your score for this mission is dynamic and directly related to the length of your code.

Scoring in this mission is based on the number of characters used in your code (comment lines are not counted).

**Rank1:**
Any code length.

**Rank2:**
Your code should be shorter than 150 characters.

**Rank3:**
Your code should be shorter than 100 characters.

**How it is used:**

Code golf missions help you to learn special tricks and give you a deeper understanding Python as a language.

---------------------
### Three Point Circle

Through any three points that do not exist on the same line, there lies a unique circle. The points of this circle are represented in a string with the coordinates like so:
````
(x1,y1),(x2,y2),(x3,y3)
````
Where *x1,y1,x2,y2,x3,y3* are digits.

You should find the circle for the three given points, such that the circle lies through these point and return the result as a string with the equation of the circle. In a Cartesian coordinate system (with an X and Y axis), the circle with central coordinates of (x0,y0) and radius of r can be described with the following equation:
````
(x-x0)^2+(y-y0)^2=r^2
````
Where *x0, y0, r* are decimal numbers rounded to **two decimal points**. Remove extraneous zeros and all decimal points, they are not necessary. For rounding, use the standard mathematical rules.

**Input:** Coordinates as a string.

**Output:** The equation of the circle as a string.

**Example:**
````
circle_equation("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
circle_equation("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
````
**Precondition:**
````
0 < radius < 10

All three given points do not lie on one line.
````

**How it is used:**

This equation, also known as Equation of the Circle, comes from the Pythagorean theorem when applied to any point on a circle: the radius is the hypotenuse of a right-angled triangle whose other sides are of length x − a and y − b. Of course you can use this concept for you mathematics software, but we really just want to remind you about how awesome circles can be.

-------------
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

---------------
### Letter Queue

We will emulate the queue process with letters. You are given a sequence of commands:

- "PUSH X" -- enqueue X, where X is a letter in uppercase.
- "POP" -- dequeue the front position. if the queue is empty, then do nothing.

The queue can only contain letters.

You should process all commands and assemble letters which remain in the queue in one word from the front to the back of the queue.
````
["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]
````
````
| Command | Queue | Note
-------------------------------------------------
| PUSH A  | A     | Added "A" in the empty queue
| POP     |       | Removed "A"
| POP     |       | The queue is empty already
| PUSH Z  | Z     |
| PUSH D  | ZD    |
| PUSH O  | ZDO   |
| POP     | DO    |
| PUSH T  | DOT   | The result
````
**Input:** A sequence of commands as a tuple of strings.

**Output:** The queue remaining as a string.

Example:
````
letter_queue(("PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T")) == "DOT"
letter_queue(("POP", "POP")) == ""
letter_queue(("PUSH H", "PUSH I")) == "HI"
letter_queue(()) == ""
````
**Precondition:**
````
0 ≤ |commands| ≤ 30

All commands match with "\APUSH [A-Z]\Z" or "\APOP\Z" regexp expression.
````
**How it is used:**

Queues provide services in computer science, transportation, and operations research where various entities such as data, objects, persons, or events are stored and held to be processed later. In these contexts, the queue performs the function of a buffer.

--------------
### Binary Count

You are given a positive integer as a number, and you need to convert it to the binary format then count how many units (1) there are. For example: 5 = 0b101 contains two units, so the answer is 2.

**Input:** A number as a positive integer.

**Output:** The quantity of units in binary form as an integer.

**Example:**
````
count_units(4) == 1
count_units(15) == 4
count_units(1) == 1
count_units(1022) == 9
````
**Precondition:**
````
0 ≤ number ≤ 2^32
````

**How it is used:**

Binary as a computer language is very difficult for humans to understand, but makes the lives of our computers and robots easier. Every time you press a key on your keyboard it sends a binary signal informing the computer you hit that key. Every time you code a program, the computer takes your code and interprets it in binary then executes your program.

-------------
### Earth Distances

To describe a specific position on the surface of the Earth, we must rely on the [geographic coordinate system](https://en.wikipedia.org/wiki/Geographic_coordinate_system). The geographic coordinate system is a method used to give every possible location on Earth as specified by a set of numbers or letters. From what we can tell, the most commonly used coordinate system involved [latitude](https://en.wikipedia.org/wiki/Latitude) and [longitude](https://en.wikipedia.org/wiki/Longitude). With this information we can calculate the distance between two points on the surface of this "Globe".

For simplicity’s sake, we will suppose that the Earth is a perfect sphere with a radius of 6,371 kilometers (this gives an error margin of no more than 0.3%). You are given two points as coordinates and must find the shortest distance between these points on the surface of the Earth, measured along the surface of the Earth.

Coordinates are given as a string with the latitude and longitude separated by comma and/or whitespace. Latitude and longitude are represented in the following format: d°m′s″X

In this example, "d" is degrees, "m" is minutes, "s" is seconds as integers, while "X" is "N" (north) or "S" (south) for a latitude and "W" (west) or "E" (east) for a longitude.

The result should be given as a number in kilometers with a precision of ±0.1 (100 metres).

**Input:** Two arguments. Coordinates as strings.

**Output:** The distance as a number (int or float).

**Example:**
````
distance("51°28′48″N 0°0′0″E", "46°12′0″N, 6°9′0″E") # 739.2
distance("90°0′0″N 0°0′0″E", "90°0′0″S, 0°0′0″W") # 20015.1
````
**Precondition:**

Correct Earth coordinates.

**How it is used:**

The concepts presented in this mission are the exact sorts of concepts used in navigational software, enabling a ship or plane to understand where it is, where it must go and how far it has gone. Along the same vein, Global Positioning Satellites use similar principles to provide pinpoint accurate locations to GPS receivers for use in navigation.

---------------
### Super Root

The super root of a number **N** is the number **x**, such that `x^x = N`.

The result should be accurate so that `x^x ≈ N±0.001`.

Or `N - 0.001 < x^x < N + 0.001`.

**Input:** A number (N) as an integer.

**Output:** The super root (x) as a float or an integer.

**Example:**
````
super_root(4) # 2
super_root(27) # 3
super_root(81) # 3.504339593597054
````
**Precondition:**
````
1 ≤ number ≤ 10^10
````
**How it is used:**

This concept comes in useful when working in cryptography as complex mathematics often comes into play. In addition this skill could come in useful should you find yourself in a situation where you need ot develop a smarter calculator.

----------------
### Call Base

The bill is represented as an array with information about the calls that our accountant has made. Write a function to calculate the cost of these calls.

Each call is represented as a string with the date, time and duration of the call in seconds in the follow format:

`"YYYY-MM-DD hh:mm:ss duration"`

The date and time in this information describes the start of the call.

Space-Time Communications Co. has several rules on how it calculates the cost of calls made on their network:

- First 100 (one hundred) minutes in one day are priced at 1 coin per minute;
- After the first 100 minutes in one day, each minute costs 2 coins per minute;
- All calls are rounded up to the nearest minute. For example 59 sec ≈ 1 min, 61 sec ≈ 2 min;
- Calls are billed based on the day when they began So if a call was started at 2014-01-01 23:59:59, then it counts as having started on 2014-01-01.
Here's an example communications bill:
````
2014-01-01 01:12:13 181
2014-01-02 20:11:10 600
2014-01-03 01:12:13 6009
2014-01-03 12:13:55 200
````
- First day -- 181s≈4m -- 4 coins;
- Second day -- 600s=10m -- 10 coins;
- Third day -- 6009s≈101m + 200s≈4m -- 100 + 5 * 2 = 110 coins;
- Total -- 124 coins.
**Input:** Information about calls as a tuple of strings.

**Output:** The total cost as an integer.

**Example:**
````
total_cost(("2014-01-01 01:12:13 181",
        "2014-01-02 20:11:10 600",
        "2014-01-03 01:12:13 6009",
        "2014-01-03 12:13:55 200")) == 124
````
**Precondition:**
````
0 < |calls| ≤ 30

0 < call_duration ≤ 7200

The bill is sorted by datetime.
````
**How it is used:**

This mission will teach you how to parse and analyse various types data and encourages you to single out important fragments from a larger dataset.

------------------
### Counting Tiles

Each square tile has a size of 1x1 meters. You need to calculate how many whole and partial tiles are needed for a circle with a radius of N meters. The center of the circle will be at the intersection of four tiles. For example: a circle with a radius of 2 metres requires 4 whole tiles and 12 partial tiles.

**Input:** The radius of a circle as a float.

**Output:** The quantities of whole and partial tiles as a list or tuple with two integers -- \[solid, partial\].

**Example:**
````
golf(2) == [4, 12]
golf(3) == [16, 20]
golf(2.1) == [4, 20]
golf(2.5) == [12, 20]
````
**Precondition:**
````
0 < radius ≤ 4
````
**Scoring:**

In this mission the main goal is to make your code as short as possible. The shorter your code, the more points you earn. Your score for this mission is dynamic and directly related to the length of your code.

Scoring in this mission is based on the number of characters used in your code (comment lines are not counted).

**Rank1:**

Any code length.

**Rank2:**

Your code should be shorter than 250 characters.

**Rank3:**

Your code should be shorter than 150 characters.

**How it is used:**

This task is a simple geometry problem which uses concepts you can find in architecture and topography. You can even use it to calculate the amount of materials needed for your own building project.

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

---------------
### Roman Numbers

Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which are combined to signify the sum (or, in some cases, the difference) of their values. The first ten Roman numerals are:

I, II, III, IV, V, VI, VII, VIII, IX, and X.

The Roman numeral system is decimal based but not directly positional and does not include a zero. Roman numerals are based on combinations of these seven symbols:

- **I** 1 (unus)
- **V** 5 (quinque)
- **X** 10 (decem)
- **L** 50 (quinquaginta)
- **C** 100 (centum)
- **D** 500 (quingenti)
- **M** 1,000 (mille)

More additional information about roman numerals can be found on [the Wikipedia article](http://en.wikipedia.org/wiki/Roman_numerals).

For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.

**Input:** A number as an integer.

**Output:** The Roman numeral as a string.

**Example:**
````
roman(6) == 'VI'
roman(76) == 'LXXVI'
roman(13) == 'XIII'
roman(44) == 'XLIV'
roman(3999) == 'MMMCMXCIX'
````
**Precondition:**
````
0 < number < 4000
````
**How it is used:**

This is an educational task that allows you to explore different numbering systems. Since roman numerals are often used in the typography, it can alternatively be used for text generation. The year of construction on building faces and cornerstones is most often written by Roman numerals. These numerals have many other uses in the modern world and you read about it [here...](http://en.wikipedia.org/wiki/Roman_numerals#Modern_usage) Or maybe you will have a customer from Ancient Rome ;-)

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

--------------
### Verify Anagrams

An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once. Two words are anagrams to each other if we can get one from another by rearranging the letters. Anagrams are case-insensitive and don't take whitespaces into account.

For example: "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not.

You are given two words or phrases. Try to verify if they are anagrams.

**Input:** Two arguments. Words as strings.

**Output:** Determination if the passwords are anagrams or not as boolean (True or False).

**Example:**
````
verify_anagrams("Programming", "Gram Ring Mop") == True
verify_anagrams("Hello", "Ole Oh") == False
verify_anagrams("Kyoto", "Tokyo") == True
````
**Precondition:**
````
0 < |first_word| < 100

0 < |second_word| < 100
````
Words contain only ASCII latin letters and whitespaces.

**How it is used:**

Anagramming can be a fun way to train your brain, but they have other applications. Psychologists use anagram-oriented tests, often called "anagram solution tasks", to assess the implicit memory. Anagrams are often used to create pseudonyms, allowing one to conceal, reveal or operate somewhere in between - like a mask that can establish identity. In addition to this, multiple anagramming is a technique sometimes used to solve some kinds of cryptograms.

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

--------------------
### Probably Dice

Typically, when using multiple dice, you simply roll them and sum up all the result. To get started with your investigation of dice probability, write a function that takes the number of dice, the number of sides per die and a target number and returns the probability of getting a total roll of exactly the target value. The result should be given with four digits precision as ±0.0001. For example, if you roll 2 six-sided dice, the probability of getting exactly a 3 is 2/36 or 5.56%, which you should return as ≈0.0556.

For each test, assume all the dice are the same and are numbered from 1 to the number of sides, inclusive. So a 4-sided die (D4) would have an equal chance of rolling a 1, 2, 3 or 4. A 20-sided die (D20) would have an equal chance of rolling any number from 1 to 20.

**Tips:** Be careful if you want to use a brute-force solution -- you could have a very, very long wait for edge cases.

**Input:** Three arguments. The number of dice, the number of sides per die and the target number as integers.

**Output:** The probability of getting exactly target number on a single roll of the given dice as a float.

**Example:**
````
probability(2, 6, 3) == 0.0556  # 2 six-sided dice have a 5.56% chance of totalling 3
probability(2, 6, 4) == 0.0833
probability(2, 6, 7) == 0.1667
probability(2, 3, 5) == 0.2222  # 2 three-sided dice have a 22.22% chance of totalling 5
probability(2, 3, 7) == 0       # The maximum you can roll on 2 three-sided dice is 6
probability(3, 6, 7) == 0.0694
probability(10, 10, 50) == 0.0375
````
**Precondition:**
````
1 ≤ dice_number ≤ 10

2 ≤ sides ≤ 20

0 ≤ target < 1000
````

**How it is used:**

This task illustrates basic probability. Many events can be described as the combination of other events. In this case you're combining several dice into one total to crit the Orc King for massive damage.

------------------------
### Mona Captcha

The Robots use monospaced fonts with low resolution. You can see the font on the picture below. This font has noise immunity to one-pixel error.

Your program should read the number shown in an image encoded as a binary matrix. Each digit can contain a wrong pixel, but no more than one for each digit. The space between digits is equal to one pixel (just think about "1" which is narrower than other letters, but has a width of 3 pixels).

**Input:** An image as a list of lists with 1 or 0.

**Output:** The number as an integer.

**Example:**
````
recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
     [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394
recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
     [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
     [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394
````
**Precondition:**
````
matrix_rows = 5

5 ≤ matrix_columns < 30

digit_width = 3

digits_space = 1

Each digit contains no more than one wrong pixel.
````
**How it is used:**

This task will show you how optical character recognition works and will familiarize you with low-resolution fonts requiring noise-immunity. This can be useful for the systems that required the reliability.

-----------------------
### Crystal Lattice

With the linear and slice scans completed, we are now ready to check the crystals with a 3D scanner. For this, we'll start with a cubic sample of the crystal and check the adjacent atoms, much like in the previous scans. This crystal type contains two atoms composed of the elements "X" (Xenatom) and "Z" (Zorium). In a well grown crystal, these atoms should alternate down each of the three axis.

You are given a sample crystal as a 3D array of atoms. Well formed crystals will have atoms alternating along the X, Y and Z axis (height, width, depth). If any atoms are found next to the same type of atom, then this crystal is unusable.

**Input:** Crystal cube as a list of lists of lists of strings.

**Output:** The crystal quality as a boolean.

**Example:**
````
golf([[["X", "Z"],
     ["Z", "X"]],
    [["Z", "X"],
     ["X", "Z"]]]) == True
golf([[
     ["X", "Z"],
     ["Z", "X"]],
    [["X", "Z"],
     ["Z", "X"]]]) == False
````
**Precondition:**
````
1 < |cube| ≤ 5
````
All slices are rectangular and have the same size.

cube can contain only "X" or "Z".

**Scoring:**

In this mission the main goal is to make your code as short as possible. The shorter your code, the more points you earn. Your score for this mission is dynamic and directly related to the length of your code.

Scoring in this mission is based on the number of characters used in your code (comment lines are not counted).

**Rank1:**

Any code length.

**Rank2:**

Your code should be shorter than 300 characters.

**Rank3:**

Your code should be shorter than 200 characters.

**How it is used:**

This mission can show you work with more deep structures, which can not be easily drawn in notebook.

---------------------
### Pattern Recognition

In our computer, a slice image and pattern can be represented as a binary matrix, where the main atoms (X and Z) are represented with 1 and 0. You should write a program to search a binary matrix (pattern) within another binary matrix (image). The recognition process consists of scanning the image matrix row by row (horizontal scanning) and marking patterns when one is located in the image. To mark a located pattern, the program must change 1 to 3 and 0 to 2. The result will be the image matrix with the located patterns marked.

The patterns in the image matrix will never cross because the value of each number in the pattern is immediately changed when marked.
````
Pattern     Image

  1 0       0 1 0 1 0
  1 1       0 1 1 0 0
            1 0 1 1 0
            1 1 0 1 1
            0 1 1 0 0

   1st         2nd         3rd
0 3 2 1 0   0 3 2 1 0   0 3 2 1 0
0 3 3 0 0   0 3 3 0 0   0 3 3 0 0
1 0 1 1 0   3 2 1 1 0   3 2 1 3 2
1 1 0 1 1   3 3 0 1 1   3 3 0 3 3
0 1 1 0 0   0 1 1 0 0   0 1 1 0 0
````

**Input:** Two arguments. A pattern as a list of lists and an image as a list of lists.

**Output:** The marked image as a matrix as a list of lists.

**Example:**
````
mark_patterns([[1, 0], [1, 1]],
              [[0, 1, 0, 1, 0],
               [0, 1, 1, 0, 0],
               [1, 0, 1, 1, 0],
               [1, 1, 0, 1, 1],
               [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                                     [0, 3, 3, 0, 0],
                                     [3, 2, 1, 3, 2],
                                     [3, 3, 0, 3, 3],
                                     [0, 1, 1, 0, 0]]
mark_patterns([[1, 1], [1, 1]],
              [[1, 1, 1],
               [1, 1, 1],
               [1, 1, 1]]) == [[3, 3, 1],
                               [3, 3, 1],
                               [1, 1, 1]]
````
**Precondition:**
````
0 < |image| ≤ 10

0 < |pattern| < |image| ≤ 10
````

pattern and image are rectangular.

**How it is used:**

As we can see in the first paragraph, this task is simple monochromatic pattern recognition. You can take a monochrome image and find various sub-images inside, such as the alien spaceships in the Galaxy Game.

-----------
### Morse Clock

You will create a module for converting a normal time string to a morse time string. As you can see in the illustration, a gray circle means on, while a white circle means off. Every digit in the time string contains a different number of slots. The first digit for the hours has a length of 2 while the second digit for the hour has a length of 4. The first digits for the minutes and seconds have a length of 3 while the second digits for the minutes and seconds have a length of 4. Every digit in the time is converted to binary representation. You will convert every "on" (or 1) signal to dash ("-") and every "off" (or 0) signal to dot (".").

A time string can be in any of the following formats: *"hh:mm:ss"*, *"h:m:s"* or *"hh:m:ss"*. The "missing" digits are zeroes. For example, "1:2:3" is the same as "01:02:03".

The result will be a morse time string with specific format:
````
h h : m m : s s
````
where each digits is represented as sequence of "." and "-" (dots and dashes).

**Input:** A normal time string as a string.

**Output:** The morse time string as a string.

**Example:**
````
morse_time("10:37:49") == ".- .... : .-- .--- : -.. -..-"
morse_time("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
morse_time("00:1:02") == ".. .... : ... ...- : ... ..-."
morse_time("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"
````
**Precondition:**

`time` string contains correct time.

**How it is used:**

Did you play the binary clocks mission earlier? This can be the basis for a fun gift for any geek. Now we've remixed the binary clock idea with Morse Code. Now you can create an even more complex binary clock, one which doesn't just tell time -- but makes morse style bips and beeps. ;-)

-----------
### Pangram

For this mission, we will use the latin alphabet (A-Z). You are given a text with latin letters and punctuation symbols. You need to check if the sentence is a pangram or not. Case does not matter.

**Input:** A text as a string.

**Output:** Whether the sentence is a pangram or not as a boolean.

**Example:**
````
check_pangram("The quick brown fox jumps over the lazy dog.") == True
check_pangram("ABCDEF.") == False
````
**Precondition:**

Input text can contain only ASCII letters, whitespaces and punctuation symbols.
````
0 < |text|
````
**How it is used:**

Pangrams have been used to display typefaces, test equipment, and develop skills in handwriting, calligraphy, and keyboarding for ages.

------------
### Xs and Os Referee

Think back to the game Tic-Tac-Toe, sometimes also known as Xs and Os. This is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".
````
 X | . | O 
-*-|---|---
 X | X | .   X Wins
-*-|---|---
 X | O | O

 O | O | . 
---|-*-|---
 X | O | X   O Wins
---|-*-|---
 X | O | . 
 
 O | O | X 
---|---|---
 X | X | O   Draw
---|---|---
 O | X | X
 ````
A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

**Input:** A game result as a list of strings (unicode).

**Output:** "X", "O" or "D" as a string.

**Example:**
````
xo_referee([
    "X.O",
    "XX.",
    "XOO"]) == "X"
xo_referee([
    "OO.",
    "XOX",
    "XOX"]) == "O"
xo_referee([
    "OOX",
    "XXO",
    "OXX"]) == "D"
````
**Precondition:**
````
len(game_result) == 3
all(len(row) == 3 for row in game_result)
````
There is either one winner or a draw.

**Optional Goals**

**Rank 2:** There is possible a game state when both players "wins" (Last chance game). This case is a draw -- "D". For example:
````
XXX
...
OOO
````
**Rank 3:** A grid can be 4 by 4 cells. As early player should place three consecutive marks in rows. For example "XX.X" is not win, but ".XXX" is.

**How it is used:**

The concepts in this task will help you when iterating data types. They can also be used in game algorithms, allowing you to know how to check results.

------------
### Spheroid Bullet

We know the height and the width (in centimeters) for this spheroid. You should create a function to calculate the volume (cubic centimeters) and the surface area (square centimeters). **The results should be rounded to two decimals.**

**Tips:** Be careful with sin-1x -- this is arcsin.

**Input:** Two arguments. A height and a width as integers.

**Output:** The volume and the surface area as a list/tuple of floats.

**Example:**
````
golf(4, 2) == [8.38, 21.48] # or (8.38, 21.48)
golf(2, 2) == [4.19, 12.57]
golf(2, 4) == [16.76, 34.69]
````
**Precondition:**
````
0 < width < 100

0 < height < 100
````
**Scoring:**

Scoring in this mission is based on the number of characters used in your code (comment lines are not counted).

**Rank1:**

Any code length.

**Rank2:**

Your code should be shorter than 250 characters.

**Rank3:**

Your code should be shorter than 150 characters.

**How it is used:**

This is a simple math task, but we want to introduce you to the ubiquitous spheroid.

For example, the prolate spheroid is the shape of the ball in several sports such as in rugby and Australian football. In American football, a more pointed prolate spheroid is used. Several moons of the Solar system approximate prolate spheroids in shape, though they are actually scalene. Examples of these are Mimas, Enceladus, and Tethys which orbit Saturn and Miranda which orbits Uranus.

Even the true shape of the Earth is an Oblate Spheroid, though it is only very slightly oblate. The diameter from the North Pole to the South Pole (the shortest diameter) is approximately 12,714 km. The equatorial diameter (the longest diameter) is approximately 12,756 km. This is not a big difference, but it does mean the Earth is not quite a sphere.

------------
### Transpose Matrix

In linear algebra, the transpose of a matrix **A** is another matrix **A**<sup>T</sup> (also written **A**′, **A**<sup>tr</sup>,<sup>t</sup>**A** or **A**<sup>t</sup>) created by any one of the following equivalent actions:

- reflect **A** over its main diagonal (which runs from top-left to bottom-right) to obtain **A**<sup>T</sup>
- write the rows of **A** as the columns of **A**<sup>T</sup>
- write the columns of **A** as the rows of **A**<sup>T</sup>

Formally, the *i* row, *j* column element of **A**<sup>T</sup> is the *j* row, *i* column element of **A**:

[**A**<sup>TL</sup>]<sub>i j</sub> = [**A**]<sub>j i</sub>

If **A** is an `m × n` matrix then **A**<sup>T</sup> is an `n × m` matrix.

You have been given a matrix as a 2D list with integers. Your task is to return a transposed matrix based on input.

````
|1 2 3|   |1 4 7|
|4 5 6| T |2 5 8|
|7 8 9|   |3 6 9|

|1 4 3|
|8 2 6|   |1 8 7 4 7|
|7 8 3| T |4 2 8 9 8|
|4 6 9|   |3 6 3 6 1|
|7 8 1|
````

**Input:** A matrix as a list of lists with integers.

**Output:** The transposed matrix as a list of lists with integers.

**Example:**
````
transpose([[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]) == [[1, 4, 7],
                     [2, 5, 8],
                     [3, 6, 9]]
transpose([[1, 4, 3],
     [8, 2, 6],
     [7, 8, 3],
     [4, 9, 6],
     [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                     [4, 2, 8, 9, 8],
                     [3, 6, 3, 6, 1]]
````

**Precondition:**
````
0 < |matrix| < 10

∀ row ∈ matrix: 0 < |row| < 10
````

**How it is used:**

The most obvious use for this idea is in mathematical software, but the concept can be applied in the area of vector graphics. On a computer, one can often avoid explicitly transposing a matrix in memory by simply accessing the same data in a different order.

-----------------
### Weak Point

The durability map is represented as a matrix with digits. Each number is the durability measurement for the cell. To find the weakest point we should find the weakest row and column. The weakest point is placed in the intersection of these rows and columns. Row (column) durability is a sum of cell durability in that row (column). You should find coordinates of the weakest point (row, column). The first row (column) is 0th row (column). If a section has several equal weak points, then choose the top left point.
````
    20  30  22  19  25
  |---|---|---|-*-|---|
27| 7 | 2 | 7 | 3 | 8 |
  |---|---|---|-*-|---|
23| 2 | 9 | 4 | 1 | 7 |
  |---|---|---|-*-|---|
23| 3 | 8 | 6 | 2 | 4 |
  |---|---|---|-*-|---|
19* 2 * 5 * 2 **9** 1 *
  |---|---|---|-*-|---|
26| 6 | 6 | 5 | 4 | 5 |
  |---|---|---|-*-|---|
  
  Weak point (3, 3)

    20  29  19  19  25
  |---|---|-*-|-*-|---|
27| 7 | 2 | 7 | 3 | 8 |
  |---|---|-*-|-*-|---|
19* 2 * 8 **1** 1 * 7 *
  |---|---|-*-|-*-|---|
23| 3 | 8 | 6 | 2 | 4 |
  |---|---|-*-|-*-|---|
19* 2 * 5 * 2 * 9 * 1 *
  |---|---|-*-|-*-|---|
26| 6 | 6 | 5 | 4 | 5 |
  |---|---|-*-|-*-|---|

  Weak point (1, 2)
````
**Input:** A durability map as a list of lists with integers.

**Output:** The coordinates of the weak point as a list (tuple) of integers.

**Example:**
````
golf([[7, 2, 7, 2, 8],
      [2, 9, 4, 1, 7],
      [3, 8, 6, 2, 4],
      [2, 5, 2, 9, 1],
      [6, 6, 5, 4, 5]]) == [3, 3]
golf([[7, 2, 4, 2, 8],
      [2, 8, 1, 1, 7],
      [3, 8, 6, 2, 4],
      [2, 5, 2, 9, 1],
      [6, 6, 5, 4, 5]]) == [1, 2]
````
**Precondition:**
````
0 < len(matrix) <= 10
all(len(row) == len(matrix) for row in matrix)
all(all(0 < x < 10 for x in row) for row in matrix)
````
**Scoring:**

In this mission the main goal to make your code as short as possible. The shorter your code, the more points you earn. Your score for this mission is dynamic and directly related to the length of your code.

Scoring in this mission is based on the number of characters used in your code (comment lines are not counted).

**Rank1:**

Any code length.

**Rank2:**

Your code should be shorter than 175 characters.

**Rank3:**

Your code should be shorter than 125 characters.

**How it is used:**

Matrices (2D array) are an often used data structure and it will be helpful to sharpen your skills with them.