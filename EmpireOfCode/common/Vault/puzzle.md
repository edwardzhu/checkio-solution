### Vault Password

The password will be considered strong enough if its length is greater than or equal to 10 characters, it contains at least one digit, as well as at least one uppercase letter and one lowercase letter. The password may only contain ASCII latin letters or digits, no punctuation symbols.

You are given a password. We need your code to verify if it meets the conditions for a secure password.

In this mission the main goal to make your code as short as possible. The shorter your code, the more points you earn. Your score for this mission is dynamic and directly related to the length of your code.

**Input:** A password as a string.

**Output:** A determination if the password safe or not as a boolean, or any data type that can be converted and processed as a boolean. When the results process, you will see the converted results.

**Example:**
````
golf('A1213pokl') == False
golf('bAse730onE') == True
golf('asasasasasasasaas') == False
golf('QWERTYqwerty') == False
golf('123456123456') == False
golf('QwErTy911poqqqq') == True
````
**Precondition:**

0 < "password| ≤ 64

password matches by regexp expression `"[a-zA-Z0-9]+"`

**Scoring:**

Scoring in this mission is based on the number of characters used in your code (comment lines are not counted).

*Rank1:*

Any code length.

*Rank2:*

Your code should be shorter than 200 characters.

*Rank3:*

Your code should be shorter than 100 characters.

**How it is used:**

If you are worried about the security of your app or service, you can use this handy code to personally check your users' passwords for complexity. You can further use these skills to require that your users passwords meet or include even more conditions, punctuation or unicode.

--------------
### Verify Anagrams

An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once. Two words are anagrams to each other if we can get one from another by rearranging the letters. Anagrams are case-insensitive and don't take whitespaces into account.

For example: "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not.

You are given two words or phrases. Try to verify if they are anagrams.

**Input:** Two arguments. Words as strings.

**Output:** Determination if the passwords are anagrams or not as boolean (True or False).

**Example:**
````
verify_anagrams("Programming", "Gram Ring Mop") == True
verify_anagrams("Hello", "Ole Oh") == False
verify_anagrams("Kyoto", "Tokyo") == True
````
**Precondition:**
````
0 < |first_word| < 100

0 < |second_word| < 100
````
Words contain only ASCII latin letters and whitespaces.

**How it is used:**

Anagramming can be a fun way to train your brain, but they have other applications. Psychologists use anagram-oriented tests, often called "anagram solution tasks", to assess the implicit memory. Anagrams are often used to create pseudonyms, allowing one to conceal, reveal or operate somewhere in between - like a mask that can establish identity. In addition to this, multiple anagramming is a technique sometimes used to solve some kinds of cryptograms.

-----------------
### Cipher Map

A cipher grille is a 4×4 square of paper with four windows cut out. Placing the grille on a paper sheet of the same size, the encoder writes down the first four symbols of his password inside the windows (see fig. below). After that, the encoder turns the grille 90 degrees clockwise. The symbols written earlier become hidden under the grille and clean spaces appear inside the windows. The encoder then writes down the next four symbols of the password in the windows and turns the grille 90 degrees again. Then, they write down the next four symbols and turn the grille once more. They then write down the final four symbols of the password. Without the cipher grille, it is very difficult to discern the password from the resulting square comprised of 16 symbols.

Write a module that enables the robots to easily recall their passwords using a cipher grille.
````
Grille      Password

X . . .     i t d f
. . X .     g d c e
X . . X     a t o n
. . . .     q r d i

i . . .   . t . f   . . . .   . . d .
. . c .   . . . .   g . . e   . d . .
a . . n   . . o .   . t . .   . . . .
. . . .   . r . .   . . . i   q . d .
 ican   +  tfor   +  geti   +  ddqd
````

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
**Precondition:**
````
|cipher grille| = 4

|ciphered password| = 4
````
cipher `grille` and `ciphered password` are square.

**Optional goals**

**Rank 2:**

A grille can be bigger size than 4 by 4. And the password can be more than 16 characters.

*Precondition Rank 2:*
````
|cipher grille| ≥ 4

|ciphered password| ≥ 4
````

**Rank 3:**

If first letter (first row, first column) is a capital letter, then turns the grille 90 degrees **counterclockwise**.

**How it is used:**

In this mission you learn how to work with 2D arrays. You also get to learn about Grille Ciphers, a technique of encoding messages which has been in use for nearly half a millenium. The earliest known description of the grille cipher comes from the Italian mathematician, Girolamo Cardano in 1550.