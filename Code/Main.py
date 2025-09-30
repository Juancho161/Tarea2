#!/usr/bin/env python3
import numpy as np
from Script import gaussxw, gaussxwab, func



for i in range(1, 10):  #A partir de N = 4 se estabiliza, al ser grado 6 necesita un N = 4 (N = 4 es exacto hasta polinomiios de grado 7.
    N2X, N2W = gaussxw(i)
    N2X, N2W = gaussxwab(1, 3, N2X, N2W)
    ValIntN2 = np.dot(N2W, func(N2X))
    print("N = ", i, "   Valor I =  ", ValIntN2)

