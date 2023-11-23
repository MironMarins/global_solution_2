import oracledb

user='rm98959'
password='071100'
dsn='oracle.fiap.com.br/orcl'

def create(book):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = """
                INSERT INTO livros (titulo, autor, sinopse, lancamento, editora)
                VALUES (:titulo, :autor, :sinopse, TO_DATE(:lancamento, 'DD-MM-YYYY'), :editora)
                """
                cur.execute(sql, book)
            
            con.commit()

    except Exception as error:
        print("Ocorreu um erro ao cadastrar o livro.")
        raise error

def find_all():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM livros'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro ao consultar os livros")
        raise error


def find_one_by_id(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM livros WHERE id = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao consultar os livros")
        raise error

def update(book, id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = """UPDATE livros SET titulo=:titulo, autor=:autor, sinopse=:sinopse, lancamento=TO_DATE(:lancamento, 'DD-MM-YYYY'), editora=:editora WHERE id = :id"""
                cur.execute(sql, { **book, 'id': id })
            
            con.commit()

    except Exception as erro:
        print("Ocorreu um erro ao atualizar o livro.")
        raise erro

def delete(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM livros WHERE id = :id'
                cur.execute(sql, { 'id': id })
                affected_rows = cur.rowcount
            con.commit()
            return  affected_rows

    except Exception as erro:
        print("Ocorreu um erro ao deletar o livro.")
        raise erro