import unittest
from app import app

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def teste_rota_raiz(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "API de Pokémon funcionando corretamente!"})

    def teste_listar_pokemon(self):
        response = self.client.get("/pokemon")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "pokemon": [
                {"nome": "Bulbasaur", "tipo": "Planta/Veneno", "geracao": 1},
                {"nome": "Charmander", "tipo": "Fogo", "geracao": 1},
                {"nome": "Squirtle", "tipo": "Água", "geracao": 1}
            ]
        })

    def teste_rota_login_POST(self):
        response = self.client.post("/login")
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json)

    def teste_rota_login_GET_deve_falhar(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 405)
    def teste_acesso_area_segura_sem_token(self):
        response = self.client.get("/centro-pokemon")
        self.assertEqual(response.status_code, 401)

    def teste_acesso_area_segura_com_token(self):
        login_response = self.client.post("/login")
        token = login_response.json['token']
        headers = {
            "Authorization": f'Bearer {token}'
        }
        response = self.client.get("/centro-pokemon", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "message": "Bem-vindo ao Centro Pokémon! Apenas treinadores autenticados podem acessar."
        })

if __name__ == "__main__":
    unittest.main()