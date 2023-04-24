import matplotlib as mpl
import math
import numpy as np
import matplotlib.pyplot as plt

''' 
Código de implementação da função de bisseção em python
A função é x^3 - x^2 + 2
'''

class Bisect_class:

    def __init__(self, data, n):
        self.n = n
        self.data = data
        self.bis_array = []
        self.tol_array = []
        self.n_array = []
        self.middle_array = []
        self.a_array = []
        self.b_array = []
        self.matrix = []
        self.fx_array = []
        self.epsilon_array = [0]
        self.bisection()
        self.trans_matrix()
        self.plot_func()

        
    def func(self, x): 

        return  x**2 -3
    
    def bisection(self):
    
        if (self.func(self.data[0]) * self.func(self.data[1]) >= 0):
            print("a e b determinandos incorretamente\n")
            return
        
        middle = self.data[0]
        tol_array = []
        n_array = []
        for p in range(1, self.n+1):
            self.n_array.append(p)

            #calculo da tolerancia
            tol = 1 * math.pow(10, -p)
            tol_array.append(tol)

            #verificação da tolerancia
            while ((self.data[1]-self.data[0]) >= tol):
        
                # encontra ponto médio
                middle = (self.data[0]+self.data[1])/2
                

                # verifica se ponto médio é raiz
                if (self.func(middle) == 0.0):
                    break
        
                # Verifica onde repete os passos
                if (self.func(middle)*self.func(self.data[0]) < 0):
                    self.data[1] = middle
                else:
                    self.data[0] = middle
                

                #Preparação dos arrays para impressão da matriz
                self.a_array.append(self.data[0])
                self.b_array.append(self.data[1])
            self.middle_array.append(middle)
            if p != 1:
                self.epsilon_array.append(self.middle_array[p-1] - self.middle_array[p-2])      

            
            
            print("O valor para n = {} é: {:.4f} \n".format(p, middle))
            
        print('c: {} \n'.format(middle) )
        
        self.bis_array = np.array(self.middle_array)
        self.tol_array = np.array(tol_array)
        print('tolerancias: ')
        print(self.tol_array)
        print('\n')
        #self.matrix = [self.n_array, self.a_array, self.b_array, self.middle_array]
        #print(self.tol_array)
        #print(self.bis_array)


    def plot_func(self):
        # 100 valores espaçados linearmente
        x = np.linspace(-5,5,200)

        
        y = self.func(x)

        # prepando os axis da figura
        fig = plt.figure()
        ax = fig.add_subplot(2, 2, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # plota a função
        plt.plot(x, y, 'r')
        plt.plot(self.tol_array, self.bis_array)

        ax2=fig.add_subplot(2,2,2)
        plt.plot(self.tol_array, self.bis_array)
        
        ax3=fig.add_subplot(2,2,3)
        plt.plot(range(1, self.n+1), self.bis_array)

        # show the plot
        plt.show()

    # (transpõe a matriz)
    def trans_matrix(self):
        print()
        for i in range(len(self.n_array)):

            self.matrix.append([self.n_array[i], self.a_array[i], self.b_array[i], self.middle_array[i], self.epsilon_array[i]])

        print("|  n  |  a  |  b  |  X  | epsilon  |")
        for p in self.matrix:  
            np.array(p)
            print(p)
    
