# Refaça o problema "Verificação de Expressão Matemática" mas agora com o uso da classe queue.

# Importando a biblioteca
import queue


def verificador(expressao):
    # Criando uma fila
    pilha = queue.LifoQueue()
    for caracter in expressao:
        if caracter == '(':
            pilha.put(caracter)
        elif caracter == ')':
            if not pilha.qsize() or pilha.get() != '(':     #Verificando se está vazio
                return False
    return pilha.qsize() == 0


valor = verificador(')2+1(')
print(valor)
