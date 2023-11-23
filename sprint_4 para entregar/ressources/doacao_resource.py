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

def create(doacao):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = """
                INSERT INTO t_vs_doacao (id_doacao, id_usuario, vl_doacao, mt_pagamento, dt_cadastro, nm_usuario)
                VALUES (seq_doacao.nextval, :idUsuario, :valor, :forma, to_date(:data, 'DD/MM/YYYY HH24:MI'), :usuario) """
                cur.execute(sql, doacao)
            
            con.commit()

    except Exception as error:
        print("Ocorreu um erro ao realizar sua doacao.")
        raise error






