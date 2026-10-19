from flask import Flask
from flasgger import Swagger


def create_app() -> Flask:
    app = Flask(__name__)
    swagger = Swagger(app)

    @app.get("/health")
    def health_check():

           ''' Endpoint de prueba
      responses:
        200:
          description: Respuesta exitosa
          examples:
            application/json:
              mensaje: Hola desde Flask'''
    return {"status": "200 ok"}



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
