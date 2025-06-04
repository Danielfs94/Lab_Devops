from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'POKEMON_NAO_TEM_PLURAL'
jwt = JWTManager(app)

SWAGGER_URL = '/swagger'
API_DOC_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_DOC_URL)

app.register_blueprint(swaggerui_blueprint, url_prefix = SWAGGER_URL)

@app.route('/')
def index():
    return jsonify(message="API de Pokémon funcionando corretamente!")

@app.route("/pokemon", methods=["GET"])
def listar_pokemon():
    return jsonify(pokemon=[
        {"nome": "Bulbasaur", "tipo": "Planta/Veneno", "geracao": 1},
        {"nome": "Charmander", "tipo": "Fogo", "geracao": 1},
        {"nome": "Squirtle", "tipo": "Água", "geracao": 1}
    ])

@app.route("/login", methods=["POST"])
def autenticar_usuario():
    token = create_access_token(identity="treinador_exemplo")
    return jsonify(token=token)

@app.route("/centro-pokemon", methods=['GET'])
@jwt_required()
def acessar_area_segura():
    return jsonify(message="Bem-vindo ao Centro Pokémon! Apenas treinadores autenticados podem acessar.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
