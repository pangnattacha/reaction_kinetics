# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import class written in kinetics_python.py
from kinetics_python import Optimize_k

# define function to load data, optimize k and plot the result
def fun1(temp):
    # Read excel file
    table = pd.read_excel('../MATLAB/data_dummy.xlsx')
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
    plt.scatter(t,y['A'],marker='o')
    plt.scatter(t,y['B'],marker='s')
    plt.scatter(t,y['C'],marker='*')
    plt.scatter(t,y['D'],marker='^')
    plt.legend(['predicted A','predicted B','predicted C','predicted D',
                'A','B','C','D'], bbox_to_anchor=(1.,0.5,0.5, 0.5))
    plt.xlabel('time [min]')
    plt.ylabel(r'concentration [mol.L$^{-1}$]')
    plt.xlim(0,60)
    plt.ylim(0,1)
    plt.plot()
    
    return k_optim

# plot the result to subplots and store k results
plt.figure(figsize=(15,3))
plt.subplots_adjust(wspace=1)
# temp = 100 
plt.subplot(131)
k_100 = fun1(100)
# temp = 200
plt.subplot(132)
k_200 = fun1(200)
# temp = 300
plt.subplot(133)
k_300 = fun1(300)
plt.show()