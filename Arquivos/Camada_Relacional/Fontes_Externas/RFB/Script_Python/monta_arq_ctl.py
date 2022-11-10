import os
from dotenv_decodificador import *

PATH_OUTPUT = 'output/'
PATH_CARGA = 'carga_v2/'
PATH_ARQUIVOS_PROCESSAR = path_arquivos_processar
PATH_CARGA_N = path_carga_v2
PATH_EMPRESA = 'empresa/'
PATH_ESTABELECIMENTO = 'estabelecimento/'
PATH_SOCIO = 'socio/'
PATH_SIMEI = 'simei/'
PATH_CNAE = 'cnae/'
PATH_MUNICIPIO = 'municipio/'
PATH_NAT_JU = 'nat_ju/'
PATH_PAIS = 'pais/'
PATH_QUALIF_SOCIO = 'qualif_socio/'
#PATH_MOTIVOS_SITU = 'motivos_situ/'

path_list = [PATH_EMPRESA, PATH_ESTABELECIMENTO, PATH_SOCIO, PATH_SIMEI, PATH_CNAE, PATH_MUNICIPIO, PATH_NAT_JU, PATH_PAIS, PATH_QUALIF_SOCIO]

txt_ctl = None
txt_tabela = None

print("Montando arquivos de controle\n")
print(PATH_CARGA_N)
for path_dir in path_list:
    txt_ctl = '''OPTIONS (errors=9999999, SKIP=0)
load data CHARACTERSET WE8MSWIN1252
'''

    for file in os.listdir(PATH_OUTPUT+path_dir):
        #pega nome de cada arquivo
        txt_ctl = txt_ctl + '''infile \''''+PATH_ARQUIVOS_PROCESSAR+'''{2}/{1}' "str '\{0}'"
'''.format('n',file,path_dir.replace("/",""))

    txt_ctl = txt_ctl + '''badfile \''''+PATH_CARGA_N+'''{0}.bad'
'''.format(path_dir.replace("/",""))

    txt_ctl = txt_ctl + '''discardfile \''''+PATH_CARGA_N+'''{0}.dsc'
'''.format(path_dir.replace("/",""))

    
    if path_dir == PATH_EMPRESA:
        txt_tabela = '''truncate
into table EXTR_EMPRESAS
fields terminated by ';'
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
    ( CNPJ_BASICO,
     RAZAO_SOCIAL,
     COD_NAT_JURIDICA,
     QUALIF_RESP,
     CAPITAL_SOCIAL,
     PORTE,
     ENTE_FEDERATIVO
    )
'''
    elif path_dir == PATH_ESTABELECIMENTO:
        txt_tabela = '''truncate
into table EXTR_ESTABELECIMENTO
fields terminated by ';'
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
           ( CNPJ_BASICO,
             CNPJ_ORDEM,
             CNPJ_DV,
             MATRIZ_FILIAL,
             NOME_FANTASIA,
             SITUACAO,
             DATA_SITUACAO,
             MOTIVO_SITUACAO,
             NM_CIDADE_EXTERIOR,
             COD_PAIS,
             DATA_INICIO_ATIV,
             CNAE_FISCAL,
             CNAE_FISCAL_SEC CHAR(1607),
             TIPO_LOGRADOURO,
             LOGRADOURO,
             NUMERO,
             COMPLEMENTO,
             BAIRRO,
             CEP,
             UF,
             COD_MUNICIPIO,
             DDD_1,
             TELEFONE_1,
             DDD_2,
             TELEFONE_2,
             DDD_FAX,
             NUM_FAX,
             EMAIL,
             SIT_ESPECIAL,
             DATA_SIT_ESPECIAL
           )
'''
    elif path_dir == PATH_SOCIO:
        txt_tabela = '''truncate
into table EXTR_SOCIO
fields terminated by ';'
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
           ( CNPJ_BASICO,
             TIPO_SOCIO,
             NOME_SOCIO,
             CNPJ_CPF_SOCIO,
             COD_QUALIFICACAO,
             DATA_ENTRADA,
             COD_PAIS_EXT,
             CPF_REPRES,
             NOME_REPRES,
             COD_QUALIF_REPRES,
             FAIXA_ETARIA
           )
'''
    elif path_dir == PATH_SIMEI:
        txt_tabela = '''truncate
into table EXTR_SIMEI
fields terminated by ';'
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
           ( CNPJ_BASICO,
             OPC_SIMPLES,
             DATA_OPC_SIMPLES,
             DATA_EXC_SIMPLES,
             OPC_MEI,
             DATA_OPC_MEI,
             DATA_EXC_MEI
           )
'''
    elif path_dir == PATH_QUALIF_SOCIO:
        txt_tabela = '''truncate
into table DOM_QUALIFICACAO_SOCIO
fields terminated by ';'
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
           ( COD,
             DESCRICAO
           )
'''
    elif path_dir == PATH_NAT_JU:
        txt_tabela = '''truncate
into table DOM_NATUREZA_JURIDICA
fields terminated by ';'
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
           ( CODIGO,
             NATUREZA_JURIDICA
           )
'''
    elif path_dir == PATH_PAIS:
        txt_tabela = '''truncate
into table DOM_PAIS
fields terminated by ';'
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
           ( COD_PAIS,
             NOME_PAIS
           )
'''
    elif path_dir == PATH_MUNICIPIO:
        txt_tabela = '''truncate
into table DOM_MUNICIPIO
fields terminated by ';'
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
           ( COD_MUNICIPIO,
             MUNICIPIO
           )
'''
    elif path_dir == PATH_CNAE:
        txt_tabela = '''truncate
into table DOM_CNAES
fields terminated by ';'
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
           ( CNAE,
             DESCRICAO
           )
'''
    else:
        txt_tabela = None
    txt_ctl = txt_ctl + txt_tabela

    nome_ctl = '{0}.ctl'.format(path_dir.replace("/",""))
    with open(PATH_CARGA+nome_ctl,"w") as register_file:
        register_file.write(txt_ctl)

#print(txt_ctl)
