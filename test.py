import matplotlib.pyplot as plt

y = []
x2 = []
for x in range(0, 1000):
    y.append(147095000 + (-9.538E15 * x))
    x2.append(x)  
plt.plot(y, x2)
plt.show()
