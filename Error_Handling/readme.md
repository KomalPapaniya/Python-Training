## P1- You're going to write an interactive calculator!
User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space
(e.g. 1 + --> Split user input and check whether the resulting list is valid)<br>
-> If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.<br>
-> Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError<br>
-> If the second input is not '+' or '-', again raise a FormulaError<br>
-> If the input is valid, perform the calculation and print out the result.<br>
-> The user is then prompted to provide new input, and so on until the user enters quit.<br>
-> Example image in attached in thread
<br>
 
**Input:** 3 space separated values<br>
**Output:** Operation based on what user has given in input.
 
| Input | Output |
| ----- | ----- |
| 4 + 6 | 10.0 |
| 2.7 - 8.4 | -5.7 |
| g h | Input should be 3 space separated values |
| 4 5 6 | centre element should be a + or - operator |
| a - b | 1st and last value should be numeric |
#

 
## P2- Create while loop which increase counter by one every second.
-> Start count from 0 <br>
-> Stop while loop when counter is grater than 500<br>
-> Program must not stop on any keyboard press. (Not even ctrl + c or ctrl + x)
<br>
 
**Input:** Counter time in N seconds<br>
**Output:** counter from 1 to N which will not stop on any keyboard press.
 
| Input | Output |
| ----- | ----- |
| 5 | 1<br>2<br>3<br>4<br>5 |

#