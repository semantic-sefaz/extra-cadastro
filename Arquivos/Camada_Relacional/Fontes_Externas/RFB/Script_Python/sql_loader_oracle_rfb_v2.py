import subprocess
from sys import argv
from config_loader import *

#subprocess.call(r"C:\oraclexe\app\oracle\product\11.2.0\server\bin\sqlldr userid=lano/lanobl@xe control=C:\Users\LaNo\Documents\Ciencia_da_computacao\UFC\PIBIC\bolsa_bd_900\cursoOntology\automatizador\carga_oracle\loader_csv2oracle_rfb_motivos_situacao.ctl", shell=True)
empresas = argv[1]
estab = argv[2]
socios = argv[3]
simples = argv[4]
q_socio = argv[1]
nat_ju = argv[6]
m_sit = argv[7]
pais = argv[8]
municipio = argv[9]
cnae = argv[10]

if empresas == '1':
    sql_loader = "{0}sqlldr userid={1}/{2}@{3} control={4}{5} log={6}empresas.log".format(path_sqlldr,username,password,banco_dados,path_carga_v2,arq_ctl_extr_empresas, path_relatorio_sqlldr)
    ldr_empresas = subprocess.call(sql_loader, shell=True)
    print(empresas)
if socios == '1':
    sql_loader = "{0}sqlldr userid={1}/{2}@{3} control={4}{5} log={6}socio.log".format(path_sqlldr,username,password,banco_dados,path_carga_v2,arq_ctl_extr_socio, path_relatorio_sqlldr)
    ldr_socios = subprocess.call(sql_loader, shell=True)
    print(socios)
if estab == '1':
    sql_loader = "{0}sqlldr userid={1}/{2}@{3} control={4}{5} log={6}estabele.log".format(path_sqlldr,username,password,banco_dados,path_carga_v2,arq_ctl_extr_estabelecimento,path_relatorio_sqlldr)
    ldr_estab = subprocess.call(sql_loader, shell=True)
    print(estab)
if simples == '1':
    sql_loader = "{0}sqlldr userid={1}/{2}@{3} control={4}{5} log={6}simples.log".format(path_sqlldr,username,password,banco_dados,path_carga_v2,arq_ctl_extr_simples,path_relatorio_sqlldr)
    ldr_simples = subprocess.call(sql_loader, shell=True)
    print(simples)
if q_socio == '1':
    sql_loader = "{0}sqlldr userid={1}/{2}@{3} control={4}{5} log={6}qualificacao_socio.log".format(path_sqlldr,username,password,banco_dados,path_carga_v2,arq_ctl_extr_qualificacao_socio,path_relatorio_sqlldr)
    ldr_qualificacao_socio = subprocess.call(sql_loader, shell=True)
    print(q_socio)
if nat_ju == '1':
    sql_loader = "{0}sqlldr userid={1}/{2}@{3} control={4}{5} log={6}natureza_juridica.log".format(path_sqlldr,username,password,banco_dados,path_carga_v2,arq_ctl_extr_natureza_juridica,path_relatorio_sqlldr)
    ldr_natureza_juridica = subprocess.call(sql_loader, shell=True)
    print(nat_ju)
if m_sit == '1':
    sql_loader = "{0}sqlldr userid={1}/{2}@{3} control={4}{5} log={6}motivos_situacao.log".format(path_sqlldr,username,password,banco_dados,path_carga_v2,arq_ctl_motivos_situacao,path_relatorio_sqlldr)
    ldr_motivo_situacao = subprocess.call(sql_loader, shell=True)
    print(m_sit)
    print(ldr_motivo_situacao)
if pais == '1':
    sql_loader = "{0}sqlldr userid={1}/{2}@{3} control={4}{5} log={6}pais.log".format(path_sqlldr,username,password,banco_dados,path_carga_v2,arq_ctl_extr_pais,path_relatorio_sqlldr)
    ldr_pais = subprocess.call(sql_loader, shell=True)
if municipio == '1':
    sql_loader = "{0}sqlldr userid={1}/{2}@{3} control={4}{5} log={6}municipio.log".format(path_sqlldr,username,password,banco_dados,path_carga_v2,arq_ctl_extr_municipio,path_relatorio_sqlldr)
    ldr_municipio = subprocess.call(sql_loader, shell=True)
if cnae == '1':
    sql_loader = "{0}sqlldr userid={1}/{2}@{3} control={4}{5} log={6}cnae.log".format(path_sqlldr,username,password,banco_dados,path_carga_v2,arq_ctl_extr_cnae,path_relatorio_sqlldr)
    ldr_cnae = subprocess.call(sql_loader, shell=True)
