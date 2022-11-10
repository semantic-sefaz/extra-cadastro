OPTIONS (errors=9999999, SKIP=0)
load data CHARACTERSET WE8MSWIN1252
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/simei/F.K03200W.SIMPLES.CSV.D10814.csv' "str '\n'"
badfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/simei.bad'
discardfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/simei.dsc'
truncate
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
