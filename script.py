import json
import os
import subprocess
from threading import Timer



#definir isto em função
#abrir os ficheiros .json
with open("subm.json") as json1_file:
    json1_data = json.load(json1_file)


with open("exerc.json") as json_file:
    json_data = json.load(json_file)

print(json_data['exercicio']['Valores de teste'])


#criar e escrever em um ficheiro
        #f = open("teste.c","w+")
        #f.write(json_data['exercicio']['Template'])
        #f.write(json1_data['submissao']['Código'])


        #f.close()

with open("teste.c","w+") as f:
    f.write(json_data['exercicio']['Template'])
    f.write(json1_data['submissao']['Código'])



#adicionar o compilar e ler os resultados

def run(cmd, timeout):
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    kill = lambda p: p.kill()
    timer = Timer(timeout, kill, [proc])
    try:
        timer.start()
        return proc.communicate()
    finally:
        timer.cancel()

   
if __name__ == '__main__':
    
    compilers = {
        "C" : "gcc -Wall -Wextra -pedantic -O2",
        "Java" : "javac",
        "PY" : "python",
        "PY3" : "python3"
    }
    command = "ping google.pt" #"gcc -Wall teste.c"
    #os change dir -> aluno + "/" + id 
    # command = compilers[language] + file
    out, err = run(command, 2)

    print('------------------------------------------')
    for l in out.decode("utf8").splitlines():
        print(l)

    for l in err.decode("utf8").splitlines():
        print(l)
    print('------------------------------------------')
    




#interpretador dos resultados da compilação



#executar no sistema
