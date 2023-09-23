import random
import threading
import time

tempo_min_espera = 1
tempo_max_espera = 5

lebre_pulando = threading.Lock()
resultados = []


def corrida(nome):
    posicao = 0
    quant_pulos = 0

    while posicao < 20:
        with lebre_pulando:
            quant_pulos += 1
            tamanho_pulo = random.randint(1, 3)
            posicao = posicao + tamanho_pulo
            if posicao >= 20:
                resultados.append([nome, quant_pulos])
            print(f'A lebre "{nome}" deu um salto de {tamanho_pulo} metros!')
        time.sleep(random.randint(tempo_min_espera, tempo_max_espera))


if __name__ == '__main__':
    lebre1 = threading.Thread(target=corrida, args=["Amanda"])
    lebre2 = threading.Thread(target=corrida, args=["Paula"])
    lebre3 = threading.Thread(target=corrida, args=["Lucas"])
    lebre4 = threading.Thread(target=corrida, args=["Ravi"])
    lebre5 = threading.Thread(target=corrida, args=["Jennifer"])

    lebre1.start()
    lebre2.start()
    lebre3.start()
    lebre4.start()
    lebre5.start()

    lebre1.join()
    lebre2.join()
    lebre3.join()
    lebre4.join()
    lebre5.join()

    print('\n')
    print('Resultados da corrida: \n')

    print(f'A lebre "{resultados[0][0]}" venceu!\n')
    for posicao, lebre in enumerate(resultados):
        print(f'"{lebre[0]}" ficou em {posicao + 1}° lugar, com {lebre[1]} pulos.')
