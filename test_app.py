import pytest
from app import app

@pytest.fixture # Prepara el servidor que se utilizará para los tests
def client():
    with app.test_client() as client:
        yield client

# Verifica que existen los archivos app.py, script.js, index.html y style.css
def test_static_files():
    assert open('app.py').read()
    assert open('js/script.js').read()
    assert open('static/style.css').read() 
    assert open('templates/index.html').read()

def test_index_route(client):
    # Prueba la ruta principal (/) para asegurar que carga correctamente.
    response = client.get('/')
    assert response.status_code == 200

def test_predict_endpoint(client):
    # Simula una solicitud POST con un set vacío de imágenes
    response = client.post('/predict', data={'images': []})
    assert response.status_code == 400
    assert b'error' in response.data or b'predicted_class' in response.data

def test_invalid_request(client):
    # Simula una solicitud POST sin imágenes
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b'error' in response.data
