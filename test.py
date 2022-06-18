import math
import matplotlib.pyplot as plt
import matplotlib.animation as ani
hastighet = input("Vilken starthastighet med vilken vinkel? (ex: '30.5, 40' betyder 30.5m/s 40 grader från horisontalplanet)\n")
#massa = input("Vilken massa ska föremålet ha? (ex: '10' betyder 10kg)\n") Använder inte denna just nu.
komposanter = tuple(map(float,hastighet.split(', ')))
upplösning = int(input("Vilket upplösning vill du ha på simuleringen (uppdateringar per sekund)? (Ju högre upplösning ju längre tid tar det)\n"))

#Starthastighetens komposanter
x_komposant = komposanter[0]*math.cos(komposanter[1]/180*math.pi)
y_komposant = komposanter[0]*math.sin(komposanter[1]/180*math.pi)

#Använder oss av formeln: F = CρAv^2/2. Vi låter C = 1, ρ = luftens densitet = 1.29kg/m^3, A = tvärsnittsarean hos en kula med diametern 10cm = 0.00785398m^2, och v är en funktion av tiden
g = -9.82
def nya_hastigheter(t):
    x_komposant = komposanter[0] * math.cos(komposanter[1] / 180 * math.pi)
    y_komposant = komposanter[0] * math.sin(komposanter[1] / 180 * math.pi)
    for i in range(int(10000/upplösning * t)):
        prev_x_komposant = x_komposant
        x_komposant = x_komposant + 1 / 10000 * (x_komposant ** 2 + y_komposant ** 2) * math.cos((math.atan(y_komposant / x_komposant) + math.pi)) * 1.29 * 0.00785398 / 2
        y_komposant = y_komposant + 1 / 10000 * ((prev_x_komposant ** 2 + y_komposant ** 2) * math.sin((math.atan(y_komposant / prev_x_komposant) + math.pi)) * 1.29 * 0.00785398 / 2 + g)
    return x_komposant, y_komposant
x_lista = [0.0]
y_lista = [0.0]
def position(t):
    x_komposant, y_komposant = nya_hastigheter(t)
    x_position = x_lista[-1] + x_komposant*(1/upplösning)
    y_position = y_lista[-1] + y_komposant*(1/upplösning)
    x_lista.append(x_position)
    y_lista.append(y_position)
    x_lista.pop(0)
    y_lista.pop(0)
    plt.title("Tid: {}s".format(t/upplösning))
    plt.ylabel("Höjd (m)")
    plt.xlabel("Längd (m)")
    plt.plot(x_position, y_position, '-p', color = 'blue')
    if y_position < 0:
        animering.event_source.stop()

fig = plt.figure(figsize=(100,100))
animering = ani.FuncAnimation(fig, position, interval = 0.0)

plt.show()