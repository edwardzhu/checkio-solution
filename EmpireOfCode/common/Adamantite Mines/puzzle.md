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