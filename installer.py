import os
import shutil
import sys

def verify_CS(filename,disco):
    a = []
    for r,d,f in os.walk(disco):
        for files in f:
            if files == filename:
                a.append(os.path.join(r,files))
    return "".join(a)

def verify_CFG(filename,path):
    a = []
    for r,d,f in os.walk(path):
        for files in f:
            if files == filename:
                return True
    return False

def transform_to_str_and_cut(list,cut):
    a = list.split(cut)
    b = a[0]
    return b

def check_2(cs,cfg):
    disc = input("ESCOLHE A MERDA DO DISCO SEU ATRASADO (SE NAO FOR NO C ÉS UM CONAS) NINGUEM POE O CS NOUTRO DISCO, SEU ATRASADO DA MERDA: ")
    disco = disc.upper() + ":\\"
    diretorio = cs("csgo.exe",disco)
    diretorio_cfg = transform_to_str_and_cut(diretorio,"csgo.exe") + "csgo\\cfg\\"
    if cfg("gamestate_integration_GSI.cfg",diretorio_cfg) == True:
        print("Está tudo pronto!")
        return True
    else:
        print("A copiar para cfg")
        shutil.copy("gamestate_integration_GSI.cfg",diretorio_cfg)
        if cfg("gamestate_integration_GSI.cfg",diretorio_cfg) == True:
            print("Está tudo pronto")
            return True
        else:
            print("Algo correu mal")
            return False

if check_2(verify_CS,verify_CFG) == True:
    print("A abrir")
    os.system("python teste(1).py")
