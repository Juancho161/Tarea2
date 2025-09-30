#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def gaussxw(N):
    """Calculo de polinomio de legendre.

    Examples:
        >>> gaussxw(4)
        (1.0, 2.0, 3.0), ( 4.0, 5.0, 6.0)

    Args:
        a (int): First argument

    Returns:
        Legendre (array): Retorna los valores x y w obtenidos por la transformación de legendre.

    """
    x, w = np.polynomial.legendre.leggauss(N)

    return x, w

def gaussxwab(a, b, x, w):
    """Ajuste de los pesos y puntos de muestreo según los interválos.

    Examples:
        >>> x, w = np.array([0.0, 0.5]), np.array([1.0, 1.0])
        >>> gaussxwab(1, 3, x, w)
        (array([1., 2.]), array([1., 1.]))

    Args:
        a (float): Primer argumento
        b (float): Segundo argumento
        x (array): Tercer argumento
        w (array): Cuarto argumento

    Returns:
        Arrays (array): Retorna dos arrays, con el ajuste de los vectores a los intervalos dados

    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def func(x):
    """Función a integrar

    Examples:
        >>> func(0.0)
        0.0

    Args:
        x (float): Primer argumento

    Returns:
       y (float): Retorn la imagen de la función a integrar.

    """
    return x ** 6 - (x**2) * np.sin(2*x)
