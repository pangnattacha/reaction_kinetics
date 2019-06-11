# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import optimize


class Optimize_k():
    
    def __init__(self,y,t):
        self.y = y
        self.x0 =list(y.iloc[0])
        self.t = t
        
    # define ode function according to reaction paths   
    def ode(self,x,t,k):
      x1,x2,x3,x4= x      # unpack current values of x
      k1,k2,k3 = k  # unpack parameters
      # list of dx/dt
      dxdt = [ -k1*x1, #A 
                k1*x1-(k2+k3)*x2, #B
                k2*x2, #C
                k3*x2 ] #D 
      return dxdt
    
    # define function to solve ode equations
    def model(self,t,k):
        return odeint(self.ode,self.x0,t,args=(k,))
    
    # define error function
    def errfun(self,k):
        return (self.y.values - self.model(self.t,k)).flatten()
    
    # define function to optimize k values
    def optim(self,k_guess):
        return optimize.leastsq(self.errfun,k_guess)

# define function to load data, optimize k and plot the result
def fun1(temp):
    # Read excel file
    table = pd.read_excel('data_dummy.xlsx')
    idx = table['Temp'] == temp
    t = table[idx].time
    comp = ['A','B','C','D']
    y = table[idx][comp]
    
    # Assign Optimize_k
    ok = Optimize_k(y,t)
  
    # Initialize k values
    k1,k2,k3 = 0.,0.,0.
    # Bundle parameters for ODE solver
    k_guess = [k1,k2,k3]
  
    # optimize k values
    k_optim,kvg = ok.optim(k_guess)
  
    # predict values from k_optim
    t_span = np.arange(0,t.iloc[-1]+0.1,0.1)
    x = ok.model(t_span,k_optim)
    
    # plot data comparing to the prediction
    plt.plot(t_span,x)
    plt.scatter(t,y['A'])
    plt.scatter(t,y['B'])
    plt.scatter(t,y['C'])
    plt.scatter(t,y['D'])
    plt.legend(['predicted A','predicted B','predicted C','predicted D',
                'A','B','C','D'])
    plt.xlabel('time [min]')
    plt.ylabel(r'concentration [mol.L$^{-1}$]')
    plt.xlim(0,60)
    plt.ylim(0,1)
    plt.plot()
    
    return k_optim