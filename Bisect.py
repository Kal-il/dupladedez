import matplotlib as mpl
import math
import numpy as np
import matplotlib.pyplot as plt

# An example function whose
# solution is determined using
# Bisection Method.
# The function is x^3 - x^2  + 2

class Bisect_class:

    def __init__(self, data, n):
        self.n = n
        self.data = data
        self.bisection()
        self.plot_func()
        self.bis_array = []
        self.tol_array = []
    def func(self, x): 

        return  x**3 - x**2 + 20
    
    # Prints root of func(x)
    # with error of EPSILON
    def bisection(self):
    
        if (self.func(self.data[0]) * self.func(self.data[1]) >= 0):
            print("You have not assumed right a and b\n")
            return
        
        middle = self.data[0]
        array = []
        middle_array = []
        for p in range(1, self.n+1):
            tol = 1 * math.pow(10, -p)
            #print(tol)
            array.append(tol)
            #print(array)
            while ((self.data[1]-self.data[0]) >= tol):
        
                # Find middle point
                middle = (self.data[0]+self.data[1])/2
                

                # Check if middle point is root
                if (self.func(middle) == 0.0):
                    break
        
                # Decide the side to repeat the steps
                if (self.func(middle)*self.func(self.data[0]) < 0):
                    self.data[1] = middle
                else:
                    self.data[0] = middle
            middle_array.append(middle)      

            
            print("The value of root for n = {} is: {:.4f} ".format(p, middle))
            
        print(middle)
        
        self.bis_array = np.array(middle_array)
        self.tol_array = np.array(array)
        print(self.tol_array)
        print(self.bis_array)

        return middle, middle_array

    def plot_func(self):
        # 100 linearly spaced numbers
        x = np.linspace(-5,5,200)

        # the function, which is y = x^2 here
        y = self.func(x)

        # setting the axes at the centre
        fig = plt.figure()
        ax = fig.add_subplot(2, 2, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # plot the function
        plt.plot(x, y, 'r')
        plt.plot(self.tol_array, self.bis_array)

        ax2=fig.add_subplot(2,2,2)
        plt.plot(self.tol_array, self.bis_array)
        
        ax3=fig.add_subplot(2,2,3)
        plt.plot(range(1, self.n+1), self.bis_array)

        # show the plot
        plt.show()
