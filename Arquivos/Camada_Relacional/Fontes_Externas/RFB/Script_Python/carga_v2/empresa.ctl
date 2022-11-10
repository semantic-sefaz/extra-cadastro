OPTIONS (errors=9999999, SKIP=0)
load data CHARACTERSET WE8MSWIN1252
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/empresa/K3241.K03200Y8.D10814.EMPRECSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/empresa/K3241.K03200Y2.D10814.EMPRECSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/empresa/K3241.K03200Y7.D10814.EMPRECSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/empresa/K3241.K03200Y5.D10814.EMPRECSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/empresa/K3241.K03200Y1.D10814.EMPRECSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/empresa/K3241.K03200Y9.D10814.EMPRECSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/empresa/K3241.K03200Y4.D10814.EMPRECSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/empresa/K3241.K03200Y6.D10814.EMPRECSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/empresa/K3241.K03200Y3.D10814.EMPRECSV.csv' "str '\n'"
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/empresa/K3241.K03200Y0.D10814.EMPRECSV.csv' "str '\n'"
badfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/empresa.bad'
discardfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/empresa.dsc'
truncate
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
