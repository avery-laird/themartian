import matplotlib.pyplot as plt
import math

# TO FIND NTH SOLUTION
def solution(f1, f2, i=0):
    while f1(i) < f2:
        i+=0.01
    while f1(i) > f2:
        i-=0.001
    return i
#    while f2(i) > f1(i):
#        i+=1
#    while f2(i) < f1(i):
#        i-=0.001
#    return i
#    while nterm > 0:
#        solution = solve(i)
#        nterm -= 1

def main():
    def f1(x):
        return (1-0.0167)*(math.tan(x/2))**2
    f2 = (1+0.0167)*(math.tan(3.442176/2))**2
    print solution(f1, f2, solution(f1,f2)+0.5)


if __name__ == "__main__":
    main()
