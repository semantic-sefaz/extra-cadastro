# -*- coding: utf-8 -*-
import os
import shutil
import json
import platform

PATH_DATA = 'data/'
PATH_OUTPUT = 'output/'
PATH_EMPRESA = 'empresa/'
PATH_ESTABELECIMENTO = 'estabelecimento/'
PATH_SOCIO = 'socio/'
PATH_SIMEI = 'simei/'
PATH_CNAE = 'cnae/'
PATH_MUNICIPIO = 'municipio/'
PATH_NAT_JU = 'nat_ju/'
PATH_PAIS = 'pais/'
PATH_QUALIF_SOCIO = 'qualif_socio/'
PATH_RFB_ANTIGOS = 'rfb_antigos/'
PATH_HTML = 'html/'

if not os.path.isdir(PATH_RFB_ANTIGOS):  # Diretório de arquivos não existe
    os.mkdir(PATH_RFB_ANTIGOS)


if not os.path.isdir(PATH_OUTPUT):  # Diretório de arquivos não existe
    os.mkdir(PATH_OUTPUT)
    os.mkdir(PATH_OUTPUT + PATH_EMPRESA)
    os.mkdir(PATH_OUTPUT + PATH_ESTABELECIMENTO)
    os.mkdir(PATH_OUTPUT + PATH_SOCIO)
    os.mkdir(PATH_OUTPUT + PATH_SIMEI)
    os.mkdir(PATH_OUTPUT + PATH_CNAE)
    os.mkdir(PATH_OUTPUT + PATH_MUNICIPIO)
    os.mkdir(PATH_OUTPUT + PATH_NAT_JU)
    os.mkdir(PATH_OUTPUT + PATH_PAIS)
    os.mkdir(PATH_OUTPUT + PATH_QUALIF_SOCIO)

with open("register_scrapping.json", "r") as register_file:
    register = json.load(register_file)
    date_RFB = register["date_last_update"]

date_splitted = date_RFB.split("/")
data_gravacao = "{0}_{1}_{2}".format(
    date_splitted[2],
    date_splitted[1],
    date_splitted[0])
path_gravacao = "{0}{1}/".format(PATH_RFB_ANTIGOS, data_gravacao)
if not os.path.isdir(path_gravacao):  # Diretório de arquivos não existe
    os.mkdir(path_gravacao)  # para armazenar .zip da rfb apos carga

path_list = [
    PATH_EMPRESA,
    PATH_ESTABELECIMENTO,
    PATH_SOCIO,
    PATH_SIMEI,
    PATH_CNAE,
    PATH_MUNICIPIO,
    PATH_NAT_JU,
    PATH_PAIS,
    PATH_QUALIF_SOCIO]

for path_dir in path_list:
    for file in os.listdir(PATH_DATA + path_dir):
        novo_nome_zip = '{0}'.format(file.replace("$", ""))
        os.rename(
            PATH_DATA +
            path_dir +
            file,
            PATH_DATA +
            path_dir +
            novo_nome_zip)
        if platform.system() == 'Windows':
            unzip = 'PowerShell Expand-Archive -Path "{0}{1}{2}" -DestinationPath "{3}{1}"'.format(
                PATH_DATA, path_dir, novo_nome_zip, PATH_OUTPUT)
        if platform.system() == 'Linux':
            unzip = 'unzip {0}{1}{2} -d {3}{1}'.format(
                PATH_DATA, path_dir, novo_nome_zip, PATH_OUTPUT)
        print(unzip)
        descomp = os.system(unzip)
        if descomp == 0:
            msg = "descompactou arquivo {0}".format(novo_nome_zip)
            print(msg)
            # move os .zip da rfb para seu dir com data de atualizacao
            # shutil.move(PATH_DATA+path_dir+file,path_gravacao)

for path_dir in path_list:
    for file in os.listdir(PATH_OUTPUT + path_dir):
        novo_nome = '{0}.csv'.format(file)
        novo_nome = novo_nome.replace("$", "")
        os.rename(
            PATH_OUTPUT +
            path_dir +
            file,
            PATH_OUTPUT +
            path_dir +
            novo_nome)
'''
# Para o arquivo html
for file in os.listdir(PATH_DATA+PATH_HTML):
    shutil.move(PATH_DATA + PATH_HTML,PATH_RFB_ANTIGOS + file)
'''
