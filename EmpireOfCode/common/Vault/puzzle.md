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

------------
### Playfair Cipher

The Playfair cipher uses a 5 by 5 table containing a keyword or phrase. Memorization of the keyword and 4 simple rules are all that’s required to create the 5 by 5 table and use the cipher. For this mission, we will do one better and use a 6 by 6 table.

For the key table, we should use ASCII letters in lowercase ("abcdefghijklmnopqrstuvwxyz") and digits ("0123456789"). They are have the following order:
````
"abcdefghijklmnopqrstuvwxyz0123456789"
````
To generate the key table, the spaces in the table must be filled with the letters contained in the keyword, dropping any duplicate letters and digits. Then the remaining spaces are filled with the rest of the letters and digits of the alphabet in order. The key is written in the top rows of the table, from left to right. The keyword together with the conventions for filling in the 6 by 6 table constitute the cipher key.

To encrypt a message, we will need to prepare a block of text. Upper case letters get transposed into lower case of letters, we’d break the message into digraphs (groups of 2 letters) and skip white spaces and punctuation symbols. The result would turn a message like "Hello World!" into "`he ll ow or ld`", and would get mapped out in the key table. The two letters of the digraph are considered to be the opposite corners of a rectangle in the key table. Note the relative position of the corners of this rectangle. Then apply the following 4 rules, in order, to each pair of letters in the plaintext:

- Prepare the text: convert it to lowercase, remove all non-useable symbols (white spaces, punctuation etc) and break the message into digraphs. If both letters are the same, add an "x" after the first letter (for double "x" use "z" as completion character) and shift following digraphs. If needed, append a "z" to complete the final digraph (or "x" if the last letter is "z"). For example "pp dr ..." will become "px pd r..." before encoding and "xx zz ..." will became "xz xz z...".

- If the letters appear on the same row of your table, replace them with the letters to their immediate right respectively and wrap around to the left side of the row if a letter in the original pair was on the right side of the row.

- If the letters appear on the same column of your table, replace them with the letters immediately below respectively and wrap around to the top side of the column if a letter in the original pair was on the bottom side of the column.

- If the letters are not on the same row or column, replace them with the letters on the same row respectively but at the other pair of corners of the rectangle defined by the original pair. The order is important – the first letter of the encrypted pair is the one that lies on the same row as the first letter of the plaintext pair.

To decrypt, use the inverse (opposite) of the last 3 rules and you will get the processed (cut version).

For example, the keyword is "checkio101". Then the key table will look like
````
c h e k i o
1 0 a b d f
g j l m n p
q r s t u v
w x y z 2 3
4 5 6 7 8 9
````
Let's use the message "Fizz Buzz is x89 XX." After using rule 1 (text preparation) we will get - "`fi zx zb uz zi sx 89 xz xz`".

- "fi" => "do";
- "zx" => "2y";
- "zb" => "7m";
- "uz" => "t2";
- "zi" => "2k";
- "sx" => "ry";
- "89" => "94";
- "xz" => "y2";
- "xz" => "y2".

And the encoded message is "`do2y7mt22kry94y2y2`".

You should write two functions - "encode" and "decode". Each function receives a message (ciphered or opened) and keyword. The "encode" function processes and encrypts a message. The "decode" function decrypts the encoded message (of course in the processed version).

**Input:** Two arguments. A message as a string and a keyword as a string.

**Output:** The encoded or decoded message (related to function).

**Example:**
````
encode("Fizz Buzz is x89 XX.", "checkio101") == "do2y7mt22kry94y2y2"
decode("do2y7mt22kry94y2y2", "checkio101") == "fizxzbuzzisx89xzxz"
````
**Precondition:**
````
0 < |key| ≤ 36
````
**How it is used:**

This mission gives you a little practice in working with data structures and shows you how to use positional ciphers. You can also use this cipher for your spy correspondence should you have no computer access.