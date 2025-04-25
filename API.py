import numpy as np
from tensorflow import keras
from Feature_Extractor import extract_features

# Return probability that URL is fake or not
def get_prediction(url, model_path):
    print("Loading the model...")
    model = keras.models.load_model(model_path)

    print("Extracting features from url...")
    url_features = extract_features(url)

    # ✅ Convert to NumPy array with proper shape and type
    url_features = np.array([url_features], dtype=np.float32)
    
    print("Making prediction...")
    prediction = model.predict(url_features)

    i = prediction[0][0] * 100
    i = round(i, 3)
    print(f"There is {i}% chance the URL is malicious!")

    return i
