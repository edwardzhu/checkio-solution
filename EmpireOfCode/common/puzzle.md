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