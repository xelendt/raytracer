# PYTHON TUTORIAL

This will cover everything (or almost everything) you need to know to make a ray tracer in python using pygame

## Syntax

All the syntax you need to know will be as follows
   ##### Printing (for debugging)
   ```python
   print "Hello, World!"
   ```
   ##### Lists
   ```python
   a = [1, 4, 6, 2, 4]
   print a[0] # 1
   a[0] = 4
   print a[0] # 4
   ```
   ##### For loops
   The variable in the for loop becomes each element in a list. The code below prints numbers from 1 to 100:
   ```python
   for i in range(1, 100):
		print i
   ```
   This code prints elements from an array
   ```python
   a = [4, 6, 2, 6,2, 6, 7, "hello", "world"]
   for i in a:
		print i
   ```
   ##### File parsing
   For this we simply need to parse a .obj file. The following code creates an array of all the lines in the file and prints them.
   ```python
   lines = []
   file = open("name.obj", "r")
   for l in file:
   		lines.append(l)
		print l
   ```

## Running Code

  * Enter a terminal
  * use ```cd``` to go to the directory where your .py file lies
  * run ```python raytracery.py``` 

