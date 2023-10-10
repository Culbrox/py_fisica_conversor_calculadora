import math

while True:

    ask = input("introduce si quieres calcular energia cinetica o potencial:")

    velocidad = float(input("Introduce la velocidad:"))

    masa = float(input("Introduce la masa:"))

    altura = float(input("Introduce la altrua:"))

    if ask == "potencial":

        print("Esta es tu Energia Potencial:", masa * 9.8 * altura) 

    elif ask == "cinetica":

        velocidad_elevada = math.pow(velocidad, 2)

        print("Esta es tu Energia cinetica:", 1/2 * masa * velocidad_elevada) 




