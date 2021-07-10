import mysql.connector


db = mysql.connector.connect(
    host='localhost',
    database='CADASTRO',
    user='root',
    password='Blumenau1'
)


def add(nome, sobrenome, cpf, email, telefone):
    try:
        cursor = db.cursor()
        print('Conectado com sucesso')
        comando_sql = "INSERT INTO PESSOAS (NOME, SOBRENOME, CPF, EMAIL, TELEFONE) VALUES(%s, %s, %s, %s, %s)"
        valores = (nome, sobrenome, cpf, email, telefone)
        cursor.execute(comando_sql, valores)
        db.commit()
        cursor.close()
    except:
        print('Não foi possivel conectar ao banco.')

def delete(cpf):
    try:
        cursor = db.cursor()
        print('Conectado com sucesso')
        comando_sql = f"DELETE FROM PESSOAS WHERE CPF = {cpf}"
        cursor.execute(comando_sql)
        db.commit()
        cursor.close()
    except:
        print('Não foi possivel conectar ao banco.')

def read(cpf):
    try:
        cursor = db.cursor()
        print('Conectado com sucesso')
        comando_sql = f"SELECT * FROM PESSOAS WHERE CPF = {cpf}" 
        cursor.execute(comando_sql)
        resultado = cursor.fetchall()
        cursor.close()
        print(resultado)
    except:
        print('Não foi possivel conectar ao banco.')