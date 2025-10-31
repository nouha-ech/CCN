from sympy import *
x=symbols('x')
expression=x**3 - 6 * x**2 + 5 * x + 12
der= diff(expression,x)
print(der)
solve(der,x)
y=symbols('y')
exp2= sin(x) * cos(y) + cos(x) * sin(y)
exp3= (2 * x + 3) ** 4
simpl= simplify(exp2)
print(exp2)
print("la simplification est ", simpl)
dev= expand(exp3)
print(exp3)
print("le dévloppement est ", dev)





from sympy import *
x=symbols('x')
import math
pi = math.pi
b=pi / 2
exp4=sin(x)*cos(x)
integral = integrate(exp4,(x,0,b))
print(integral)

exp5= 4 * x + 7 - 3 * (x - 1)
simp= simplify(exp5)
print(simp)
solve(simp,x)


exp6= (exp(2 * x) - 1) /  x 
limite= limit(exp6, x, 0)
print(limite)

solution = solve((2*x - 3 * y - 5, -x + 2 * y +3),(x,y))
print(solution[x])
print(solution[y])   



from sympy import symbols, Function, Derivative, dsolve
x = symbols('x')
y = Function('y')

der = Derivative(y(x), x)
exp7 = der - y(x) - x**2
res = dsolve(exp7, y(x))
print(res)


 
 
 
 
 
 
 
 
 
 






