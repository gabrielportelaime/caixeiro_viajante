# CAIXEIRO VIAJANTE

def caixeiro(visitados, custo_atual, no_atual):
    if(len(visitados) > 0 and visitados[-1] == 0):
        completos.append(visitados)
        return 0
    

completos = []
orcamento = 10
valores = [10, 20, 30, 40]
matriz_adjacencia =[[0, 1, 2, 5], 
                    [1, 0, 6, 4], 
                    [2, 6, 0, 4], 
                    [5, 4, 4, 0]]

tamanho = len(matriz_adjacencia)

if(len(completos) == 0):
    print('0')
else:
    print(max())