def text_binary(kivv):
    # Convertir la cadena en un array de bytes y obtener la representación binaria de cada byte
    result = ' '.join(format(x, '08b') for x in bytearray(kivv, 'utf-8'))
    array = []
    
    # Eliminar los espacios entre los números binarios para procesarlos más fácilmente
    result = result.replace(' ', '')
    
    # Ahora, agrupamos los bits en pares de dos bits
    length = len(result)
    
    a = 0
    b = 0

    # Crear los pares de bits
    while a < length:
        pair = result[a:a+2]  # Obtener el siguiente par de bits
        print(pair)  # Imprimir el par de bits
        array.append(pair)  # Insertar el par de bits en el array
        
        a += 2  # Avanzar dos posiciones para el siguiente par
        b += 1  # Contador de pares
    
    # Llamar a la función `amount` para mostrar la cantidad de pares
    amount(b, array)


def amount(count, array):
    # Imprimir la cantidad de pares de dos bits
    print(f"Número de pares de 2 bits: {count}")
    print("Array de pares de bits:", array)


# Probar la función con un ejemplo
text_binary("Hello")
