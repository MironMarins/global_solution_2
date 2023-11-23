import datetime as dt
import oracledb
user='rm551801'
password='040591'
dsn='oracle.fiap.com.br/orcl'

#função que trará uma lista de tuplas referente a tabela t_porto_problema
def find_all_problemas():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_problema'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro")
        raise error

#função que procurará uma tupla referente a uma linha da tabela t_porto_problema
def find_one_by_id_problema(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_problema WHERE id_problema = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro na consulta ao tipo de erro")
        raise error

#função que trará uma lista de tuplas referente a tabela t_porto_especificacao

def find_all_especificacao():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_especificacao'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro")
        raise error

#função que procurará uma tupla referente a uma linha da tabela t_porto_especificacao
def find_one_by_id_especificacao(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_especificacao WHERE id_especicacao = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro na consulta ao tipo de especificacao")
        raise error


#função que trará uma lista de tuplas referente a tabela t_porto_especificacao
def find_all_auxilio():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_auxilio'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro")
        raise error

#função que procurará uma tupla referente a uma linha da tabela t_porto_especificacao
def find_one_by_id_auxilio(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_auxilio WHERE id_auxilio = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro na consulta ao tipo de especificacao")
        raise error