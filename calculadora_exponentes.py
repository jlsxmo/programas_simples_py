# -- Calculadora de exponentes --
print('--- Calculadora de exponentes ---')

# Solicitamos al usuario dos números, uno para la base y otro para el exponente.
base = int(input('Ingrese el primer número(base): '))
exponente = int(input('Ingrese el segundo número(exponente): '))

# Hacemos el cálculo de la potencia.
resultado = base**exponente

# Mostramos al usuario el resultado.
print('El resultado de elevar ' + str(base) + ' a la potencia ' + str(exponente) + ' es: ' + str(resultado))