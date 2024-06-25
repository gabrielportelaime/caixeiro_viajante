# CAIXEIRO VIAJANTE

def caixeiro(vertices_visitados = [0], arestas_visitadas = [], custo_atual = 0, valor_atual = 0, no_atual = 0):
    # PERCORRE TODOS OS VÉRTICES ADJACENTES AO VÉRTICE ATUAL
    for i in range(vertices):
        # VERIFICA SE É DIFERENTE DO NÓ ATUAL E VERIFICA SE HÁ ARESTA ENTRE NÓ ATUAL E O NÓ I
        if(i != no_atual and matriz_adjacencia[no_atual][i] > 0):
            # ATUALIZA O CUSTO E O VALOR CASO PASSE POR ESSE VÉRTICE
            custo_operacao = matriz_adjacencia[no_atual][i] + custo_atual
            valor_operacao = valor_atual + valores[i]
            # CONTINUA SE A INCLUSÃO DO VÉRTICE AINDA ESTÁ NO ORÇAMENTO
            if(custo_operacao <= orcamento):
                # CONTINUA APENAS SE A ARESTA NÃO FOI USADA ANTES
                if(set([no_atual, i]) not in arestas_visitadas):
                    # CONTINUA APENAS SE O VÉRTICE NÃO FOI ANTES VISITADO
                    if(i not in vertices_visitados):
                        # INCLUI O VÉRTICE E ARESTA COMO VISITADOS
                        vertices_visitados.append(i)
                        arestas_visitadas.append(set([no_atual, i]))
                        caixeiro(vertices_visitados[:], arestas_visitadas[:], custo_operacao, valor_operacao, i)
                        # REMOVE O VÉRTICE E ARESTA DEPOIS DE CHAMAR O MÉTODO
                        vertices_visitados.pop(-1)
                        arestas_visitadas.pop(-1)
                    elif(i == 0):
                        # SE O VÉRTICE DESTINO JÁ FOI VISITADO MAS É O PRIMEIRO VÉRTICE ENTÃO FINALIZA O CAMINHO
                        caminho_final = vertices_visitados[:]
                        caminho_final.append(0)
                        completos.append([caminho_final, custo_operacao, valor_operacao])
orcamento = 10

valores = [10, 20, 30, 40]
# PREENCHER COM O CUSTO CASO HAJA UMA ARESTA ENTRE I E J 
# PREENCHER COM ZERO CASO NÃO HAJA ARESTA ENTRE I E J
matriz_adjacencia =[[0, 1, 2, 5], 
                    [1, 0, 6, 4], 
                    [2, 6, 0, 4], 
                    [5, 4, 4, 0]]
vertices = len(matriz_adjacencia)
completos = []

letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

caixeiro()
# #IMPRIME TODOS OS CAMINHOS QUE SATISFAZEM:
# #   1) COMEÇAM NO VÉRTICE A E TERMINAM NO VÉRTICE A; 
# #   2) OBEDECEM AO VALOR DO ORÇAMENTO;
# print('------------------------------------------------------------------')
# print('TODOS OS CAMINHOS:')
# print('------------------------------------------------------------------')
# for i in range(len(completos)):
#     print('Caminho:', ' '.join([letras[x] for x in completos[i][0]]))
#     print('Custo: ', completos[i][1])
#     print('Valor: ', completos[i][2], end="\n\n")
# print('------------------------------------------------------------------')

#VALOR ÓTIMO
#IMPRIME QUALQUER CAMINHO QUE SATISFAZ:
#   1) COMEÇAM NO VÉRTICE A E TERMINAM NO VÉRTICE A; 
#   2) OBEDECEM AO VALOR DO ORÇAMENTO;
#   3) TEM O MENOR VALOR DE CUSTO;
completos.sort(key = lambda x:x[1])
i = 0
print('------------------------------------------------------------------')
print('VALOR ÓTIMO:')
print('------------------------------------------------------------------')
print('Caminho:', ' '.join([letras[x] for x in completos[i][0]]))
print('Custo mínimo:', completos[i][1])
print('Valor:', completos[i][2])
print('------------------------------------------------------------------')

#VALOR MÁXIMO
#IMPRIME QUALQUER CAMINHO QUE SATISFAZ:
#   1) COMEÇAM NO VÉRTICE A E TERMINAM NO VÉRTICE A; 
#   2) OBEDECEM AO VALOR DO ORÇAMENTO; 
#   3) TEM O MAIOR VALOR;
completos.sort(key = lambda x:x[2], reverse=True)
i = 0
print('VALOR MÁXIMO:')
print('------------------------------------------------------------------')
print('Melhor caminho:', ' '.join([letras[x] for x in completos[i][0]]))
print('Custo:', completos[i][1])
print('Valor máximo:', completos[i][2])
print('------------------------------------------------------------------')