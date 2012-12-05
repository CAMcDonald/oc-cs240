####### Cassie McDonald
####### Computer Science II
####### CS 240
####### GPS for Hikers

####### Program creates a GPS Unit

import random

def gpsGetLongLat():
    longitude = 0.0
    latitude = 0.0
    return longitude, latitude

class Waypoint(object):
    class_var = None
    def __init__(self, latitude, longitude, name = ''):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name

class Path(object):
    def __init__(self, name = ''):
        self.waypoints = []
        self.name = name

    def add_waypoint(self, waypoint):
        self.waypoints.append(waypoint)


w1 = Waypoint(0,0, 'Equator')
w2 = Waypoint(39.8333, -98.5833, 'Middle of the United States')
w3 = Waypoint(4.0755, -76.3299, 'Olivet, Michigan')
w4 = Waypoint(3,5)
w5 = Waypoint(3, 8, 'right here')

p1 = Path('Here to Lebanon, KS')
p1.add_waypoint(w3)
p1.add_waypoint(w2)

p2 = Path('Here and Back Again')
p2.add_waypoint(w3)
p2.add_waypoint(w2)
p2.add_waypoint(w3)