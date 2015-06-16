from matplotlib import pyplot as plt
import math
y1 = []
y2 = []
x = []
r = (1 + 0.0167)*(math.tan(3.4373092/2))**2
for num in range(0, 10000):
    y1.append((1-0.0176)*(math.tan(num/2000))**2)
    y2.append(r)
    x.append(num/1000)
print y1
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
