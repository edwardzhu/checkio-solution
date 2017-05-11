### Rotate List

Write a function that rotates a list by k elements. For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2]. Try solving this without creating a copy of the list.

**Input:** Two arguments. List of elements and positive integer

**Output:** Converter list of elements

**Example:**
````
rotate_list([1, 2, 3, 4, 5, 6], 2) === [3, 4, 5, 6, 1, 2]
rotate_list([1, 2, 3, 4, 5, 6], 3) === [4, 5, 6, 1, 2, 3]
````

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

-------------
### Skew Symmetry

In mathematics, particularly in linear algebra, a skew-symmetric matrix(also known as an antisymmetric or antimetric) is a square matrix **A** whose transpose is also its negative. This means it satisfies the equation A=-A<sup>T</sup>. If the entry in the i-th row and j-th column is a<sub>ij</sub>, i.e. A=(a<sub>ij</sub>) then the symmetric condition becomes a<sub>ij</sub>=-a<sub>ji</sub>.

You should determine whether the specified square matrix is skew-symmetric or not.

You can find more details on Skew-symmetric matrices on its [Wikipedia page](https://en.wikipedia.org/wiki/Skew-symmetric_matrix)

**Input:** A square matrix as a list of lists with integers.

**Output:** If the matrix is skew-symmetric or not as a boolean.

**Example:**
````
is_skew_symmetric([
    [ 0,  1,  2],
    [-1,  0,  1],
    [-2, -1,  0]]) == True
is_skew_symmetric([
    [ 0,  1, 2],
    [-1,  1, 1],
    [-2, -1, 0]]) == False
is_skew_symmetric([
    [ 0,  1, 2],
    [-1,  0, 1],
    [-3, -1, 0]]) == False
````
**Precondition:**

A `matrix` is square and non-empty.

**How it is used:**

Skew-symmetric matrices can be useful for the cross product, an operation in mathematics used in the calculation of movement of forces. Matrixes are basis for the linear algebra and vector graphics.

-----------
### Pawn Brotherhood

Chess is a two-player strategy game played on a square checkered game board laid out in eight rows called ranks which are denoted with numbers 1 to 8, and eight columns called files and denoted with letters a to h. Each square of the chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", "d6"). To train the snipers, we only need to concern ourselves with pawns for now. A pawn may capture an opponent's piece on a square diagonally in front of it on an adjacent file, by moving to that square. For white pawns the front squares are squares with greater row than their.

A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square. We have several white pawns on the chess board and only white pawns. You should design your code to find how many pawns are safe.
````
S - Safe pawn
U - Unsafe pawn

   |---|---|---|---|---|---|---|---|
8  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
7  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
6  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
5  |   |   |   |   |   |   | S |   |
   |---|---|---|---|---|---|---|---|
4  |   | S |   | S |   | S |   |   |
   |---|---|---|---|---|---|---|---|
3  |   |   | S |   | S |   |   |   |
   |---|---|---|---|---|---|---|---|
2  |   |   |   | U |   |   |   |   |
   |---|---|---|---|---|---|---|---|
1  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
     a   b   c   d   e   f   g   h


   |---|---|---|---|---|---|---|---|
8  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
7  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
6  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
5  |   |   |   |   | S |   |   |   |
   |---|---|---|---|---|---|---|---|
4  |   | U | U | U | U | U | U |   |
   |---|---|---|---|---|---|---|---|
3  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
2  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
1  |   |   |   |   |   |   |   |   |
   |---|---|---|---|---|---|---|---|
     a   b   c   d   e   f   g   h
````

**Input:** Placed pawns coordinates as a set of strings.

**Output:** The number of safe pawns as an integer.

**Example:**
````
safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
````
**Precondition:**
````
0 < |pawns| ≤ 8
````
**How it is used:**

For game AI, the the important task is the ability to understand the game state. This mission will show how you can do this using simple chess figure positions.

--------------
### Determinant

In linear algebra, the [determinant](https://en.wikipedia.org/wiki/Determinant) is a value associated with a square matrix. It can be computed from the entries of the matrix by a specific arithmetic expression (There are other ways to determine its value as well.)

The determinant of a matrix **A** is denoted **det(A)**, **det A**, or **|A|**. In the case where the matrix entries are written out in full, the determinant is denoted by surrounding the matrix entries by vertical bars instead of the brackets or parentheses of the matrix.

There are various ways to define the determinant of a square matrix **A**, i.e. one with the same number of rows and columns. Perhaps the most natural way is expressed in terms of the columns of the matrix. If we write an **N×N** matrix in terms of its column vectors:

A = \[a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>\]

Where there are vectors of size n, then the determinant of A is defined so that:

det\[a<sub>1</sub>, ..., ba<sub>j</sub>+cv, ..., a<sub>n</sub>\] = b*det(A)*+*c*det\[a<sub>1</sub>, ..., v, ..., a<sub>n</sub>\]

det\[a<sub>1</sub>, ..., a<sub>j</sub>, a<sub>j+1</sub>, ..., a<sub>n</sub>] = -det\[a<sub>1</sub>, ..., a<sub>j+1</sub>, a<sub>j</sub>, ..., a<sub>n</sub>\]

det(I) = 1

Where **b** and **c** are scalars, **v** is any vector of size **N** and **I** is the identity matrix of size **N**. These properties state that the determinant is an alternating multilinear function of the columns, and they suffice to uniquely calculate the determinant of any square matrix. Provided the underlying scalars form a field (more generally, a commutative ring with unity). Equivalently, the determinant can be expressed as a sum of products of entries of the matrix where each product has **N** terms and the coefficient of each product is −1 or 1 or 0 according to a given rule: it is a polynomial expression of the matrix entries. This expression grows rapidly with the size of the matrix (an **NxN** matrix contributes **N!** terms), so it will first be given explicitly for the case of 2×2 matrices and 3×3 matrices, followed by the rule for arbitrary size matrices, which subsumes these two cases.

**Input:** A square matrix as a list of lists with integers.

**Output:** The determinant of the matrix as an integer.

**Example:**
````
golf([[4,3], [6,3]]) == -6
golf([[1, 3, 2],
      [1, 1, 4],
      [2, 2, 1]]) == 14
````
**Precondition:**
````
0 < |matrix| ≤ 5
````
A matrix is square.

**Scoring:**

In this mission the main goal to make your code as short as possible. The shorter your code, the more points you earn. Your score for this mission is dynamic and directly related to the length of your code.

Scoring in this mission is based on the number of characters used in your code (comment lines are not counted).

**Rank1:**

Any code length.

**Rank2:**

Your code should be shorter than 350 characters.

**Rank3:**

Your code should be shorter than 250 characters.

**How it is used:**

The determinant is a basis for linear algebra and mathematical software. Linear algebra is used in vector graphics to calculate line paths and shapes. It can also be of use for many optimisation problems along with cryptography (videocipher) and geometry (testing for collinear points).

-----------
### Number Factory

For this mission, you are given the number **N** (which will be comprised of at least two digits). You must work to find the smallest positive number of **X** such that the product of its digits is equal to N. If X does not exist, then you should return 0.

Let's look at an example. N = 20. We can factorize this number as 2\*10, but 10 is not a digit. Also we can factorize it as 4\*5 or 2\*2\*5. The smallest number for 2\*2\*5 is 225, for 4\*5 -- 45. So we select 45.

**Input:** The number N as an integer.

**Output:** The number X as an integer.

**Example:**
````
reconstruct(20) == 45
reconstruct(21) == 37
reconstruct(17) == 0
reconstruct(33) == 0
````
**Precondition:**
````
9 < number < 100000
````
**How it is used:**

This task will teach you how to work with numbers and simple math in code, teaching you to factorize numbers and reconstruct them into new numbers. Of course you could try to solve this problem with brute force, but is that the best way? Numbers are the foundation of mathematics and programming and you would do well to remember this.