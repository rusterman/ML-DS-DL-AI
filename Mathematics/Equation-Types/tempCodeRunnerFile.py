import sympy as sp
x,y=sp.symbols('x y')
# x_vals=np.linspace(-5,5,200)
y1=(4-x)/2
y2=3*x-1
sol=sp.solve(sp.Eq(y1,y2),(x,y))
print(sol)