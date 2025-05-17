# Leaf Disease Detection

A Flask-based web application that uses a pre-trained MobileNetV2 model to detect plant diseases from leaf images. The application features a modern UI with drag-and-drop functionality for image uploads, providing farmers and plant enthusiasts with an accessible tool for rapid disease identification and management.A highly accurate modal trained over plantVillage Dataset ( a huge datset of disease and name of plants leaf as well as healty leafs )

### Description

https://github.com/user-attachments/assets/29c56ac6-736c-4a85-ac02-c5a6ba3c415c


A Flask-based web application that uses a pre-trained MobileNetV2 model to detect plant diseases from leaf images. The application features a modern UI with drag-and-drop functionality for image uploads, providing farmers and plant enthusiasts with an accessible tool for rapid disease identification and management. After testing various models, this specific MobileNetV2 implementation was selected as it demonstrated superior performance, largely due to being trained on the PlantVillage dataset - the largest and most comprehensive plant disease image collection available.

## Features

- Drag and drop image upload
- Real-time disease detection
- Modern and responsive UI
- Confidence score display
- Support for multiple image formats (PNG, JPG, JPEG)

## Setup

1. Create a virtual environment (recommended/optional):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Drag and drop a leaf image onto the upload area or click to select a file
2. Wait for the model to process the image
3. View the prediction results, including:
   - Detected disease
   - Confidence score
   - Preview of the uploaded image

## Technical Details

- Built with Flask for the backend server
- Uses the Hugging Face Transformers library for model integration
- Leverages the [MobileNetV2 1.0 224 Plant Disease Identification](https://huggingface.co/linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification) model by linkanjarad on Hugging Face
- Frontend built with Tailwind CSS for a responsive and modern UI
- Supports images up to 16MB in size
- Optimized for real-time inference with minimal latency

## Note

The first time you run the application, it will download the pre-trained model which might take a few minutes depending on your internet connection. The model can identify over 38 different types of plant diseases across various crop species including tomato, potato, corn, and more.
