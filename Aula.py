# Python e MySQL
# Criar um crud simples, validar os campos e nao ter informaçães duplicadas,
# aconselho ser um cadastro de contatos

#import mysql.connector

#db = mysql.connector.connect(
#    host='localhost',
#    database='CADASTRO',
#    user='root',
#    password='Blumenau1'
#)

#try:
#    cursor = db.cursor()
#    print('Conectado com sucesso')
#
#    comando_sql = "INSERT INTO CONTATOS (NOME, SOBRENOME, CPF, EMAIL, TELEFONE) VALUES('Guilherme', 'Marcelino', '19375673026', 'gmarcelino@gmail.com', '47910283642')"
#    comando_sql = "INSERT INTO CONTATOS (NOME, SOBRENOME, CPF, EMAIL, TELEFONE) VALUES('Henrique', 'Tierling', '10764086995', 'henrique.manske.tierling@gmail.com', '47992620666')"
    #comando_sql = 'UPDATE CONTATOS SET NOME = "Enrique" WHERE ID = 5'
    #comando_sql = 'DELETE FROM CONTATOS WHERE ID = 5'     
    #comando_sql = 'SELECT * FROM CONTATOS'
    #cursor.execute(comando_sql)
    #resultado = cursor.fetchall()
    #for linha in resultado:
        #print(f'Nome: {linha[1]}, Sobrenome: {linha[2]}, CPF: {linha[3]}, E-mail: {linha[4]}, Telefone: {linha[5]}')
#    db.commit()
#    cursor.close()
#except:
#    print('Não foi possivel conectar ao banco.')