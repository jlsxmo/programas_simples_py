# -- Calculadora básica/estándar en consola --

# Título de la calculadora
print("\n---- Calculadora básica ----")

# Menú de opciones, que el usuario puede elegir
print('Eliga una opción:')
print('1. Suma')
print('2. Resta')
print('3. Multiplicación')
print('4. División')
print('5. Módulo')
print('6. Exponenciación')

# Entrada: Se pide al usuario que elija una opción
opcion = int(input('\nTeclee el número de la opción y pulse ENTER: \n'))

# Variable para controlar errores
error = False

match opcion:
    case 1:
        print("\n---- Suma ----")
    case 2:
        print("\n---- Resta ----")
    case 3:
        print("\n---- Multiplicación ----")
    case 4:
        print("\n---- División ----")
    case 5:
        print("\n---- Módulo ----")
    case 6:
        print("\n---- Exponenciación ----")
    case _:
        print("\nError: Opción no válida")
        error = True

if not error:
    # Entrada: Se pide al usuario que introduzca dos números
    num1 = float(input('Introduce el primer operando: '))
    num2 = float(input('Introduce el segundo operando: '))

    # Procesamiento: Se realiza la operación correspondiente
    match opcion:
        case 1:
            resultado = round(num1 + num2, 2)
            print(f'El resultado de sumar {num1} y {num2} es: {resultado}')
        case 2:
            resultado = round(num1 - num2, 2)
            print(f'El resultado de restar {num2} a {num1} es: {resultado}')
        case 3:
            resultado = round(num1 * num2, 2)
            print(f'El resultado de multiplicar {num1} por {num2} es: {resultado}')
        case 4:
            if num2 == 0:
                print('Error: No se puede dividir por cero')
            else:
                resultado = round(num1 / num2, 2)
                print(f'El resultado de dividir {num1} entre {num2} es: {resultado}')
        case 5:
            resultado = round(num1 % num2, 2)
            print(f'El resultado de calcular el módulo de {num1} entre {num2} es: {resultado}')
        case 6:
            resultado = round(num1 ** num2, 2)
            print(f'El resultado de elevar {num1} a la potencia {num2} es: {resultado}')
else:
    print('Por favor, vuelva a ejecutar la calculadora')