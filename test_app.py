import pytest
from app import app
from io import BytesIO
from PIL import Image
import numpy as np

BASE_URL = "http://app:5000"  # Dirección de la red Docker

@pytest.fixture
def client():
    return BASE_URL

""" Función auxiliar. 
    Genera una imagen válida para la IA (size, size, 1) en el formato format.
"""
def create_test_image(size, format='JPEG'):
    image = Image.fromarray((np.random.rand(size, size) * 255).astype('uint8'), 'L')
    byte_io = BytesIO()
    image.save(byte_io, format)  # Guardar como JPEG
    byte_io.seek(0)  # Posicionar el cursor al inicio
    return byte_io



# Verifica que existen los archivos necesarios para que funcione la aplicación
def test_static_files():
    assert open('app.py').read()
    assert open('static/script.js').read()
    assert open('static/style.css').read() 
    assert open('templates/index.html').read()

# Prepara el servidor que se utilizará para los tests
@pytest.fixture # Fixture permite que los otros tests puedan usar client
def client():
    with app.test_client() as client:
        yield client


""" Pruebas básicas. """
# Prueba la ruta principal (/) para asegurar que carga correctamente
def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200

# Solicitud POST sin imágenes
def test_no_images(client):
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b'error' in response.data

# Solicitud POST con un set vacío de imágenes
def test_empty_image_set(client):
    response = client.post('/predict', data={'images': []})
    assert response.status_code == 400
    assert b'error' in response.data



""" Solicitudes POST con archivos corruptos (binarios). """
# Un archivo corrupto
def test_corrupt_images(client):
    data = { 'images': [(BytesIO(b"lorem ipsum"), 'image1.jpg')] }
    response = client.post('/predict', data=data, content_type='multipart/form-data')
    assert response.status_code == 400
    assert b'Please upload exactly 24 images.' in response.data

# 24 archivos corruptos
def test_24_corrupt_images(client):
    data = { 'images': [(BytesIO(b"lorem ipsum"), f'image_{i}.jpg') for i in range(24)] }
    response = client.post('/predict', data=data, content_type='multipart/form-data')
    assert response.status_code == 500

# 48 archivos corruptos
def test_48_corrupt_images(client):
    data = { 'images': [(BytesIO(b"lorem ipsum"), f'image_{i}.jpg') for i in range(48)] }
    response = client.post('/predict', data=data, content_type='multipart/form-data')
    assert response.status_code == 400
    assert b'Please upload exactly 24 images.' in response.data



""" Solicitudes POST con imágenes generadas. """
# Una imagen
def test_one_image(client):
    data = {'images': [(create_test_image(64), f'image_1.jpg')]}
    response = client.post('/predict', data=data, content_type='multipart/form-data')
    assert response.status_code == 400
    assert b'Please upload exactly 24 images.' in response.data

# 24 imágenes
def test_24_images(client):
    data = {'images': [(create_test_image(64), f'image_{i}.jpg') for i in range(24)]}
    response = client.post('/predict', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert b'predicted_class' in response.data

# 48 imágenes
def test_48_images(client):
    data = {'images': [(create_test_image(64), f'image_{i}.jpg') for i in range(48)]}
    response = client.post('/predict', data=data, content_type='multipart/form-data')
    assert response.status_code == 400
    assert b'Please upload exactly 24 images.' in response.data

# 24 imágenes PNG
def test_images_PNG(client):
    data = {'images': [(create_test_image(64, 'PNG'), f'image_{i}.png') for i in range(24)]}
    response = client.post('/predict', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert b'predicted_class' in response.data



""" Solicitudes POST con imágenes demasiado grandes.
    El Backend debe reconvertirlas al tamaño deseado. 
"""
# 24 imágenes demasiado pequeñas
def test_small_images(client):
    data = {'images': [(create_test_image(16), f'image_{i}.jpg') for i in range(24)]}
    response = client.post('/predict', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert b'predicted_class' in response.data

# 24 imágenes demasiado grandes
def test_large_images(client):
    data = {'images': [(create_test_image(512), f'image_{i}.jpg') for i in range(24)]}
    response = client.post('/predict', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert b'predicted_class' in response.data