# import libraries
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
