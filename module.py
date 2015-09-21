import math
import matplotlib.pyplot as plt
import numpy
import statistics as st
import random

%matplotlib inline

class Car():
# """
# Responsibilities:
#     -measure velocity(min, max,rate) im meters, meters per second.
#     -measure distance traveled and position(start,end,clock)
#     -car size
#     -number of cars

#         """
    def __init__(self, min_speed = 0, max_speed = 30, length = 5, location = 0, total_cars = 30):
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.length = length
        self.location= location
        self.total_cars =total_cars
        self.speed = self.max_speed

class Road:
# +Responsibilities-
# -hold cars
# -define road length
# -control speed triggers
     def __init__(self, total_cars = 30, road_length = 1000, car = Car()):
        self.road_length = road_length
        total_cars = total_cars
        self.car = [Car() for x in range(total_cars)]


     def decelerate(self):
        if random.random() < 0.1:
            return True
        else:
            return False

     def accelerate(self):
        for car in self.car:
            vehicle = 1
            for x in range(30):
                if x == 0:
                    car.speed = 0
                elif self.decelerate() == True and (car.speed >0):
                    car.speed -= 2
                    car.location += car.speed
                else:
                    if car.speed <= (car.max_speed - 3):
                        car.speed += 2
                car.location += car.speed
                if car.location > self.road_length:
                    car.location = 0
                plt.scatter(car.location, car.speed)
                plt.show


            vehicle += 1


run = Road(1)
run.accelerate()

img_data = numpy.random.choice([0,1,1], (60, 1000)).astype('float32')
plt.figure(figsize=(20, 20))
plt.imshow(img_data, cmap='gray', interpolation='nearest')
plt.show
