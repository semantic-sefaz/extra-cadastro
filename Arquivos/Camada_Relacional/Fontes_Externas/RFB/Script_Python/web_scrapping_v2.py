# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import os
import shutil
import json
from datetime import date
import time

PATH_DATA = 'data/'
PATH_EMPRESA = 'empresa/'
PATH_ESTABELECIMENTO = 'estabelecimento/'
PATH_SOCIO = 'socio/'
PATH_SIMEI = 'simei/'
PATH_CNAE = 'cnae/'
PATH_MUNICIPIO = 'municipio/'
PATH_NAT_JU = 'nat_ju/'
PATH_PAIS = 'pais/'
PATH_QUALIF_SOCIO = 'qualif_socio/'
PATH_LOG = 'log/'
URL = "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj"
REMOVE_OLD_SOURCES = False

# Criando os diretórios
if not os.path.isdir(PATH_DATA):  # Diretório de arquivos não existe
    os.mkdir(PATH_DATA)
    os.mkdir(PATH_DATA + PATH_EMPRESA)
    os.mkdir(PATH_DATA + PATH_ESTABELECIMENTO)
    os.mkdir(PATH_DATA + PATH_SOCIO)
    os.mkdir(PATH_DATA + PATH_SIMEI)
    os.mkdir(PATH_DATA + PATH_CNAE)
    os.mkdir(PATH_DATA + PATH_MUNICIPIO)
    os.mkdir(PATH_DATA + PATH_NAT_JU)
    os.mkdir(PATH_DATA + PATH_PAIS)
    os.mkdir(PATH_DATA + PATH_QUALIF_SOCIO)

print("Solicitando página da receita em ", URL)
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

print("Minerando a página...")
paragraphs = soup.find_all(string=re.compile("Data da última extração:"))
date_RFB = paragraphs[0].replace("Data da última extração: ", "")
register = None
count = 0
print(date_RFB)
date_splitted = date_RFB.split("/")

with open("register_scrapping.json", "r") as register_file:
    register = json.load(register_file)

    if register["date_last_update"] != date_RFB:  # Houve atualização nos dados / Verificar data da última atualização
        print(
            "Processo total começou em " +
            time.strftime("%Y-%m-%dT%H:%M:%S"))

        if REMOVE_OLD_SOURCES:
            print("Apagando arquivos antigos...")
            shutil.rmtree(PATH_DATA, ignore_errors=True)  # Apaga dados antigos
            print("Criando diretório para novos arquivos...")
            os.mkdir(PATH_DATA)

        print("Minerando página para localizar links fontes de dados...")
        links_html = soup.find_all("a", class_="external-link")
        for link_html in links_html:

            if "EMPRESA" in link_html.text:
                link = link_html["href"]
                name = link.split("/")[-1]
                link = link.split("//")[-1]
                link = "http://{0}".format(link)
                print(link)
                inicio = link.find("D1")
                dia_do_link = link[inicio:inicio + 6]
                mes_do_link = link[inicio + 2:inicio + 4]
                if mes_do_link == date_splitted[1]:
                    nome_log_erro_carga = "{0}_{1}_{2}_erro.log".format(
                        date_splitted[2], date_splitted[1], date_splitted[0])
                    with open(PATH_LOG + nome_log_erro_carga, "w") as register_file:
                        txt_erro1 = "ARQUIVO DA RFB - EMPRESA - FORA DO PADRAO: {0}. FAVOR TENTAR BAIXAR MANUAL".format(
                            link)
                        register_file.write(txt_erro1)
                    continue
                #dia_do_link_correto = "D1{0}{1}".format(date_splitted[1],date_splitted[0])
                #link = link.replace(dia_do_link,dia_do_link_correto)
                done = False
                attempts = 0
                while not done:
                    print("Baixando link: ")
                    txt = 'wget -O "{0}{1}{2}" "{3}"'.format(PATH_DATA, PATH_EMPRESA, name, link)
                    print(txt)
                    result = os.system(txt)
                    if result == 0:
                        print("Arquivo Baixado com sucesso: ", link)
                        count += 1
                        done = True
                    else:
                        attempts += 1
                        if attempts > 3:  # tenta baixar o mesmo arquivo 3 vezes
                            done = True
                            print(
                                "\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nErro: Imposível baixar arquivo: ",
                                link,
                                "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")
            if "ESTABELECIMENTO" in link_html.text:
                link = link_html["href"]
                name = link.split("/")[-1]
                link = link.split("//")[-1]
                link = "http://{0}".format(link)
                print(link)
                inicio = link.find("D1")
                dia_do_link = link[inicio:inicio + 6]
                mes_do_link = link[inicio + 2:inicio + 4]
                if mes_do_link == date_splitted[1]:
                    nome_log_erro_carga = "{0}_{1}_{2}_erro.log".format(
                        date_splitted[2], date_splitted[1], date_splitted[0])
                    with open(PATH_LOG + nome_log_erro_carga, "w") as register_file:
                        txt_erro2 = "ARQUIVO DA RFB - ESTABELECIMENTO - FORA DO PADRAO: {0}. FAVOR TENTAR BAIXAR MANUAL".format(
                            link)
                        register_file.write(txt_erro2)
                    continue
                #dia_do_link_correto = "D1{0}{1}".format(date_splitted[1],date_splitted[0])
                #link = link.replace(dia_do_link,dia_do_link_correto)
                done = False
                attempts = 0
                while not done:
                    print("Baixando link: ",link)
                    txt = 'wget -O "{0}{1}{2}" "{3}"'.format(PATH_DATA, PATH_ESTABELECIMENTO, name, link)
                    print(txt)
                    result = os.system(txt)
                    if result == 0:
                        print("Arquivo Baixado com sucesso: ", link)
                        count += 1
                        done = True
                    else:
                        attempts += 1
                        if attempts > 3:  # tenta baixar o mesmo arquivo 3 vezes
                            done = True
                            print(
                                "\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nErro: Imposível baixar arquivo: ",
                                link,
                                "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")
            if "Dados Abertos CNPJ SÓCIO" in link_html.text:
                link = link_html["href"]
                name = link.split("/")[-1]
                link = link.split("//")[-1]
                link = "http://{0}".format(link)
                print(link)
                inicio = link.find("D1")
                dia_do_link = link[inicio:inicio + 6]
                mes_do_link = link[inicio + 2:inicio + 4]
                if mes_do_link == date_splitted[1]:
                    nome_log_erro_carga = "{0}_{1}_{2}_erro.log".format(
                        date_splitted[2], date_splitted[1], date_splitted[0])
                    with open(PATH_LOG + nome_log_erro_carga, "w") as register_file:
                        txt_erro3 = "ARQUIVO DA RFB - CNPJ SÓCIO - FORA DO PADRAO: {0}. FAVOR TENTAR BAIXAR MANUAL".format(
                            link)
                        register_file.write(txt_erro3)
                    continue
                #dia_do_link_correto = "D1{0}{1}".format(date_splitted[1],date_splitted[0])
                #link = link.replace(dia_do_link,dia_do_link_correto)
                done = False
                attempts = 0
                while not done:
                    print("Baixando link: ",link)
                    txt = 'wget -O "{0}{1}{2}" "{3}"'.format(PATH_DATA, PATH_SOCIO, name, link)
                    print(txt)
                    result = os.system(txt)
                    if result == 0:
                        print("Arquivo Baixado com sucesso: ", link)
                        count += 1
                        done = True
                    else:
                        attempts += 1
                        if attempts > 3:  # tenta baixar o mesmo arquivo 3 vezes
                            done = True
                            print(
                                "\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nErro: Imposível baixar arquivo: ",
                                link,
                                "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")

            if "Informações sobre o Simples Nacional/MEI" in link_html.text:
                link = link_html["href"]
                name = link.split("/")[-1]
                name = (name.replace('$', ''))
                link = link.split("//")[-1]
                link = "http://{0}".format(link)
                link = (link.replace('$', '\\$'))
                print(link)
                inicio = link.find("D1")
                dia_do_link = link[inicio:inicio + 6]
                mes_do_link = link[inicio + 2:inicio + 4]
                if mes_do_link == date_splitted[1]:
                    nome_log_erro_carga = "{0}_{1}_{2}_erro.log".format(
                        date_splitted[2], date_splitted[1], date_splitted[0])
                    with open(PATH_LOG + nome_log_erro_carga, "w") as register_file:
                        txt_erro4 = "ARQUIVO DA RFB - SIMPLES - FORA DO PADRAO: {0}. FAVOR TENTAR BAIXAR MANUAL".format(
                            link)
                        register_file.write(txt_erro4)
                    continue
                #dia_do_link_correto = "D1{0}{1}".format(date_splitted[1],date_splitted[0])
                #link = link.replace(dia_do_link,dia_do_link_correto)
                print("Baixando link: ",link)
                txt = 'wget -O "{0}{1}{2}" "{3}"'.format(PATH_DATA, PATH_SIMEI, name, link)
                print(txt)
                result = os.system(txt)
                if result == 0:
                    print("Arquivo Baixado com sucesso: ", link)
                    count += 1
                else:
                    print(
                        "\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nErro: Imposível baixar arquivo: ",
                        link,
                        "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")

            if "Tabela de atributo CNAE" in link_html.text:
                link = link_html["href"]
                name = link.split("/")[-1]
                name = (name.replace('$', ''))
                link = link.split("//")[-1]
                link = "http://{0}".format(link)
                link = (link.replace('$', '\\$'))
                print(link)
                inicio = link.find("D1")
                dia_do_link = link[inicio:inicio + 6]
                mes_do_link = link[inicio + 2:inicio + 4]
                if mes_do_link == date_splitted[1]:
                    nome_log_erro_carga = "{0}_{1}_{2}_erro.log".format(
                        date_splitted[2], date_splitted[1], date_splitted[0])
                    with open(PATH_LOG + nome_log_erro_carga, "w") as register_file:
                        txt_erro5 = "ARQUIVO DA RFB - CNAE - FORA DO PADRAO: {0}. FAVOR TENTAR BAIXAR MANUAL".format(
                            link)
                        register_file.write(txt_erro5)
                    continue
                #dia_do_link_correto = "D1{0}{1}".format(date_splitted[1],date_splitted[0])
                #link = link.replace(dia_do_link,dia_do_link_correto)
                print("Baixando link: ",link)
                txt = 'wget -O "{0}{1}{2}" "{3}"'.format(PATH_DATA, PATH_CNAE, name, link)
                print(txt)
                result = os.system(txt)
                if result == 0:
                    print("Arquivo Baixado com sucesso: ", link)
                    count += 1
                else:
                    print(
                        "\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nErro: Imposível baixar arquivo: ",
                        link,
                        "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")
            if "Tabela de atributo Município" in link_html.text:
                link = link_html["href"]
                name = link.split("/")[-1]
                name = (name.replace('$', ''))
                link = link.split("//")[-1]
                link = "http://{0}".format(link)
                link = (link.replace('$', '\\$'))
                print(link)
                inicio = link.find("D1")
                dia_do_link = link[inicio:inicio + 6]
                mes_do_link = link[inicio + 2:inicio + 4]
                if mes_do_link == date_splitted[1]:
                    nome_log_erro_carga = "{0}_{1}_{2}_erro.log".format(
                        date_splitted[2], date_splitted[1], date_splitted[0])
                    with open(PATH_LOG + nome_log_erro_carga, "w") as register_file:
                        txt_erro6 = "ARQUIVO DA RFB - ATRIBUTO MUNICIPIO - FORA DO PADRAO: {0}. FAVOR TENTAR BAIXAR MANUAL".format(
                            link)
                        register_file.write(txt_erro6)
                    continue
                #dia_do_link_correto = "D1{0}{1}".format(date_splitted[1],date_splitted[0])
                #link = link.replace(dia_do_link,dia_do_link_correto)
                print("Baixando link: ",link)
                txt = 'wget -O "{0}{1}{2}" "{3}"'.format(PATH_DATA, PATH_MUNICIPIO, name, link)
                print(txt)
                result = os.system(txt)
                if result == 0:
                    print("Arquivo Baixado com sucesso: ", link)
                    count += 1
                else:
                    print(
                        "\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nErro: Imposível baixar arquivo: ",
                        link,
                        "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")
            if "Tabela de atributo Natureza Jurídica" in link_html.text:
                link = link_html["href"]
                name = link.split("/")[-1]
                name = (name.replace('$', ''))
                link = link.split("//")[-1]
                link = "http://{0}".format(link)
                link = (link.replace('$', '\\$'))
                print(link)
                inicio = link.find("D1")
                dia_do_link = link[inicio:inicio + 6]
                mes_do_link = link[inicio + 2:inicio + 4]
                if mes_do_link == date_splitted[1]:
                    nome_log_erro_carga = "{0}_{1}_{2}_erro.log".format(
                        date_splitted[2], date_splitted[1], date_splitted[0])
                    with open(PATH_LOG + nome_log_erro_carga, "w") as register_file:
                        txt_erro7 = "ARQUIVO DA RFB - ATRIBUTO NATUREZA JURIDICA - FORA DO PADRAO: {0}. FAVOR TENTAR BAIXAR MANUAL".format(
                            link)
                        register_file.write(txt_erro7)
                    continue
                #dia_do_link_correto = "D1{0}{1}".format(date_splitted[1],date_splitted[0])
                #link = link.replace(dia_do_link,dia_do_link_correto)
                print("Baixando link: ",link)
                txt = 'wget -O "{0}{1}{2}" "{3}"'.format(PATH_DATA, PATH_NAT_JU, name, link)
                print(txt)
                result = os.system(txt)
                if result == 0:
                    print("Arquivo Baixado com sucesso: ", link)
                    count += 1
                else:
                    print(
                        "\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nErro: Imposível baixar arquivo: ",
                        link,
                        "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")
            if "Tabela de atributo País" in link_html.text:
                link = link_html["href"]
                name = link.split("/")[-1]
                name = (name.replace('$', ''))
                link = link.split("//")[-1]
                link = "http://{0}".format(link)
                link = (link.replace('$', '\\$'))
                print(link)
                inicio = link.find("D1")
                dia_do_link = link[inicio:inicio + 6]
                mes_do_link = link[inicio + 2:inicio + 4]
                if mes_do_link == date_splitted[1]:
                    nome_log_erro_carga = "{0}_{1}_{2}_erro.log".format(
                        date_splitted[2], date_splitted[1], date_splitted[0])
                    with open(PATH_LOG + nome_log_erro_carga, "w") as register_file:
                        txt_erro8 = "ARQUIVO DA RFB - ATRIBUTO PAIS - FORA DO PADRAO: {0}. FAVOR TENTAR BAIXAR MANUAL".format(
                            link)
                        register_file.write(txt_erro8)
                    continue
                #dia_do_link_correto = "D1{0}{1}".format(date_splitted[1],date_splitted[0])
                #link = link.replace(dia_do_link,dia_do_link_correto)
                print("Baixando link: ",link)
                txt = 'wget -O "{0}{1}{2}" "{3}"'.format(PATH_DATA, PATH_PAIS, name, link)
                print(txt)
                result = os.system(txt)
                if result == 0:
                    print("Arquivo Baixado com sucesso: ", link)
                    count += 1
                else:
                    print(
                        "\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nErro: Imposível baixar arquivo: ",
                        link,
                        "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")
            if "Tabela de atributo qualificação dos sócios" in link_html.text:
                link = link_html["href"]
                name = link.split("/")[-1]
                name = (name.replace('$', ''))
                link = link.split("//")[-1]
                link = "http://{0}".format(link)
                link = (link.replace('$', '\\$'))
                print(link)
                inicio = link.find("D1")
                dia_do_link = link[inicio:inicio + 6]
                mes_do_link = link[inicio + 2:inicio + 4]
                if mes_do_link == date_splitted[1]:
                    nome_log_erro_carga = "{0}_{1}_{2}_erro.log".format(
                        date_splitted[2], date_splitted[1], date_splitted[0])
                    with open(PATH_LOG + nome_log_erro_carga, "w") as register_file:
                        txt_erro9 = "ARQUIVO DA RFB - QUALIFICACOES - FORA DO PADRAO: {0}. FAVOR TENTAR BAIXAR MANUAL".format(
                            link)
                        register_file.write(txt_erro9)
                    continue

                #dia_do_link_correto = "D1{0}{1}".format(date_splitted[1],date_splitted[0])
                #link = link.replace(dia_do_link,dia_do_link_correto)
                print("Baixando link: ",link)
                txt = 'wget -O "{0}{1}{2}" "{3}"'.format(PATH_DATA, PATH_QUALIF_SOCIO, name, link)
                print(txt)
                result = os.system(txt)
                if result == 0:
                    print("Arquivo Baixado com sucesso: ", link)
                    count += 1
                else:
                    print(
                        "\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nErro: Imposível baixar arquivo: ",
                        link,
                        "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")

        print("Foram baixados ", str(count), " arquivos")

        if count > 0:  # Conseguiu baixar algum arquivo
            with open("register_scrapping.json", "w") as register_file:
                register["num_arq_baixados"] = count
                register_file.write(json.dumps(register))

    else:  # Dados inalterados
        print("Nenhuma atualização encontrada.")
        with open("register_scrapping.json", "w") as register_file:
            register["updated"] = False
            register_file.write(json.dumps(register))

if register is not None and count > 0:
    with open("register_scrapping.json", "w") as register_file:
        print("Atualizando registros...")
        register["date_last_update"] = date_RFB
        register["updated"] = True
        register_file.write(json.dumps(register))
