import datetime as dt
import oracledb

user='rm551801'
password='040591'
dsn='oracle.fiap.com.br/orcl'
hoje = dt.datetime.now()
dataHora = hoje.strftime('%d/%m/%Y %H:%M')


# função responçavel por receber um dicionario e usar essas informações para montar uma linha na tabela
#  t_porto_chamada
def create(chamada):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = """
                INSERT INTO t_porto_chamada (id_chamada, id_problema, id_cliente, id_auxilio, id_veiculo, id_especificacao, id_carga, dt_chamada, cd_chamada)
                VALUES (seq_cham.nextval, :idProblema, :idCliente, :idAuxilio, :idVeiculo, :idEspecificacao, :idCarga, to_date(:dtChamada, 'DD/MM/YYYY HH24:MI'), :idCodigo) """
                cur.execute(sql, chamada)
            
            con.commit()

    except Exception as error:
        print("Ocorreu um erro ao realizar sua chamada.")
        raise error


#função que trará uma lista de tuplas referente a tabela t_porto_chamada

def find_all():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_chamada'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro ao consultar os livros")
        raise error

#função que procurará uma tupla referente a uma linha da tabela t_porto_chamada, ulizando
# o codigo de chamada correspondente a "cd_chamada"

def find_one_by_codigo(chamada):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_chamada WHERE cd_chamada = :chamada'
                cur.execute(sql, { 'chamada': chamada })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao consultar os livros")
        raise error
#função que procurará uma tupla referente a uma linha da tabela t_porto_chamada, ulizando
# o id de chamada correspondente a "id_chamada"

def find_one_by_id(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_chamada WHERE id_chamada = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao consultar os livros")
        raise error

#função reponsalvel por deletar uma linha da tabela t_porto_chamada correspondente ao 
# id de um veiculo id_veiculo
def deletePorIdVeiculo(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM t_porto_chamada WHERE id_veiculo = :id'
                cur.execute(sql, { 'id': id })
                affected_rows = cur.rowcount
            con.commit()
            return  affected_rows

    except Exception as erro:
        print("Ocorreu um erro ao deletar o livro.")
        raise erro
#função reponsalvel por deletar uma linha da tabela t_porto_chamada correspondente ao 
# id de um cliente "id_cliente"

def deletePorIdCliente(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM t_porto_chamada WHERE id_cliente = :id'
                cur.execute(sql, { 'id': id })
                affected_rows = cur.rowcount
            con.commit()
            return  affected_rows

    except Exception as erro:
        print("Ocorreu um erro ao deletar o livro.")
        raise erro


