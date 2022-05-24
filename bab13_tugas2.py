import sympy as sym
t = sym.Symbol('t')
a = sym.Symbol('a', positive = True)
k = sym.Symbol('k')
fungsi = sym.exp(-a*t)*sym.Heaviside(t)
sym.fourier_transform(fungsi, t,  k)