import random
import math
# 1D functions 

# 1: f(x) = ax3 + bx2 + cx 
def polynomial1D(input):
    a=1
    b=5
    c=1

    output_points = [a*x**3+b*x**2+c*x for x in input]

    return output_points

# 2: f(x) = sin(x)
def trigonometrical1D(input):
    output_points =[math.sin(x) for x in input]

    return output_points


# 3: f(x) = |x| 
def absolutevalue1D(input):
    output_points =[abs(x) for x in input]

    return output_points
# 4: f(x) = exp(sin(x))
def exponential1D(input):
    output_points =[math.exp(x) for x in input]

    return output_points

# 1: f(x) = ax3 + bx2 + cx +dy**2+ey
def polynomial2D(input1,input2):
    a=1
    b=5
    c=1
    d=6
    e=3

    output_points = [a*x**3+b*x**2+c*x+d*y**2+e*y for x,y in zip(input1,input2)]

    return output_points

# 2: f(x) = sin(x)*cos(y)
def trigonometrical2D(input1,input2):
    output_points =[math.sin(x)*math.cos(y) for x,y in zip(input1,input2)]

    return output_points


# 3: f(x) = |x+y| 
def absolutevalue2D(input1,input2):
    output_points =[abs(x+y) for x,y in zip(input1,input2)]

    return output_points
# 4: f(x) = exp(sin(x)*cos(y))
def exponential2D(input1,input2):
    output_points =[math.exp(math.sin(x)*math.cos(y)) for x,y in zip(input1,input2)]

    return output_points


# Generate 100 random input points in the range [0, 100]
input_points = [100*random.uniform(0, 1) for _ in range(5)]

input_points2 = [100*random.uniform(0, 1) for _ in range(5)]


print(input_points)

#1 Dimension

print("1D Polynomial: ")
print(polynomial1D(input_points))

print("1D Trigonometrical: ")
print(trigonometrical1D(input_points))

print("1D Absolute Value: ")
print(absolutevalue1D(input_points))

print("1D Exponential: ")
print(exponential1D(input_points))

#2 Dimension
print("2D Polynomial: ")
print(polynomial2D(input_points,input_points2))

print("2D Trigonometrical: ")
print(trigonometrical2D(input_points,input_points2))

print("2D Absolute Value: ")
print(absolutevalue2D(input_points,input_points2))

print("2D Exponential: ")
print(exponential2D(input_points,input_points2))
