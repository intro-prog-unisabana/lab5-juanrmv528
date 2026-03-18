from utils import *

mensaje = input("Please type your message\n")

invertido = flip(mensaje)
cantidad_a = count_letters(mensaje, 'a')

resultado = invertido + str(cantidad_a)

print(f"Your encoded message is: {resultado}")