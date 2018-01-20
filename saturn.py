import math
while 1:
    weigth = float(input("enter weigth usefull mass kg"))
    powerimpulse = float(input("enter power nuclear exlosion (KT)"))
    energy = 4200000*1000000* powerimpulse
    print("energy explosion =",energy/1000000,"MJ")
    velocity=math.sqrt(energy*2/weigth)
    print("speed after exlosion=", velocity/1000,"km/s")

