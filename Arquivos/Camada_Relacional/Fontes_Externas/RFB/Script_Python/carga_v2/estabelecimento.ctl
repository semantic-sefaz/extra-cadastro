OPTIONS (errors=9999999, SKIP=0)
load data CHARACTERSET WE8MSWIN1252
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/estabelecimento/K3241.K03200Y2.D10814.ESTABELE.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/estabelecimento/K3241.K03200Y5.D10814.ESTABELE.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/estabelecimento/K3241.K03200Y1.D10814.ESTABELE.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/estabelecimento/K3241.K03200Y7.D10814.ESTABELE.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/estabelecimento/K3241.K03200Y0.D10814.ESTABELE.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/estabelecimento/K3241.K03200Y6.D10814.ESTABELE.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/estabelecimento/K3241.K03200Y4.D10814.ESTABELE.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/estabelecimento/K3241.K03200Y3.D10814.ESTABELE.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/estabelecimento/K3241.K03200Y9.D10814.ESTABELE.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/estabelecimento/K3241.K03200Y8.D10814.ESTABELE.csv' "str '\n'"
badfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/estabelecimento.bad'
discardfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/estabelecimento.dsc'
truncate
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
