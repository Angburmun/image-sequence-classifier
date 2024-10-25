from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Cargar el modelo entrenado
model = load_model('models/LSTM.keras')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    files = request.files.getlist("images")
    
    if len(files) != 24:
        return jsonify({'error': 'Please upload exactly 24 images.'}), 400
    
    images = []
    for file in files:
        img = Image.open(file).resize((64, 64)).convert('L')
        img_array = np.array(img) / 255.0
        images.append(img_array)
    
    input_data = np.array(images).reshape(1, 24, 64, 64, 1)
    predictions = model.predict(input_data)
    predicted_class = np.argmax(predictions, axis=1)
    
    return jsonify({'predicted_class': int(predicted_class[0])})

if __name__ == '__main__':
    app.run(debug=True)
