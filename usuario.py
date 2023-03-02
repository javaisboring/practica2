import modulo

def aplicacion():
    filas = int( input("Diga el número de filas de la matriz: ") )
    columnas = int( input("Diga el número de columnas de la matriz: ") )
    print("Ahora introduciremos la matriz de {}x{}".format(filas, columnas))
    matriz=[]
    for i in range(filas):
        linea=[]
        for j in range(columnas):
            linea.append( int(input("Indique el valor de la columna [ {} ] en la fila [ {} ]: ".format(j+1, i+1)) ) )
        
        matriz.append(linea)
    print("Matriz recibida:")
    for i in matriz:
        print(i)
    print()
    print("Por Columnas", modulo.estadistica_por_columna(matriz), sep="\n" )
    print("Por Filas", modulo.estadistica_por_fila(matriz), sep="\n")

if __name__ == "__main__":
    aplicacion()
