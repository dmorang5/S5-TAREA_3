
def sumatoria(lista):
    suma=0
    for n in lista:
        suma += n
    return suma

def numeroMenores(lista, limite):
    nueva=[]
    for n in lista:
        if n<limite:
            nueva.append(n)
    return nueva

def frecuencias(lista):
    nueva=[]
    for n in lista:
        if (n, lista.count(n)) not in nueva:
            nueva.append((n, lista.count(n)))
    return nueva

def agregarPasajeros(pasajeros):
    nombre = input("Nombre -x para cortar: ")
    while nombre!="x":
        dni=int(input("DNI: "))
        destino = input("Ciudad destino: ")
        pasajeros.append((nombre, dni, destino))
    nombre = input("Nombre -x para cortar: ")
    return pasajeros

def agregarCiudades(ciudades):
    ciudad=input("Ciudad -x para cortar: ")
    while ciudad!="x":
        pais=input("Pais: ")
        ciudades.append((ciudad, pais))
        ciudad=input("Ciudad -x para cortar: ")
    return ciudades

def buscarCiudad(pasajeros, dni):
    for viaje in pasajeros:
        if viaje[1]==dni:
            return viaje[2]
    return ""

def cantidadPasajerosCiudad(pasajeros,ciudad):
    cantidad=0
    for viaje in pasajeros:
        if viaje [2]==ciudad:
            cantidad+=1
    return cantidad

def buscarPaisDestino(pasajeros, ciudades, dni):
    ciudadBuscada=buscarCiudad(pasajeros,dni)
    for ciudad in ciudades:
        if ciudad[0]==ciudadBuscada:
            return ciudad[1]
    return ""

def cantidadPasajerosPais(pasajeros,ciudades,pais):
    cantidad=0
    for viaje in pasajeros:
        if pais==buscarPaisDestino(pasajeros, ciudades, viaje[1]):
            cantidad+=1
    return cantidad

def cargarNombres(alumnos):
    nombre=input("Nombre: ")
    while nombre!="x":
        alumnos.add(nombre)
        nombre=input("Nombre: ")
    return alumnos

def DNIvalido(dni):
    cantidad = 0
    while dni !=0:
        cantidad = cantidad+1
        dni=dni//10
    return cantidad==7 or cantidad==8

def lenUltimaPalabra(cadena):
    longitud = len(cadena)
    if longitud == 0:
        return 0
    cantidad=0
    for i in range (longitud):
        if cadena[i]!=" ":
            cantidad=cantidad+1
        else:
            if cadena[i]==" " and i <(longitud-1) and cadena [i+1] !=" " :
                cantidad = 0
    return cantidad

def primerosTresDigitos(numero):
    while numero >= 1000:
        numero = numero / 10
    return int (numero)

def obtenerIdentificador(nombre,dni):
    nombre = nombre.strip()
    i = nombre [0:nombre.find(" ")]
    i = i + str(lenUltimaPalabra(nombre))
    i = i + str(primerosTresDigitos(dni))
    return i

def cargarSocios(socios):
    numero=int(input("Numero del socio: "))
    while numero!=0:
        nombre=input("Nombre y apellido: ")
        fecha=input("Fecha de ingreso: ")
        cuota=input("¿Cuota al día? s/n: ")
        pago=cuota.lower()=="s"
        socios[numero]=[nombre,fecha,pago]
        numero=int(input("Numero de socio: "))
    return socios

def modificarFecha(socios, fecha_anterior, fecha_nueva):
    for datos in socios.values():
        if datos[1]==fecha_anterior:
            datos[1]=fecha_nueva
    return socios

def numeroSocio(socios, nombre):
    for numero,datos in socios.items():
        if datos[0].lower()==nombre.lower():
            return numero
    return 0

def formatoFecha(fecha):
    return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

def imprimirListado(socios):
    for numero,datos in socios.items():
        print("-Número: ",numero)
        print("-Nombre: ",datos[0])
        print("-Fecha de ingreso: ",formatoFecha(datos[1]))
        if datos [2]:
            print("-Cuota al dia")
        else:
            print("-En deuda")
        print("--------")
    return None
