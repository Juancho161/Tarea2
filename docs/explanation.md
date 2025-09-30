# Cuadratura Gaussiana

Este documento explica cómo se implementa y utiliza la cuadratura gaussiana en el proyecto.

## 1. Introducción
La **cuadratura gaussiana** es un método numérico para aproximar integrales definidas.  
En lugar de usar puntos igualmente espaciados como en el método del trapecio o Simpson, se eligen nodos y pesos de forma que la integral sea exacta para polinomios hasta cierto grado.

En este caso usamos los **polinomios de Legendre**, que proporcionan los puntos de integración adecuados en el intervalo estándar `[-1, 1]`.

En el caso de la integral dada, el N que logra la exactitud es N = 4.

## 2. Fórmula general

La integral:


$$
I = \int_a^b f(x)\,dx
$$

se aproxima como:


$$
I \approx \sum_{i=1}^{N} w_i \, f(x_i)
$$


donde:

- \( x_i \) son los nodos transformados al intervalo \([a, b]\),

- \( w_i \) son los pesos correspondientes.


## 3. Código en Python
#Script.py

import matplotlib.pyplot as plt

import numpy as np


def gaussxw(N):

    x, w = np.polynomial.legendre.leggauss(N)
    

    return x, w
    

def gaussxwab(a, b, x, w):

    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w
    

def func(x):

    return x ** 6 - (x**2) * np.sin(2*x)
    
    
    
    
#Main.py
    
for i in range(1, 10):  

    N2X, N2W = gaussxw(i)
    
    N2X, N2W = gaussxwab(1, 3, N2X, N2W)
    
    ValIntN2 = np.dot(N2W, func(N2X))
    
    print("N = ", i, "   Valor I =  ", ValIntN2)
    

