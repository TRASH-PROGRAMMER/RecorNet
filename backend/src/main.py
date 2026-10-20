import os

from flasgger import Swagger
from flask import Flask


def create_app() -> Flask:
    """Create and configure the RecorNet Flask application."""
    app = Flask(__name__)
    Swagger(app)

    @app.get("/health")
    def health_check():
        """Endpoint de prueba
        ---
        responses:
          200:
            description: Respuesta exitosa
            examples:
              application/json:
                status: 200 ok
        """
        return {"status": "200 ok"}

    return app


if __name__ == "__main__":
    create_app().run(debug=os.getenv("FLASK_DEBUG", "0") == "1")
