# Real Image Detection Web App using Flask and Deep Learning

This project is a web application built with Flask and a deep learning model to distinguish between real images (captured by cameras) and fake images (generated using GANs). Users can upload an image, and the app will predict whether the image is real or fake, displaying the result along with a preview of the uploaded image.

---

## Features

- **User-Friendly Interface**: Simple upload form for users to upload an image.
- **Deep Learning Prediction**: Uses a pre-trained Convolutional Neural Network (CNN) to classify images as "Real" or "Fake."
- **Image Preview**: Displays the uploaded image along with the prediction result.
- **Responsive Design**: The web app works well on desktop and mobile browsers.
- **Secure File Handling**: Temporarily stores the uploaded image and deletes it after prediction.

---

## Project Structure

```
project-folder/
├── app.py                 # Main Flask application
├── fake_vs_real_cnn_model.h5  # Trained deep learning model
├── requirements.txt       # Python dependencies
├── Procfile               # Heroku configuration file
├── uploads/               # Temporary folder for uploaded files
├── templates/             # HTML templates
│   ├── upload.html        # Upload page
│   ├── result.html        # Result page
└── README.md              # Project documentation
```

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/fake-vs-real-image-detection.git
   cd fake-vs-real-image-detection
   ```

2. **Install Dependencies**
   Make sure you have Python 3.8+ installed. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Access the Web App**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## Usage

1. Open the web application in your browser.
2. Upload an image (supported formats: JPG, JPEG, PNG).
3. The app will display whether the image is **Real** or **Fake**, along with a preview of the uploaded image.

---

## Deployment

This project can be deployed on platforms like **Heroku**, **Render**, or **PythonAnywhere**. Here's an example for deploying on Heroku:

1. Install the Heroku CLI.
2. Login to Heroku:
   ```bash
   heroku login
   ```
3. Create a new Heroku app:
   ```bash
   heroku create
   ```
4. Deploy the project:
   ```bash
   git push heroku main
   ```
5. Open your app:
   ```bash
   heroku open
   ```

---

## Model Information

- The deep learning model (`fake_vs_real_cnn_model.h5`) is a Convolutional Neural Network (CNN) trained on a dataset of 1709 images to classify images as:
  - **Real**: Captured by a camera.
  - **Fake**: Generated using Generative Adversarial Networks (GANs).

---

## Technologies Used

- **Backend**: Flask (Python)
- **Deep Learning Framework**: TensorFlow/Keras
- **Frontend**: HTML, CSS
- **Model Training**: Custom CNN trained on labeled images
- **Deployment**: Compatible with Heroku, Render, AWS, and PythonAnywhere

---

## Screenshots

### Upload Page
![Upload Page](https://ibb.co/S4Wf6LQF)

### Result Page
![Result Page](https://ibb.co/3Ym8mL57)

---

## Future Enhancements

- Add support for multiple image uploads.
- Implement drag-and-drop functionality.
- Enhance the UI with modern design frameworks (e.g., Bootstrap).
- Add a feature to show the confidence score of predictions.

---

## Acknowledgments

- Dataset used for training: A custom dataset of real and fake images.
- Inspiration: The rise of AI-generated images and the need to detect fake media.

---

## Author

- **Abhishek Satpathy (Voodoo Coder)** - [Abhishek Satpathy](https://github.com/codersattu)

