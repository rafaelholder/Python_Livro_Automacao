import time as bibliotecaTempo

print("Hello World Python with time")
tempoInicial = bibliotecaTempo.time() #Armazena a hora inicial 
soma = 0
totalRange = 1000000

for i in range(totalRange):
    soma += i
    if(i == totalRange - 1):
        print("--Soma finalizada--")
print("A soma é: " + str(soma))
tempoFinal = bibliotecaTempo.time() #Armazena a hora final

print(f'Tempo total: {tempoFinal-tempoInicial:.6f} seconds')
## f = Sinaliza e marca uma função dentro das '' do print
# ex: print(f'{print('esse é um print dentro de outro')}')
## :.6f = Formata o resultado de tempoFinal-tempoInicial para 
#        mostrar 6 casas decimais depois do 0.