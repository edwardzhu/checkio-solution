### Two Monkeys

We have two monkeys, a and b, and the parameters asmile and bsmile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

**Input:** Two arguments as numbers.

**Output:** Maximum of two.

**Example:**
````
two_monkeys(True, True) == True
two_monkeys(False, False) == True
two_monkeys(True, False) == False
two_monkeys(False, True) == False
````

----------------------------
### List Combitation

Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].

**Input:** Two lists

**Output:** List - combination of two

**Example:**
````
list_combination([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]
list_combination([1, 1, 1, 1], [2, 2, 2, 2]) == [1, 2, 1, 2, 1, 2, 1, 2]
````

-----------------
### Daily Report
Ingots in each consignment are numbered in the row from A1 to Z9 as A1, A2,..., A9, B1, B2, ..., Z9. Each consignment are marked by the last ingots in it. So you can define the quantity of ingots by marks. Each daily report written as consignments of marks in string separated by commas. So you can count the total quantity of ingots for a day.

The full report contain daily reports for several days. Each report is given with a date in the next format: YYYY-MM-DD, where YYYY is year, MM is month, DD is day. Date and report are separated by whitespace. Each date-report are placed on separated lines.

You are given a full report as a multiline text and two dates. You should calculate the total quantity ingots for the days between given dates **(including)**.

For example you are given the next full report and dates:
````
2015-01-01 A1,B2
2015-01-05 C3,C2,C1
2015-02-01 B4
2015-01-03 Z9,Z9

From: 2015-01-01
To:   2015-01-31
````

For these dates we see three "good" days: 2015-01-01, 2015-01-03, 2015-01-05.

- 2015-01-01 == 1 + 11 == 12
- 2015-01-03 == 21 + 20 + 19 == 60
- 2015-01-05 == 234 + 234 == 468

So the result is 540.

**Input:** Three arguments. A full report as a multiline string. A start and end date as strings.

**Output:** The total quantity of ingots for daily reports between these days as an integer.

**Example:**
````
count_reports("2015-01-01 A1,B2\n"
              "2015-01-05 C3,C2,C1\n"
              "2015-02-01 B4\n"
              "2015-01-03 Z9,Z9",
              "2015-01-01", "2015-01-31") == 540,
````
**Precondition:**

All report lines are correct.

**How it is used:**

String date representation often appears in various reports and documents. This concept is useful for parsing and process documents.

----------------
### Call Base

The bill is represented as an array with information about the calls that our accountant has made. Write a function to calculate the cost of these calls.

Each call is represented as a string with the date, time and duration of the call in seconds in the follow format:

`"YYYY-MM-DD hh:mm:ss duration"`

The date and time in this information describes the start of the call.

Space-Time Communications Co. has several rules on how it calculates the cost of calls made on their network:

- First 100 (one hundred) minutes in one day are priced at 1 coin per minute;
- After the first 100 minutes in one day, each minute costs 2 coins per minute;
- All calls are rounded up to the nearest minute. For example 59 sec ≈ 1 min, 61 sec ≈ 2 min;
- Calls are billed based on the day when they began So if a call was started at 2014-01-01 23:59:59, then it counts as having started on 2014-01-01.
Here's an example communications bill:
````
2014-01-01 01:12:13 181
2014-01-02 20:11:10 600
2014-01-03 01:12:13 6009
2014-01-03 12:13:55 200
````
- First day -- 181s≈4m -- 4 coins;
- Second day -- 600s=10m -- 10 coins;
- Third day -- 6009s≈101m + 200s≈4m -- 100 + 5 * 2 = 110 coins;
- Total -- 124 coins.
**Input:** Information about calls as a tuple of strings.

**Output:** The total cost as an integer.

**Example:**
````
total_cost(("2014-01-01 01:12:13 181",
        "2014-01-02 20:11:10 600",
        "2014-01-03 01:12:13 6009",
        "2014-01-03 12:13:55 200")) == 124
````
**Precondition:**
````
0 < |calls| ≤ 30

0 < call_duration ≤ 7200

The bill is sorted by datetime.
````
**How it is used:**

This mission will teach you how to parse and analyse various types data and encourages you to single out important fragments from a larger dataset.

-----------
### Count Ingots

Ingots in each consignment are numbered in the row from A1 to Z9 as A1, A2,..., A9, B1, B2, ..., Z9. Each consignment is marked with the number of the last ingot in it. So you can define the quantity of ingots by the number of marks.

You are given a report of daily consignments as number marks written in a string separated by commas. Count the total quantity of ingots. Take the report "A2,B1" for example. Here we can see two consignments with 2 (A2) and 10 (B1) ingots, giving us a result of 12.

**Input:** A daily report as a string.

**Output:** The total quantity of ingots as an integer.

**Example:**
````
count_ingots("A2,B1") == 12
count_ingots("A1,A1,A1") == 3
count_ingots("Z9,X8,Y7") == 672
count_ingots("C1,D1,B1,E1,F1") == 140
````
**Precondition:**

report match with regexp expression `"[A-Z][1-9](,[A-Z][1-9])*"`

**How it is used:**

This concept uses a modified numeral system and provides you with a basis for working with strings.

--------------
### Broken Reports

Ingots in each consignment are numbered in the row from A1 to Z9 as A1, A2,..., A9, B1, B2, ..., Z9. Each consignment is marked with the number of the last ingot in it. This lets you define the quantity of ingots by the number of marks.

Our daily report is broken. For some reason all of the commas separating values were removed or replaced with a junk data. We need to figure out which are the good marks in todays report. Each mark will look a little like "LD", where "L" is a capital english letter and "D" is a digit ranging from 1 to 9 (zero indicates junk data).

You are given a report as a chunk of text. Your code needs to find all consignment marks and count the total quantity of ingots. Take the report "ASDA1,BB22D01C1" for example. Here we can find three marks: A1, B2 and C1, so the result is 31.

**Input:** A broken report as a string.

**Output:** The total quantity of ingots as an integer.

**Example:**
````
golf("ASDA1,BB22D01C1") == 31
````
**Precondition:**

report can contains only ASCI letters, digits and commas.

**Scoring:**

In this mission the main goal is to make your code as short as possible. The shorter your code, the more points you earn. Your score for this mission is dynamic and directly related to the length of your code.

Scoring in this mission is based on the number of characters used in your code (comment lines are not counted).

**Rank1:**
Any code length.

**Rank2:**
Your code should be shorter than 150 characters.

**Rank3:**
Your code should be shorter than 100 characters.

**How it is used:**

Code golf missions help you to learn special tricks and give you a deeper understanding Python as a language.

---------------
### Letter Queue

We will emulate the queue process with letters. You are given a sequence of commands:

- "PUSH X" -- enqueue X, where X is a letter in uppercase.
- "POP" -- dequeue the front position. if the queue is empty, then do nothing.

The queue can only contain letters.

You should process all commands and assemble letters which remain in the queue in one word from the front to the back of the queue.
````
["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]
````
````
| Command | Queue | Note
-------------------------------------------------
| PUSH A  | A     | Added "A" in the empty queue
| POP     |       | Removed "A"
| POP     |       | The queue is empty already
| PUSH Z  | Z     |
| PUSH D  | ZD    |
| PUSH O  | ZDO   |
| POP     | DO    |
| PUSH T  | DOT   | The result
````
**Input:** A sequence of commands as a tuple of strings.

**Output:** The queue remaining as a string.

Example:
````
letter_queue(("PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T")) == "DOT"
letter_queue(("POP", "POP")) == ""
letter_queue(("PUSH H", "PUSH I")) == "HI"
letter_queue(()) == ""
````
**Precondition:**
````
0 ≤ |commands| ≤ 30

All commands match with "\APUSH [A-Z]\Z" or "\APOP\Z" regexp expression.
````
**How it is used:**

Queues provide services in computer science, transportation, and operations research where various entities such as data, objects, persons, or events are stored and held to be processed later. In these contexts, the queue performs the function of a buffer.
