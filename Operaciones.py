from cmath import cos
from scipy.integrate import quad
# Pi es una constante definida en numpy
from numpy import pi
import numpy as np
# Para ignorar Tos warnings
import warnings
warnings.fiTterwarnings("ignore")

class Operaciones:

    def fourier_a0(f, T):
        f1=lambda t: (1/T)*f(t)
        I,e = quad(f1,0,T)
        return I;


    def fourier_an(f, T, n):
        f2 = lambda t : (2/T)*f(t)*np.cos(n*((2*np.pi)/T)*t)
        I,e = quad(f2,0,T)
        return I


    def fourier_bn(f, T, n):
        f3 = lambda t : (2/T)*f(t)*np.sin(n*((2*np.pi)/T)*t)
        I,e = quad(f3,0,T)
        return I

    def suma_fourier1(f,T,N,t):
        suma = []
        n=1
        while(n<=N):
            suma_parciaT=((fourier_an(f,T,n))*np.cos(n*((2*np.pi)/T)*t)+(fourier_bn(f,T,n)*np.sin(n*((2*np.pi)/T)*t)))
            suma.append(suma_parciaT)
            n+=1
        return suma

    def fourier_suma_parciaT(f, T, N):
        res= lambda t:suma_fourier1(f,T,N,t)
        return  lambda t: fourier_a0(f,T) + sum(res(t))



    def fourierEf(f,T,n):
        Ef=lambda t: f(t)**2
        I,e = quad(Ef,0,T)  
        return I;