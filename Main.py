# import numpy as np
# from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS
# from API import get_prediction
# from tensorflow.keras.models import load_model

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# # Load the model
# model_path = "model/Prediction_model.h5"
# model = load_model(model_path)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/prediction', methods=['POST'])
# def prediction():
#     url = request.json.get('inputUrl')  # Accept JSON payload
    
#     # Get the prediction
#     prediction = get_prediction(url, model_path)
    
#     # Return prediction as a JSON response
#     return jsonify({'prediction': f"You are {100 - prediction}% Safe."})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)  # Changed port to 5000


# ---- old code ----
# removing on 25-04-2025 abhay
import numpy as np
from flask import Flask, request, jsonify, render_template
from API import get_prediction

app = Flask(__name__)


from tensorflow.keras.models import load_model

# Load the model
model_path = "model/Prediction_model.h5"
model = load_model(model_path)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    global model_path
    # Get the URL from the form data
    url = request.form['inputUrl']
    
    # Get the prediction
    prediction = get_prediction(url, model_path)
    
    # Return the prediction as a JSON response
    #return jsonify({'prediction': prediction})
    return render_template('home.html', Result=f"You are {100-prediction}% Safe.")
    # return render_template('home.html', Result=f"There is {prediction}% chance that domain is m")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=33,debug=True)
