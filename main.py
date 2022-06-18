import math
import matplotlib.pyplot as plt
import matplotlib.animation as ani

hastighet = input("Vilken starthastighet med vilken vinkel? (ex: '30.5, 40' betyder 30.5m/s, 40 grader "
                  "från horisontalplanet)\n")
# massa = input("Vilken massa ska föremålet ha? (ex: '10' betyder 10kg)\n") Använder inte denna just nu.
komposanter = tuple(map(float, hastighet.split(', ')))
upplösning = int(input("Vilken upplösning vill du ha på simuleringen (uppdateringar per sekund)? (Ju högre upplösning "
                       "ju längre tid tar det)\n"))

# Starthastighetens komposanter
x_komposant = komposanter[0] * math.cos(komposanter[1] / 180 * math.pi)
y_komposant = komposanter[0] * math.sin(komposanter[1] / 180 * math.pi)

# Använder oss av formeln: F = CρAv^2/2. Vi låter C = 0.355 (från Foilsim JS Student), ρ = luftens densitet
# = 1.225kg/m^3, A = tvärsnittsarean hos en kula med diametern 10cm = 0.00785398m^2, och v är en funktion av tiden
g = -9.82
dt = 1 / 1000000
x_komposant_lista = [x_komposant]
y_komposant_lista = [y_komposant]


def nya_hastigheter():
    for i in range(int(1 / dt / upplösning)):
        x_komposant_lista.append(
            x_komposant_lista[-1] + dt * (x_komposant_lista[-1] ** 2 + y_komposant_lista[-1] ** 2) * math.cos(
                (math.atan(y_komposant_lista[-1] / x_komposant_lista[-1]) + math.pi)) * 0.355 * 1.225 * 0.00785398 / 2)
        y_komposant_lista.append(
            y_komposant_lista[-1] + dt * ((x_komposant_lista[-2] ** 2 + y_komposant_lista[-1] ** 2) * math.sin(
                (math.atan(y_komposant_lista[-1] / x_komposant_lista[-2]) + math.pi)) * 0.355 * 1.225 * 0.00785398 / 2 + g))
    x_komposant = x_komposant_lista[-1]
    y_komposant = y_komposant_lista[-1]
    return x_komposant, y_komposant


x_position_lista = [0.0]
y_position_lista = [0.0]


def position(t):
    x_komposant, y_komposant = nya_hastigheter()
    x_position_lista[0] = x_position_lista[0] + x_komposant * (1 / upplösning)
    y_position_lista[0] = y_position_lista[0] + y_komposant * (1 / upplösning)
    plt.title("Tid: {}s".format(t / upplösning))
    plt.ylabel("Höjd (m)")
    plt.xlabel("Längd (m)")
    x_position = x_position_lista[0]
    y_position = y_position_lista[0]
    plt.plot(x_position, y_position, '-p', color='blue')
    if y_position < 0:
        animering.event_source.stop()


fig = plt.figure(figsize=(100, 100))
animering = ani.FuncAnimation(fig, position, interval=0.0)
plt.show()