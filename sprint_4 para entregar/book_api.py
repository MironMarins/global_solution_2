from flask import Flask, request
import book_resource
import traceback

app = Flask(__name__)

@app.route("/books", methods=['POST'])
def create():
    book = request.json
    try:
        book_resource.create(book)
        return book, 201
    except Exception:
        traceback.print_exc()
        info = {
            "errorCode": 202301,
            "message": "Ocorreu um erro ao cadastrar o livro"
        }
        return info, 400

@app.route("/books", methods=['GET'])
def find_all():
    try:
        resp = book_resource.find_all()
        books = []

        for row in resp:
            book = {
                "id": row[0],
                "titulo": row[1],
                "autor": row[2],
                "sinopse": row[3],
                "lancamento": row[4],
                "editora": row[5]
            }

            books.append(book) 

        return books, 200
    except Exception:
        traceback.print_exc()
        info = {
            "errorCode": 202302,
            "message": "Ocorreu um erro ao listar os livro"
        }
        return info, 400

@app.route("/books/<int:id>", methods=['GET'])
def find_one_by_id(id):
    try:
        resp = book_resource.find_one_by_id(id)
        
        if resp == None: 
            return {
                "errorCode": 202303,
                "message": "Livro não encontrado"
            }, 404

        book = {
                "id": resp[0],
                "titulo": resp[1],
                "autor": resp[2],
                "sinopse": resp[3],
                "lancamento": resp[4],
                "editora": resp[5]
            }
        
        return book, 200
        
    except Exception:
        traceback.print_exc()
        info = {
            "errorCode": 202303,
            "message": "Ocorreu um erro ao buscar livro"
        }
        return info, 400

@app.route("/books/<int:id>", methods=['PUT'])
def update(id):
    new_book_payload = request.json
    try:
        book_resource.update(new_book_payload, id)
        return new_book_payload, 200
    except Exception:
        traceback.print_exc()
        info = {
            "errorCode": 202304,
            "message": "Ocorreu um erro ao atualizar o livro"
        }
        return info, 400

@app.route("/books/<int:id>", methods=['DELETE'])
def delete(id):
    try:
        resp = book_resource.delete(id)
        print(resp)
        if resp == 0: 
            return  {
                "errorCode": 202305,
                "message": "Livro não encontrado"
            }, 404

        return '', 204
    except Exception:
        traceback.print_exc()
        info = {
            "errorCode": 202305,
            "message": "Ocorreu um erro ao deletar o livro"
        }
        return info, 400

app.run(debug=True)