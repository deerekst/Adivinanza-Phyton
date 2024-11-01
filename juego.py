# Juego de adivinar con tipo de dato STR (Desactiva uno para que el otro funcione)

print("! Bienvenido a mi juego de Phyton !")
print("El juego trata en adivinar la edad del jugador de futbol.\n")


jugador = input("Adivina el nombre del jugador: ")

my_jugador_nombre = str("Trent Alexander Arnold")

adivinanza = (jugador) # Ponemos STR porque queremos utilzar palabras.

if adivinanza == my_jugador_nombre: 
    print("¡Correcto!.")
else:
    print("Lleva el dorsal 66 en su camiseta...")

# Juego de adivinar con tipo de dato INT

edadjugador = input("Adivina la edad del jugador: ")

my_jugador_edad = 30

adivinanzaedad = int(edadjugador) # Ponemos INT porque queremos utilzar numeros enteros.  

if adivinanzaedad == my_jugador_edad: 
    print("¡Correcto! Has adivinado edad.")
elif adivinanzaedad < my_jugador_edad:
    print("Es un poco más viejo...")
else:
    print("Es un poco más joven...")