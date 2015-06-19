from sympy.solvers import solve
from sympy import Symbol, tan

x = Symbol('x')
def main():
    print solve(((1 - 0.0167)*(tan(x/2))**2) - ((1+0.0167)*(tan(3.4373092/2))**2), x)


if __name__ == "__main__":
    main()
