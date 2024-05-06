# Informamos al usuario que vamos a hacerle unas preguntas para conocerlo mejor.
saludo = '¡Hola!, voy a hacerle unas preguntas para conocerlo mejor.\nPresione Enter para continuar.'
input(saludo)
# Solicitamos al usuario su nombre, edad y país de origen.
nombre = input('¿Cuál es su nombre? ')
edad = input('¿Cuántos años tiene? ')
pais = input('¿De qué país es? ') # país
# Mostramos al usuario la información que nos proporcionó.
print('¡Hola ' + nombre + '!, es un placer conocerte, usted tiene ' + edad + ' años y es de ' + pais + '.')