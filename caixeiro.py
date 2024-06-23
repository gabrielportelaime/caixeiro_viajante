# CAIXEIRO VIAJANTE

def caixeiro(vertices_visitados = [0], arestas_visitadas = [], custo_atual = 0, valor_atual = 0, no_atual = 0):
    for i in range(vertices):
        if(i != no_atual):
            custo_operacao = matriz_adjacencia[no_atual][i] + custo_atual
            valor_operacao = valor_atual + valores[i]
            if(custo_operacao <= orcamento):
                if(set([no_atual, i]) not in arestas_visitadas):
                    if(i not in vertices_visitados):
                        vertices_visitados.append(i)
                        arestas_visitadas.append(set([no_atual, i]))
                        caixeiro(vertices_visitados[:], arestas_visitadas[:], custo_operacao, valor_operacao, i)
                        vertices_visitados.pop(-1)
                        arestas_visitadas.pop(-1)
                    elif(i == 0):
                        caminho_final = vertices_visitados[:]
                        caminho_final.append(0)
                        completos.append([caminho_final, custo_operacao, valor_operacao])
                    
orcamento = 10
valores = [10, 20, 30, 40]
matriz_adjacencia =[[0, 1, 2, 5], 
                    [1, 0, 6, 4], 
                    [2, 6, 0, 4], 
                    [5, 4, 4, 0]]
vertices = len(matriz_adjacencia)
completos = []

caixeiro()
for i in range(len(completos)):
    print('Caminho:', ' '.join([str(x) for x in completos[i][0]]))
    print('Custo total: ', completos[i][1])
    print('Valor total: ', completos[i][2], end="\n\n")