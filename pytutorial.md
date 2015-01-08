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
##### Classes
   It would make life easier if each surface were a custom object.  Below is the format. To reference member data within the class use ```python self.data``` and to reference outside of the class, use ```point.data```
   ```python
   class point3d:
		   def __init__ (self, x, y, z):
				   self.x = x
				   self.y = y
				   self.z = z

   p = point3d(1, 0, 0)
   print p.x # 1
   p.x = 5
   print p.x # 5
   ```

## Running Code

  * Enter a terminal
  * use ```cd``` to go to the directory where your .py file lies
  * run ```python raytracery.py``` 

## Updating github

  * In a terminal, type ```git clone https://github.com/xelendt/raytracer.git```.  This will make a new directory called "raytracer" and you can go to that directory using ```cd raytracter```
  * Once you edit your files type ```git add file.py``` to add the changes to the repository on your computer. Then, you can commit your code by simply typing ```git commit``` into the terminal. This will commit the changes on your personal computer. 
  * To push your changes to the online repository, type ```git push``` and your changed will be updated.
