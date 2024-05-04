#  Refaça o problema "Simulação de Fila de Impressão" mas agora com o uso da classe queue.

import queue
import random as r


def simular_impressao(numero_documentos, tempo_medio_impressao):
    fila_impressao = queue.Queue()
    tempo_espera_total = 0

    for documento in range(1, numero_documentos + 1):
        tempo_impressao = r.expovariate(1 / tempo_medio_impressao)
        print(f'Documento {documento}: Tempo de impressão estimado -'
              f'{tempo_impressao:.2f} minutos.')

    while fila_impressao:
        documento_atual, tempo_impressao_atual = fila_impressao.get()
        