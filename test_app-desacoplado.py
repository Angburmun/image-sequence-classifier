import pytest
from io import BytesIO
from PIL import Image
import numpy as np
import requests

BASE_URL = "http://app:5000"  # Dirección del servicio Flask en la red Docker

""" Función auxiliar.
    Genera una imagen válida para la IA (size, size, 1) en el formato format.
"""
def create_test_image(size, format='JPEG'):
    image = Image.fromarray((np.random.rand(size, size) * 255).astype('uint8'), 'L')
    byte_io = BytesIO()
    image.save(byte_io, format)  # Guardar como JPEG
    byte_io.seek(0)  # Posicionar el cursor al inicio
    return byte_io


# Prepara la URL base que usarán los tests
@pytest.fixture
def client():
    return BASE_URL



""" Pruebas básicas. """
# Prueba la ruta principal (/) para asegurar que carga correctamente
def test_index_route(client):
    response = requests.get(f"{client}/")
    assert response.status_code == 200

# Solicitud POST sin imágenes
def test_no_images(client):
    response = requests.post(f"{client}/predict", files={})
    assert response.status_code == 400
    assert 'error' in response.json()

# Solicitud POST con un set vacío de imágenes
def test_empty_image_set(client):
    response = requests.post(f"{client}/predict", files={})
    assert response.status_code == 400



""" Solicitudes POST con archivos corruptos (binarios). """
# Un archivo corrupto
def test_corrupt_images(client):
    files = [('images', ('image1.jpg', BytesIO(b"lorem ipsum"), 'application/octet-stream'))]
    response = requests.post(f"{client}/predict", files=files)
    assert response.status_code == 400
    assert 'Please upload exactly 24 images.' in response.text

# 24 archivos corruptos
def test_24_corrupt_images(client):
    files = [('images', (f'image_{i}.jpg', BytesIO(b"lorem ipsum"), 'application/octet-stream')) for i in range(24)]
    response = requests.post(f"{client}/predict", files=files)
    assert response.status_code == 500

# 48 archivos corruptos
def test_48_corrupt_images(client):
    files = [('images', (f'image_{i}.jpg', BytesIO(b"lorem ipsum"), 'application/octet-stream')) for i in range(48)]
    response = requests.post(f"{client}/predict", files=files)
    assert response.status_code == 400
    assert 'Please upload exactly 24 images.' in response.text



""" Solicitudes POST con imágenes generadas. """
# Una imagen
def test_one_image(client):
    files = [('images', ('image_1.jpg', create_test_image(64), 'image/jpeg'))]
    response = requests.post(f"{client}/predict", files=files)
    assert response.status_code == 400

# 24 imágenes
def test_24_images(client):
    files = [('images', (f'image_{i}.jpg', create_test_image(64), 'image/jpeg')) for i in range(24)]
    response = requests.post(f"{client}/predict", files=files)
    assert response.status_code == 200
    assert 'predicted_class' in response.json()

# 48 imágenes
def test_48_images(client):
    files = [('images', (f'image_{i}.jpg', create_test_image(64), 'image/jpeg')) for i in range(48)]
    response = requests.post(f"{client}/predict", files=files)
    assert response.status_code == 400
    assert 'Please upload exactly 24 images.' in response.text

# 24 imágenes PNG
def test_images_PNG(client):
    files = [('images', (f'image_{i}.png', create_test_image(64, 'PNG'), 'image/png')) for i in range(24)]
    response = requests.post(f"{client}/predict", files=files)
    assert response.status_code == 200
    assert 'predicted_class' in response.json()



""" Solicitudes POST con imágenes de tamaños incorrectos """
# 24 imágenes demasiado pequeñas
def test_small_images(client):
    files = [('images', (f'image_{i}.jpg', create_test_image(16), 'image/jpeg')) for i in range(24)]
    response = requests.post(f"{client}/predict", files=files)
    assert response.status_code == 200
    assert 'predicted_class' in response.json()

# 24 imágenes demasiado grandes
def test_large_images(client):
    files = [('images', (f'image_{i}.jpg', create_test_image(512), 'image/jpeg')) for i in range(24)]
    response = requests.post(f"{client}/predict", files=files)
    assert response.status_code == 200
    assert 'predicted_class' in response.json()
