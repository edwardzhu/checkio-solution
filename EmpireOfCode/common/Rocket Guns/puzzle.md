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

-------------------
### Find Sequence

You are given a matrix of NxN. You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

````
*1*| 2 | 1 | 1 
---|---|---|---
*1*| 1 | 4 | 1 
---|---|---|---  True
*1*| 3 | 1 | 6 
---|---|---|---
*1*| 7 | 2 | 5 

 7 | 1 | 4 | 1 
---|---|---|---
 1 | 2 | 5 | 2 
---|---|---|---  False
 3 | 4 | 1 | 3 
---|---|---|---
 1 | 1 | 8 | 1 
 
 2 | 1 | 1 | 6 | 1  
---|---|---|---|---
 1 | 3 | 2 | 1 | 1
---|---|---|---|---
 4 | 1 | 1 | 3 | 1   True
---|---|---|---|---
*5*|*5*|*5*|*5*|*5*
---|---|---|---|---
 1 | 1 | 3 | 1 | 1 

 7 | 1 | 1 | 8 | 1 | 1 
---|---|---|---|---|---
 1 | 1 | 7 | 3 | 1 |*5* 
---|---|---|---|---|---
 2 | 3 | 1 | 2 |*5*| 1 
---|---|---|---|---|---  True
 1 | 1 | 1 |*5*| 1 | 4 
---|---|---|---|---|---
 4 | 6 |*5*| 1 | 3 | 1 
---|---|---|---|---|---
 1 | 1 | 9 | 1 | 2 | 1
```` 

**Input:** A matrix as a list of lists with integers.

**Output:** Whether or not a sequence exists as a boolean.

**Example:**
````
has_sequence([
    [1, 2, 1, 1],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5]
]) == True
has_sequence([
    [7, 1, 4, 1],
    [1, 2, 5, 2],
    [3, 4, 1, 3],
    [1, 1, 8, 1]
]) == False
has_sequence([
    [2, 1, 1, 6, 1],
    [1, 3, 2, 1, 1],
    [4, 1, 1, 3, 1],
    [5, 5, 5, 5, 5],
    [1, 1, 3, 1, 1]
]) == True
has_sequence([
    [7, 1, 1, 8, 1, 1],
    [1, 1, 7, 3, 1, 5],
    [2, 3, 1, 2, 5, 1],
    [1, 1, 1, 5, 1, 4],
    [4, 6, 5, 1, 3, 1],
    [1, 1, 9, 1, 2, 1]
    ]) == True
````
**Precondition:**
````
0 ≤ |matrix| ≤ 10
````
A `matrix` is a rectangular.

**How it is used:**

This concept is useful for basic pattern recognition, and in games where you need to detect various lines similar elements (match 3 games for example).

