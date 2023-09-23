# Davi Gonçalves Valério - Sistemas Operacionais - Turma A - Corrida das Lebres
import random
import threading
import time

# Em segundos
waiting_min_time = 1
# Em segundos
waiting_max_time = 5

hare_jumping_now = threading.Lock()
finalists = []


class Hare:
    name = ''
    position = 0
    jumps_count = 0

    def __init__(self, name):
        self.name = name

    def jump(self):
        self.jumps_count += 1
        # Cada lebre pode dar um salto que varia de 1 a 3 metros de distância.
        jump_size = random.randint(1, 3)
        self.position += jump_size
        if self.position >= 20:
            finalists.append(self)
        # Cada lebre informará quantos metros ela pulou a cada salto realizado.
        print(f'"{self.name}" pulou {jump_size} metros!')

    # Na corrida, cada lebre dará um salto de comprimento aleatorio (dentro do intervalo permitido)
    def start_jump(self):
        # A distancia percorrida é de 20 metros.
        while self.position < 20:
            with hare_jumping_now:
                self.jump()
            # A lebre para para descansar (tempo aleatório), ficando parada enquanto as outras lebres saltam.
            time.sleep(random.randint(waiting_min_time, waiting_max_time))


def run_hare_run(hare_name):
    an_hare = Hare(hare_name)
    an_hare.start_jump()


if __name__ == '__main__':
    # Cinco lebres disputarão uma corrida.
    # Escreva um programa, utilizando threads (uma para cada lebre)
    hare1 = threading.Thread(target=run_hare_run, args=["Lebre 1"])
    hare2 = threading.Thread(target=run_hare_run, args=["Lebre 2"])
    hare3 = threading.Thread(target=run_hare_run, args=["Lebre 3"])
    hare4 = threading.Thread(target=run_hare_run, args=["Lebre 4"])
    hare5 = threading.Thread(target=run_hare_run, args=["Lebre 5"])

    # RUNNNNN!
    hare1.start()
    hare2.start()
    hare3.start()
    hare4.start()
    hare5.start()

    hare1.join()
    hare2.join()
    hare3.join()
    hare4.join()
    hare5.join()

    print('\n - - - - - FINALISTAS! - - - - - \n')

    # que informe a lebre vencedora e a colocação de cada uma delas no final da corrida.
    print(f'A lebre "{finalists[0].name}" venceu!\n')
    for position, hare in enumerate(finalists):
        # Informar também quantos pulos cada uma delas deu.
        print(f'A lebre "{hare.name}" terminou em {position + 1}° pulando {hare.jumps_count} vezes!')
