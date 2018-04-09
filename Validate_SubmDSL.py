import re

def valida_Subm(file_subm):

    with open(file_subm) as f:
        new_lines=[]
        for line in f.read().split('},\n'):
            if not line.endswith(".") or not line:
                new_lines.append((line+'}'))
            if line.endswith("."):
                new_lines.append(line[:-1])    
        
        for line in new_lines:
            print(line)

   
    if(bool(re.match('[nN]umero [aA]luno: *{"[a-zA-Z]?[0-9]{5}"}', new_lines[0]))):                                       
        if (bool(re.match('[rR]esposta: *{"[^"]*"}', new_lines[1]))):           # É preciso rever esta expressão regular (visto que strings estão entre "")!
            return 1
        else:
                return -1
    else:
        return -2

if __name__ == '__main__':
    res = valida_Subm('plain.txt')

    if(res==1):
        print("Ficheiro corretamente criado!")
    elif(res==-1):
        print("CODIGO INVALIDO")
    elif(res==-2):
        print("N ALUNO INVALIDO")