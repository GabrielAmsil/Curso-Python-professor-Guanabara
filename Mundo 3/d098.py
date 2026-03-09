import time

def contador(inicio, fim, passo):
    for i in range(inicio, fim+1, passo):
        print(i, end=" ")
        time.sleep(0.3)
    print("FIM")

contador(1,10,1)