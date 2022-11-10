OPTIONS (errors=9999999, SKIP=1)
load data
characterset UTF8
infile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/output/motivos_situ/DominiosMotivoSituaoCadastral.csv' "str '\n'"
badfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/MotivoSituao.bad'
discardfile '/h1_centnas_bkp01/arquivos_processar/ufc/decodificador_v2.0/carga_v2/MotivoSituao.dsc'
truncate 
into table motivos_situacao
fields terminated by ";"	optionally enclosed by '"'
trailing nullcols
( CODIGO, DESCRICAO CHAR (128))
