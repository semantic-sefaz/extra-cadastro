OPTIONS (errors=9999999, SKIP=0)
load data CHARACTERSET WE8MSWIN1252
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/socio/K3241.K03200Y0.D10814.SOCIOCSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/socio/K3241.K03200Y3.D10814.SOCIOCSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/socio/K3241.K03200Y7.D10814.SOCIOCSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/socio/K3241.K03200Y5.D10814.SOCIOCSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/socio/K3241.K03200Y1.D10814.SOCIOCSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/socio/K3241.K03200Y8.D10814.SOCIOCSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/socio/K3241.K03200Y2.D10814.SOCIOCSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/socio/K3241.K03200Y9.D10814.SOCIOCSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/socio/K3241.K03200Y6.D10814.SOCIOCSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/socio/K3241.K03200Y4.D10814.SOCIOCSV.csv' "str '\n'"
badfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/socio.bad'
discardfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/socio.dsc'
truncate
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
