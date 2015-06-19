# import sys
import math
from matplotlib import pyplot as plt
import matplotlib.animation as animation

# An interesting point concerning the hyperbolic case has been made by Chris Marriott, 
# author of SkyMap . He noted that the two "guesses" for an initial anomaly, 
# E1=cube_root(6*M) and E2=asinh(M/ecc), define bounds for the actual value of E; you 
# can be certain that E2 < E < E1. This makes implementing a secant or binary-search method much easier.

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
        self.period = period
        self.theta = theta

    def radius_from_angle(self, theta):
        return self.semi_latus_r / (1 + (self.eccentricity * math.cos(theta)))

    def angle_from_radius(self, radius):
        return math.acos(((self.semi_latus_r / radius) - 1) / self.eccentricity)

    def find_e_anomaly(self, m, e, i=0):
         # assume non-negative values 
         # TODO: change back to simple version
         def l(x):
             return m - i
         def r(x):
             return -1 * e * math.sin(i)
         while l(i) > r(i):
             i += 1
         while l(i) < r(i):
             i -= 0.0001
         return i

    def find_true_anomaly(self, E, rotation = 1, i=0):
        # TODO: figure out when to use the solutions
        def l(i):
            return (1-self.eccentricity)*(math.tan(i/2))**2
        r = (1 + self.eccentricity)*(math.tan(E/2))**2
        while l(i) < r:
            i += 0.01
        while l(i) > r:
            i -= 0.0001
        #if rotation == 2:
        #    return 2*(math.pi - i) + i
        return i
         
    def calc_position(self, days):
        ## calculate mean anomaly
        #  n = mean motion
        n = (2 * math.pi)/self.period
#        print "n = " + str(n)
        mean_anomaly = n * days * 24 * 60 * 60
#        print "mean anomaly = " + str(mean_anomaly)
        ecc_anomaly = self.find_e_anomaly(mean_anomaly, self.eccentricity)
#        print "eccentric anomaly = " + str(ecc_anomaly)
        rotations = int(float(self.period)/days)+1

        true_anomaly = self.find_true_anomaly(ecc_anomaly, rotations)
        print true_anomaly
        self.radius = self.semi_major_axis * (1 - (self.eccentricity * math.cos(ecc_anomaly)))
        self.true_anomaly = true_anomaly


def main():
    earth = Body([0, 147090000000], 2929000, 5.9726E24, Orbit(0.016710219, 149600000000, 1.495583757E8, 365))
#    print earth.orbit.radius_from_angle(math.pi)
#    print earth.orbit.find_e_anomaly(271433.6, 0.016710219)
#    print earth.orbit.find_true_anomaly(earth.orbit.find_e_anomaly(271433.6, 0.016710219))
    theta = []
    radius = []
    for time in [3]:
        earth.orbit.calc_position(time)
        theta.append(earth.orbit.true_anomaly)
        radius.append(earth.orbit.radius)
    plt.polar(theta, radius, 'o')
    plt.show()
    

if __name__ == "__main__":
    main()
