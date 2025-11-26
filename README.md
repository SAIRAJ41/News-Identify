## Fake News Detector - Application Setup Complete
# Summary
Successfully set up and launched the Fake News Detector application on localhost. The application is now running at http://127.0.0.1:5000 and ready to accept news article URLs for authenticity prediction.

# What Was Done
Dataset Acquisition
Downloaded the LIAR-PLUS dataset from GitHub
Dataset contains labeled statements for training the fake news detection model
Data Processing
Executed 
preprocess.py
 to process raw TSV files into cleaned CSV format
Generated three datasets:
train.csv - Training data
val.csv - Validation data
test.csv - Test data
Applied label mapping: consolidated original labels into three categories (fake, neutral, real)
Model Training
Trained a Logistic Regression model using TF-IDF vectorization
Validation Accuracy: 50.5%
Saved trained model as model.joblib in the project root
Application Deployment
Installed all required Python dependencies from 
requirements.txt
Started Flask development server on port 5000
Server running in debug mode at http://127.0.0.1:5000
Application Interface
The application provides a simple web interface for fake news detection:

Application Home Page
Review
Application Home Page

## Features
URL Input: Enter any news article URL for analysis
Web Scraping: Automatically extracts article content from the provided URL
Prediction: Uses the trained model to classify the article as fake, neutral, or real
Confidence Score: Displays prediction confidence percentage
Technical Details
Components Created
LIAR-PLUS/ - Dataset directory
train.csv, val.csv, test.csv - Preprocessed data files
model.joblib - Trained ML model (Logistic Regression + TF-IDF)
Technology Stack
Backend: Flask 3.1.2
ML: scikit-learn 1.7.2
Web Scraping: BeautifulSoup4, Requests
Data Processing: Pandas, NumPy
Server Status
✅ Server Running: Flask development server active on http://127.0.0.1:5000

# The application is fully functional and ready to process news article URLs for authenticity prediction.
