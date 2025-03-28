## Ejercicio 1
## print('Me encanta estudiar Python')


## Ejercicio 2
## print('Estudiar "Python" es muy divertido')

## Ejercicio 3
## print(554+1)

## Ejercicio 4
## print('Hola Mundo1\nHola Mundo2\nHola Mundo3')

## Ejercicio 5
## print('A\tB\tC\nD\tE\tF\nG\tH\tI')

## Ejercicio 6
## print('Barra normal: C:\\nBarra invertida: \\\nComillas simples: \'\nComillas dobles: \"')

## Ejercicio 7
## print(input('¿Cuál es tu nombre? '))

## Ejercicio 8
## print(input('¿Donde vives? '))

## Ejercicio 9
## print(input('Escribe tu nombre: ') + ' ' + input('Escribe tu primer apellido:') + ' ' + input('Escribe tu segundo apellido:'))

## Ejercicio 10
## number = 20
## name = "Jose"

## Ejercicio 11
## nombre = 'Jose'
## apellido = 'Monsalvo'
## edad = 20
## print('Hola, me llamo ' + nombre + ' ' + apellido + ' y tengo ' + str(edad) + ' años')

## Ejercicio 12
## curso = 'Python'
## print('Estoy estudiando ' + curso)

## Ejercicio 13
## numEntero = 10
## print(type(numEntero))

## Ejercicio 14
## num_decimal = 3.1416
##print(type(num_decimal))

## Ejercicio 15
## num1 = 7.5
## num2 = 2.5
## num3 = num1 + num2
## print(type (num3))

## Ejercicio 16
## num1 = 10.5
## print(type (num1))
## print(type(int(num1)))

## Ejercicio 17
## num2 = 10
## print(type(float(num2)))

## Ejercicio 18
## num1 = 3.5
## num2 = 2
## print(float(num1) + int(num2))
## print(type(float(num1) + int(num2)))

## Ejercicio 19
## nombreAsociado = 'Jose'
## numeroAsociado = 12345
## print('Estimado ' + nombreAsociado + ', gracias por su compra. Su número de pedido es ' + str(numeroAsociado))
## print('Estimado {}, gracias por su compra. Su número de pedido es {}'.format(nombreAsociado, numeroAsociado))
## print(f'Estimado {nombreAsociado}, gracias por su compra. Su número de pedido es {numeroAsociado}')

## Ejercicio 20
## puntosGanados = 350
## puntosTotales = 700
## print('Felicidades! Has ganado ' + str(puntosGanados) + ' puntos. Ahora tienes un total de ' + str(puntosTotales) + ' puntos')
## print('Felicidades! Has ganado {} puntos. Ahora tienes un total de {} puntos'.format(puntosGanados, puntosTotales))
## print(f'Felicidades! Has ganado {puntosGanados} puntos. Ahora tienes un total de {puntosTotales} puntos')

## Ejercicio 21
## puntosAnteriores = 300
## puntosNuevos = 100
## print('Felicidades! Has ganado ' + str(puntosNuevos) + ' puntos. Ahora tienes ' + str(puntosNuevos+puntosAnteriores) + ' puntos')
## print('Felicidades! Has ganado {} puntos. Ahora tienes {} puntos'.format(puntosNuevos, puntosNuevos+puntosAnteriores))
## print(f'Felicidades! Has ganado {puntosNuevos} puntos. Ahora tienes {puntosNuevos+puntosAnteriores} puntos')

## Ejercicio 22

## dividendo = 70
## divisor = 10
## print(str(dividendo) + ' / ' + str(divisor) + ' = ' + str(dividendo/divisor))
## print('{} / {} = {}'.format(dividendo, divisor, dividendo/divisor))
## print(f'{dividendo} / {divisor} = {dividendo/divisor}')

## Ejercicio 23
## num1 = 301
## num2 = 150
## print(str(num1) + ' % ' + str(num2) + ' = ' + str(num1 % num2))

## Ejercicio 24
## num = 783
## print(str(num) + ' ** 0.5 = '  + str(num ** 0.5))
## print(f"{num} ** 0.5 = {num ** 0.5}")
## print('{} ** 0.5 = {}'.format(num, num ** 0.5))

## Ejercicio 25
## num1 = 10
## num2 = 3
## print(str(num1) + ' / ' + str(num2) + ' = ' + str(round(num1/num2, 2)))
## print('{} / {} = {}' .format(num1, num2, round(num1/num2, 2)))
## print(f'{num1} / {num2} = {round(num1/num2, 2)}')

## Ejercicio 26
## num1 = 10.3333333
## print(round(num1, 0))


## Ejercicio 27
## num1 = 5
## print(round(num1**0.5, 4))

## Ejercicio 28
## palabra = "Ordenador"
## print(palabra[4])

## Ejercicio 29
## frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
## print(frase.index('práctica', 0))

## Ejercicio 30
## frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
## print(frase.rindex('práctica', 0))

## Ejercicio 31
## frase = "Controlar la complejidad es la esencia de la programación"
## print(frase[0:9])

## Ejercicio 32
## frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
## print(frase[0::3])

## Ejercicio 33
## frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
## print(frase[::-1])

## Ejercicio 34
## frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
## print(frase.upper())

## Ejercicio 35
## lista_palabras = ['Hola', 'Mundo', 'Python']
## print(" ".join(lista_palabras))

## Ejercicio 36
## frase = "Si los cocos malos hablaran, serían los más malhablados del mundo"
## print(frase.replace('malos', 'buenos').replace('malhablados', 'educados'))

## Ejercicio 37
## palabraRepetida= "Repetir"
## print(palabraRepetida*100)

## Ejercicio 38
## frase = "Tierra mojada, mis recuerdos de viaje entre las lluvias"
## print("agua" not in frase)

## Ejercicio 39
## palabra = "electroencefalografista"
## print(len(palabra))

## Ejercicio 40/41
## mi_lista = [1, 2, 3, 4, 5, "hola", "mundo", "si", 4.5, 5.5, 6.5]
## mi_lista.append("motocicletas")
## print(mi_lista)

## Ejercicio 42
## mi_lista = ["manzana", "banana", "mango" , "cereza" , "sandía"]
## frutasEliminadas = mi_lista.pop(2)
## print(frutasEliminadas)

## Ejercicio 55
## num1 = 10
## num2 = 5
## bool = (num1>=num2)
## print(bool)

## Ejercicio 56
## num1 = 25**0.5
## num2 = 5
## bool = num1 == num2
## print(bool)

## Ejercicio 57
## num1 = 64 * 3
## num2 = 24 * 8
## bool = (num1 != num2)
## print(bool)


## Ejercicio 58

## num1 = 36
## num2 = 72/2
## num3 = 48
## mi_bool = (num1 > num2) and (num1 < num3)
## print(mi_bool)


## Ejercicio 59
## num1 = 36
## num2 = 72/2
## num3 = 48
## mi_bool = (num1 > num2) or (num1 < num3)
## print(mi_bool)


## Ejercicio 60
## palabra1 = "hola"
## palabra2 = "trasero"
## frase = "hola, quería decirtelo al oído, pero me da vergüenza, así que te lo digo por aquí: Buen trasero"
## mi_bool = palabra1 not in frase and palabra2 not in frase
## print(mi_bool)


## Ejercicio 61

## num1 = input("ingresa un número: ")
## num2 = input("ingresa otro número: ")

## if num1 > num2: 
    ## print(f"{num1} es mayor que {num2}")
## elif num2 > num1:
    ## print(f"{num1} es menor que {num2}")
## else: 
    ##print(f"{num1} y {num2} son iguales")



## Ejercicio 62

## edad = int(input('Escribe tu edad:'))
## licencia = input('¿Tienes licencia de conducir? Si/No:')
## if (edad >= 18) and (licencia == 'Si' or licencia == 'si'):
##    print('Puedes conducir')
## else:
##     print('No puedes conducir')


## Ejercicio 63
## hablaIngles = bool(True)
## sabePython = bool(True)
## if hablaIngles and sabePython:
##     print('Eres un programador de Python que habla inglés')
## elif hablaIngles and not sabePython:
##     print('Eres un programador que habla inglés pero no sabes Python')
## elif not hablaIngles and sabePython:
##     print('Eres un programador de Python que no habla inglés')
## else:
##     print('No eres un programador de Python y no hablas inglés') 

## Ejercicio 64
## nombres_alumnos = ['Juan', 'Ana', 'Pedro', 'María', 'Luis', 'Sara', 'Pablo', 'Carmen', 'Jorge', 'Lucía']
## for alumno in nombres_alumnos:
##     print('Hola ' + alumno)


## Ejercicio 65
## lista_numeros = [2, 5, 1, 7, 4, 8, 3, 6, 9]
## suma = 0

## for numeros in lista_numeros:
##     suma = suma + numeros

## print(suma)



## Ejercicio 66
## import random

## lista_numeros = [random.randint(1, 99999999) for i in range(1000)]

## suma_pares = 0
## suma_impares = 0

## for numeros in lista_numeros:
##     if numeros%2 == 0:
##         print(f'{numeros} es par')
##         suma_pares = suma_pares + 1
##     elif numeros != 0:
##         print(f'{numeros} es impar')
##         suma_impares = suma_impares + 1

## print(f' Hay {suma_pares} números pares y {suma_impares} números impares en la lista')


## Ejercicio 67

## numero = 10

## while numero > 0:
##     print(numero)
##     numero = numero - 1
## else: 
##     print('Has terminado!')



## Ejercicio 68

## numero = 50 
## while numero > 0:
##
##     if numero % 5 == 0:
##         print(numero)
##         numero -= 1
##     else:
##         
##         numero -= 1
## print('Has terminado!')

## Ejercicio 69





##############################################################################################################

## Ejercicio Extra
#nombre = input('Escribe tu nombre:' )
#apellido = input('Escribe tu apellido:' )
## edad = int(input('Escribe tu edad:'))
## if (edad > 100) or (edad < 0):
##     print("Has puesto una edad incorrecta")
## else: 
##     print("Tu edad es correcta")
