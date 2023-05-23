from app import main  # noqa : F401


def test_ping(test_app):
    response = test_app.get("/api/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "environment": "dev", "testing": True}
