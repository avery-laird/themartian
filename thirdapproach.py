import math

def step_one(t, p):
    """
    M = mean anomaly
    M = 2pi * t
        -------
           P
    """
    return (2 * math.pi * t) / p

def step_two(m, e):
    """
    M = mean anomaly
    E = eccentric anomaly
    e = eccentricity

    M = E - esinE
    """
    def M(E): return E - (e * math.sin(E))
    E = 0
    while m > M(E):
        E += 1
    while M(E) > m:
        E -= 0.00001
    return E

def step_three(e, E):
    """
    (1 - e)tan^2(theta/2) = (1 + e)tan^2(E/2)
    e = eccentricity
    theta = true anomaly
    E = eccentric anomaly
    """
    def l(theta): return (1-e)*(math.tan(theta/2))**2
    r = (1+e)*(math.tan(E/2))**2
    theta = 0
    while l(theta) < r:
        theta += 0.1
    while r < l(theta):
        theta -= 0.00001
    return [theta, 2*(math.pi - theta) + theta]

def step_four(a, e, E):
    """
    a = semi-major axis
    e = eccentricity
    E = eccentric anomaly

    r = a(1 - ecosE)
    """
    return a * (1 - (e * math.cos(E)))

print "Mean anomaly:  \t\t%f" % step_one(200, 365)
print "Eccentric anomaly: \t%f " % step_two(step_one(200, 365), 0.0167)
print "True anomaly: \t\t" + str(step_three(0.0167, step_two(step_one(200, 365), 0.0167)))
print "Heliocentric distance: \t%f m" % step_four(1.496E8, 0.0167, step_two(step_one(200, 365), 0.0167))


