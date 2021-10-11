import sympy
from sympy.core.function import diff
from sympy.solvers.solvers import solve
z = sympy.Symbol('z')
x, y = sympy.symbols('x y')
#x = 2
#y = 1
#gfg = x**2 + 4 * y + 4
#print(gfg)
#
#ans = sympy.diff(z**5) * sympy.diff(x**7+1)
#print(ans)


#revenue = (22000 - 70*x)*x   #รายรับ
#cost = (8000*x + 20000)      #ต้นทุน
#test =  revenue - cost
test = (120-x)*x - (10*x + 50)
dif = sympy.diff(test)
ans = solve(dif)
print(ans)

x = 55
test = (120-x)*x - (10*x + 50)
print(test)
