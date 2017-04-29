### Count Neighbours

You are given a state for a rectangular board game grid with chips in a binary matrix, where 1 is a cell with an enemy and 0 is an empty cell. You are also given the coordinates for a cell in the form of row and column numbers (starting from 0). You should determine how many enemies are close to this cell. Every cell interacts with its eight neighbours; those cells that are horizontally, vertically, or diagonally adjacent.
````
|-----|-----|-----|-----|-----|
|     |. . .|. . .|. . .|     |
|  X  |.   .|. X .|.   .|     |
|     |. . .|. . .|. . .|     |
|-----|-----|-----|-----|-----|
|     |. . .|* * *|. . .|     |
|     |. X .|*   *|.   .|     |
|     |. . .|* * *|. . .|     |
|-----|-----|-----|-----|-----|
|     |. . .|. . .|. . .|     |
|     |.   .|. X .|.   .|  X  |
|     |. . .|. . .|. . .|     |
|-----|-----|-----|-----|-----|
|     |     |     |     |     |
|  X  |     |     |     |     |
|     |     |     |     |     |
|-----|-----|-----|-----|-----|
|     |     |     |     |     |
|     |     |  X  |     |     |
|     |     |     |     |     |
|-----|-----|-----|-----|-----|


|-----|-----|-----|-----|-----|
|* * *|. . .|     |     |     |
|* X *|.   .|  X  |     |     |
|* * *|. . .|     |     |     |
|-----|-----|-----|-----|-----|
|. . .|. . .|     |     |     |
|.   .|. X .|     |     |     |
|. . .|. . .|     |     |     |
|-----|-----|-----|-----|-----|
|     |     |     |     |     |
|     |     |  X  |     |  X  |
|     |     |     |     |     |
|-----|-----|-----|-----|-----|
|     |     |     |     |     |
|  X  |     |     |     |     |
|     |     |     |     |     |
|-----|-----|-----|-----|-----|
|     |     |     |     |     |
|     |     |  X  |     |     |
|     |     |     |     |     |
|-----|-----|-----|-----|-----|
````
For the given examples (see the schema) there is the same grid:
````
((1, 0, 1, 0, 0),
 (0, 1, 0, 0, 0),
 (0, 0, 1, 0, 1),
 (1, 0, 0, 0, 0),
 (0, 0, 1, 0, 0),)
````
For the first example, the coordinates of the cell are (1, 2) and as we can see from the schema this cell has 3 neighbour enemies. For the second example the coordinates are (0, 0) and this cell contains an enemy, but we are only counting the neighbours so the answer is 1.

**Input:** Three arguments. A grid as a tuple of tuples with integers (1/0), a row number and column number for a cell as integers.

**Output:** How many neighbouring cells have chips as an integer.

**Example:**
````
count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 1, 2) == 3
count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 0, 0) == 1
````
**Precondition:**
````
3 ≤ |grid| ≤ 10

∀ row ∈ grid: |grid[0]| = |row|
````
**How it is used:**

This idea can be useful for developing board game algorithms. In addition, the same principles it can be useful for navigational software, or geographical surveying software or even basic cellular reproduction.

------------------
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