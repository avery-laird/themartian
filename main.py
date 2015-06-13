import matplotlib.pyplot as plt
import math, sys

# Simulate earth orbit, 1 second intervals
class Planet:
    def __init__(self):
        self.e = 0
        self.rmax = 0
        self.rmin = 0
        self.slr = 0
        self.theta = 0 # degrees
	self.count = 0
        self.period = 0
        self.semi_major_axis = 0
	self.r = 0

    def set_e(self, e):
        self.e = e

    def set_rmax(self, d):
        self.rmax = d
        self.slr = self.rmax * (1 - self.e)

    def set_rmin(self, d):
        self.rmin = d
        self.slr = self.rmin * (1 + self.e)
    
    def set_period(self, period):
        self.period = period

    def set_semi_major_axis(self, sma):
        self.semi_major_axis = sma

    def update_theta(self):
        if self.r == 0:
            self.theta += (math.pi * float(self.semi_major_axis) * (float(self.slr) / (math.sqrt(1 - self.e**2)))) / (self.period * 0.5 * self.rmin**2) + 0.01
        else:
	    self.theta += (math.pi * float(self.semi_major_axis) * (self.slr / (math.sqrt(1 - self.e**2)))) / (self.period * 0.5 * self.r**2) + 0.01

    def velocity(self):
        return math.sqrt((1.989E30 * 6.67E-11)/self.r)


    def step(self):
        self.r = self.slr / (1 + (self.e * math.cos(self.theta)))
        self.update_theta()
        # self.theta = math.acos(((self.slr / r) - 1) / self.e)
	#if self.count % 10000 == 0:
        #    print "Step " + str(self.count) + " Radius: " + str(self.r)
        self.count += 1
        return self.r

    def plot_from_days(self, days):
        """
        Given the number of days elapsed, so the position
        """
        pass 
        
        

def main():
    re = []
    rm = []
    t = []
    ve = []
    vm = []
    earth = Planet()
    earth.set_e(0.0167)
    earth.set_rmin(1.471E11)
    earth.set_period(365*86400)
    earth.set_semi_major_axis(149600000)
    mars = Planet()
    mars.set_e(0.09341233)
    mars.set_rmin(2.0662E11)
    mars.set_period(687*86400)
    mars.set_semi_major_axis(227920000)
    
    for x in range(0, int(sys.argv[1])):
        re.append(earth.step())
        rm.append(mars.step())
        ve.append(earth.velocity())
        vm.append(mars.velocity())
        t.append(earth.theta)
        sys.stdout.write("\rStep " + str(earth.count) + " / " + sys.argv[1] + " " + str((float(earth.count)/float(sys.argv[1]))*100) + "% " + str(earth.theta) + " " + str(mars.theta))
        sys.stdout.flush()
 	
    print "\n"
    plt.figure(1)
    plt.polar(t, re)
    plt.polar(t, rm)

    plt.figure(2)
    plt.plot(t, ve)
    plt.plot(t, vm)
    plt.show()


if __name__ == "__main__":
    main()
