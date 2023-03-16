# Hello world em pytho com:
# print() - Mostra algo na tela. Se usa "" para mostrar textos, mas não precisa para mostrar números
# input() - Da ao user a possibilidade de digitar algum valor, 
# Função len() - mostra a quantidade de caracteres, numeros, ou items de algo, 
# int(), float(), str() - Transformam valores em inteiros, floats ou string, respectivamente,
# if, elif, else - Condicionais que verificam se algo cumpre a condição imposta e executa o bloco de codigo,
# verificação de equivalencia com if, else - Um int não é igual a uma str (42 não é igual a '42')


print("Hello world!") #print("")
print(42) #print()

print("Whats your name?")
myname = input() #input()
print("Nice to meet you " + myname)

quant = str(len(myname)) #len(), str()
print("Seu nome tem " + quant  + " Letras")

print("Whats your age?")
age = int(input()) #int()

#If, elif, else
if(age <= 3):
    print("Como vim parar aqui se eu so tenho 3 anos??????")
elif(age > 18):
    print("Idoso... ")
    print('Você vai ter ' + str(age + 1) + ' anos daqui a um ano')
else:
    print("Kid")
    print('Você vai ter ' + str(age + 1) + ' anos daqui a um ano')



