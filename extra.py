from random import randint, random
from math import sqrt, floor

r = 1000000000

scooter_x, scooter_y = 0, 0
drone_x, drone_y = 0, 0

scooter, drone = 0, 0

scooter_time = 1000000000000000
drone_time = 1000000000000000

while scooter_time > 0 or drone_time > 0:
    # pick new point in city
    x = randint(-r, r)
    y = floor(sqrt(r*r - x*x))
    if random() < 0.5: y *= -1

    # move to point if possible
    abs_x, abs_y = abs(scooter_x - x), abs(scooter_y - y)
    min_dist = min(abs_x, abs_y)
    max_dist = max(abs_x, abs_y)
    scooter_time -= (sqrt(2*min_dist*min_dist) + max_dist - min_dist)
    if scooter_time > 0: scooter += 1
    abs_x, abs_y = abs(drone_x - x), abs(drone_y - y)
    drone_time -= sqrt(abs_x*abs_x + abs_y*abs_y)
    if drone_time > 0: drone += 1

print(drone/scooter)
