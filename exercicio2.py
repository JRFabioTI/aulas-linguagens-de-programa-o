nome = input ("Digite o nome: ")
i = int (input("Informe a posição desejada para adicionar a letra: "))

print(nome[i])

if nome[i] == "s":
    print (nome[:i]+"r" + nome[i+1:])
elif nome[i] == "m" :
    print (nome[:i]+"n" + nome[i+1:])
else:
    print (nome[:i] + nome[i+1:])