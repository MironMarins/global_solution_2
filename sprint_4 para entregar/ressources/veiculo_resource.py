import datetime as dt
import oracledb

user='rm551801'
password='040591'
dsn='oracle.fiap.com.br/orcl'
hoje = dt.datetime.now()
dataHora = hoje.strftime('%d/%m/%Y %H:%M')

# função responçavel por receber um as informações de um 
# dicionario e usar essas informações para montar uma linha na tabela
#  t_porto_veiculo_cliente

def create(veiculo):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = """
                INSERT INTO t_porto_veiculo_cliente (id_veiculo, id_cliente, nr_peso, nr_comprimento, nr_largura, nr_altura, nr_eixos, cd_placa, ds_marca,dt_cadastro)
                VALUES (seq_veiculocli.nextval, :CodigoCliente, :peso, :comprimento, :largura, :altura, :eixos, :placa, :marca, to_date(:data, 'DD/MM/YYYY HH24:MI')) """
                cur.execute(sql, veiculo)
            
            con.commit()

    except Exception as error:
        print("Ocorreu um erro ao cadastrar seu veiculo .")
        raise error



#função que trará uma lista de tuplas referente a tabela t_porto_veiculo_cliente

def find_all():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_veiculo_cliente'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro ao consultar os livros")
        raise error

#função que trará uma tupla referente a uma linha da tabela t_porto_veiculo_cliente, ulizando
# a placa do carro de um cliente cadastrado em nosso banco de dados 
# essa aplicação, que será correspondente

def find_one_by_placa(placa):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_veiculo_cliente WHERE cd_placa = :placa'
                cur.execute(sql, { 'placa': placa })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao consultar seu veiculo")
        raise error
#função que trará uma tupla referente a uma linha da tabela t_porto_veiculo_cliente, ulizando
# o id de cliente que será correspondente a informação em "id_veiculo"
def find_one_by_idVeiculo(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_veiculo_cliente WHERE id_veiculo = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao seu veiculo")
        raise error

#função responsavel por alterar informações na tabela t_porto_veiculo_cliente
#ela placa de veiculo de um cliente cadastrado em nosso banco de dados e um dicionario com novas informações 
#que substituiram as informações correspondentes a mesma linha da informação "cd_placa"

def update(veiculo, placa):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
                                         
            with con.cursor() as cur:
                sql = """UPDATE t_porto_veiculo_cliente SET id_veiculo=:idveiculo, id_cliente=:id, nr_peso=:peso, nr_comprimento=:comprimento,
                  nr_largura=:largura, nr_altura=:altura, nr_eixos=:eixos, ds_marca=:marca,dt_cadastro=:data WHERE cd_placa = :placa"""
                cur.execute(sql, { **veiculo, 'placa': placa })
            
            con.commit()

    except Exception as erro:
        print("Ocorreu um erro ao atualizar seu veiculo.")
        raise erro

#função reponsalvel por deletar uma linha da tabela t_porto_veiculo_cliente correspondente ao 
# codigo do veiculo de um cliente "correspondente a "cd_placa"

def delete(placa):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM t_porto_veiculo_cliente WHERE cd_placa = :placa'
                cur.execute(sql, { 'placa': placa })
                affected_rows = cur.rowcount
            con.commit()
            return  affected_rows

    except Exception as erro:
        print("Ocorreu um erro ao deletar o livro.")
        raise erro
#função reponsalvel por deletar uma linha da tabela t_porto_veiculo_cliente correspondente ao 
# id do veiculo de um cliente "correspondente a "id_veiculo"
def deletePorId(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM t_porto_veiculo_cliente WHERE id_cliente = :id'
                cur.execute(sql, { 'id': id })
                affected_rows = cur.rowcount
            con.commit()
            return  affected_rows

    except Exception as erro:
        print("Ocorreu um erro ao deletar o livro.")
        raise erro



