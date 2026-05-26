from flask import Flask, render_template, request, jsonify
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No se envió ninguna imagen'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400

    try:
        image = Image.open(file)
        text = pytesseract.image_to_string(image, lang='spa+eng')
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': f'Error al procesar la imagen: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)
