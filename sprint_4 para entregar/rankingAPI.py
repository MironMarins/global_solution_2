from flask import Flask, request
import ressources.ranking_resource as ranking_ressources
import traceback

app = Flask(__name__)

@app.route("/ranking", methods=['GET'])
def find_all():
    try:
        resp = ranking_ressources.find_all_ranking()
        rankigList = []

        for row in resp:
            rankingDic = {
                "posicao": row+1,
                "login_usuario": row[0],
                "Valor_doacao": row[1],
                
            }

            rankigList.append(rankingDic) 

        return rankigList, 200
    except Exception:
        traceback.print_exc()
        info = {
            "errorCode": 202302,
            "message": "Ocorreu um erro ao listar o ranking de doações"
        }
        return info, 400


app.run(debug=True)