from random import randint

# Solicita a senha do usuário
sh = input("teste pra ver ")

# Lista de caracteres possíveis
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '%', '$', '&', '*', '(', ')', '-', '_', '+', '=', 
          '§', '<', '>', '|', '\\', '.', '~', '^', '}', '{', '[', ']', '?', '/', ':', ';', '0', '1', '2', '3', 
          '4', '5', '6', '7', '8', '9']


acho = ""


while acho != sh:
    acho = "" 
    for letra in sh: 
        acholetra = letras[randint(0, len(letras) - 1)]  
        acho += acholetra  

    print(acho)  


print("Senha é: {}".format(acho))

