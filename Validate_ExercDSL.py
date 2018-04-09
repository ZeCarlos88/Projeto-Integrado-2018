import re

# Separa ficheiro de entrada por linhas, sendo dividido por '},\n'.
# É adicionado o caractér '}' no final de cada linha não vazia e que não termina em '.'

def split_file(file_exerc):
    new_lines=[]
    with open(file_exerc) as f:
        for line in f.read().split('},\n'):
            if not line.endswith(".") or not line:
                new_lines.append((line+'}'))
            if line.endswith("."):
                new_lines.append(line[:-1])
    return new_lines

# Valida todos os campos do ficheiro de entrada de acordo com a estrutura definida no ficheiro "teste.txt"
# Esta função tem que ser optimizada, visto que, só retorna um erro de cada vez (Era fixe retornar todos)
def valida_Exerc(file_ex):
    split_lines = split_file(file_ex) 

    if (bool(re.match('Enunciado: *{"[^"]*"}', split_lines[0]))):
        if(bool(re.match('Template: *{"[^"]*"}', split_lines[1]))):           # É preciso rever esta expressão regular (visto que strings estão entre "")!                               
            if (bool(re.match('Valores de teste: *{(\("[^"]*","[^"]*"\),?)+}', split_lines[2]))):
                if(bool(re.match('Linguagem: *{"[a-zA-Z]*"}', split_lines[3]))):
                    return 1
                else:
                    return -1
            else:
                return -2
        else:
            return -3
    else:
        return -4

# Cria uma matriz 2 por numero de campos, sendo que guarda a info neste formato:
# [["Enunciado","Cria o fatorial de um dado inteiro X"],["Template","ASD"],etc]
# Todas as chavetas são removidas (tem de ser ver isto)
def check_lines(file_exec):
    new_lines = split_file(file_exec)
    largura, altura = 2, len(new_lines)
    matrix = [["" for x in range(largura)] for y in range(altura)]

    for line in new_lines:
        str_dividida = line.split(':')

        conteudo_campo = remove_chavetas(str_dividida[1])

        matrix[new_lines.index(line)][0] = "\"" + str_dividida[0] + "\""
        matrix[new_lines.index(line)][1] = conteudo_campo

    return matrix

#Redifinir este método, está feito à pressa (fazer uma expressão regular para remover as chavetas)
def remove_chavetas(str):
    str = str.replace("{","")
    str = str.replace("}","")
    return str

# Cria um ficheiro JSON com o formato de exerc.json (os valores de teste ainda não estão criados como nesse ficheiro)
def criarJSON(matriz_linhas):
    f = open("testeaux.json","w+")
    f.write("{\"exercicio\": {\n")
    for line in matriz_linhas:
        f.write('\t'+line[0]+':'+line[1]+',\n')
    f.write("}}")
    f.close()

if __name__ == '__main__':
    res = valida_Exerc('teste.txt')

    if(res==1):
        print("Ficheiro corretamente criado!")
        criarJSON(check_lines('teste.txt'))

    elif(res==-1):
        print("LINGUAGEM INVALIDA")
    elif(res==-2):
        print("VALORES DE TESTE INVALIDOS")
    elif(res==-3):
        print("TEMPLATE INVALIDO")
    elif(res==-4):
        print("ENUNCIADO INVALIDO")