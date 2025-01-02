import logging
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

app = Flask(__name__)

# Configuración de logging
logging.basicConfig(level=logging.INFO,  # Nivel mínimo para registrar (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del log
                    handlers=[
                        logging.FileHandler("app.log"),  # Guardar logs en un archivo
                        logging.StreamHandler()          # Mostrar logs en la consola
                    ])

# Cargar el modelo entrenado
model = load_model('models/LSTM.keras')
app.logger.info("Modelo cargado.")

@app.route('/')
def index():
    app.logger.info("Ruta '/' llamada, renderizando index.html")
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    app.logger.info("Ruta '/predict' llamada, método: POST")

    # Verificar los archivos enviados
    files = request.files.getlist("images")
    if len(files) != 24:
        app.logger.warning("Cantidad incorrecta de imágenes recibidas: %d", len(files))
        return jsonify({'error': 'Please upload exactly 24 images.'}), 400
    
    images = []
    try:
        for idx, file in enumerate(files):
            app.logger.debug("Procesando imagen %d", idx + 1)
            img = Image.open(file).resize((64, 64)).convert('L')
            img_array = np.array(img) / 255.0
            images.append(img_array)
        
        # Preparar los datos para el modelo
        input_data = np.array(images).reshape(1, 24, 64, 64, 1)
        app.logger.info("Imágenes procesadas a 64x64 en blanco y negro.")
        
        # Hacer predicción
        predictions = model.predict(input_data)
        predicted_class = np.argmax(predictions, axis=1)
        app.logger.info("Predicción realizada. Clase predicha: %d", predicted_class[0])
        
        return jsonify({'predicted_class': int(predicted_class[0])})
    
    except Exception as e:
        app.logger.error("Error durante la predicción: %s", str(e), exc_info=True)
        return jsonify({'error': 'An error occurred during prediction.'}), 500

if __name__ == '__main__':
    app.logger.info("Iniciando la aplicación Flask en modo debug.")
    app.run(host='0.0.0.0', port=5000, debug=True)
