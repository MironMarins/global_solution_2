
import oracledb
import datetime as dt

user='rm551801'
password='040591'
dsn='oracle.fiap.com.br/orcl'
hoje = dt.datetime.now()
dataHora = hoje.strftime('%d/%m/%Y %H:%M')

# função responçavel por receber um as informações de uma 
# dicionario e usar essas informações para montar uma linha na tabela
#  t_rs_usuario

def create(cliente):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = """
                INSERT INTO t_vs_usuario (id_usuario, no_usuario, nr_cpf, nr_rg, lg_usuario, sh_usuario,
                  dt_nascimento, fl_sexo_biologico, ds_estado_civil, nm_grupo_sanguineo, dt_cadastro, nm_usuario)
                VALUES (seq_usuario.nextval, :nome, :cpf, :rg, :login,:senha, to_date(:nascimento, 'DD/MM/YYYY'), :sexo, :estadoCivil, :sangue, to_date(:data, 'DD/MM/YYYY'), :nome)
                """
                cur.execute(sql, cliente)
            
            con.commit()

    except Exception as error:
        print("Ocorreu um erro ao realizar seu cadastro.")
        raise error

#função que trará uma tupla referente a uma linha da tabela t_vs_usuario, ulizando
# o login de usuario e senha criada por ele proprio a "lg_usuario" e "sh_usuario"

def find_one_by_SENHA(senha,login):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_vs_usuario WHERE sh_usuario = :senha and lg_usuario= :login'
                cur.execute(sql, { 'senha': senha, 'login': login })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro na consulta ao seu cadastro")
        raise error


#função que trará uma tupla referente a uma linha da tabela t_rs_usuario, ulizando
# o id de usuario que será correspondente a "id_usuario"
def find_one_by_id(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_ts_usuario WHERE id_usuario = :id'
                cur.execute(sql, { 'id': id  })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro na consulta ao seu cadastro")
        raise error



#função responsavel por alterar informações na tabela t_vs_usuario
#ela recebera o id correspondente a id_usuario e um dicionario com novas informações 
#que substituiram as informações correspondentes a mesma linha da informação id_usuario
def update(cliente, id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
                                         
            with con.cursor() as cur:
                sql = """UPDATE t_vs_usuario SET no_usuario=:nome, nr_cpf=:cpf,nm_rg=:rg, lg_usuario=:login, sh_usuario=:senha, dt_nascimento=:nascimento, fl_sexo_biologico=:sexo, ds_estado_civil=:estadoCivil, nm_grupo_sanguineo=:sangue,dt_cadastro=:data, nm_usuario=:nome WHERE id_usuario = :id"""
                cur.execute(sql, { **cliente, 'id': id })
            
            con.commit()

    except Exception as erro:
        print("Ocorreu um erro ao atualizar seu cadastro.")
        raise erro

#função responsavel por deletar uma linha da tabela t_vs_usuario correspondente ao 
#ao login de usuario e senha criada por ele proprio, "lg_usuario" e "sh_usuario"

def delete(senha,login):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM t_vs_usuario WHERE sh_usuario = :senha and lg_usuario= :login'
                cur.execute(sql, { 'senha': senha, 'login':login })
                affected_rows = cur.rowcount
            con.commit()
            return  affected_rows

    except Exception as erro:
        print("Ocorreu um erro ao deletar seu cadastro.")
        raise erro



