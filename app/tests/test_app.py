from app import app


def test_index_returns_version_and_pod():
    data = app.test_client().get("/").get_json()
    assert set(data) == {"version", "pod"}


def test_healthz():
    assert app.test_client().get("/healthz").status_code == 200