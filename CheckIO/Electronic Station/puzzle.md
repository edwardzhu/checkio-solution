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