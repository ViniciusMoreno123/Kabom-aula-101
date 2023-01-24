import time 

valueMax = input(("Digite o tempo desejado em segundos:"))


def contagemMaxima(seg):
    while seg > 0 :
        min = (int(seg/60))
        segundos = (int(seg%60))
        temp = (f'{min}:{segundos}')
        print(temp)
        time.sleep(1)
        seg -=1
    print("KABOMMMMMMMMM")
    

contagemMaxima(int(valueMax))