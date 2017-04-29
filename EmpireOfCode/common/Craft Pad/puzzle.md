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

-----------
### Morse Clock

You will create a module for converting a normal time string to a morse time string. As you can see in the illustration, a gray circle means on, while a white circle means off. Every digit in the time string contains a different number of slots. The first digit for the hours has a length of 2 while the second digit for the hour has a length of 4. The first digits for the minutes and seconds have a length of 3 while the second digits for the minutes and seconds have a length of 4. Every digit in the time is converted to binary representation. You will convert every "on" (or 1) signal to dash ("-") and every "off" (or 0) signal to dot (".").

A time string can be in any of the following formats: *"hh:mm:ss"*, *"h:m:s"* or *"hh:m:ss"*. The "missing" digits are zeroes. For example, "1:2:3" is the same as "01:02:03".

The result will be a morse time string with specific format:
````
h h : m m : s s
````
where each digits is represented as sequence of "." and "-" (dots and dashes).

**Input:** A normal time string as a string.

**Output:** The morse time string as a string.

**Example:**
````
morse_time("10:37:49") == ".- .... : .-- .--- : -.. -..-"
morse_time("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
morse_time("00:1:02") == ".. .... : ... ...- : ... ..-."
morse_time("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"
````
**Precondition:**

`time` string contains correct time.

**How it is used:**

Did you play the binary clocks mission earlier? This can be the basis for a fun gift for any geek. Now we've remixed the binary clock idea with Morse Code. Now you can create an even more complex binary clock, one which doesn't just tell time -- but makes morse style bips and beeps. ;-)

------------------------
### Mona Captcha

The Robots use monospaced fonts with low resolution. You can see the font on the picture below. This font has noise immunity to one-pixel error.

Your program should read the number shown in an image encoded as a binary matrix. Each digit can contain a wrong pixel, but no more than one for each digit. The space between digits is equal to one pixel (just think about "1" which is narrower than other letters, but has a width of 3 pixels).

**Input:** An image as a list of lists with 1 or 0.

**Output:** The number as an integer.

**Example:**
````
recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
     [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394
recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
     [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
     [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394
````
**Precondition:**
````
matrix_rows = 5

5 ≤ matrix_columns < 30

digit_width = 3

digits_space = 1

Each digit contains no more than one wrong pixel.
````
**How it is used:**

This task will show you how optical character recognition works and will familiarize you with low-resolution fonts requiring noise-immunity. This can be useful for the systems that required the reliability.

--------------------
### Probably Dice

Typically, when using multiple dice, you simply roll them and sum up all the result. To get started with your investigation of dice probability, write a function that takes the number of dice, the number of sides per die and a target number and returns the probability of getting a total roll of exactly the target value. The result should be given with four digits precision as ±0.0001. For example, if you roll 2 six-sided dice, the probability of getting exactly a 3 is 2/36 or 5.56%, which you should return as ≈0.0556.

For each test, assume all the dice are the same and are numbered from 1 to the number of sides, inclusive. So a 4-sided die (D4) would have an equal chance of rolling a 1, 2, 3 or 4. A 20-sided die (D20) would have an equal chance of rolling any number from 1 to 20.

**Tips:** Be careful if you want to use a brute-force solution -- you could have a very, very long wait for edge cases.

**Input:** Three arguments. The number of dice, the number of sides per die and the target number as integers.

**Output:** The probability of getting exactly target number on a single roll of the given dice as a float.

**Example:**
````
probability(2, 6, 3) == 0.0556  # 2 six-sided dice have a 5.56% chance of totalling 3
probability(2, 6, 4) == 0.0833
probability(2, 6, 7) == 0.1667
probability(2, 3, 5) == 0.2222  # 2 three-sided dice have a 22.22% chance of totalling 5
probability(2, 3, 7) == 0       # The maximum you can roll on 2 three-sided dice is 6
probability(3, 6, 7) == 0.0694
probability(10, 10, 50) == 0.0375
````
**Precondition:**
````
1 ≤ dice_number ≤ 10

2 ≤ sides ≤ 20

0 ≤ target < 1000
````

**How it is used:**

This task illustrates basic probability. Many events can be described as the combination of other events. In this case you're combining several dice into one total to crit the Orc King for massive damage.

---------
### Energy Pie

The robots were returning to the energy charging base in small groups or by themselves and did not see each other upon their return. This meant that each group did not know how many robots had fueled their part of the squad energy container. Some groups knew what the charged capacity of the battery was, but other groups didn't know this information and think the remaining juice is the full capacity of the battery, then take their portion from the remaining electricity. So, each group had divided the remaining or initial charge and took their part. How much power will remain after all of the robots return from their mission?

Let’s take a look at an example of how this should work: There are 6 robots. The first group consists of 2 robots. They had divided the energy into 6 parts and took 2/6 of it. The remainder of the energy is 2/3 of the initial charge. Next returns a single robot, it doesn’t know about the original charge of the battery, so it divides the remaining energy into 6 parts and takes 1 part. This leaves `10/18 = 5/9`. The last group is 3 robots, which knew about the original charge. They took half of the original container, so the remaining is `5/9 - 3/6 = 1/18`

You are given an ordered array with sizes of the groups in the order they arrived. If a group knows about the initial charge capacity, then the charge is positive. If not, then charge will be negative. The recent example will given as (2, -1, 3).

````
######   ******   ......   ...... 
######   ******   ......   ......
######   ######   ****##   ....**
######   ######   ######   ****** 
######   ######   ######   ******
######   ######   ######   ****##
 init      2        -1       3
````
You should calculate the amount as remaining energy in the container as a fraction from the starting size. The result should be represented as two numbers - numerator and denominator. Zero should be represented as (0, 1).

**Input:** Sizes of groups as a tuple of integers.

**Output:** The remaining of the pie as a list or tuple of two integers.

**Example:**
````
energy_pie((2, -1, 3)) == (1, 18)
energy_pie((1, 2, 3)) == (0, 1)
````
**Precondition:**
````
∀ x ∈ groups: -1000 < x < 100 AND x ≠ 0
````
**How it is used:**

This mission will familiarize you with operations involving fractions because we must deal with fractions every day of our lives.
