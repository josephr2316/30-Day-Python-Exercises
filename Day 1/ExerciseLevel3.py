import math

number_int = 6
number_float = 8.98
number_complex = 5 + 10j
string = 'Martha'
bool = True
list = [5, 6, 7, 7, 3]
tuple = (7, 3, 47, 1)
set = {7, 4, 8, 'hello'}
dict = {'1':'hola', 8: 78}

# Calculate Euclidean distance
p = (2,3)
q = (10,8)
print (math.dist(p, q))

print(math.sqrt(((q[0] - p[0]) ** 2) + ((q[1] - p[1]) ** 2)))
print(math.sqrt(math.pow(q[0] - p[0],2) + math.pow(q[1] - p[1],2)))
