import sympy as sym
t = sym.Symbol('t')
s = sym.Symbol('s')
fungsi = 3*t**2
fungsi_laplace = sym.laplace_transform(fungsi, t, s, noconds = True)
fungsi_laplace