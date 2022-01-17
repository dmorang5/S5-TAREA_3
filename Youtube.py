"""
Nombre: Dennisse Michelle Morán Guachichulca
Curso: 3er Nivel - Software A1
"""

from funciones import *
class Youtube:

#5.1 Ejercicios resueltos de input y print 
#Escribí un programa que solicite al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada nombre. 
#A continuación se debe mostrar en pantalla el texto “Ahora estás en la matrix, [usuario]”, donde “[usuario]” se reemplazará por 
# el nombre que el usuario haya ingresado. 
    def matrix(self):
        print("\t5.1 Ejercicios resueltos de input y print ")
        nombrem=input("Tu nombre:")
        print("Ahora estás en la matrix,", nombrem)
    
#Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. 
#Imprimir en pantalla el monto final a pagar.
    def cena(self):
        print("\n")
        costo=float(input("Costo de la cena: $"))
        servicio=costo * 0.062
        propina=costo * 0.1
        print("Costo total de la comida: $", costo + servicio + propina)

#Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica (en total, tres variables difeentes).
#Finalmente, mostrar la fecha en formato dd/mm/aaaa
    def fecha1(self):
        print("\n")
        dia1=input("Día de tu nacimiento: ")
        mes1=input("Mes de tu nacimiento: ")
        anio1=input("Año de tu nacimiento: ")
        print(dia1+"/"+mes1+"/"+anio1)

#Hacer otra versión del programa, pero esta vez almacenando todo en una única variable numérica, en la forma DDMMAAAA. ¿Y si la varible fuera tipo string?"""
    def fecha2(self):
        print("\n")
        fecha=int(input("Fecha en formato DDMMAAAA: "))
        anio2=fecha%10000
        dia2=fecha//1000000
        mes2=(fecha//10000)%100
        print(dia2,"/",mes2,"/",anio2)

    def fecha3(self):
        print("\n")
        fecha_3=input("Fecha en formato DDMMAAAA: ")
        dia3=fecha_3[:2]
        mes3=fecha_3[2:4]
        anio3=fecha_3[4:]
        print(dia3,"/",mes3,"/",anio3)

#Una pareja de motociclistas necesita hacer cálculos antes de emprender un viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero.
#Por eso deben ingresar: cuantos kilometros puede recorrer su moto con 1 litro de conbustible, que capacidad(en litros) tiene el tanque y cuántos kilómetros en total
#recorreran.
#Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios."""
    def motociclistas(self):
        print("\n")
        capacidad=float(input("Capacidad del tanque: "))
        kmxl=float(input("Rendimiento (km pot litro): "))
        recorrido=float(input("km totales a recorrer: "))
        kmxtanque=capacidad*kmxl
        print("Serán necesarios", recorrido/kmxtanque, "tanques.")

#5.2 Ejercicio resuelto de input y print

#Un empresario que se dedica al espectáculo quiere tener una herramienta (un programa) que le ayude a sacar ciertos cálculos cada vez que trae una banda a tocar en algún estadio.
#Lo primero que necesita saber es cuánta gente va a poder asistir a cada recital. Para eso, cuando arregla con un club para usar su estadio, pregunta cuántos metros cuadrados tiene. Él sabe que, por metro cuadrado, entran 4 personas. También sabe que las tribunas ocupan un 20% de ese espacio, entonces pregunta cuántas personas caben en las tribunas.
#Cuando contrata a la banda que va a tocar, le pregunta qué porcentaje del espacio necesitan ellos para su escenario.
#Con estos datos, debe calcularse cuánta gente va a caber en el estadio para un recital determinado, para saber cuántas entradas tiene que mandar a imprimir. El empresario, cada vez que use el programa, va a ingresar la cantidad de metros cuadrados que tiene el estadio que contrató, la cantidad de gente que cabe en las tribunas y el porcentaje de espacio ocupado por el escenario.
#Luego, él quiere saber cuánto dinero ingresaría si vende todas las entradas disponibles, sabiendo que el 30% de las entradas vendidas son “entradas vip” y el resto son “entradas comunes”. El empresario ingresa el precio de cada tipo de entrada cuando usa el programa.
    def empresario(self):
        print("\n")
        print("\t5.2 Ejercicio resuelto de input y print")
        print("\n")
        CAPACIDAM2=4
        PORCENTAJEGRADAS=0.2
        PORCENTAJEESPECIALES=0.3
        PORCENTAJECOMUNES=0.7

        dimensiones=float(input("Dimensiones del estadio (en m2): "))
        personasengradas=int(input("Cantidad de personas que caben en las gradas: "))
        porcentajeescenario=int(input("Porcentaje de espacio que ocupa el escenario: "))
        m2gradas=dimensiones*PORCENTAJEGRADAS
        m2escenario=dimensiones*(porcentajeescenario/100)
        m2disponibles=dimensiones-m2gradas-m2escenario
        personastotales=(m2disponibles*4)+personasengradas
        print("Caben ", personastotales, " personas.")
        precioentradaespecial=float(input("Precio de entrada especial:$ "))
        precioentradacomun=float(input("Precio de entradas comunes:$ "))
        print("Ingresos total de ventas: $ ",
            (personastotales*PORCENTAJEESPECIALES)*precioentradaespecial + 
            (personastotales*PORCENTAJECOMUNES)*precioentradacomun)

#6.1 Ejercicios resueltos de if-else (y elif)
#Escribir un programa que, dado un número entero, muestre su valor absoluto. 
#Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, 
#para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52)."""
    def valorAbsoluto(self):
        print("\n")
        print("\t6.1 Ejercicios resueltos de if-else (y elif)")
        print("\n")
        numero1=int(input("Número:"))
        if numero1<0:
            numero1=numero1*-1
        print("Valor absoluto:", numero1)

#Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. 
#A continuación, imprimir “coincidencia” si los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. 
#Si no es así, imprimir “no hay coincidencia”."""
    def CoincidenciaOno(self):
        print("\n")
        nombre1=input("Un nombre: ")
        nombre2=input("Otro nombre: ")
        posicion_final_nombre1=len(nombre1)-1
        posicion_final_nombre2=len(nombre2)-1
        if nombre1[0] == nombre2[0] or nombre1[posicion_final_nombre1] == nombre2[posicion_final_nombre2]:
            print("Coincidencia")
        else:
            print("No hay coincidencia")

#Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. 
#Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a 
#ninguno de los candidatos disponibles, indicar “Opción errónea”."""
    def candidatos(self):
        print("\n")
        candidato=input("Candidato elegido: ")
        if candidato.upper()=="A":
            print("Usted ha votado por el partido rojo")
        elif candidato.upper()=="B":
            print("Usted ha votado por el partido verde")
        elif candidato.upper()=="C":
            print("Usted ha votado por el partido azul")
        else:
            print("Opción errónea")

#Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, 
#informarle que no se puede procesar el dato."""
    def vocales(self):
        print("\n")
        letra=input("Letra:")
        if len(letra)!=1:
            print("Debe ser sólo una letra")
        else:
            if letra in "aeiou":
                print("Es vocal")

#Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400."""
    def bisiesto(self):
        print("\n")
        anio=int(input("Año:"))
        if anio%4 == 0:
            if anio%100 != 0 or anio%400 == 0:
                print("Bisiesto")
            else:
                print("No bisiesto")
        else:
            print("No bisiesto")

#6.2 Ejercicio de if-else (y elif) 

#Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones sobre las clases de ese día. 
#El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes se dicta el nivel inicial, los martes el nivel intermedio, 
#los miércoles el nivel avanzado, los jueves son para práctica hablada y los viernes se dicta inglés para viajeros.
#Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato "día, DD/MM", donde [día] es un día de la semana, DD es el número de día y MM es el número de mes. 
#Si el usuario ingresa un día de la semana inexistente o una fecha cuyo día supere el número 31 o el mes supere el número 12, finalizar el programa indicando que se produjo un error. 
#Debe permitirse que ingrese el día de la semana en minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
#Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron exámenes, pero eso sólo si se trata de los niveles inicial, intermedio o avanzado, ya que las prácticas habladas y el inglés para viajeros no tienen exámenes. 
#Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el programa le mostrará el porcentaje de aprobados.
#Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a clase y el programa le indicará "asistió la mayoría" en caso de que la asistencia sea mayor al 50% o "no asistió la mayoría" si no es así.
#Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del mes 7, se deberá imprimir "Comienzo de nuevo ciclo" y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, 
#para luego imprimir el ingreso total en $."""
    def institutoIngles(self):
        print("\n")
        print("\t6.2 Ejercicio de if-else (y elif) ")
        print("\n")
        fecha=input("Fecha (formato 'día, DD/MM'): ")
        fecha=fecha.lower()
        diasemana=fecha[0:fecha.find(',')]
        dianro=int(fecha[fecha.find(',')+2:fecha.find('/')])
        mesnro=int(fecha[fecha.find('/')+1:])
        if dianro>31 or mesnro>12:
            print("Fecha incorrecta")
        else:
            if diasemana in "lunes,martes,miércoles":
                respuesta=input("¿Se tomaron exámenes? S/N: ")
                if respuesta.lower()=="s":
                    aprobados=int(input("Cantidad de aprobados: "))
                    reprobados=int(input("Cantidad de reprobados: "))
                    print("Porcentaje de aprobados:", (aprobados*100)/(aprobados+reprobados), "%")
            elif diasemana=="jueves":
                asistencia=int(input("Porcentaje de asistencia: "))
                if asistencia>50:
                    print("Asistió la mayoría")
                else:
                    print("No asistió la mayoría")
            elif diasemana=="viernes":
                if dianro==1 and (mesnro==1 or mesnro==7):
                    print("Nuevo ciclo")
                    alumnos=int(input("Cantidad de alumnos: "))
                    arancel=float(input("Arancel: $"))
                    print("Ingreso total: $", alumnos*arancel)
            else:
                print("Fecha incorrecta")
        print("Fin del programa")

#7.1 Ejercicios resueltos de bucles for 
#Escribir un programa que muestre la sumatoria de todos los números entre el 0 y el 100."""
    def sumatoria(self):
        print("\n")
        print("\t7.1 Ejercicios resueltos de bucles for ")
        print("\n")
        total=0
        for i in range(101):
            total=total+i
        print("Sumatoria:", total)

#¿Qué modificación habría que hacer si ahora sólo se deben sumar los números que sean múltiplos de 3?"""
    def multiplos3(self):
        print("\n")
        total=0
        for i in range(101):
            if i%3 == 0:
                total=total+i
        print("Sumatoria de los múltiplos de 3:", total)

#Dado un número entero positivo, mostrar su factorial. 
#El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.
#El factorial de 0 es 1."""
    def factorial(self):
        print("\n")
        nume=int(input("Número:"))
        f=1
        if nume!=0:
            for i in range(1,nume+1):
                f=f*i
        print("Factorial:", f)

#Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
#La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
    def fibonacci(self):
        print("\n")
        n1=0
        n2=1
        print(n1)
        print(n2)
        for i in range(8):
            n3=n1+n2
            print(n3)
            n1=n2
            n2=n3

#Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. 
#Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
#No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error si no se ingresaron números positivos.
    def positivosYnegativos(self):
        print("\n")
        sumaPositivos=0
        cantidadPositivos=0
        sumaNegativos=0
        for i in range(6):
            nro=int(input("Número: "))
            if nro>0:
                sumaPositivos=sumaPositivos+nro
                cantidadPositivos=cantidadPositivos+1
            else:
                sumaNegativos=sumaNegativos+nro
        print("Sumatoria de los negativos: ", sumaNegativos)
        if cantidadPositivos!=0:
            print("Promedio de los positivos: ",sumaPositivos/cantidadPositivos)
        else:
            print("No se ingresaron números positivos")

#7.2 Ejercicio resuelto con bucles for anidados

#Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”. 
#La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el contenido de sus mensajes. 
#Uno de los equipos decide utilizar un método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares. 
#Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
#Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales. Escribir un programa que permita encriptar los 5 mensajes. 
#El corrimiento (cantidad de lugares que se correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento.
#Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”. 
#Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
#Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación."""
    def juego(self):
        print("\n")
        print("\t7.2 Ejercicio resuelto con bucles for anidados ")
        print("\n")
        alfabeto="abcdefghijklmnñopqrstuvwxyz"
        corrimiento=int(input("Corrimiento: "))
        for i in range(5):
            mensaje=input("Mensaje a encriptar: ")
            encriptado=""
            for caracter in mensaje:
                if caracter.lower() in alfabeto:
                    indice=alfabeto.find(caracter.lower())
                    indice=(indice+corrimiento)%27
                    encriptado+=alfabeto[indice]
                else:
                    encriptado+=caracter
            print("*** Mensaje encriptado: ", encriptado)

#8.1 Ejercicios resueltos de bucles while

##Crear un programa que permita al usuario procesar los montos de las compras de un cliente(se desconoce la cantidad de datos que cargará), 
#cortando el ingreso de datos cuando el usuario ingrese el monto 0.
#Si ingresa un monto negativo, no se debe de procesar y se debe pedir que proporcione un nuevo monto. 
#Al finalizar, informar el total a pagar teniendo en cuenta que, si las ventas superan el total de
#$1000, se le debe aplicar un 10% de descuento"""
    def montos(self):
        print("\n")
        print("\t8.1 Ejercicios resueltos de bucles while ")
        print("\n")
        total=0
        monto=float(input("Monto de una venta: $"))
        while monto!=0:
            if monto<0:
                print("Monto no válido")
            else:
                total+=monto
            monto=float(input("Monto de una venta: $"))
        if total>1000:
            total-=total*0.1
        print("Monto total a pagar: $", total)

#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada 
#número, informar cuántos dígitos pares y cuántos impares tiene.
#Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total"""
    def parEimpar(self):
        print("\n")
        totalPares=0
        totalImpares=0
        num=int(input("Número: "))
        while num!=0:
            pares=0
            impares=0
            while num!=0:
                ultimoDigito=num%10
                if ultimoDigito%2==0:
                    pares+=1
                    totalPares+=1
                else:
                    impares+=1
                    totalImpares+=1
                num=num//10
            print("El número ingresado tiene",pares,"dígitos pares y", impares,"dígitos impares")
            num=int(input("Número: "))
        print("Total de dígitos pares: ", totalPares)
        print("Total de dígitos imapres: ",totalImpares)

#Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string "*" (asterisco). Cada vez que el usuario ingrese un string de longitud 1
#que contenga sólo una barra ("/") se considera que termina en una línea.
#Por cada linea completa, informar cuántos dígitos numéricos(del 0 al 9) aparecieron en total(en todos los títulos de libros que componen esa línea). Finalmente, informar cuántas líneas completas se ingresaron.
#Ejemplo de ejecución:
#Libro: Los 3 mosqueteros
#Libro: Historia de 2 ciudades
#Libro: /
#Línea completa. Aparecen 2 dígitos numéricos.
#Libro:20000 leguas de viaje submarino
#Libro: El señor de los anillos
#Libro: /
#Línea completa. Aparecen 5 dígitos numéricos.
#Libro: 20 años después
#Libro:*
#Fin. Se leyeron 2 líneas completas. """
    def Libros(self):
        print("\n")
        digitosEnLaLinea=0
        cantLineas=0
        titulo=input("Título del libro: ")
        while titulo!="*":
            if titulo=="/":
                cantLineas+=1
                print("Linea Compelta. Aparecen", digitosEnLaLinea, "dígitos")
                digitosEnLaLinea=0
            else:
                for caracter in titulo:
                    if caracter in "0123456789":
                        digitosEnLaLinea+=1
            titulo=input("Título del libro: ")
        print("Fin. Se leyeron", cantLineas, "líneas completas")

#8.2 Ejercicio resuelto de bucles while

#Analizar el código mostrado a continuación y, sin ejecutarlos previamente, describir que hace. 
#¿Qué salida se mostraría en pantalla si se ejecuta el programa sucesivamente con los siguientes datos?
#1.Frase: "  hola buen  día"
#2.Frase: ""
#3.Frase:"1234"
#4.Frase: "hola ¡buen día!"
    def palabraMasLarga(self):
        print("\n")
        print("\t8.2 Ejercicio resuelto de bucles while ")
        print("\n")
        frase1=input("Frase: ")
        frase1=frase1.strip()
        cantidad1=0
        len_p_mas_larga=0
        while len(frase1) !=0:
            cantidad1=cantidad1+1
            i=frase1.find(" ")
            if i != -1:
                palabra=frase1[0:i]
                while i < len(frase1) and frase1[i]==" ":
                    i=i+1
                frase1=frase1[i:]
            else:
                palabra=frase1
                frase1=""
            if len(palabra)>len_p_mas_larga:
                len_p_mas_larga=len(palabra)
                p_mas_larga=palabra
        if cantidad1>0:
            print("Palabra más larga:", p_mas_larga)
        print("Cantidad de palabras: ", cantidad1)

#9.1 Ejercicios resueltos de break/continue en bucles

#Elegir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se  reciba un cero. 
#Imprimir la cantidad total de números primos ingresos. Nota: un número primo es un número natural mayor que 1 que tiene únicamente dos divisores: él mismo y el 1. """
    def Primos(self):
        print("\n")
        print("\t9.1 Ejercicios resueltos de break/continue en bucles ")
        print("\n")
        cantidad=0
        n=int(input("Ingrese un número: "))
        while n!=0:
            primo=True
            for i in range (2,n):
                if n%i==0:
                    primo=False
                break
            if primo:
                cantidad += 1
            n=int(input("Ingrese un número: "))
        print("Primos: ", cantidad)

# Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años bisiestos en ese rango, que sean bisiestos y míltiplos de 10.
# Nota: para que un año sea bisiesto debe de ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400."""
    def Bisiesto(self):
        print("\n")
        anioInicio= int(input("Ingrese el año inicial: "))
        anioFin= int(input("Ingrese el año final: "))
        for anio in range (anioInicio, anioFin+1):
            if not anio % 10 == 0:
                continue
            if not anio % 4 == 0:
                continue
            if anio % 100 != 0 or anio % 400 == 0:
                print(anio) 

#10.1 Ejemplos de funciones

#Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. 
# Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). 
# Al finalizar el programa, mostrar el factorial del mayor número ingresado.
    def primo(num):
        for i in range(2,num):
            if num%i==0:
                return False
        return True
 
    def frecuencia(numero,digito):
        cantidad=0
        while numero!=0:
            ultDigito=numero%10
            if ultDigito==digito:
                cantidad+=1
            numero=numero//10
        return cantidad
        
    def factorial(numero):
        f=1
        if numero!=0:
            for i in range(1,numero+1):
                f=f*i
        return f

    def sumaDigitos(numero):
        suma=0
        while numero!=0:
            digito=numero%10
            suma=suma+digito
            numero=numero//10
        return suma  
    
    mayor=0
    print("\n")
    print("\t10.1 Ejemplos de funciones")
    print("\n")
    numero=int(input("Número primo: "))
    while primo(numero):
        print("Suma de los dígitos:",sumaDigitos(numero))
        digito=int(input("Dígito: "))
        print("El",digito,"aparece",frecuencia(numero,digito),"veces")
        if numero > mayor:
            mayor=numero
        numero=int(input("Número primo: "))
    print("Factorial de",mayor,":",factorial(mayor))

#10.3 Ejercicios resueltos de funciones 

# Determinar cual es la salida en pantalla si se ingresan los valor x=6, y=7"""

    def coordenadaZ (x,y):
        x = x + 10
        y = y + 15
        return x + y
#programa principal
    print("\n")
    print("\t10.3 Ejercicios resueltos de funciones")
    print("\n")
    x = int(input("Coordenada eje x: "))
    y = int(input("Coordenada eje y: "))
    for i in range(3):
        z = coordenadaZ (x,y)
        x = x + 1
        y = y + 1
    print (x, " . ", y)

#¿Qué sucede si los nombres de los parámetros dentro de la función se cambian y ahora se utilizan los nombres a,b en lugar de los nombres x,y?"""
#Cambiar el nombre de los parámetros no afecta en nada, porque el valor retornado  por la función no se esta usando en el programa principal

#El siguiente programa debería imprimir el número 2 si se le ingresan como valores  x=5, y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?"""

    # def maximo(a,b):
    #     if x>y:
    #         return x
    #     else:
    #         return y
    # def minimo(a,b):
    #     if x<y:
    #         return x
    #     else:
    #         return y
    # #programa principal
    # x = int(input("Un número: "))
    # y = int(input("Otro número: "))
    # print(maximo(x-3, minimo(x+2, y-5)))

#R// Las funciones no utlizan sus parámetros a,b sino las variables globales x,y. Para corregir el error se deben utlizar los parámetros dentro del cuerpo de ambas funciones:
    def maximo(a,b):
        if a>b:
            return a
        else:
            return b
    def minimo(a,b):
        if a<b:
            return a
        else:
            return b
    #programa principal
    print("\n")
    x = int(input("Un número: "))
    y = int(input("Otro número: "))
    print(maximo(x-3, minimo(x+2, y-5)))

#10.4 Ejercicios resueltos de funciones

#Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos"""
    def validaDNI():
        print("\n")
        print("\t10.4 Ejercicios resueltos de funciones ")
        print("\n")
        num = input('Digite su identificación: ')
        if len(num)>=7 and len(num)<=8:
            return True
        else:
            return False
    print(validaDNI())

#Escribir una función que, dado un string, retorne la longitud de la última palabra.Se considera que las palabras están separadas por uno o más espacios. También podría 
#haber espacios al principio o al final del string pasado por parámetro"""
    print("\n")
    frase = str(input('Escriba una frase: '))
    def len_ultima_palabra(str):
        longitud = 0
        str = str.strip()
        for i in str:
            if not i.isspace():
                longitud += 1
            else:
                longitud = 0
        return(longitud)
    print(len_ultima_palabra(frase))

#Escribir un programa que permita al usuario obtener un identificador para cada uno de los  socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio, indicando
# que finalizará el procedimiento mediante el ingreso de un nombre vacio. 
# Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más  de un nombre, en cuyo caso será: nombre1 nombre2 apellido. Si un socio tuviera más de un apellido, 
# el usuario sólo ingresará uno.
# Se debe validar que el número de DNI tnega 7 u 8 dígitos. En caso contrario, el programa debe dejar  al usuario en un bucle hasta que ingrese un DNI correcto. 
# Por cada socio se debe de imprimir su indentificador único, el cual estará formado por: el primer  nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su DNI. Ejemplo
# Nombre: Alba María Linares
# DNI: 25834910
# Alba7258"""
    def Club(self):
        print("\n")
        nombre = input ("Nombre del socio: ")
        while nombre!= " ":
            dni = int(input("DNI del socio: "))
            while not (DNIvalido(dni)):
                print("Número inválido")
                dni = int(input("DNI del socio: "))
            identificador = obtenerIdentificador(nombre,dni)
            print("El identificador del socio es: ", identificador)
            nombre = input("Nombre del socio: ")

#11.1 Ejercicios resueltos de listas y tuplas"""

# 1. Solicitar al usuario que ingrese números, los cuales se guardarán en una lista.  Fianlizar al ingresar el número 0, el cal no debe de guardarse. 
# 2. Acontinuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
# 3. Imprimir la sumatoria de todos los números de la lista.
# 4. Solicitar al usuario otro número y  rear una lista con los elementos de la lista  original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
# 5. Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original t la cantidad de veces que aparece en ella. 
# Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: 
# [(5,3), (16,1),(2,2),(57,1)]
    def usuarioLista(self):
        #1
        print("\n")
        numeros = []
        nro = int(input("Número: "))
        while nro !=0:
            numeros.append(nro)
            nro = int(input("Números: "))

        #2
        eliminar = int(input("Número a eliminar: "))
        if eliminar in numeros:
            numeros.remove(eliminar)
        else: 
            print("Ese número no está entre los ingresados")

        #3
        print("Sumatoria de los numeros:", sumatoria(numeros))

        #4
        limite = int(input("Filtrar los números menores a: "))
        for n in numeroMenores(numeros, limite):
            print(n)

        #5
        print("Frecuencias: ")
        for tupla in frecuencias(numeros):
            print(tupla[0], "aparece", tupla[1], "veces")

#Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con las siguiente forma: (nombre, dni, destino). 
#Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Liboa"]
#Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertencen. Ejemplo:
#[("Buenos Aires","Argentina"), ("Glasgow","Escocia"),("Lisboa","Portugal"), ("Liverpool", "Inglaterra"), ("Madrid","España")]
#Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
#-Agregar pasajeros a la lista de viajeros
#-Agregar ciudades a la lista de ciudades
#-Dado el DNI de un pasajero, ver a qué ciudad viaja
#-Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad
#-Dado el DNI de un pasajero, ver a qué país viaja
#-Dado e¡un país, mostrar cuántos pasajeris viajan a ese país
#-Salir del programa
    def destino(self):
        print("\n")
        pasajeros=[("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Liboa")]
        ciudades=[("Buenos Aires","Argentina"), ("Glasgow","Escocia"),("Lisboa","Portugal"), ("Liverpool", "Inglaterra"), ("Madrid","España")]
        while True:
            print("1. Agregar pasajeros")
            print("2. Agregar ciudades")
            print("3. Buscar ciudad destino mediante el DNI")
            print("4. Cantidad de pasajeros que viajan a una ciudad")
            print("5. Buscar país destino mediante DNI")
            print("6. Cantidad de pasajeros que viajan a un país")
            print("7. Salir del programa")
            opcion = int(input("Acción de ejecutar: "))
            if opcion==1:
                print("AGREGAR PASAJEROS")
                pasajeros=agregarPasajeros(pasajeros)
            elif opcion==2:
                print("AGREGAR CIUDADES")
                ciudades=agregarCiudades(ciudades)
            elif opcion==3:
                dni=int(input("DNI: "))
                print("El pasajero viaja a", buscarCiudad(pasajeros, dni))
            elif opcion==4:
                ciudad=input("Ciudad: ")
                print("Viajan", cantidadPasajerosCiudad(pasajeros, ciudad), "pasajeros")
            elif opcion==5:   
                dni=int(input("DNI: "))
                print("Viaja a", buscarPaisDestino(pasajeros, ciudades , dni))
            elif opcion==6:
                pais=input("País: ")
                print("Viajan", cantidadPasajerosPais(pasajeros, ciudades, pais), "pasajeros")
            elif opcion==7:
                break
            else:
                print("Opción inválida") 

#12.1 Ejercicios resueltos de conjuntos

#Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar "x". A continuación, solicitar
#que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar "x".
#1. Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.
#2. Informar que nombres se repiten entre los alumnos de nivel primario y secundario.
#3. Informar que nombres de nivel primario no se repiten en los de nivel secundario.
    def escuela(self):
        print("\n")
        print("\t12.1 Ejercicios resueltos de conjuntos")
        print("\n")
        primaria = set()
        secundaria = set()

        print("ALUMNOS DE PRIMARIA")
        primaria = cargarNombres(primaria)

        print("ALUMNOS DE SECUNDARIA")
        secundaria = cargarNombres(secundaria)

        print("NOMBRES DE TODOS LOS ALUMNOS:")
        for nombre in primaria|secundaria:
            print(nombre)

        print("NOMBRES COMUNES:")
        for nombre in primaria&secundaria:
            print(nombre)

        print("NOMBRES DE PRIMARIA QUE SE REPITEN EN SECUNDARIA:")
        for nombre in primaria-secundaria:
            print(nombre)

#Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual contiene tuplas con información de cada venta: 
#(cliente, dia del mes, monto, domicilio del cliente). Ejemplo:
#[("Nuria Costo", 5, 12780.78, "Calle Las Flotes 355"), ("Jorge Russo", 7,"Mirasol 218" ), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
#Escribir una funcion que reciba como parametro una lista con el formato mencionado anteriormente y retorne los domicilios de cada cleinte al cual se le debe de enviar una factura de compra.
#Notar que cada cliente puede haber hecho mas de una compra en el mes, por lo que la funcion debe retornar una estructura que contenga cada domicilio una sola vez."""
    def direcciones(ventas):
        print("\n")
        domicilios=set()
        for venta in ventas:
            domicilios.add(venta[3])
        return domicilios

#13.1 Ejercicios resueltos con diccionarios

#Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. 
#Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo:
#"r": 5
#"%": 3
#"a":8
#"9":1
#¿Cómo podrían informar las ocurrencias de las letras del alfabeto únicamente, incluyendo el valor 0 para las que no aparecieron?"""
    def strings(self):
        print("\n")
        print("\t13.1 Ejercicios resueltos con diccionarios")
        print("\n")
        contadores={}
        alfabeto="abcdefghijklmnñopqrstuvwxyz"
        for letra in alfabeto+alfabeto.upper():
            contadores[letra]=0
        for i in range(2):
            cadena=input("Cadena de caracteres: ")
            for caracter in cadena:
                if caracter.lower() in alfabeto:
                    contadores[caracter]=1
                else:
                    contadores[caracter]+=1

        for caracter,cantidad in contadores.items():
            print(caracter, ":", cantidad)

#13.2 Ejercicio resuelto con diccionarios

#Crear un programa para gestionar datos de los socios de un club, permitiendo:
#-Cargar información de los socios en un diccionario para acceder por numero de socio. Los datos a almacenar son: numero, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al dia (s/n). 
#El programa debe de iniciar con los datos de los socios fundadores ya cargados:
#Socio nº1, Amanda Núñez, Ingresó: 17/03/2009, cuota al día.
#Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
#Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
#-Informar cantidad de socios del club. 
#-Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas. 
#-Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018.
#-Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
#-Imprimir el listado de socios completos.
    def Club2(self):
        socios_activos={1:["Amanda Núñez", "17032009", True], 2:["Bárbara Molina", "17032009", True], 3:["Lautaro Campos", "17032003", True]}

        print("***Cargar socios")
        socios_activos=cargarSocios(socios_activos)
        print("El club tiene", len(socios_activos),"socios")

        print("***Registrar pago de cuotas")
        numero=int(input("Número de socio: "))
        socios_activos[numero][2]=True

        print("***Modificando fecha de ingreso...")
        socios_activos=modificarFecha(socios_activos, "13032018", "14032018")

        print("***Eliminar socio:")
        nombre=input("Nombre y apellido: ")
        numero=numeroSocio(socios_activos, nombre)
        del socios_activos[numero]

        imprimirListado(socios_activos)


EjerciciosYoutube=Youtube()
EjerciciosYoutube.matrix()
EjerciciosYoutube.cena()
EjerciciosYoutube.fecha1()
EjerciciosYoutube.fecha2()
EjerciciosYoutube.fecha3()
EjerciciosYoutube.motociclistas()
EjerciciosYoutube.empresario()
EjerciciosYoutube.valorAbsoluto()
EjerciciosYoutube.CoincidenciaOno()
EjerciciosYoutube.candidatos()
EjerciciosYoutube.vocales()
EjerciciosYoutube.bisiesto()
EjerciciosYoutube.institutoIngles()
EjerciciosYoutube.sumatoria()
EjerciciosYoutube.multiplos3()
EjerciciosYoutube.factorial()
EjerciciosYoutube.fibonacci()
EjerciciosYoutube.positivosYnegativos()
EjerciciosYoutube.juego()
EjerciciosYoutube.montos()
EjerciciosYoutube.parEimpar()
EjerciciosYoutube.Libros()
EjerciciosYoutube.palabraMasLarga()
EjerciciosYoutube.Primos()
EjerciciosYoutube.Bisiesto()
EjerciciosYoutube.len_ultima_palabra()
EjerciciosYoutube.Club()
EjerciciosYoutube.usuarioLista()
EjerciciosYoutube.destino()
EjerciciosYoutube.escuela()
EjerciciosYoutube.direcciones()
EjerciciosYoutube.strings()
EjerciciosYoutube.Club2()
