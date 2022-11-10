OPTIONS (errors=9999999, SKIP=0)
load data CHARACTERSET WE8MSWIN1252
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/qualif_socio/F.K03200Z.D10911.QUALSCSV.csv' "str '\n'"
badfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/qualif_socio.bad'
discardfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/qualif_socio.dsc'
truncate
into table DOM_QUALIFICACAO_SOCIO
fields terminated by ';'
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
           ( COD,
             DESCRICAO
           )
