from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.joblib')

def predict_authenticity(text):
    """
    Predicts the authenticity of a given text.
    Returns a tuple of (prediction, score).
    """
    prediction = model.predict([text])[0]
    probabilities = model.predict_proba([text])[0]
    
    # Get the index of the predicted class
    class_index = np.where(model.classes_ == prediction)[0][0]
    
    # Get the probability of the predicted class
    score = probabilities[class_index] * 100
    
    return prediction, int(score)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Raise an exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text from all paragraph tags
        paragraphs = soup.find_all('p')
        article_text = ' '.join([p.get_text() for p in paragraphs])

        if not article_text:
            return render_template('index.html', error="Could not extract text from the URL.")

        prediction, score = predict_authenticity(article_text)
        
        return render_template('result.html', prediction=prediction.capitalize(), score=score, url=url)

    except requests.exceptions.RequestException as e:
        return render_template('index.html', error=f"Error fetching URL: {e}")

if __name__ == '__main__':
    app.run(debug=True)
