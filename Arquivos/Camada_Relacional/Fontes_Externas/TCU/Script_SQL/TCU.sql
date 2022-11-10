--------------------------------------------------------
--  Arquivo criado - Quarta-feira-Junho-08-2022   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table TCU_FORNECEDOR_INIDONEO
--------------------------------------------------------

  CREATE TABLE "TCU_FORNECEDOR_INIDONEO" 
   (	"CNPJ_CPF" VARCHAR2(40 BYTE), 
	"NOME" VARCHAR2(150 BYTE), 
	"UF" VARCHAR2(150 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table TCU_FORNECEDOR_INABILITADO
--------------------------------------------------------

  CREATE TABLE "TCU_FORNECEDOR_INABILITADO" 
   (	"CPF" VARCHAR2(20 BYTE), 
	"NOME" VARCHAR2(150 BYTE), 
	"UF" VARCHAR2(150 BYTE), 
	"MUNICIPIO" VARCHAR2(150 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for View CEP_ESTADO
--------------------------------------------------------

  CREATE OR REPLACE FORCE EDITIONABLE VIEW "CEP_ESTADO" ("UF", "ESTADO", "CODIGO_IBGE") AS 
  (
    SELECT UF,
    ESTADO,
    COD_IBGE AS CODIGO_IBGE
    FROM QUALOCEP_ESTADO 
)
WITH READ ONLY
;
--------------------------------------------------------
--  DDL for View CEP_CIDADE
--------------------------------------------------------

  CREATE OR REPLACE FORCE EDITIONABLE VIEW "CEP_CIDADE" ("ID_CIDADE", "ESTADO", "CEP", "CIDADE", "CODIGO_IBGE") AS 
  (
    SELECT ID_CIDADE,
    UF AS ESTADO,
    CEP,
    UPPER(REGEXP_REPLACE(TRANSLATE(CIDADE, '����Y��������������������������������������������������',
    'SZszYACEIOUAEIOUAEIOUAOEUIONYaaceiouaeiouaeiouaoeuionyy'),'\\s','_')) AS CIDADE,
    COD_IBGE AS CODIGO_IBGE
    FROM QUALOCEP_CIDADE cidade
)
WITH READ ONLY
;
--------------------------------------------------------
--  DDL for View CEP_CEP_LOGRADOURO
--------------------------------------------------------

  CREATE OR REPLACE FORCE EDITIONABLE VIEW "CEP_CEP_LOGRADOURO" ("CEP", "LOCAL_CEP", "COMPLEMENTO", "LATITUDE", "LONGITUDE") AS 
  (
    SELECT ender.CEP,
    LOCAL AS LOCAL_CEP,
    COMPLEMENTO, 
    LATITUDE,
    LONGITUDE
    FROM QUALOCEP_ENDERECO ender
    INNER JOIN
    QUALOCEP_GEO geo
    ON 
    ender.CEP = geo.CEP
)
WITH READ ONLY
;
--------------------------------------------------------
--  DDL for View TCU_FORNECEDOR_INIDONEO_VIEW
--------------------------------------------------------

  CREATE OR REPLACE FORCE EDITIONABLE VIEW "TCU_FORNECEDOR_INIDONEO_VIEW" ("CNPJ_CPF", "NOME", "UF") AS 
  (

SELECT DISTINCT REGEXP_REPLACE(CNPJ_CPF, '\D','') AS CNPJ_CPF, NOME, UF FROM TCU_FORNECEDOR_INIDONEO
)
;
--------------------------------------------------------
--  DDL for View TCU_FORNECEDOR_INABILITADO_VIEW
--------------------------------------------------------

  CREATE OR REPLACE FORCE EDITIONABLE VIEW "TCU_FORNECEDOR_INABILITADO_VIEW" ("CNPJ_CPF", "NOME", "UF", "MUNICIPIO") AS 
  (

SELECT DISTINCT REGEXP_REPLACE(CPF, '\D','') AS CNPJ_CPF, NOME, UF, UPPER(REGEXP_REPLACE(TRANSLATE(MUNICIPIO, '����Y��������������������������������������������������',
    'SZszYACEIOUAEIOUAEIOUAOEUIONYaaceiouaeiouaeiouaoeuionyy'),'\s','_')) AS MUNICIPIO FROM TCU_FORNECEDOR_INABILITADO
)
;
--------------------------------------------------------
--  DDL for Materialized View CEP_LOGRADOURO
--------------------------------------------------------

  CREATE MATERIALIZED VIEW "CEP_LOGRADOURO" ("LOGRADOURO", "TIPO_LOGRADOURO", "CIDADE", "BAIRRO", "ESTADO", "CEP", "ID_LOGRADOURO")
  ORGANIZATION HEAP PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"   NO INMEMORY 
  BUILD IMMEDIATE
  USING INDEX 
  REFRESH FORCE ON DEMAND
  USING DEFAULT LOCAL ROLLBACK SEGMENT
  USING ENFORCED CONSTRAINTS DISABLE ON QUERY COMPUTATION DISABLE QUERY REWRITE
  AS SELECT DISTINCT logradouro.LOGRADOURO, logradouro.TIPO_LOGRADOURO, bairro.CIDADE, bairro.BAIRRO, ESTADO, logradouro.CEP,
CONCAT(CONCAT(logradouro.CEP,'-'),BAIRRO) AS ID_LOGRADOURO
    FROM "QUALOCEP_ENDERECO" logradouro
    INNER JOIN
    "CEP_BAIRRO" bairro
    ON
    logradouro.ID_BAIRRO = bairro.ID_BAIRRO
    INNER JOIN
    "CEP_CIDADE" cidade
    ON
    cidade.ID_CIDADE = bairro.ID_CIDADE;

  CREATE INDEX "CEP_LOGRADOURO_INDEX1" ON "CEP_LOGRADOURO" ("LOGRADOURO") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
  CREATE INDEX "CEP_LOGRADOURO_INDEX2" ON "CEP_LOGRADOURO" ("TIPO_LOGRADOURO") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
  CREATE INDEX "CEP_LOGRADOURO_INDEX3" ON "CEP_LOGRADOURO" ("CIDADE") 
  PCTFREE 10 INITRANS 2 MAXTRANS 167 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
  CREATE INDEX "CEP_LOGRADOURO_INDEX4" ON "CEP_LOGRADOURO" ("BAIRRO") 
  PCTFREE 10 INITRANS 2 MAXTRANS 167 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
  CREATE INDEX "CEP_LOGRADOURO_INDEX5" ON "CEP_LOGRADOURO" ("ESTADO") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
  CREATE UNIQUE INDEX "CEP_LOGRADOURO_INDEX6" ON "CEP_LOGRADOURO" ("CEP") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
  CREATE UNIQUE INDEX "CEP_LOGRADOURO_INDEX7" ON "CEP_LOGRADOURO" ("ID_LOGRADOURO") 
  PCTFREE 10 INITRANS 2 MAXTRANS 167 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;

   COMMENT ON MATERIALIZED VIEW "CEP_LOGRADOURO"  IS 'snapshot table for snapshot UFC_SEM.CEP_LOGRADOURO';
--------------------------------------------------------
--  DDL for Materialized View CEP_BAIRRO
--------------------------------------------------------

  CREATE MATERIALIZED VIEW "CEP_BAIRRO" ("ID_BAIRRO", "ID_CIDADE", "ESTADO", "CIDADE", "BAIRRO", "ID_BAIRROS")
  ORGANIZATION HEAP PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"   NO INMEMORY 
  BUILD IMMEDIATE
  USING INDEX 
  REFRESH COMPLETE ON DEMAND START WITH sysdate+0 NEXT SYSDATE + 1
  USING DEFAULT LOCAL ROLLBACK SEGMENT
  USING ENFORCED CONSTRAINTS DISABLE ON QUERY COMPUTATION DISABLE QUERY REWRITE
  AS SELECT 
    bairro.ID_BAIRRO, 
    cidade.ID_CIDADE,
    cidade.ESTADO,
    UPPER(REGEXP_REPLACE(TRANSLATE(CIDADE, '����Y��������������������������������������������������',
    'SZszYACEIOUAEIOUAEIOUAOEUIONYaaceiouaeiouaeiouaoeuionyy'),'\s','_')) AS CIDADE, 
    UPPER(REGEXP_REPLACE(TRANSLATE(BAIRRO, '����Y��������������������������������������������������',
    'SZszYACEIOUAEIOUAEIOUAOEUIONYaaceiouaeiouaeiouaoeuionyy'),'\s','_')) AS BAIRRO,
    UPPER(REGEXP_REPLACE(TRANSLATE(BAIRRO, '����Y��������������������������������������������������',
    'SZszYACEIOUAEIOUAEIOUAOEUIONYaaceiouaeiouaeiouaoeuionyy'),'\s','_'))||'-'||UPPER(REGEXP_REPLACE(TRANSLATE(CIDADE, '����Y��������������������������������������������������',
    'SZszYACEIOUAEIOUAEIOUAOEUIONYaaceiouaeiouaeiouaoeuionyy'),'\s','_')) AS ID_BAIRROS
    FROM QUALOCEP_BAIRRO bairro
    INNER JOIN
    "CEP_CIDADE" cidade
    ON
    bairro.ID_CIDADE = cidade.ID_CIDADE;

  CREATE INDEX "CEP_BAIRRO_INDEX1" ON "CEP_BAIRRO" ("ID_BAIRRO") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
  CREATE INDEX "CEP_BAIRRO_INDEX2" ON "CEP_BAIRRO" ("ID_CIDADE") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
  CREATE INDEX "CEP_BAIRRO_INDEX3" ON "CEP_BAIRRO" ("CIDADE") 
  PCTFREE 10 INITRANS 2 MAXTRANS 167 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
  CREATE INDEX "CEP_BAIRRO_INDEX4" ON "CEP_BAIRRO" ("BAIRRO") 
  PCTFREE 10 INITRANS 2 MAXTRANS 167 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
  CREATE INDEX "CEP_BAIRRO_INDEX5" ON "CEP_BAIRRO" ("ID_BAIRROS") 
  PCTFREE 10 INITRANS 2 MAXTRANS 167 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
  CREATE INDEX "CEP_BAIRRO_INDEX6" ON "CEP_BAIRRO" ("ESTADO") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;

   COMMENT ON MATERIALIZED VIEW "CEP_BAIRRO"  IS 'snapshot table for snapshot UFC_SEM.CEP_BAIRRO';
