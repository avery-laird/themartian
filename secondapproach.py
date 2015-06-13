import sys
import math


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
    def __init__(self, eccentricity, semi_major_axis, semi_lr, theta = 0):
        self.eccentricity = eccentricity
	self.semi_major_axis = semi_major_axis
        self.semi_latus_r = semi_lr
        self.theta = theta

    def radius_from_angle(self, theta):
        return self.semi_latus_r / (1 + (self.eccentricity * math.cos(theta)))

    def angle_from_radius(self, radius):
        return math.acos(((self.semi_latus_r / radius) - 1) / self.eccentricity)


def main():
    earth = Body([0, 147090000000], 2929000, 5.9726E24, Orbit(0.016710219, 149600000000, 1.495583757E8))
    print earth.orbit.radius_from_angle(math.pi)
    


if __name__ == "__main__":
    main()
