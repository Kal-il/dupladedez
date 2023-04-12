import matplotlib as mpl
import math
# An example function whose
# solution is determined using
# Bisection Method.
# The function is x^3 - x^2  + 2
def func(x): 

    return  x*x*x - x*x + 20
  
# Prints root of func(x)
# with error of EPSILON
def bisection(data):
 
    if (func(data[0]) * func(data[1]) >= 0):
        print("You have not assumed right a and b\n")
        return
    
    middle = data[0]
    array = []
    for n in range(1, 21):
        tol = 1 * math.pow(10, -n)
        print(tol)
        array.append(tol)
        print(array)
        while ((data[1]-data[0]) >= tol):
    
            # Find middle point
            middle = (data[0]+data[1])/2
    
            # Check if middle point is root
            if (func(middle) == 0.0):
                break
    
            # Decide the side to repeat the steps
            if (func(middle)*func(data[0]) < 0):
                data[1] = middle
            else:
                data[0] = middle
                
        print("The value of root for n = {} is: {:.4f} ".format(n, middle))
     
# Driver code
# Initial values assumed
data = [-2000,3000]

bisection(data)


# This code is contributed
# by Anant Agarwal.