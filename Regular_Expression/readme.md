## P1 - Write a regular expression to search digits inside a string.
<br>

**Input:** String containing characters and numbers<br>
**Output:** List of digits inside the input string<br>

   | Input | Output |
| ----- | ----- |
| 'y7u0 l8 1f9' | ['7', '0', '8', '1', '9'] |
#

## P2 - Find the words with exactly 8 letters from paragraph using regex 
<br>

**Input:** String containing characters and numbers<br>
**Output:** List containing 8 letter words<br>

   | Input | Output |
| ----- | ----- |
| "decision, apple 12345678, property a 49583229 lifetime" | ['decision', 'property', 'lifetime'] |
#

## P3 - Find the numbers starting with 212 from a string.
<br>

**Input:** String containing characters and numbers<br>
**Output:** All numbers starting with 212<br>

   | Input | Output |
| ----- | ----- |
| 'flag5 212jkl0, 212345 27, 212, 21209' | 212345<br>21209 |
#

## P4 - Loop through the list and apply the regex to each element so that only items ending with a semicolon (;) are matched
<br>

**Input:** List of elements<br>
**Output:** All elements ending with ;<br>

   | Input | Output |
| ----- | ----- |
| ["komal", "kshitij;", "Aksh", "Vishruti", "Prachi;", "Praveen"] | kshitij;<br>Prachi; |
#

## P5 - Write a regular expression to get only the part of the email before the "@" sign and include the "@" sign
<br>

**Input:** Email id<br>
**Output:** String after @ sign (including @)<br>

   | Input | Output |
| ----- | ----- |
| 'abc_123@xyz.com' | ['abc_123@'] |
#

## P6 - Replace all special characters with space using regex
<br>

**Input:** String of characters and numbers<br>
**Output:** String where special characters are replaced with space<br>

   | Input | Output |
| ----- | ----- |
| 'komal#papaniya%$python123%46' | komal papaniya  python123 46 |
#

## P7 - Replace the space character that occurs after a word ending with a or r with a newline character<br>
Sample input: <br>area not a _a2_ roar took 22<br><br>
Sample output:<br>
area<br>
not a<br>
_a2_ roar<br>
took 22
<br>

**Input:** String of characters and numbers<br>
**Output:** String where space after a or r is replaced with newline<br>

   | Input | Output |
| ----- | ----- |
| 'area not a _a2_ roar took 22' | area<br>not a<br>_a2_ roar <br>took 22 |
#

## P8 - Split the given input string on one or more repeated sequences of cat using regex <br>

* Sample input: firecatlioncatcatcatbearcatcatparrot<br>
* Sample output: ['fire', 'lion', 'bear', 'parrot']<br>

**Input:** String containing multiple 'cat' substrings inside it.<br>
**Output:** List obtained after splitting the string by 'cat'<br>

   | Input | Output |
| ----- | ----- |
| 'firecatlioncatcatcatbearcatcatparrot' | ['fire', 'lion', 'bear', 'parrot'] |
#

## P9 - Filter all elements that contain a sequence of lowercase alphabets followed by - followed by digits.
They can be optionally surrounded by {{ and }}. Any partial match shouldn't be part of the output.<br>
* Sample input: ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']<br>
* Sample output: ['{{apple-150}}', 'grape-87']
<br>

**Input:** List of elements.<br>
**Output:** Elements containing 'alphabets-digits' format. they can be optionally surrounded by {{ and }}<br>

   | Input | Output |
| ----- | ----- |
| ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87', '{{{melon-7}}}', 'guava--21'] | {{apple-150}} <br> grape-87 |
#