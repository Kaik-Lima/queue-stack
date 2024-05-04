# Crie um programa Python que avalie uma expressão matemática na forma pós-fixa (ou notação polonesa reversa) usando uma pilha.
# A expressão pós-fixa é uma notação onde os operadores seguem seus operandos e dispensa parênteses.

import queue


def posfixa(expr):
    operadores = '+' '-' '*' '/'
    pilha = queue.LifoQueue()
    valores = expr.split()
    print('valores', valores)
    for c in valores:
        if c in operadores:
            x = f'{pilha.get()} {c} {pilha.get()}'
            print(x)
            calculo = eval(x)
            print(calculo)
            pilha.put(calculo)
        else:
            pilha.put(c)
        print('c', c)
    return pilha.get()

a = posfixa('7 4 - 3 * 16 2 / -')
print('Resultado da expressao: ', a)