from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
MODEL_PATH = "fake_vs_real_cnn_model.h5"
model = load_model(MODEL_PATH)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to preprocess and predict
def predict_image(image_path):
    IMG_SIZE = (128, 128)  # Input size for the model
    image = load_img(image_path, target_size=IMG_SIZE)
    image = img_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    prediction = model.predict(image)[0][0]
    return "Real" if prediction > 0.5 else "Fake"

@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        # Check if an image file is submitted
        if 'file' not in request.files:
            return "No file part in the request"
        file = request.files['file']
        if file.filename == '':
            return "No file selected"
        if file and allowed_file(file.filename):
            # Save the uploaded file
            filepath = os.path.join("uploads", file.filename)
            file.save(filepath)

            # Predict the image
            result = predict_image(filepath)

            # Generate URL for the uploaded image
            image_url = url_for('uploaded_file', filename=file.filename)

            # Render result.html with the result and the file path
            return render_template("result.html", result=result, image_url=image_url)
    return render_template("upload.html")

# Route to serve files from the uploads directory
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory("uploads", filename)

if __name__ == "__main__":
    app.run(debug=True)
