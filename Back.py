import os
import sys
import shutil


caminhoBack = 'C:/Users/T-Gamer/Desktop/gauntlet/I'
read_log_file = open('C:/Users/T-Gamer/Desktop/gauntlet/log.txt', 'r')
for i in read_log_file:
    i = i.replace("\n",'')
    shutil.move(i, caminhoBack)
