# CAIXEIRO VIAJANTE

def caixeiro(visitados = [], custo_atual = 0, valor_atual = 0, no_atual = 0):
    visitados.append(no_atual)
    if(len(visitados) > 1 and visitados[-1] == 0):
        completos.append([visitados, custo_atual, valor_atual])
        return 0        
    for i in range(vertices):
        custo_operacao = matriz_adjacencia[no_atual][i] + custo_atual
        if(i != no_atual and custo_operacao <= orcamento and (i not in visitados or i == 0)):
            valor_operacao = valor_atual + valores[i]
            caixeiro(visitados, custo_operacao, valor_operacao, i)

orcamento = 10
valores = [10, 20, 30, 40]
matriz_adjacencia =[[0, 1, 2, 5], 
                    [1, 0, 6, 4], 
                    [2, 6, 0, 4], 
                    [5, 4, 4, 0]]
vertices = len(matriz_adjacencia)
completos = []

caixeiro()
print(completos)