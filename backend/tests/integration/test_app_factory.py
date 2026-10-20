from src.main import create_app


def test_create_app_registers_health_and_swagger():
    app = create_app()
    client = app.test_client()

    health = client.get("/health")
    assert health.status_code == 200
    assert health.get_json() == {"status": "200 ok"}

    spec = client.get("/apispec_1.json")
    assert spec.status_code == 200
    assert "/health" in spec.get_json()["paths"]
