import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib

def train_model():
    # Load the preprocessed data
    train_df = pd.read_csv('train.csv')
    val_df = pd.read_csv('val.csv')

    # Separate features and labels
    X_train = train_df['statement']
    y_train = train_df['label']
    X_val = val_df['statement']
    y_val = val_df['label']

    # Create a pipeline with a TfidfVectorizer and a LogisticRegression classifier
    pipeline = make_pipeline(
        TfidfVectorizer(stop_words='english'),
        LogisticRegression(max_iter=1000)
    )

    # Train the model
    pipeline.fit(X_train, y_train)

    # Evaluate the model
    accuracy = pipeline.score(X_val, y_val)
    print(f'Validation Accuracy: {accuracy}')

    # Save the trained model
    joblib.dump(pipeline, 'model.joblib')

if __name__ == '__main__':
    train_model()
