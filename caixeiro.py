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

letras = 'abcdefghijklmnopqrstuwxyz'

caixeiro()
# #IMPRIME TODOS OS CAMINHOS QUE SATISFAZEM:
# #   1) COMEÇAM EM 0 E TERMINAM EM 0; 
# #   2) OBEDECEM AO VALOR DO "ORÇAMENTO";
# print('------------------------------------------------------------------')
# print('TODOS OS CAMINHOS:')
# print('------------------------------------------------------------------')
# for i in range(len(completos)):
#     print('Caminho:', ' '.join([letras[x] for x in completos[i][0]]))
#     print('Custo total: ', completos[i][1])
#     print('Valor total: ', completos[i][2], end="\n\n")
# print('------------------------------------------------------------------')

#VALOR ÓTIMO
#IMPRIME QUALQUER CAMINHO QUE SATISFAZ:
#   1) COMEÇAM EM 0 E TERMINAM EM 0; 
#   2) OBEDECEM AO VALOR DO "ORÇAMENTO"; 
#   3) TEM O MENOR VALOR DE CUSTO;
completos.sort(key = lambda x:x[1])
i = 0
print('------------------------------------------------------------------')
print('VALOR ÓTIMO:')
print('------------------------------------------------------------------')
print('Caminho:', ' '.join([letras[x] for x in completos[i][0]]))
print('Custo mínimo: ', completos[i][1])
print('Valor: ', completos[i][2])
print('------------------------------------------------------------------')

#VALOR MÁXIMO
#IMPRIME QUALQUER CAMINHO QUE SATISFAZ:
#   1) COMEÇAM EM 0 E TERMINAM EM 0; 
#   2) OBEDECEM AO VALOR DO "ORÇAMENTO"; 
#   3) TEM O MAIOR VALOR;
completos.sort(key = lambda x:x[2], reverse=True)
i = 0
print('VALOR MÁXIMO:')
print('------------------------------------------------------------------')
print('Melhor caminho:', ' '.join([letras[x] for x in completos[i][0]]))
print('Custo: ', completos[i][1])
print('Valor máximo: ', completos[i][2])
print('------------------------------------------------------------------')