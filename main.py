def encriptar(contenido):
    contenidoFinal = ''
    for pos in contenido:
        contenidoFinal += pos + 'x'
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


print("Bienvenido al Encriptador de Archivos v1.0")
print("1 - Encriptar archivo")
print("2 - Desencriptar archivo")
resp = int(input("Elige: "))

if (resp == 1):
    archivo = open("archivoAEncriptar.txt", "r")
    contenido = archivo.read()
    archivo.close()
    contenidoEncriptado = encriptar(contenido)

    archivo = open("textoEncriptado.txt", "w")
    archivo.write(contenidoEncriptado)
    archivo.close()

elif (resp == 2):
    archivo = open("textoEncriptado.txt", "r")
    contenido = archivo.read()
    contenidoDesencriptado = desencriptar(contenido)
    archivo.close()

    archivo = open("textoDesencriptado.txt", "w")
    archivo.write(contenidoDesencriptado)
    archivo.close()

else:
    print("no ha elegido respuesta válida")



# arch = open("archivoAEncriptar.txt", "w")
# arch.write("JAAJAJAJAJJAAJAJJA")
# arch.close()

# arch = open("archivoAEncriptar.txt", "r")
# print(arch.read())
# arch.close()



