### Non-unique Elements
You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the non-unique elements in this list. To do so you will need to remove all unique elements (elements which are contained in a given list only once). When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].

**Input:** A list of integers.

**Output:** The list of integers.

**Example:**
````
checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
checkio([1, 2, 3, 4, 5]) == []
checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
````

**How it is used:** 

This mission will help you to understand how to manipulate arrays, something that is the basis for solving more complex tasks. The concept can be easily generalized for real world tasks. For example: if you need to clarify statistics by removing low frequency elements (noise).

**Precondition:**

0 < len(data) < 1000

----------------------------------------------------
### Roman Numerals
Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which are combined to signify the sum (or, in some cases, the difference) of their values. The first ten Roman numerals are:

I, II, III, IV, V, VI, VII, VIII, IX, and X.

The Roman numeral system is decimal based but not directly positional and does not include a zero. Roman numerals are based on combinations of these seven symbols:

- Symbol Value
- I 1 (unus)
- V 5 (quinque)
- X 10 (decem)
- L 50 (quinquaginta)
- C 100 (centum)
- D 500 (quingenti)
- M 1,000 (mille)

More additional information about roman numerals can be found on [the Wikipedia article](https://en.wikipedia.org/wiki/Roman_numerals).

For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.

**Input:** A number as an integer.

**Output:** The Roman numeral as a string.

**Example:**

````
checkio(6) == 'VI'
checkio(76) == 'LXXVI'
checkio(13) == 'XIII'
checkio(44) == 'XLIV'
checkio(3999) == 'MMMCMXCIX'
````

**How it is used:** This is an educational task that allows you to explore different numbering systems. Since roman numerals are often used in the typography, it can alternatively be used for text generation. The year of construction on building faces and cornerstones is most often written by Roman numerals. These numerals have many other uses in the modern world and you read about it here... Or maybe you will have a customer from Ancient Rome ;-)

**Precondition:** 0 < number < 4000

--------------------------------------------
### Open Labyrinth
The labyrinth has no walls, but bushes surround the path on each side. If a players move into a bush, they lose. The labyrinth is presented as a matrix (a list of lists): 1 is a bush and 0 is part of the path. The labyrinth's size is 12 x 12 and the outer cells are also bushes. Players start at cell (1,1). The exit is at cell (10,10). You need to find a route through the labyrinth. Players can move in only four directions--South (down [1,0]), North (up [-1,0]), East (right [0,1]), West (left [0, -1]). The route is described as a string consisting of different characters: "S"=South, "N"=North, "E"=East, and "W"=West.

**Input:** A labyrinth map as a list of lists with 1 and 0.

**Output:** The route as a string that contains "W", "E", "N" and "S".

**Example:**
````
checkio([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
````
**How it is used:** This is a classical problem for path-finding in graphs -- Yes, the maze can be represented as a graph. It can be used in navigation software for a to b navigation and computer games for artificial intelligence. You can find your way anywhere you wish. Just divide a map into square cells and mark up the "bad" cells.

**Precondition:** Outer cells are pits.
````
len(labyrinth) == 12
all(len(row) == 12 for row in labyrinth)
````
---------------------------------------------
### Cipher map
A cipher grille is a 4×4 square of paper with four windows cut out. Placing the grille on a paper sheet of the same size, the encoder writes down the first four symbols of his password inside the windows (see fig. below). After that, the encoder turns the grille 90 degrees clockwise. The symbols written earlier become hidden under the grille and clean paper appears inside the windows. The encoder then writes down the next four symbols of the password in the windows and turns the grille 90 degrees again. Then, they write down the following four symbols and turns the grille once more. Lastly, they write down the final four symbols of the password. Without the same cipher grille, it is difficult to discern the password from the resulting square comprised of 16 symbols. Thus, the encoder can be confident that no hooligan will easily gain access to the locked door.
Write a module that enables the robots to easily recall their passwords through codes when they return home.

The cipher grille and the ciphered password are represented as an array (tuple) of strings.

**Input:** A cipher grille and a ciphered password as a tuples of strings.

**Output:** The password as a string.

**Example:**
````
recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi')) == 'icantforgetiddqd'
​
recall_password(
    ('....',
     'X..X',
     '.X..',
     '...X'),
    ('xhwc',
     'rsqx',
     'xqzz',
     'fyzr')) == 'rxqrwsfzxqxzhczy'
````

**How it is used:** Here you can learn how to work with 2D arrays. You also get to learn about the ancient Grille Cipher, a technique of encoding messages which has been used for half a millenium. The earliest known description of the grille cipher comes from the Italian mathematician, Girolamo Cardano in 1550.

**Precondition:**
````
len(cipher_grille) == 4
len(ciphered_password) == 4
all(len(row) == 4 for row in ciphered_password)
all(len(row) == 4 for row in cipher_grille)
all(all(ch in string.ascii_lowercase for ch in row) for row in ciphered_password)
all(all(ch == "X" or ch == "." for ch in row) for row in cipher_grille)
````
-------------------------------------------
### Pawn Brotherhood
Almost everyone in the world knows about the ancient game [Chess](https://en.wikipedia.org/wiki/Chess) and has at least a basic understanding of its rules. It has various units with a wide range of movement patterns allowing for a huge number of possible different game positions (for example [Number of possible chess games at the end of the n-th plies](http://oeis.org/A048987).) For this mission, we will examine the movements and behavior of chess pawns.

Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and denoted with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. Each square of the chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", "d6"). For this mission we only need to concern ourselves with pawns. A pawn may capture an opponent's piece on a square diagonally in front of it on an adjacent file, by moving to that square. For white pawns the front squares are squares with greater row than their.

A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square. We have several white pawns on the chess board and only white pawns. You should design your code to find how many pawns are safe.

You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

**Input:** Placed pawns coordinates as a set of strings.

**Output:** The number of safe pawns as a integer.

**Example:**
````
safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
````

**How it is used:** For a game AI one of the important tasks is the ability to estimate game state. This concept will show how you can do this on the simple chess figures positions.

**Precondition:**

0 < pawns ≤ 8

-----------------------------------------
### Min and Max
In this mission you should write you own py3 implementation (but you can use py2 for this) of the built-in functions **min** and **max**. Some builtin functions are closed here: *import, eval, exec, globals*. Don't forget you should implement two functions in your code.

**max(iterable, \*[, key]) or min(iterable, \*[, key])**

**max(arg1, arg2, \*args[, key]) or min(arg1, arg2, \*args[, key])**

>Return the largest (smallest) item in an iterable or the largest(smallest) of two or more arguments.
>
>If one positional argument is provided, it should be an iterable. The largest (smallest) item in the iterable is returned. If two or more positional arguments are provided, the largest (smallest) of the positional arguments is returned.
>
>The optional keyword-only key argument specifies a function of one argument that is used to extract a comparison key from each list element (for example, key=str.lower).
>
>If multiple items are maximal (minimal), the function returns the first one encountered.
>
>*-- Python Documentation (Built-in Functions)*

**Input:** One positional argument as an iterable or two or more positional arguments. Optional keyword argument as a function.

**Output:** The largest item for the "max" function and the smallest for the "min" function.

**Example:**
````
max(3, 2) == 3
min(3, 2) == 2
max([1, 2, 0, 3, 4]) == 4
min("hello") == "e"
max(2.2, 5.6, 5.9, key=int) == 5.6
min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
````

**How it is used:** This task will help you understand how some of the built-in functions work on a more precise level.

**Precondition:** All test cases are correct and functions don't have to raise exceptions.

------------------------------------------
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

