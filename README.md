# Generic S Expression Calculator
This is a python script to calculate expressions.
Previously required s-expressions, now can evaluate arbitrary length and depth.
Ex: "(add 1 2 3 4 5 6 7 (add 1 1 1 1 1 1 1 1) 9 10)" evaluates to '55'.

## TO USE:
Download.
Change directory to where script is downloaded. 
Using command line, call python3 symbolic_expression_calculator.py "*" (where * is your expression)

## Input Format
Surround your expression with " ".

Input must be in the format (operator * * ... *) or be an integer
Where operator is one of: add, multiply, subtract, divide
Where * is one of: an expression of valid format.

Don't divide by 0. 


### Example inputs:
"123"
"(add 12 12)"
"(multiply 4 1)"
'(subtract 2 1)'
"(divide 55 5)"
"(add (multiply (add 4 (add 3 (add 3 (add 3 (add 1 (multiply 4 5)))))) 5) (multiply 10 10))"
"(add (multiply 4 5) (multiply 10 20 10) (add 1 2 3 4 5 6 7 (add 4 4) 9) (multiply 4 6 5))"


## You should make one too!
This was a very fun learning experience.
My main focus was using regex and I think this was a valuable experience. 

