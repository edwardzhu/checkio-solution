### Brackets
You are given an expression with numbers, brackets and operators. For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]". Brackets are used to determine scope or to restrict some expression. If a bracket is open, then it must be closed with a closing bracket of the same type. The scope of a bracket must not intersected by another bracket. In this task you should make a decision, whether to correct an expression or not based on the brackets. Do not worry about operators and operands.

**Input:** An expression with different of types brackets as a string (unicode).

**Output:** A verdict on the correctness of the expression in boolean (True or False).

**Example:**
````
checkio("((5+3)*2+1)") == True
checkio("{[(3+1)+2]+}") == True
checkio("(3+{1-1)}") == False
checkio("[1+1]+(2*2)-{3/3}") == True
checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
checkio("2+3") == True
````

**How it is used:** When you write code or complex expressions in a mathematical package, you can get a huge headache when it comes to excess or missing brackets. This concept can be useful for your own IDE.

**Precondition:**
````
There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").
0 < len(expression) < 10^3
````

----------------------------------------
### Binary count

For the Robots the decimal format is inconvenient. If they need to count to "1", their computer brains want to count it in the binary representation of that number. You can read more about binary here.

You are given a number (a positive integer). You should convert it to the binary format and count how many unities (1) are in the number spelling. For example: 5 = 0b101 contains two unities, so the answer is 2.

**Input:** A number as a positive integer.

**Output:** The quantity of unities in the binary form as an integer.

**Example:**
````
checkio(4) == 1
checkio(15) == 4
checkio(1) == 1
checkio(1022) == 9
````

**How it is used:** How to convert a number to the binary form. It can be useful for Computer Science purposes.

**Precondition:** 0 < number ≤ 23^2

------------------------------------
### The Hamming Distance

The Hamming distance between two binary integers is the number of bit positions that differs (read more about the Hamming distance on Wikipedia). For example:
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
checkio(117, 17) == 3
checkio(1, 2) == 2
checkio(16, 15) == 5
````

**How it is used:** This is a basis for Hamming code and other linear error-correcting programs. The Hamming distance is used in systematics as a measure of genetic distance. On a grid (ie: a chessboard,) the Hamming distance is the minimum number of moves it would take a rook to move from one cell to the other.

**Precondition:**
````
0 < n < 10^6
0 < m < 10^6
````

-------------------------------------
### Find Sequence

You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

**Input:** A matrix as a list of lists with integers.

**Output:** Whether or not a sequence exists as a boolean.

**Example:**
````
checkio([
    [1, 2, 1, 1],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5]
]) == True
checkio([
    [7, 1, 4, 1],
    [1, 2, 5, 2],
    [3, 4, 1, 3],
    [1, 1, 8, 1]
]) == False
checkio([
    [2, 1, 1, 6, 1],
    [1, 3, 2, 1, 1],
    [4, 1, 1, 3, 1],
    [5, 5, 5, 5, 5],
    [1, 1, 3, 1, 1]
]) == True
checkio([
    [7, 1, 1, 8, 1, 1],
    [1, 1, 7, 3, 1, 5],
    [2, 3, 1, 2, 5, 1],
    [1, 1, 1, 5, 1, 4],
    [4, 6, 5, 1, 3, 1],
    [1, 1, 9, 1, 2, 1]
    ]) == True
````

**How it is used:** This concept is useful for games where you need to detect various lines of the same elements (match 3 games for example). This algorithm can be used for basic pattern recognition.

**Precondition:**
````
0 ≤ len(matrix) ≤ 10
all(all(0 < x < 10 for x in row) for row in matrix)
````

-------------------------
### Restricted sum

Our new calculator is censored and as such it does not accept certain words. You should try to trick by writing a program to calculate the sum of numbers.

Given a list of numbers, you should find the sum of these numbers. Your solution should not contain any of the banned words, even as a part of another word.

The list of banned words are as follows:

* *sum*
* *import*
* *for*
* *while*
* *reduce*

**Input:** A list of numbers.

**Output:** The sum of numbers.

**Example:**
````
checkio([1, 2, 3]) == 6
checkio([2, 2, 2, 2, 2, 2]) == 12
````

**How it is used:** This task challenges your creativity to come up with a solution to fit this mission's specs!

**Precondition:** The small amount of data. Let's creativity win!

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
