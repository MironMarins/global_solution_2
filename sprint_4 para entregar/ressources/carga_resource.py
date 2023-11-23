import datetime as dt
import oracledb

user='rm551801'
password='040591'
dsn='oracle.fiap.com.br/orcl'

hoje = dt.datetime.now()
dataHora = hoje.strftime('%d/%m/%Y %H:%M')



def create(carga):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = """
                INSERT INTO t_porto_veiculo_carga (cd_placa, nr_peso, nr_comprimento, nr_altura, nr_largura, nr_eixos, ds_tipo, dt_cadastro, id_carga, cd_carga)
                VALUES (:placa, :peso, :comprimento, :altura, :largura, :eixos, :CargaTipo, to_date(:data, 'DD/MM/YYYY HH24:MI'),seq_cargavei.nextval,:codigo) """
                cur.execute(sql, carga)
            
            con.commit()

    except Exception as error:
        print("Ocorreu um erro ao cadastrar sua carga.")
        raise error




def find_all():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_veiculo_carga'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro ao consultar sua carga")
        raise error



def find_one_by_placa(placa):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_veiculo_carga WHERE cd_placa = :placa'
                cur.execute(sql, { 'placa': placa })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao consultar sua carga")
        raise error


def find_one_by_id(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_veiculo_carga WHERE id_carga = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao consultar sua carga")
        raise error
def find_one_by_codigo(codigo):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_veiculo_carga WHERE cd_carga = :codigo'
                cur.execute(sql, { 'codigo': codigo })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao consultar sua carga")
        raise error

def update(carga, placa):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
                                         
            with con.cursor() as cur:   
                sql = """UPDATE t_porto_veiculo_carga SET nr_peso=:peso, nr_comprimento=:comprimento, nr_altura=:altura, nr_largura=:largura,
                  nr_eixos=:eixos, ds_tipo=:CargaTipo,dt_cadastro=:data WHERE cd_placa = :placa"""
                cur.execute(sql, { **carga, 'placa': placa })
            
            con.commit()

    except Exception as erro:
        print("Ocorreu um erro ao atualizar sua carga.")
        raise erro




def suaCarga(carga):
    print("Qual informação gostaria de alterar? ")
    print("[1] peso: ",carga[1])
    print("[2] comprimento: ",carga[2])
    print("[3] altura: ",carga[3])
    print("[4] largura: ",carga[4])
    print("[5] eixos: ",carga[5])
    print("[6] cargaTipo: ",carga[6])
    
    



def delete(placa):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM t_porto_veiculo_carga WHERE cd_placa = :placa'
                cur.execute(sql, { 'placa': placa })
                affected_rows = cur.rowcount
            con.commit()
            return  affected_rows

    except Exception as erro:
        print("Ocorreu um erro ao deletar sua carga.")
        raise erro



