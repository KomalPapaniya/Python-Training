## P1 - Slice list into 3 equal chunks and reverse each chunk.<br><br>

**Input:** List of integers and number of chunks N you want to slice the list into.<br>
**Output:** List of N chunks in reversed order. <br><br>

   | Input | Output |
| ----- | ----- |
| 3, [11,45,8,23,14,12] | [[45, 11], [23, 8], [12, 14]] |
|  2, [1,4,6,7,5,0]  | [[6, 4, 1], [0, 5, 7]] |
#
## P2 - Count the occurrence of each element from a list
<br>

**Input:** Non-empty list of integers.<br>
**Output:** Dictionary of elements with their occurrence.<br>

| Input | Output |
| ----- | ----- |
| [11, 45, 8, 11, 23, 45, 23, 45, 89] | {11: 2, 45: 3, 8: 1, 23: 2, 89: 1} |
#


## P3 - Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
<br>

**Input:** Non-empty list of tuples<br>
**Output:** List sorted with the last element of each tuple.

| Input | Output |
| ----- | ----- |
| [(2, 5, 8), (1, 2), (4, 4, 9, 6), (3, 3), (2, 1)] | [(2, 1), (1, 2), (3, 3), (4, 4, 9, 6), (2, 5, 8)] |
#


## P4 -  Find the intersection (common) of two sets and remove those elements from the first set.
 <br>


**Input:** Two sets, set1 and set2<br>
**Output:** Two sets, one containing intersection of two and the other containing elements present in set1 but not in set2.

| Input | Output |
| ----- | ----- |
| {23, 42, 65, 57, 78, 83, 29} <br> {57, 83, 29, 67, 73, 43, 48} | {57, 83, 29} {65, 42, 78, 23} |

#

## P5 - Sort given array of three random elements. 0,1 & 2. Without any sorting algorithm. Time complexity: O(n)
<br>

**Input:** non-empty list contains 0,1,2 multiple times<br>
**Output:** output as a sorted list without using sorted algorithm

| Input | Output |
| ----- | ----- |
| [1,0,2,2,0,1,0,1,2,0,0] | [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2]  |
#

 
## P6 - Create a function to reverse the entire list without any function and also do not use any indexing or slicing shortcut. Time Complexity O(logn)
<br>
 
**Input:** List of integers<br>
**Output:** Reversed list.
 
| Input | Output |
| ----- | ----- |
| [3, 6, 9, 1, 12, 7, 21] | [21, 7, 12, 1, 9, 6, 3] |
#
 
## P7 - Convert any lower case string to upper case without in-built python functions.
<br>
 
**Input:** Lower case string<br>
**Output:** Upper case string
 
| Input | Output |
| ----- | ----- |
| 'komal papaniya' | 'KOMAL PAPANIYA' |
#
 
## P8 - Return the sum of duplicates elements from the given List
<br>
 
**Input:** List of integers<br>
**Output:** Sum of duplicates in the list
 
| Input | Output |
| ----- | ----- |
| [3, 5, 6, 11, 12, 3, 5, 5, 4, 4, 4] | 12 (3+5+4) |
#
 
## P9 - Count the subsequence in the given string.
<br>
 
**Input:** String and subsequence string<br>
**Output:** Total subsequence in the given string
 
| Input | Output |
| ----- | ----- |
| "BCAHGBNAJKGTYUALKWG" <br>"AG"  | 6 |
#
## P10 - Find the max sum of sub array
<br>
 
**Input:** List of integers<br>
**Output:** Max sum of sub array
 
| Input | Output |
| ----- | ----- |
| [5, 4, 7, -2, 5, 0, 6, 9, 15, -3] | 49 |
#
 
## P11 -Return product of minimum of odd and maximum of even from a given list.
<br>
 
**Input:** List of numbers<br>
**Output:** Product of largest even and smallest odd integer from the list
 
| Input | Output |
| ----- | ----- |
| [7, 5,  2, 3, 12, 9, 15, 24] | 72 |
#
 
## P12 - Create a simulation program for Hot Potato Game.
### You can develop with your ideas. Just take care of the following things:
### - At least one person must remove from each round.
### - Display name in the console that which user has a hot potato.
### - Each user holds a potato for random seconds between 0.1 to 3.0
### - Each round starts after 3 seconds of the previous elimination.
### - Each round stops at random seconds between 5 to 20.
### - Display the name of the winner.
<br>
 
**Input:** List containing name of players<br>
**Output:** Name of players who are out of the game in each round and lastly, the winner.
 
| Input | Output |
| ----- | ----- |
| ['Komal', 'Vishruti', 'Aksh', 'Kshitij', 'Prachi', 'Praveen'] | Vishruti wins the game 😎🥳🎉 |
#
 
## P13 - Return the array which contains the elements which are greater than from its right side
<br>
 
**Input:** List of integers<br>
**Output:** List of integers which are greater than all the elements present on their right.
 
| Input | Output |
| ----- | ----- |
| [9, 15, 1, 7, 10, 6, 8, 4] | [15, 10, 8, 4] |
#
 
## P14 - Add 1 to given list elements. Do not use string conversion.
<br>
 
**Input:** List of integers<br>
**Output:** List of integers after adding 1 to the input list
 
| Input | Output |
| ----- | ----- |
| [3, 5, 9, 9] | [3, 6, 0, 0] |
#

## P15 - Calculate the sum of the major and minor diagonals of the given matrix.
<br>
 
**Input:** A matrix of integers.<br>
**Output:** Sum of major and minor diagonals of given matrix.
 
| Input | Output |
| ----- | ----- |
| [[2,0,7,-3],<br>[4,1,9,6],<br>[8,1,-1,0],<br>[2,21,0,-8]] | Sum of major diagonal = -6 <br> Sum of minor diagonal = 9 |
#


## P16 - Find the elements of the given list which are exactly the same as the entire product of the list except itself.
<br>
 
**Input:** A list of integers.<br>
**Output:** Elements of the given list which are exactly the same as the entire product of the list except itself.
 
| Input | Output |
| ----- | ----- |
| [1, 5, 1, 10, 50] | [50] |
| [1, 2, 2, 1, 1] | [2, 2] |
| [1, 2, 4, 8, 1] | [8] |
#

## P17 - Print reverse string using recursion.
<br>
 
**Input:** String of characters<br>
**Output:** Reverse of the input string
 
| Input | Output |
| ----- | ----- |
| "Komal Papaniya" | "ayinapaP lamoK" |
#

## P18 - Find the majority element of the given list.
## Majority element = Whose number of count > N/2
## N = length of list.
<br>
 
**Input:** List of integers<br>
**Output:** Majority element
 
| Input | Output |
| ----- | ----- |
| [5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5] | 5 |
#

## P19 - Find the overlapping area of two rectangles. Rectangles can be in any direction.
<br>
 
**Input:** Co-ordinates of both rectangles<br>
**Output:** Overlapping area of both rectangles
 
| Input | Output |
| ----- | ----- |
| [2, 2]<br>[6, 6]<br>[4, 4]<br>[8, 8] | Overlapping Area = 4 squared units |
| [1, 1]<br>[4, 5]<br>[3, 2]<br>[6, 4] | Overlapping Area = 2 squared units |
| [0, 0]<br>[2, 2]<br>[1.5, 2]<br>[2, 1] | Overlapping Area = 0.5 squared units |
| [-3, 2]<br>[1, -3]<br>[3, -2]<br>[-4, -7] | Overlapping Area = 4 squared units |
#
