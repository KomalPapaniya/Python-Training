## P1- Take the word and its meaning as input from the user.
-> Create a class named flashcard, use the __init__() function to assign values for Word and Meaning.<br>
-> Now use the __str__() function to return a string that contains the word and meaning.<br>
-> Store the returned strings in a list named flash.<br>
-> Use a while loop to print all the stored flashcards.<br>
-> Add proper error handling<br>
<br>
 
**Input:** Acronym and its meaning<br>
**Output:** List of flashcards.
 
| Input | Output |
| ----- | ----- |
| ty <br> thank you | > ty (thank you) |
| rofl <br> rolling on the floor laughing | > rofl (rolling on the floor laughing) |
| lol <br> laughing out loud | > lol (laughing out loud) |
#

## P2- Create classes according to the following class map:
->  Animal => Wild => Leopard, Tiger <br>
=> Pet => Dog <br>
=> Canine => Fox <br>
-> Each class contains two methods to get a name and info. Get the name returns the name of that animal and get the info returns hierarchy.<br>
For example,<br>
print(dog.get_name())  ⇒ My name is Tommy<br>
print(dog.get_info())  ⇒  I am Dog. I am Pet. I am Animal<br>

**Input:** Get the name or info<br>
**Output:** Information based on the input given.
 
| Input | Output |
| ----- | ----- |
| get the name | I am Leo |
| get the info | I am Tiger. I am Wild. I am Animal |
| get the name | I am Denzo |
| get the info | I am Pet. I am Animal |
#

## P3- Create class Cards with two list suits (Hearts, Diamonds, Clubs, Spades) and  values (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
-> Create a class deck. That contains a method to get a card set containing 52 elements. <br>
-> Create class shuffle. That contains two methods to shuffle given cards and remove/pick a single card.<br>
-> Create two objects of the above class as players. Each player pick/remove 5 cards from the shuffle cards. Total points of both players and display name of winner player.<br>

**Input:** -<br>
**Output:** Display cards of each player along with points and the winner.
 
| Input | Output |
| ----- | ----- |
| run the program | Player 1 picks:<br>2 of Spades----->1<br>Q of Diamonds----->11<br>8 of Spades----->7<br>A of Diamonds----->13<br>2 of Clubs----->1<br>Total points of Player 1: 33<br><br>Player 2 picks:<br>6 of Clubs----->5<br>8 of Diamonds----->7<br>4 of Diamonds----->3<br>4 of Clubs----->3<br>8 of Clubs----->7<br>Total points of Player 2: 25<br><br>Player 1 Wins |
#

## P4- Create a class for Users,
username<br>
account no<br>
mobile no<br>
address<br>
account balance<br>
-> Create a class for user manager<br>
Manages user => Add new user, Get existing user, remove user<br>
-> Create a class for ATM,<br>
Enter account no and get user if not found then show a valid message<br>
Show options for user operations like creating new users, View Balance. Deposit, Withdraw, Close account, etc...<br>
Transaction charge: 0.5 for every operation<br>
Account balance limit: 10000 <br>

**Input:** Data based on the options given.<br>
**Output:** Operations according on the input given.
 
| Input | Output |
| ----- | ----- |
| 1. select options based on the operation you want the ATM to perform.<br>2. provide data wherever asked  | perform operations according on the input given |
#

## P5- Employee Database
Create class Person:<br>
Name, DOB, City, Contact No

Create class Employee (Inherit person class)<br>
employee id, joining date, salary, department, post

Create Employee manager class<br>
Add/Remove Employee, Get all employees list, get employee by his name, get all employees by his/her department<br>
**Task:**<br>
Add few employees<br>
Print all the employees<br>
Find an employee with the name<br>
Print all employees with department Finance<br>
Find all employees whose salary is greater than 50000<br>
Find all employees whose salary is between 50000-100000<br>
Find a list of employees who are joined in the current year<br>
Find all employees who are from Mirzapur<br>
Find employees whose birthday in the current month<br>
Sort employee list with salary in descending order<br>

**Input:** Data based on the options given.<br>
**Output:** Operations according on the input given.
 
| Input | Output |
| ----- | ----- |
| 1. select options based on the operation you want to perform.<br>2. provide data wherever asked  | perform operations according on the input given |
#