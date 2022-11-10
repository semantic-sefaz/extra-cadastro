OPTIONS (errors=9999999, SKIP=0)
load data CHARACTERSET WE8MSWIN1252
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/cnae/F.K03200Z.D10814.CNAECSV.csv' "str '\n'"
badfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/cnae.bad'
discardfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/cnae.dsc'
truncate
into table DOM_CNAES
fields terminated by ';'
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
           ( CNAE,
             DESCRICAO
           )
