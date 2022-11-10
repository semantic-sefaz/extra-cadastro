import cx_Oracle
#import config_db_oracle as cfg
from dotenv_decodificador import username, password, dsn, encoding_db
import requests
import re
import os
import shutil
import json
import time  



def retorna_data():
    with open("register_scrapping.json","r") as register_file:
        register = json.load(register_file)
    return (register["date_last_update"])





def cria_tb ():
    data = retorna_data()
    data = data.replace("/", "-")
    sql = ("insert into hist_carga (data_carga,versao_layout) values(:data_carga,:versao) ")
    versao = 'v2'
    data_carga = data
    try:
        # create a connection to the Oracle Database
        #cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_12_2") # for windows platform
        with cx_Oracle.connect(username,
                            password,
                            dsn,  
                            encoding=encoding_db) as connection:
            # create a new cursor
            with connection.cursor() as cursor:
                # call the function
                revenue = cursor.execute(sql,[data_carga,versao])
                connection.commit()
    except cx_Oracle.Error as error:
        print(error)

#cria_tb()


def truncate_tbs():

    sql = ("""TRUNCATE TABLE RFB_EMPRESA; 
    RFB_EMPRESA_HOLDING; TRUNCATE TABLE RFB_ENDERECO; TRUNCATE TABLE RFB_ENDERECO_EXTERIOR, 
    TRUNCATE TABLE RFB_ESTABELECIMENTO; TRUNCATE TABLE RFB_ESTABELECIMENTO_EXTERIOR, 
    TRUNCATE TABLE RFB_ESTRANGEIRO; TRUNCATE TABLE RFB_FAIXA_ETARIA; TRUNCATE TABLE RFB_NAO_OPTANTE_EXCLUSO_SIMPLES,
    TRUNCATE TABLE RFB_NATUREZA_LEGAL; TRUNCATE TABLE RFB_OPCAO_MEI; TRUNCATE TABLE RFB_OPCAO_SIMPLES; TRUNCATE TABLE RFB_PESSOA; TRUNCATE TABLE RFB_QUALIFICACAO, 
    TRUNCATE TABLE RFB_RAZAO_SITUACAO_CADASTRAL; TRUNCATE TABLE RFB_REPRESENTANTE; TRUNCATE TABLE RFB_SITUACAO_CADASTRAL, 
    TRUNCATE TABLE RFB_SITUACAO_ESPECIAL,  TRUNCATE TABLE RFB_SOCIEDADE_COM_ESTRANGEIRO; TRUNCATE TABLE RFB_SOCIEDADE_COM_HOLDING,
    TRUNCATE TABLE RFB_SOCIEDADE_COM_PESSOA_FISICA; TRUNCATE TABLE RFB_TEM_ATIV_ECONOMICA_SECUNDARIA; TRUNCATE TABLE RFB_TEM_ESTABELECIMENTO,
    TRUNCATE TABLE RFB_TEM_SITUACAO_CADASTRAL; TRUNCATE TABLE RFB_TEM_SITUACAO_ESPECIAL; TRUNCATE TABLE RFB_TEM_SOCIEDADE_ESTRANGEIRA, 
    TRUNCATE TABLE RFB_TEM_SOCIEDADE_FISICA; TRUNCATE TABLE RFB_TEM_SOCIEDADE_JURIDICA; TRUNCATE TABLE RFB_TEM_SOCIO_PESSOA_FISICA,
    TRUNCATE TABLE RFB_TEM_SOCIO_PESSOA_JURIDICA; """)
    try:
        # create a connection to the Oracle Database
        #cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_12_2") # for windows platform
        with cx_Oracle.connect(username,
                            password,
                            dsn,  
                            encoding=encoding_db) as connection:
            # create a new cursor
            with connection.cursor() as cursor:
                # call the function
                revenue = cursor.execute(sql)
                connection.commit()
    except cx_Oracle.Error as error:
        print(error)



def truncate_olds_tbs():

    sql = ("""TRUNCATE TABLE RFB_EMPRESA_OLD; TRUNCATE TABLE RFB_EMPRESA_HOLDING_OLD; 
TRUNCATE TABLE RFB_ENDERECO_OLD; 
TRUNCATE TABLE RFB_ENDERECO_EXTERIOR_OLD; TRUNCATE TABLE RFB_ESTABELECIMENTO_OLD; 
TRUNCATE TABLE RFB_ESTABELECIMENTO_EXTERIOR_OLD; TRUNCATE TABLE RFB_ESTRANGEIRO_OLD; 
TRUNCATE TABLE RFB_FAIXA_ETARIA_OLD; TRUNCATE TABLE RFB_NATUREZA_LEGAL_OLD,  TRUNCATE TABLE RFB_OPCAO_MEI_OLD, 
TRUNCATE TABLE RFB_OPCAO_SIMPLES_OLD; TRUNCATE TABLE RFB_PESSOA_OLD; TRUNCATE TABLE RFB_QUALIFICACAO_OLD;
TRUNCATE TABLE RFB_RAZAO_SITUACAO_CADASTRAL_OLD; TRUNCATE TABLE RFB_REPRESENTANTE_OLD,
TRUNCATE TABLE RFB_SITUACAO_CADASTRAL_OLD; TRUNCATE TABLE RFB_SITUACAO_ESPECIAL_OLD;
TRUNCATE TABLE RFB_SOCIEDADE_COM_ESTRANGEIRO_OLD; TRUNCATE TABLE RFB_SOCIEDADE_COM_HOLDING_OLD;
TRUNCATE TABLE RFB_SOCIEDADE_COM_PESSOA_FISICA_OLD; TRUNCATE TABLE RFB_TEM_ATIV_ECONOMICA_SECUNDARIA_OLD; 
TRUNCATE TABLE RFB_TEM_ESTABELECIMENTO_OLD ; TRUNCATE TABLE RFB_TEM_SITUACAO_CADASTRAL_OLD; 
TRUNCATE TABLE RFB_TEM_SITUACAO_ESPECIAL_OLD; TRUNCATE TABLE RFB_TEM_SOCIEDADE_ESTRANGEIRA_OLD; 
TRUNCATE TABLE RFB_TEM_SOCIEDADE_FISICA_OLD; TRUNCATE TABLE RFB_TEM_SOCIEDADE_JURIDICA_OLD; """)
    try:
        # create a connection to the Oracle Database
        #cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_12_2") # for windows platform
        with cx_Oracle.connect(username,
                            password,
                            dsn,  
                            encoding=encoding_db) as connection:
            # create a new cursor
            with connection.cursor() as cursor:
                # call the function
                revenue = cursor.execute(sql)
                connection.commit()
    except cx_Oracle.Error as error:
        print(error)


# def load_tabelas_normalizadas():
#     load_norm = None
#     try:
#         # create a connection to the Oracle Database
#         cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_12_2") # for windows platform
#         with cx_Oracle.connect(username,
#                             password,
#                             dsn,
#                             encoding=encoding_db) as connection:
#             # create a new cursor
#             with connection.cursor() as cursor:
#                 # call the function
#                 load_norm = cursor.callfunc('carrega_tb_norm',
#                                         int,
#                                         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
#                 if load_norm == 1:
#                     connection.commit()
#                 else:
#                     connection.rollback()
                
    
    # except cx_Oracle.Error as error:
    #     print(error)
'''
def load_tabelas_normalizadas_1():
    load_norm = None
    try:
        # create a connection to the Oracle Database
        #cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\instantclient_19_11") # for windows platform
        with cx_Oracle.connect(username,
                            password,
                            dsn,  
                            encoding=encoding_db) as connection:
            # create a new cursor
            with connection.cursor() as cursor:
                # call the function
                load_norm = cursor.callfunc('POVOA_RFB_EMPRESA',
                                        int
                                        )
                if load_norm == 13:
                     print("Povoando...")
                     connection.commit()
                     print("Ok!")
                else:
                    print("Erro no povoamento da POVOA_RFB_EMPRESA")
                    connection.rollback()
                
    
    except cx_Oracle.Error as error:
        print(error)



'''


def check_versions():

    sql = ("""SELECT COUNT(*) FROM HIST_CARGA HAVING (COUNT(*) > 1)""")
    try:
        with cx_Oracle.connect(username,
                            password,
                            dsn,  
                            encoding=encoding_db) as connection:
            # create a new cursor
            with connection.cursor() as cursor:
                # call the function
                revenue = cursor.execute(sql)
                result = revenue.fetchone()[0]
                return result

    except cx_Oracle.Error as error:
        print(error)



#print(check_versions())


def count(table):

    sql = ("SELECT COUNT(*) FROM "+table)
    try:
        with cx_Oracle.connect(username,
                            password,
                            dsn,  
                            encoding=encoding_db) as connection:
            # create a new cursor
            with connection.cursor() as cursor:
                # call the function
                revenue = cursor.execute(sql)
                result = revenue.fetchone()[0]
                return result

    except cx_Oracle.Error as error:
        print(error)

#print(count("RFB_FAIXA_ETARIA"))

def recreate_olds():

    queriesDrop = ['DROP TABLE RFB_EMPRESA_OLD','DROP TABLE RFB_EMPRESA_HOLDING_OLD', 'DROP TABLE RFB_ENDERECO_OLD',
    'DROP TABLE RFB_ENDERECO_EXTERIOR_OLD', 'DROP TABLE RFB_ESTABELECIMENTO_OLD', 'DROP TABLE RFB_ESTABELECIMENTO_EXTERIOR_OLD',
    'DROP TABLE RFB_ESTRANGEIRO_OLD', 'DROP TABLE RFB_FAIXA_ETARIA_OLD',
    'DROP TABLE RFB_NATUREZA_LEGAL_OLD', 'DROP TABLE RFB_OPCAO_MEI_OLD', 'DROP TABLE RFB_OPCAO_SIMPLES_OLD',
    'DROP TABLE RFB_PESSOA_OLD', 'DROP TABLE RFB_QUALIFICACAO_OLD', 'DROP TABLE RFB_RAZAO_SITUACAO_CADASTRAL_OLD',
    'DROP TABLE RFB_SITUACAO_CADASTRAL_OLD', 'DROP TABLE RFB_SITUACAO_ESPECIAL_OLD', 'DROP TABLE RFB_SOCIEDADE_COM_ESTRANGEIRO_OLD',
    'DROP TABLE RFB_SOCIEDADE_COM_HOLDING_OLD', 'DROP TABLE RFB_SOCIEDADE_COM_PESSOA_FISICA_OLD',
    'DROP TABLE RFB_TEM_ATIV_ECONOMICA_SECUNDARIA_OLD', 'DROP TABLE RFB_TEM_ESTABELECIMENTO_OLD', 'DROP TABLE RFB_TEM_SITUACAO_ESPECIAL_OLD',
    'DROP TABLE RFB_TEM_SOCIEDADE_ESTRANGEIRA_OLD', 'DROP TABLE RFB_TEM_SOCIEDADE_FISICA_OLD', 'DROP TABLE RFB_TEM_SOCIEDADE_JURIDICA_OLD']

    queriesCreate = ['CREATE TABLE RFB_EMPRESA_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_EMPRESA',
'CREATE TABLE RFB_EMPRESA_HOLDING_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_EMPRESA_HOLDING',
'CREATE TABLE RFB_ENDERECO_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_ENDERECO',
'CREATE TABLE RFB_ENDERECO_EXTERIOR_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_ENDERECO_EXTERIOR',
'CREATE TABLE RFB_ESTABELECIMENTO_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_ESTABELECIMENTO',
'CREATE TABLE RFB_ESTABELECIMENTO_EXTERIOR_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_ESTABELECIMENTO_EXTERIOR',
'CREATE TABLE RFB_ESTRANGEIRO_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_ESTRANGEIRO', 
'CREATE TABLE RFB_FAIXA_ETARIA_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_FAIXA_ETARIA',
'CREATE TABLE RFB_NATUREZA_LEGAL_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_NATUREZA_LEGAL', 
'CREATE TABLE RFB_OPCAO_MEI_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_OPCAO_MEI', 
'CREATE TABLE RFB_OPCAO_SIMPLES_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_OPCAO_SIMPLES', 
'CREATE TABLE RFB_PESSOA_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_PESSOA', 
'CREATE TABLE RFB_QUALIFICACAO_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_QUALIFICACAO', 
'CREATE TABLE RFB_RAZAO_SITUACAO_CADASTRAL_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_RAZAO_SITUACAO_CADASTRAL',
'CREATE TABLE RFB_SITUACAO_CADASTRAL_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_SITUACAO_CADASTRAL', 
'CREATE TABLE RFB_SITUACAO_ESPECIAL_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_SITUACAO_ESPECIAL',
'CREATE TABLE RFB_SOCIEDADE_COM_ESTRANGEIRO_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_SOCIEDADE_COM_ESTRANGEIRO',
'CREATE TABLE RFB_SOCIEDADE_COM_HOLDING_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_SOCIEDADE_COM_HOLDING',
'CREATE TABLE RFB_SOCIEDADE_COM_PESSOA_FISICA_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_SOCIEDADE_COM_PESSOA_FISICA', 
'CREATE TABLE RFB_TEM_ATIV_ECONOMICA_SECUNDARIA_OLD TABLESPACE TS_NORM_TB_HIST  AS SELECT * FROM RFB_TEM_ATIV_ECONOMICA_SECUNDARIA',
'CREATE TABLE RFB_TEM_ESTABELECIMENTO_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_TEM_ESTABELECIMENTO', 
'CREATE TABLE RFB_TEM_SITUACAO_ESPECIAL_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_TEM_SITUACAO_ESPECIAL', 
'CREATE TABLE RFB_TEM_SOCIEDADE_ESTRANGEIRA_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_TEM_SOCIEDADE_ESTRANGEIRA', 
'CREATE TABLE RFB_TEM_SOCIEDADE_FISICA_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_TEM_SOCIEDADE_FISICA', 
'CREATE TABLE RFB_TEM_SOCIEDADE_JURIDICA_OLD TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_TEM_SOCIEDADE_JURIDICA' ]

    try:
        # create a connection to the Oracle Database
        #cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_12_2") # for windows platform
        with cx_Oracle.connect(username,
                            password,
                            dsn,  
                            encoding=encoding_db) as connection:
            # create a new cursor
            for x in queriesDrop:
                with connection.cursor() as cursor:
                # call the function
                    revenue = cursor.execute(x)
                    print('Tabela OLD dropada: '+x)
                    connection.commit()
            
            for x in queriesCreate:
                with connection.cursor() as cursor:
                # call the function
                    revenue = cursor.execute(x)
                    print('Tabela OLD recriada: '+x)
                    connection.commit()

    except cx_Oracle.Error as error:
        print(error)


def recreate_news():

    queriesDrop = ['DROP TABLE RFB_EMPRESA_NEW','DROP TABLE RFB_EMPRESA_HOLDING_NEW', 'DROP TABLE RFB_ENDERECO_NEW',
    'DROP TABLE RFB_ENDERECO_EXTERIOR_NEW', 'DROP TABLE RFB_ESTABELECIMENTO_NEW', 'DROP TABLE RFB_ESTABELECIMENTO_EXTERIOR_NEW',
    'DROP TABLE RFB_ESTRANGEIRO_NEW', 'DROP TABLE RFB_FAIXA_ETARIA_NEW',
    'DROP TABLE RFB_NATUREZA_LEGAL_NEW', 'DROP TABLE RFB_OPCAO_MEI_NEW', 'DROP TABLE RFB_OPCAO_SIMPLES_NEW',
    'DROP TABLE RFB_PESSOA_NEW', 'DROP TABLE RFB_QUALIFICACAO_NEW', 'DROP TABLE RFB_RAZAO_SITUACAO_CADASTRAL_NEW',
    'DROP TABLE RFB_SITUACAO_CADASTRAL_NEW', 'DROP TABLE RFB_SITUACAO_ESPECIAL_NEW', 'DROP TABLE RFB_SOCIEDADE_COM_ESTRANGEIRO_NEW',
    'DROP TABLE RFB_SOCIEDADE_COM_HOLDING_NEW', 'DROP TABLE RFB_SOCIEDADE_COM_PESSOA_FISICA_NEW',
    'DROP TABLE RFB_TEM_ATIV_ECONOMICA_SECUNDARIA_NEW', 'DROP TABLE RFB_TEM_ESTABELECIMENTO_NEW', 'DROP TABLE RFB_TEM_SITUACAO_ESPECIAL_NEW',
    'DROP TABLE RFB_TEM_SOCIEDADE_ESTRANGEIRA_NEW', 'DROP TABLE RFB_TEM_SOCIEDADE_FISICA_NEW', 'DROP TABLE RFB_TEM_SOCIEDADE_JURIDICA_NEW']

    queriesCreate = ['CREATE TABLE RFB_EMPRESA_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_EMPRESA',
'CREATE TABLE RFB_EMPRESA_HOLDING_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_EMPRESA_HOLDING',
'CREATE TABLE RFB_ENDERECO_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_ENDERECO',
'CREATE TABLE RFB_ENDERECO_EXTERIOR_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_ENDERECO_EXTERIOR',
'CREATE TABLE RFB_ESTABELECIMENTO_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_ESTABELECIMENTO',
'CREATE TABLE RFB_ESTABELECIMENTO_EXTERIOR_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_ESTABELECIMENTO_EXTERIOR',
'CREATE TABLE RFB_ESTRANGEIRO_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_ESTRANGEIRO', 
'CREATE TABLE RFB_FAIXA_ETARIA_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_FAIXA_ETARIA',
'CREATE TABLE RFB_NATUREZA_LEGAL_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_NATUREZA_LEGAL', 
'CREATE TABLE RFB_OPCAO_MEI_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_OPCAO_MEI', 
'CREATE TABLE RFB_OPCAO_SIMPLES_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_OPCAO_SIMPLES', 
'CREATE TABLE RFB_PESSOA_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_PESSOA', 
'CREATE TABLE RFB_QUALIFICACAO_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_QUALIFICACAO', 
'CREATE TABLE RFB_RAZAO_SITUACAO_CADASTRAL_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_RAZAO_SITUACAO_CADASTRAL',
'CREATE TABLE RFB_SITUACAO_CADASTRAL_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_SITUACAO_CADASTRAL', 
'CREATE TABLE RFB_SITUACAO_ESPECIAL_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_SITUACAO_ESPECIAL',
'CREATE TABLE RFB_SOCIEDADE_COM_ESTRANGEIRO_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_SOCIEDADE_COM_ESTRANGEIRO',
'CREATE TABLE RFB_SOCIEDADE_COM_HOLDING_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_SOCIEDADE_COM_HOLDING',
'CREATE TABLE RFB_SOCIEDADE_COM_PESSOA_FISICA_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_SOCIEDADE_COM_PESSOA_FISICA', 
'CREATE TABLE RFB_TEM_ATIV_ECONOMICA_SECUNDARIA_NEW TABLESPACE TS_NORM_TB_HIST  AS SELECT * FROM RFB_TEM_ATIV_ECONOMICA_SECUNDARIA',
'CREATE TABLE RFB_TEM_ESTABELECIMENTO_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_TEM_ESTABELECIMENTO', 
'CREATE TABLE RFB_TEM_SITUACAO_ESPECIAL_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_TEM_SITUACAO_ESPECIAL', 
'CREATE TABLE RFB_TEM_SOCIEDADE_ESTRANGEIRA_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_TEM_SOCIEDADE_ESTRANGEIRA', 
'CREATE TABLE RFB_TEM_SOCIEDADE_FISICA_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_TEM_SOCIEDADE_FISICA', 
'CREATE TABLE RFB_TEM_SOCIEDADE_JURIDICA_NEW TABLESPACE TS_NORM_TB_HIST AS SELECT * FROM RFB_TEM_SOCIEDADE_JURIDICA' ]

    try:
        # create a connection to the Oracle Database
        #cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_12_2") # for windows platform
        with cx_Oracle.connect(username,
                            password,
                            dsn,  
                            encoding=encoding_db) as connection:
            # create a new cursor
            for x in queriesDrop:
                with connection.cursor() as cursor:
                # call the function
                    revenue = cursor.execute(x)
                    print('Tabela NEW dropada: '+x)
                    connection.commit()
            
            for x in queriesCreate:
                with connection.cursor() as cursor:
                # call the function
                    revenue = cursor.execute(x)
                    print('Tabela NEW recriada: '+x)
                    connection.commit()
        connection.close();
    except cx_Oracle.Error as error:
        print(error)
