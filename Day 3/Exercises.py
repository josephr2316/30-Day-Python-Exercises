import math
import cmath
age: int = 28
height: float = 1.85
complex_number = 5 + 9j

base = int(input('Enter base: '))
height_triangle = int(input('Enter height: '))
are = int(0.5 * base * height_triangle)
print('The are of the triangle is ', are)

a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
perimiter = a + b + c
print('The perimeter of the triangle is ',perimiter)

# 8-Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = 2 // 2  # (2, 0)
y = 2 * 0 - 2 # (0, 2)
m = 2 
print ('x-intercept: ', x)
print ('y-intercept: ', y)
print ('The slope is: ', m)
# 9-Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

m = (10 -2) / (6 - 2)

print ('The slope is: ', m)
# Calculate Euclidean distance
p = (2,2)
q = (6,10)
print ('Euclidean distance: ', math.dist(p, q))

print("Euclidean distance: ", math.sqrt(((q[0] - p[0]) ** 2) + ((q[1] - p[1]) ** 2)))
print("Euclidean distance: ", math.sqrt(math.pow(q[0] - p[0],2) + math.pow(q[1] - p[1],2)))

# 11-Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

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

    