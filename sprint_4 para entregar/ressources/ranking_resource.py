import datetime as dt
import oracledb
user='rm551801'
password='040591'
dsn='oracle.fiap.com.br/orcl'

#função que trará uma lista de tuplas referente a tabela t_porto_problema

def find_all_ranking():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = '''SELECT lg_usuario, SUM(vl_docao) as soma_total
                        FROM t_vs_doacao
                        join t_vs_usuario = id_usuario
                        GROUP BY lg_usuario
                        ORDER BY soma_total DESC'''
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro")
        raise error
