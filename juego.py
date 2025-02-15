# Juego de piedra, papel o tijera para 2 jugadores

name_jugador_1 = input("Jugador 1 - Ingresa tu nombre: ")
opcion_jugador_1 = input(f"{name_jugador_1}, elige: piedra, papel o tijera: ").lower()

name_jugador_2 = input("Jugador 2 - Ingresa tu nombre: ")
opcion_jugador_2 = input(f"{name_jugador_2}, elige: piedra, papel o tijera: ").lower()

# Validar elecciones de ambos jugadores
if opcion_jugador_1 not in ["piedra", "papel", "tijera"] or opcion_jugador_2 not in ["piedra", "papel", "tijera"]:
    print("¡Al menos una de las elecciones es inválida!")
elif opcion_jugador_1 == opcion_jugador_2:
    print(f"¡Empate! Ambos eligieron {opcion_jugador_1}")
else:
    # Casos donde gana el jugador 1
    if (opcion_jugador_1 == "piedra" and opcion_jugador_2 == "tijera") or \
       (opcion_jugador_1 == "papel" and opcion_jugador_2 == "piedra") or \
       (opcion_jugador_1 == "tijera" and opcion_jugador_2 == "papel"):
       
        mensaje = f"¡{name_jugador_1} gana! "
        if opcion_jugador_1 == "piedra":
            mensaje += "Piedra rompe tijera"
        elif opcion_jugador_1 == "papel":
            mensaje += "Papel cubre piedra"
        else:
            mensaje += "Tijera corta papel"
        print(mensaje)
    
    # Casos donde gana el jugador 2
    else:
        mensaje = f"¡{name_jugador_2} gana! "
        if opcion_jugador_2 == "piedra":
            mensaje += "Piedra rompe tijera"
        elif opcion_jugador_2 == "papel":
            mensaje += "Papel cubre piedra"
        else:
            mensaje += "Tijera corta papel"
        print(mensaje)