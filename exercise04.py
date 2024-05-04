# A fila de prioridade (priority queue) pode ser usada facilmente para ordenar uma sequência qualquer de números.
# Como você faria isso? Analise as propriedades dessa estrutura de dados e implemente uma função que recebe
# uma lista de números e retorna essa lista ordenada via a ação de uma fila de prioridade. Exemplo:

import queue


def prioridade(expr):
    fila = queue.PriorityQueue()
    # Enfileirando
    n = expr.split()

    for contador in n:
        fila.put(int(contador))
    # Desenfilerando
    for contador in n:
        print(fila.get(contador), end= ' ')

prioridade('7 -1 5 2 14 -13')
