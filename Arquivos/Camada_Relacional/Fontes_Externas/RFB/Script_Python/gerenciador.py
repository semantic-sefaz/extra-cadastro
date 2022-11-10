import os
import shutil
import time
import json
import execute_func_oracle

empresas = 1
socios = 1
cnaes_sec = 1
qualif_socio = 1
natu_jur = 1
motivos_situ = 1
PATH_RFB_ANTIGOS = 'rfb_antigos/'
PATH_DATA = 'data/'
PATH_OUTPUT = 'output/'

date_start = time.strftime("%Y-%m-%d")

def sent_email(date_start):
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	gmail_user = 'semantic.arida@gmail.com'
	gmail_password = 'semantic2020'

	sent_from = gmail_user
	to = 'caioviktor@alu.ufc.br'
	subject = 'Relatório do script de monitoramento e triplificação da RFB'
	body = """
	Prezado Gestor,

	Este é um e-mail automático enviado para informar que o script de monitoramento e triplicação dos dados cadastrais da Receita Federal do Brasil foi executado, realizando o processo de recuperação e carga dos dados na data de {}.
	Para informações sobre o estado do processo, acesse o arquivo de log "decodificador_RFB/log/{}.log".
	Para mais informações entre em contato com a equipe técnica da SEFAZ e UFC.
	""".format(time.strftime("%d/%m/%Y"),date_start)
	
	message = MIMEMultipart()
	message['From'] = gmail_user
	message['To'] = to
	message['Subject'] = 'Relatório do script de monitoramento e triplificação da RFB'
	message.attach(MIMEText(body, 'plain',"utf-8"))

	session = smtplib.SMTP('smtp.gmail.com', 587)
	session.starttls() #enable security
	session.login(gmail_user, gmail_password) #login with mail_id and password
	text = message.as_string()
	session.sendmail(gmail_user, to, text)
	session.quit()
	print('Email enviado!')
	
def create_provenance(data_gravacao):
	with open("provenance.ttl","w") as out_file:
		today = date.today()
		graph_uri = "http://www.sefaz.ma.gov.br/ontology/Graph/RFB-Cadastro-"+today.strftime("%Y_%m_%d")
		provenance_graph = """
@prefix sd: <http://www.w3.org/ns/sparql-service-description#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix sfz: <http://www.sefaz.ma.gov.br/ontology/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .


<{0}> a sd:NamedGraph;
    sd:name <{0}>;
    prov:generatedAtTime "{2}"^^xsd:dateTime;
    sfz:source_recorded "{1}"^^xsd:dateTime;
    sfz:type_view sfz:MATERIALIZED;
    rdfs:seeAlso <{3}>;
    rdfs:label "RFB Cadastro".""".format(graph_uri,data_gravacao,time.strftime("%Y-%m-%dT%H:%M:%S"),SOURCE_URL)
		out_file.write(provenance_graph)
		print("Proveniência construída com sucesso.")
		return graph_uri

if not os.path.isdir(PATH_RFB_ANTIGOS): #Diretório de arquivos não existe
	os.mkdir(PATH_RFB_ANTIGOS)

tem_atualizacao = False
date_RFB = 0
#baixar os arquivos
message = "Inicio baixar arquivos da RFB "+time.strftime("%Y-%m-%dT%H:%M:%S")
print(message)
websc = os.system("python web_scrapping.py")
if websc == 0:
	message = "Fim baixar arquivos da RFB "+time.strftime("%Y-%m-%dT%H:%M:%S")
	print(message)
	
	with open("register_scrapping.json","r") as register_file:
		register = json.load(register_file)

		if register == None or register["date_last_update"] != "":
			qualif_socio = 0
			natu_jur = 0
			motivos_situ = 0

		qtd_carga = register["num_arq_baixados"]
		tem_atualizacao = register["updated"]
		date_RFB = register["date_last_update"]

if tem_atualizacao:
	date_splitted = date_RFB.split("/")
	data_gravacao = "{0}_{1}_{2}".format(date_splitted[2],date_splitted[1],date_splitted[0])
	path_gravacao = "{0}{1}/".format(PATH_RFB_ANTIGOS,data_gravacao)
	if not os.path.isdir(path_gravacao): #Diretório de arquivos não existe
		os.mkdir(path_gravacao)#para armazenar .zip da rfb apos carga

	#deixar arquivos baixados .zip em .csv
	#fazer a carga dos .csv para o oracle

	message = "Inicio extracao dados RFB "+time.strftime("%Y-%m-%dT%H:%M:%S")
	print(message)
	carga = "python sql_loader_oracle_rfb.py {0} {1} {2} {3} {4} {5}".format(empresas, socios, cnaes_sec, qualif_socio, natu_jur, motivos_situ)
	for file in os.listdir(PATH_DATA):
		message ="\n\n\n--------------------------------------------\nProcessando arquivo: "+file+"\n\n\n"
		print(message)
		file_path = PATH_DATA + file
		gera_csv = 'python "cnpj.py" "{}" csv "output"'.format(file_path)
		file_out_emp = 'empresas.csv'
		file_out_soc = 'socios.csv'
		file_out_cs = 'cnaes_secundarios.csv'
		attempts = 0
		carga_tb_norm = 0
		while attempts < 3 and not file_out_emp in os.listdir(PATH_OUTPUT) and not file_out_soc in os.listdir(PATH_OUTPUT) and not file_out_cs in os.listdir(PATH_OUTPUT):
			attempts += 1
			gerou_csv = os.system(gera_csv)
			if gerou_csv == 0:
				attempts = 3
				message = "Inicio sql loader arquivo "+file+" "+time.strftime("%Y-%m-%dT%H:%M:%S")
				print(message)
				carga_tb_norm = os.system(carga)
				if carga_tb_norm == 0:
					message = "Fim sql loader arquivo "+file+" "+time.strftime("%Y-%m-%dT%H:%M:%S")
					print(message)
					if os.stat("carga/empresas.bad")[6] == 0.0 and os.stat("carga/socios.bad")[6] == 0.0 and os.stat("carga/cnaes_secundarios.bad")[6] == 0.0:#.st_size() == 0:
						continue
					else: 
						print("problema no sqlldr, verificar arquivos .bad na pasta carga. Limpe-os apos correcao do problema!")
						break
				else:
					break
			else: 
				for files in os.listdir(PATH_OUTPUT):
					os.remove(PATH_OUTPUT+files) #remove possivel csv incompleto gerado
		
		if not file_out_emp in os.listdir(PATH_OUTPUT) or not file_out_soc in os.listdir(PATH_OUTPUT) or not file_out_cs in os.listdir(PATH_OUTPUT):
			print("Nao foi possivel extrair os arquivos compactados para csv")
			break
		
		for files in os.listdir(PATH_OUTPUT):
			os.remove(PATH_OUTPUT+files) #remove csv apos a carga

		if carga_tb_norm != 0:
			print("erro no carregamento do sql loader")
			break

	message = "Fim extracao dados RFB "+time.strftime("%Y-%m-%dT%H:%M:%S")
	print(message)
	#move os .zip da rfb para seu dir com data de atualizacao
	for file in os.listdir(PATH_DATA):
		shutil.move(PATH_DATA+file,path_gravacao)

	#funcao popular tb normalizadas 172.20.3.59
	popula_tb_norm = execute_func_oracle.load_tabelas_normalizadas()
	if popula_tb_norm == 1:
		#funcao calcular delta das tabelas

		#triplificar os dados do delta
		ontop = ""
		os.system(ontop)
		#bulk loading no virtuoso
	else: 
		print("erro ao tentar popular tabelas normalizadas")
else:
	print("sem atualizacao")
#######fim###

print("Executando script para triplificar os dados")
os.system("python run.py")
#Construindo proveniência
print("Construindo proveniência...")
date_splitted = date_RFB.split("/")
data_gravacao = "{0}-{1}-{2}T00:00:00".format(date_splitted[2],date_splitted[1],date_splitted[0])
graph_uri = create_provenance(data_gravacao)

temp_configs = {'uri':graph_uri,'date':"{0}-{1}-{2}".format(date_splitted[2],date_splitted[1],date_splitted[0])}
with open("temp.json","w") as temp_file:
    temp_file.write(json.dumps(temp_configs))

print("Iniciando processo de carga no virtuoso...")
os.system("python import_to_triplestore.py")

print("\n\nProcesso total concluído em "+time.strftime("%Y-%m-%dT%H:%M:%S"))
sent_email(date_start)
#https://buscacepinter.correios.com.br/app/endereco/carrega-cep-endereco.php?pagina=%2Fapp%2Fendereco%2Findex.php&cepaux=&mensagem_alerta=&endereco=60360820&tipoCEP=ALL
#COPY products_273 TO '/tmp/products_199.csv' WITH (FORMAT CSV, HEADER);
