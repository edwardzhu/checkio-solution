### Exchange Symbols

Given a string, return a new string where the first and last chars have been exchanged.

**Input:** String.

**Output:** Changed string.

**Example:**
````
sym_exchange("az") === "za"
sym_exchange("aiiiiiz") === "ziiiiia"
sym_exchange("length") === "hengtl"
````

-------------------------------
### Count Inversion

In computer science and discrete mathematics, an [inversion](https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics)) is a pair of places in a sequence where the elements in these places are out of their natural order. So, if we use ascending order for a group of numbers, then an inversion is when the order is reversed and larger numbers appear before lower number in a sequence.

Check out this example sequence: (1, 2, 5, 3, 4, 7, 6) and we can see here three inversions:

- 5 and 3;
- 5 and 4; 
- 7 and 6.

You are given a sequence of unique numbers and you should count the number of inversions in this sequence.

**Input:** A sequence as a tuple of integers.

**Output:** The inversion number as an integer.

**Example:**
````
count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3
count_inversion((0, 1, 2, 3)) == 0
````
**Precondition:**
````
2 < |sequence| < 200
All elements of a sequence are unique.
````

**How it is used:**

In this mission you will experience the wonder of nested loops, that is of course supposing you don't use advanced algorithms or black magic.
