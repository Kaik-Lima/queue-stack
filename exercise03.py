#  Implemente uma função para reverter uma string usando uma pilha.

import queue


def reverter(expressao):
    pilha = queue.LifoQueue()
    if not pilha.qsize():
        for x in expressao:
            pilha.put(x)
        for c in expressao:
            print(pilha.get(), end='')
    return pilha.qsize() == 0

reverter('dado cabra')
