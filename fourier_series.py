import matplotlib.pyplot as plt
import sympy as smp
import numpy as np
from sympy.abc import x

#f = smp.Piecewise((1, smp.And( x >= -smp.pi, x <= 0)), (0, smp.And( x > 0, x <= smp.pi)))
#f = smp.Piecewise((x, smp.And( x >= -smp.pi, x <= 0)), (0, smp.And( x > 0, x <= smp.pi)))
f = smp.exp(x**2)

f_series = smp.fourier_series(f, (x, -smp.pi, smp.pi))
ff_series = smp.lambdify(x, f_series.truncate(n=5))

t = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
plt.plot(t, ff_series(t), 'r')
plt.show()
