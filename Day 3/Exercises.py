import math
import cmath

# 1.Declare your age as integer variable
age: int = 28

# 2.Declare your height as a float variable
height: float = 1.85

# 3.Declare a variable that store a complex number
complex_number = 5 + 9j

# 4.Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input('Enter base: '))
height_triangle = int(input('Enter height: '))
area = int(0.5 * base * height_triangle)
print('The are of the triangle is ', area)


# 5.Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
perimiter = a + b + c
print('The perimeter of the triangle is ',perimiter)

# 6.Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
lenght = float(input('Enter the lenght: '))
width = float(input('Enter the width: '))
area = lenght * width
perimiter = 2 * (lenght + width)
print('The area of the rectangle is: ', area)
print('The perimeter of the rectangle is: ', perimiter)

# 7.Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input('Enter the radius of a circle: '))
area = 3.14 * radius * radius
circunference = 2 * 3.14 * radius
print('The area of the circle is: ', area)
print('The circunference of the circle is: ', circunference)


# 8.Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = 2 // 2  # (2, 0)
y = 2 * 0 - 2 # (0, 2)
m_t = 2 
print ('x-intercept: ', x)
print ('y-intercept: ', y)
print ('The slope is: ', m_t)

# 9.Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
m = (10 -2) / (6 - 2)
print ('The slope is: ', m)
# Calculate Euclidean distance
p = (2,2)
q = (6,10)
print ('Euclidean distance: ', math.dist(p, q))

print("Euclidean distance: ", math.sqrt(((q[0] - p[0]) ** 2) + ((q[1] - p[1]) ** 2)))
print("Euclidean distance: ", math.sqrt(math.pow(q[0] - p[0],2) + math.pow(q[1] - p[1],2)))

# 10. Compare the slopes in tasks 8 and 9.

# 11.Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 6
c = 9

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# method #2

print("Equation: ax^2 + bx + c ")
d=b**2-4*a*c
d1=d**0.5
if(d<0):
    print("The roots are imaginary. ")
else:
    r1=(-b+d1)/2*a
    r2=(-b-d1)/2*a
    print("The first root: ",round(r1,2))
    print("The second root: ",round(r2,2))

    # https://www.knowprogram.com/python/python-program-quadratic-equation/

# 12.Find the length of 'python' and 'dragon' and make a falsy comparison statement.
    
    print(len('python') != len('dragon'))

# 13.Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in 'python'  and  'on' in 'dragon':
    print(True)
else:
    print(False)

# 14.I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
if 'jargon' in 'I hope this course is not full of jargon':
    print(True)
else:
    print(False)

# 15.There is no 'on' in both dragon and python
if 'on' not in 'python'  and  'on' not in 'dragon':
    print(True)
else:
    print(False)

# 16.Find the length of the text python and convert the value to float and convert it to string

float_number = float(len('python'))
int_number = int(len('python'))
string_value = str(len('python'))
print(float_number)
print(int_number)
print(string_value)

# 17.Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
value = int(input('Insert a value: '))

if value%2 is 0 and value > 2:
    print("Even")
else:
    print('Odd')

# 18.Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

floor_division = 7 // 3
int_value = int(2.7)

if floor_division is int_value:
    print(True)
else:
    print(False)

# 19.Check if type of '10' is equal to type of 10

if type('10') is type(10):
    print(True)
else:
    print(False)

# 20.Check if int('9.8') is equal to 10

if int(9.8) is 10:
    print(True)
else:
    print(False)

# 21.Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
print('Your weekly earning is ',hours * rate_per_hour)

# 22.Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
year = int(input('Enter number of years you have lived: '))
years_lived = year * 365 * 24 * 60 * 60;
print(f"You have lived for {years_lived} seconds")

# 23.Write a Python script that displays the following table

for i in range(5):
    print(pow(i+1,1),end=" ")
    print(pow(i+1,0),end=" ")
    print(pow(i+1,1),end=" ")
    print(pow(i+1,2),end=" ")
    print(pow(i+1,3))