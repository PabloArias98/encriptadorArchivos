def encriptar(contenido):
    contenidoFinal = ''
    for pos in contenido:
        contenidoFinal += pos + 'x'
    return contenidoFinal

def aleatorioEncriptar(contenido):
    contenidoFinal = ''
    for pos in contenido:
        ascii = ord(pos)
        ascii += 1
        contenidoFinal += chr(ascii)
    return contenidoFinal


def desencriptar(contenido):
    contenidoFinal = ''
    contador = 0
    for pos in contenido:
        if contador % 2 == 0:
            #Si el número es par lo va a agregar sino no
            contenidoFinal += pos
        contador += 1
    return contenidoFinal

def aleatorioDesencriptar(contenido):
    contenidoFinal = ''
    for pos in contenido:
        ascii = ord(pos)
        ascii -= 1
        contenidoFinal += chr(ascii)
    return contenidoFinal


print("Bienvenido al Encriptador de Archivos v1.0")
print("1 - Encriptar archivo mediante equis (simple)")
print("2 - Desencriptar archivo mediante equis (simple)")
print("3 - Encriptar archivo mediante aleatorio (avanzado)")
print("4 - Desencriptar archivo mediante aleatorio (avanzado)")

resp = int(input("Elige: "))
rutaArchivo = input("Elige la ruta del archivo: ")

if (resp == 1):
    archivo = open(rutaArchivo, "r")
    contenido = archivo.read()
    archivo.close()
    contenidoEncriptado = encriptar(contenido)
    print("El archivo se ha encriptado correctamente!")
    archivo = open("textoEncriptado.txt", "w")
    archivo.write(contenidoEncriptado)
    archivo.close()

    print("El texto encriptado es: "+contenidoEncriptado)

elif (resp == 2):
    archivo = open(rutaArchivo, "r")
    contenido = archivo.read()
    contenidoDesencriptado = desencriptar(contenido)
    archivo.close()
    print("El archivo se ha desencriptado correctamente!")
    archivo = open("textoDesencriptado.txt", "w")
    archivo.write(contenidoDesencriptado)
    archivo.close()

    print("El texto desencriptado es: "+contenidoDesencriptado)

elif (resp == 3):
    archivo = open(rutaArchivo, "r")
    contenido = archivo.read()
    archivo.close()
    contenidoEncriptado = aleatorioEncriptar(contenido)
    print("El archivo se ha encriptado correctamente!")
    archivo = open("textoEncriptado.txt", "w")
    archivo.write(contenidoEncriptado)
    archivo.close()

    print("El texto encriptado es: "+contenidoEncriptado)

elif (resp == 4):
    archivo = open(rutaArchivo, "r")
    contenido = archivo.read()
    contenidoDesencriptado = aleatorioDesencriptar(contenido)
    archivo.close()
    print("El archivo se ha desencriptado correctamente!")
    archivo = open("textoDesencriptado.txt", "w")
    archivo.write(contenidoDesencriptado)
    archivo.close()

    print("El texto desencriptado es: "+contenidoDesencriptado)

else:
    print("no ha elegido respuesta válida")




