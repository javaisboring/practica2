def estadistica_por_fila(matriz:list, fila:int=None)->list:
    if fila==None: # todas
        retorno=""
        posicion=1
        for i in matriz:
            minima = (min(i))
            maxima = (max(i))
            promedio = (sum(i)/len(i))
            retorno+=("{} --> Mínima: {} Máxima: {} Promedio: {}\n".format(posicion, minima, maxima, round(promedio, 2) ))
            posicion+=1
        return retorno
    else:
        minima = (min(matriz[fila]))
        maxima = (max(matriz[fila]))
        promedio = (sum(matriz[fila])/len(matriz[fila]))
        return "Mínima: {} \nMáxima: {} \nPromedio: {}".format(minima, maxima, round(promedio, 2) )

def estadistica_por_columna(matriz:list, columna:int=None)->list:
    if columna==None: # todas
        retorno=""
        posicion=1
        for j in range(len(matriz[0])):
            minima=None
            maxima=None
            suma=0
            for i in range(len(matriz)):
                if minima==None:
                    minima = matriz[i][j]
                    maxima = matriz[i][j]
                elif minima > matriz[i][j]:
                    minima = matriz[i][j]
                if matriz[i][j] > maxima:
                    maxima = matriz[i][j]
                suma+=matriz[i][j]
            retorno+=("{} --> Mínima: {} Máxima: {} Promedio: {}\n".format(posicion, minima, maxima, round(suma/len(matriz), 2) ))
            posicion+=1
        return retorno
    else:
        retorno=""
        minima=None
        maxima=None
        suma=0
        for i in range(len(matriz)):
            if minima==None:
                minima = matriz[i][columna]
                maxima = matriz[i][columna]
            elif minima > matriz[i][columna]:
                minima = matriz[i][columna]
            if matriz[i][columna] > maxima:
                maxima = matriz[i][columna]
        suma+=matriz[i][columna]
        return ("Mínima: {} \nMáxima: {} \nPromedio: {}\n".format(minima, maxima, round(suma/len(matriz), 2) ))

if __name__ =='__main__':
    print( estadistica_por_columna([ [1,2,3] , [4,5,6] , [2,3,4] ]) )
    print( estadistica_por_fila([ [1,2,3] , [4,5,6] , [2,3,4] ]) )
    print( estadistica_por_columna([ [1,2,3] , [4,5,6] , [2,3,4] ],1) )
    print( estadistica_por_fila([ [1,2,3] , [4,5,6] , [2,3,4] ],1) )
