from more_itertools import locate


def geraEspiral(fimLinha, fimColuna, listaPontos) :
    lista = []
    comecoLinha = 0
    comecoColuna = 0
    contador = 0
 
    total = fimLinha * fimColuna
 
    while (comecoLinha < fimLinha and comecoColuna < fimColuna) :
        if (contador == total) :
            break
 
        # pegar a primeira coluna das colunas restantes
        for i in range(comecoLinha, fimLinha) :
            lista.append(listaPontos[i][comecoColuna])
            contador += 1
        
        lista.append(listaPontos[i][comecoColuna]-1)
        comecoColuna += 1
 
        if (contador == total) :
            break
 
        # pegar a última linha das linhas restantes
        for i in range (comecoColuna, fimColuna) :
            lista.append(listaPontos[fimLinha - 1][i])
            contador += 1
        fimLinha -= 1
         
        if (contador == total) :
            break
 
        # pegar a última coluna das colunas restantes
        if (comecoLinha < fimLinha) :
            for i in range(fimLinha - 1, comecoLinha - 1, -1) :
                lista.append(listaPontos[i][fimColuna - 1])
                
                contador += 1
            fimColuna -= 1

        if (contador == total) :
            break
 
        # pegar a primeira linha das linhas restantes
        if (comecoColuna < fimColuna) :
            for i in range(fimColuna - 1, comecoColuna - 1, -1) :
                lista.append(listaPontos[comecoLinha][i])
                contador += 1    
            comecoLinha += 1
    
    return lista

def removeDuplicates(listofElements):
    uniqueList = []
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)

    return uniqueList

if __name__ == '__main__':
    listaPontos1 = [(39, 9), (40.375, 4.0), (40.375, 14.0), (42.0, 0.0), (42.0, 6.0), (42.0, 12.0), (42.0, 18.0), (48.5, 0.0), (48.5, 6.0), (48.5, 12.0), (48.5, 18.0), (55.0, 0.0), (55.0, 6.0), (55.0, 12.0), (55.0, 18.0), (56.625, 4.0), (56.625, 14.0), (58, 9)]
    linhas = 7
    colunas = 4
   
    
    listaX = [i[0] for i in listaPontos1]
    ant = []
    listaPosicao = []
    for i in range(len(listaX)):   
        atual = list(locate(listaX, lambda x: x == listaX[i]))
        if(atual != ant):
            listaPosicao.append(list(locate (listaX, lambda x: x == listaX[i])))
        ant = atual 
    
    for i in range(linhas):
        if len(listaPosicao[i]) < colunas:
            valor = colunas+1 - len(listaPosicao[i])
            
            for j in range(valor,1,-1):
                listaPosicao[i].insert(j,'')


    listaSaida = []
    listaSaida = geraEspiral(linhas, colunas, listaPosicao)
    listaSaida = list(filter(lambda a: a != '', listaSaida))

    
    listaZ = []
    listaZ = removeDuplicates(listaSaida)

    novaLista = []
    for i in range (len(listaPontos1)):
        novaLista.append(listaPontos1[listaZ[i]])
    

    print("novaLista: ",novaLista)


 