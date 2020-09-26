import os
import sys
import shutil
import subprocess
import urllib
import random
#import main



def init():

    #Toda vez que o programa inicia ele verifica se os arquivos estão perdidos pela máquina chamando o BACK
    try:
        import Back
        Back
    except:
        pass

    user = (os.path.expanduser("~")) #Nome do Usuario da Maquina + Caminho dos arquivos

    oldAdress = user + '/Desktop/gauntlet/I/' #pasta origem
    newAdress = user + '/Desktop/gauntlet/D1/' #pasta única de destino
    finishAdress = user + '/Desktop/gauntlet/F/' #pasta destino
    #Lista de Diretorios
    newAdressList = [user + '/Desktop/gauntlet/D1/', user + '/Desktop/gauntlet/D2/', user + '/Desktop/gauntlet/D3/', user + '/Desktop/gauntlet/D4/', user + '/Desktop/gauntlet/D4/']


    list = os.listdir(oldAdress) #lista separando apenas os arquivos do caminho.



    #Essa é a Lista onde armazenará todos os caminhos que os arquivos serão enviados
    log_list = []

    contador_controle = 0 #contador de controle
    validate = True #Controle
    memoryDirs = [] #Armazena todos os diretorios
    memoryArch = [] #Armazena o nome dos arquivos
    while (validate == True):
        #print(len(os.listdir(oldAdress)))
        if (len(os.listdir(oldAdress))) != 0: #Verifica quantos arquivos temos no OLDADRESS
            caminhoCompleto_old = oldAdress + list[contador_controle] #variável recebe caminho + arquivo, conforme indice
            __caminhoCompleto_new = random.choice(newAdressList) #variável recebe caminho + arquivo, conforme indice
            caminhoCompleto_new = __caminhoCompleto_new + list[contador_controle] #Une Diretório com Arquivo

            #Adiciona o caminho no LOG
            log_list.append(caminhoCompleto_new)

            shutil.move(caminhoCompleto_old, caminhoCompleto_new) #módulo 'shutil.move()' move os arquivos

            hiddenAdress = __caminhoCompleto_new[:-1] #Retira a Barra no final do caminho
            subprocess.call('attrib +s +h "'+ hiddenAdress +'"', shell=True) # deixa a pasta invísivel

            #print(caminhoCompleto_new , '-')
            #print(x, '-', list[x])  # apenas para ver como está sendo feito

            memoryDirs.append(__caminhoCompleto_new) #Adiciona na memoria
            memoryArch.append(list[contador_controle]) #Adiciona na memoria



        else:
            validate = False #Parada da Função
        contador_controle +=1 #Contador de controle


    #Grava o LOG
    log_file = open('C:/Users/T-Gamer/Desktop/gauntlet/log.txt', 'w')
    for cont in range(len(log_list)):
        print(cont)
        log_file_text = str(log_list[cont]) + "\n"
        log_file.writelines(log_file_text)

    p = input("Qual a sua senha? ")






    def back(): #Serve para voltar os arquivos a pasta de origem caso a senha esteja correta
        y = 0
        validate = True
        while y != (len(memoryDirs)) and validate == True: #Usa as memórias para verificação

            if (len(memoryDirs)) != 0:

                hiddenAdress = memoryDirs[y][:-1] #Identifica o caminho, deletando a ultima / para deixar visível
                if (pw == True): #Se a senha estiver correta:
                    caminhoCompleto_old = memoryDirs[y] + memoryArch[y] #Une o caminho + nome do arquivo
                    caminhoCompleto_new = oldAdress + memoryArch[y] #Faz o mesmo
                    shutil.move(caminhoCompleto_old, finishAdress) #Envia os arquivos para a pasta FINAL
                    subprocess.call('attrib +s -h "' + hiddenAdress + '"', shell=True) #Deixa tudo visível
                else:
                    subprocess.call('attrib +s +h "' + hiddenAdress + '"', shell=True) #Deixa tudo Invisível
            else:
                validate = False #Criterio de parada
            y += 1
        return print("finish")





    pw = False
    if (p == '123'):
        pw = True

    else:
        pw = False

    if (pw == True):
        print("Password Success")
        subprocess.call('attrib +s -h "' + oldAdress[:-1] + '"', shell=True)
        print(oldAdress)
        print(oldAdress[-1])
        back()
    else:
        print("F")
        subprocess.call('attrib +s +h "' + oldAdress[:-1] + '"', shell=True)
        back()
        sys.exit()


init()
