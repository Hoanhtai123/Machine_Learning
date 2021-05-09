import math
import matplotlib.pyplot as plt
def Byvine():
    time = 5
    solar_system_radius = 6.95 * (10 ** 8)  # meter
    chestnut_radius = 0.0035  # meter
    solar_sys_volume = (4 / 3) * math.pi * (solar_system_radius ** 3)
    chestnut_volume_total = chestnut_volume = (4 / 3) * math.pi * (chestnut_radius ** 3)
    i = 1;
    solar_sys_volume = (4 / 3) * math.pi * (solar_system_radius ** 3)
    print("volume of the solar system {} cubic metre and volume of the chestnut {} cubic metre".format(solar_sys_volume, chestnut_volume_total))
    while chestnut_volume_total < solar_sys_volume:
        chestnut_volume_total = chestnut_volume_total * 2
        i += 1
    print("time need to fill up the solar system with chestnut {} hrs".format((i * 5) / 60))
Byvine()
"""
t_double is the time it take for an object to be doubled after being sprinkle Byvine
capacity_to_fill = the volume of place or object that you want to fill up
volume_fill_in = the volume of the object that you sprinkle Byvine 
-------------------------------------------------------------------------------------
In this example 

t_double = 5 mins
capacity_to_fill = 1.240.000 m^3 (the capacity of the Tokyo Dome stadium according to wikipedia)
    src: https://en.wikipedia.org/wiki/Tokyo_Dome
volume_fill_in = the volume of a standard soccer ball
    diameter of a ball = 15 cm = 0.15 m ("https://en.wikipedia.org/wiki/Football_(ball)#:~:text=The%20ball%20is%20made%20of%20leather%20%28possibly%20from,the%20Smith%20Art%20Gallery%20and%20Museum%20in%20Stirling.")
    volume of the ball = (4/3) * math.pi * (diameter/2)**3
    volume_fill_in =  volume of the ball = 0.0017671458676442582 m^3 
"""
def time_to_fill(t_double, capacity_to_fill, volume_fill_in):
    time_take = []
    area_filled = []
    i = 0
    while capacity_to_fill > volume_fill_in:
        volume_fill_in = volume_fill_in * 2
        area_filled.append(volume_fill_in)
        i += 1
        time_take.append(i)

    print("Time it take to fill up: {} hrs".format((i*t_double) / 60))
    plt.title("Byevine problem")
    plt.xlabel("volume filled in cubic metre")
    plt.ylabel("time in hours")
    plt.plot(time_take,area_filled, color='blue', linestyle='dashed', linewidth=1)
    plt.show()

time_to_fill(5,1240000,0.0017671458676442582)