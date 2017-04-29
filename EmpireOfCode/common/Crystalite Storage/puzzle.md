### Sure Not

Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

**Input:** String.

**Output:** Changed string.

**Example:**
````
sure_not("sure") === "not sure"
sure_not("not sure") === "not sure"
sure_not("noter") === "not noter"
````

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