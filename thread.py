import threading
import time
import random

# Inicializando o lock
lock = threading.Lock()

def tarefa(contador, thread_id):
    total = 0
    while total < 20:
        incremento = random.randint(1, 5)

        with lock:  # Adquire o lock antes de somar
            if total + incremento <= 20:
                total += incremento
                print(f"Thread {thread_id}: Total = {total}")

        time.sleep(0.1)  # Pequeno intervalo para simular concorrência

# Criando as threads
threads = []
for i in range(2):
    thread = threading.Thread(target=tarefa, args=(20, i+1))
    threads.append(thread)
    thread.start()

# Aguardando as threads terminarem
for thread in threads:
    thread.join()

print("Todas as tarefas foram concluídas.")
