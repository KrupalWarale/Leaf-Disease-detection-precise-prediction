import os
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from transformers import pipeline
from PIL import Image
import torch

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize the model
pipe = pipeline("image-classification", 
                model="linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Process the image and get prediction
        try:
            image = Image.open(filepath)
            predictions = pipe(image)
            
            # Format all predictions
            formatted_predictions = [
                {
                    'disease': pred['label'],
                    'confidence': f"{pred['score']*100:.2f}%",
                    'score': pred['score']  # Keep raw score for graph
                }
                for pred in predictions
            ]
            
            return jsonify({
                'success': True,
                'predictions': formatted_predictions,
                'top_prediction': formatted_predictions[0],
                'image_path': f'/static/uploads/{filename}'
            })
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True) 