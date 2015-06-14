import sys
import math
from matplotlib import pyplot as plt

class Body:
    def __init__(self, position, velocity, mass, orbit = None):
        self.position = [] # polar coordinates theta, r in radians and metres
        self.velocity = 0  # m/s
        self.mass = mass   # kg
        self.orbit = orbit # Orbit object

    def set_orbit(self, orbit):
	# Body has-a orbit
        self.orbit = orbit
        
class Orbit:
    # period is in DAYS
    def __init__(self, eccentricity, semi_major_axis, semi_lr, period, theta = 0):
        self.eccentricity = eccentricity
	self.semi_major_axis = semi_major_axis
        self.semi_latus_r = semi_lr
        self.period = period*24*60*60
        self.theta = theta

    def radius_from_angle(self, theta):
        return self.semi_latus_r / (1 + (self.eccentricity * math.cos(theta)))

    def angle_from_radius(self, radius):
        return math.acos(((self.semi_latus_r / radius) - 1) / self.eccentricity)

    def find_e_anomaly(self, m, e, i=0):
         # assume non-negative values less than 300 million
         def f(x):
             return x - (e * math.sin(x))
         while f(i) < m:
             i += 1
         return i

    def find_true_anomaly(self, E, i=0):
        def l(theta):
            return (1-self.eccentricity)*(math.tan(theta/2))**2
        r = (1 + self.eccentricity)*(math.tan(E/2))**2
        while l(i) < r:
            i += 0.0001
        return i
         
    def calc_position(self, seconds):
        ## calculate mean anomaly
        #  n = mean motion
        n = (2 * math.pi)/self.period
        print "n = " + str(n)
        mean_anomaly = n * seconds
        print "mean anomaly = " + str(mean_anomaly)
        ecc_anomaly = self.find_e_anomaly(mean_anomaly, self.eccentricity)
        print "eccentric anomaly = " + str(ecc_anomaly)
        true_anomaly = self.find_true_anomaly(ecc_anomaly)
        print "true anomaly = " + str(true_anomaly)
        return ([self.semi_major_axis * (1 - (self.eccentricity * math.cos(ecc_anomaly))), true_anomaly])


def main():
    earth = Body([0, 147090000000], 2929000, 5.9726E24, Orbit(0.016710219, 149600000000, 1.495583757E8, 365))
#    print earth.orbit.radius_from_angle(math.pi)
#    print earth.orbit.find_e_anomaly(271433.6, 0.016710219)
#    print earth.orbit.find_true_anomaly(earth.orbit.find_e_anomaly(271433.6, 0.016710219))

#    plt.show()


if __name__ == "__main__":
    main()
