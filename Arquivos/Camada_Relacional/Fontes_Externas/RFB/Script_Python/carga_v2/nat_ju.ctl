OPTIONS (errors=9999999, SKIP=0)
load data CHARACTERSET WE8MSWIN1252
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/nat_ju/F.K03200Z.D10814.NATJUCSV.csv' "str '\n'"
badfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/nat_ju.bad'
discardfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/nat_ju.dsc'
truncate
into table DOM_NATUREZA_JURIDICA
fields terminated by ';'
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
           ( CODIGO,
             NATUREZA_JURIDICA
           )
