# -*- coding: utf-8 -*-
import os
import shutil
import time
import json
import cx_Oracle
import execute_func_oracle


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
PATH_MOTIVOS_SITU = 'motivos_situ/'
PATH_CARGA = 'carga_v2/'
date_start = time.strftime("%Y-%m-%d")

tem_atualizacao = False
date_RFB = None

#tem_atualizacao = True ## REMOVER DEPOIS QUE CONCLUIR A CARGA 15/09/2022

print("Chamando o web scrapping")
rodou_webscrapping = os.system("python web_scrapping_v2.py")

if rodou_webscrapping == 0:
	with open("register_scrapping.json","r") as register_file:
		register = json.load(register_file)
		if register == None or register["date_last_update"] != "":
			date_RFB = register["date_last_update"]
			tem_atualizacao = register["updated"]

if rodou_webscrapping != 0:
	print("O webscrapping nao rodou corretamente. Por favor, tente novamente.")

#os.system("python descomgen_csv_arq_baixados.py") USEI FORA DO IF PARA CONSERTAR O ERRO DO DESCOMPACTAR
if tem_atualizacao:
    if execute_func_oracle.check_versions() > 1:
        execute_func_oracle.recreate_olds() #Carrega OLDs
        print('Tabelas OLDs recriadas')

    os.system("python descomgen_csv_arq_baixados.py")
    os.system("python monta_arq_ctl.py")
    path_list = [PATH_EMPRESA, PATH_ESTABELECIMENTO, PATH_SOCIO, PATH_SIMEI, PATH_CNAE, PATH_MUNICIPIO, 
		PATH_NAT_JU, PATH_PAIS, PATH_QUALIF_SOCIO]

    message = "Inicio CARGA V2 dados RFB " + time.strftime("%Y-%m-%dT%H:%M:%S")
    print(message)
    for path_dir in path_list:
        empresa = 1 if path_dir == PATH_EMPRESA else 0
        estabelecimento = 1 if path_dir == PATH_ESTABELECIMENTO else 0
        socio = 1 if path_dir == PATH_SOCIO else 0
        simei = 1 if path_dir == PATH_SIMEI else 0
        qualif_socio = 1 if path_dir == PATH_QUALIF_SOCIO and date_RFB is not None else 0
        nat_ju = 1 if path_dir == PATH_NAT_JU and date_RFB is not None else 0
        motivos_situ = 1 if path_dir == PATH_MOTIVOS_SITU and date_RFB is not None else 0
        pais = 1 if path_dir == PATH_PAIS and date_RFB is not None else 0
        municipio = 1 if path_dir == PATH_MUNICIPIO and date_RFB is not None else 0
        cnae = 1 if path_dir == PATH_CNAE and date_RFB is not None else 0

        carga = "python sql_loader_oracle_rfb_v2.py {0} {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(
            empresa, estabelecimento, socio, simei, qualif_socio, nat_ju, motivos_situ, pais, municipio, cnae)
        '''
		for file in os.listdir(PATH_OUTPUT+path_dir):
			message ="\n\n\n--------------------------------------------\nProcessando arquivo: "+file+"\n\n\n"
			print(message)
			carga_tb_norm = 0
			message = "Inicio sql loader arquivo "+file+" "+time.strftime("%Y-%m-%dT%H:%M:%S")
			print(message)

			if empresa == 1:
				nome_ctl = "EMPRE.csv"
			elif estabelecimento == 1:
				nome_ctl = "ESTABELE.csv"
			elif socio == 1:
				nome_ctl = "SOCIO.csv"
			elif simei == 1:
				nome_ctl = "SIMPLES.csv"
			elif qualif_socio == 1:
				nome_ctl = "QUALS.csv"
			elif nat_ju == 1:
				nome_ctl = "NATJU.csv"
			elif motivos_situ == 1:
				nome_ctl = "DominiosMotivoSituaoCadastral.csv"
			elif pais == 1:
				nome_ctl = "PAIS.csv"
			elif municipio == 1:
				nome_ctl = "MUNIC.csv"
			elif cnae == 1:
				nome_ctl = "CNAE.csv"
			os.rename(PATH_OUTPUT+path_dir+file, PATH_OUTPUT+path_dir+nome_ctl)
			carga_tb_norm = os.system(carga)
			if carga_tb_norm == 0:
				os.remove(PATH_OUTPUT+path_dir+nome_ctl)
				message = "Fim sql loader arquivo "+file+" "+time.strftime("%Y-%m-%dT%H:%M:%S")
				print(message)
				if os.stat("carga_v2/EMPRE.bad")[6] == 0.0 and os.stat("carga_v2/ESTABELE.bad")[6] == 0.0 and os.stat("carga_v2/SOCIO.bad")[6] == 0.0 and os.stat("carga_v2/SIMPLES.bad")[6] == 0.0:
					continue
				else:
					print("problema no sqlldr, verificar arquivos .bad na pasta carga. Limpe-os apos correcao do problema!")
					break
			else:
				print("erro no carregamento do sql loader")
				break'''
        message = "\n\n\n--------------------------------------------\nProcessando arquivos do: " + \
            path_dir + " " + time.strftime("%Y-%m-%dT%H:%M:%S") + "\n\n\n"
        carga_tb_norm = os.system(carga)
        if carga_tb_norm == 0:
            message = "Fim sql loader arquivos do " + path_dir + \
                " " + time.strftime("%Y-%m-%dT%H:%M:%S")
            print(message)
            nome_bad = '{0}.bad'.format(path_dir.replace("/", ""))
            if os.path.isfile(PATH_CARGA + nome_bad):
                if os.stat(PATH_CARGA + nome_bad)[6] == 0.0:
                    continue
                else:
                    sucesso_carga = False
                    msg_erro = "problema durante a carga sqlldr, verificar arquivo {0} na pasta carga {1}. Limpe-os apos correcao do problema!".format(
                        nome_bad, PATH_CARGA)
                    print(msg_erro)
                    break
            for file in os.listdir(PATH_OUTPUT + path_dir):
                os.remove(PATH_OUTPUT + path_dir + file)
            execute_func_oracle.truncate_tbs() # Limpa as tabelas normalizadas
            execute_func_oracle.cria_tb() # Insere uma nova tupla em HIST_CARGA
        else:
            sucesso_carga = False
            msg_erro = "erro no carregamento do sql loader, verificar arquivo {0}.log em {1}".format(
                nome_bad.replace(".bad", "", PATH_CARGA))
            print(msg_erro)
            break
        print(message)

    message = "Fim CARGA V2 dados RFB " + time.strftime("%Y-%m-%dT%H:%M:%S")
    sucesso_carga = True
    #sent_email(date_start)
    #execute_func_oracle.recreate_news() #Carrega NEWs
    #print('Tabelas NEW criadas')
    print(message)

else:
    print("sem atualizacao")


