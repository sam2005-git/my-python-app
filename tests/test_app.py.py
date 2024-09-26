from app import app
def test_hello_world():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b'Hello Jenkins'
