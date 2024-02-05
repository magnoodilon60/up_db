import mysql.connector
import pandas as pd
from time import sleep
#from app.config_banco import host, port, user, password, database
from app.config_banco import host, port, user, password, database

# ler o arquivo excel
df = pd.read_excel(r"D:\\py_hnna\\data\\precos_cisfa_TESTE.xls")

# fazer interação com o dataframe "df"
for i, valores in df.iterrows():
	# abrir conexão com o banco
	try:

		if valores.mnemonico == 'A200' or valores.codigo == '' or valores.preco == 0:
			log_arquivo = [valores.mnemonico, valores.codigo, valores.preco]
			
			with open("log_valores_nulos.txt", "a") as stream:
				for x in log_arquivo.split():
					print(x, file=stream)
	except:

		conexao = mysql.connector.connect(
		host = host,
		port = port,
		user = user,
		password = password,
		database = database,
	)
		cursor = conexao.cursor()
		# pega o resultado do for faz o slice em seguida monta o update para o banco
		tb_preco = f''' UPDATE precos SET Codigo='{valores.codigo}', Preco='{valores.preco}' WHERE  Tabela=5 AND Mnemonico='{valores.mnemonico}';	'''
		# executa o update 
		cursor.execute(tb_preco)
		# comita / salva no banco de dados
		conexao.commit()
		# fecha a conexão com o banco
		cursor.close()

		conexao.close()
		sleep(2)




