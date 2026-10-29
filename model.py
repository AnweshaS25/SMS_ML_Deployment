import joblib   
#import joblib — imports the library used to load saved Python objects.

# Load the saved TF-IDF vectorizer
tfidf = joblib.load("tfidf_vectorizer.pkl")
#joblib.load() — reads a saved .pkl file and reconstructs the object in memory.
#tfidf — stores the fitted TF-IDF vectorizer.

# Load the trained Balanced Logistic Regression model
model = joblib.load("balanced_logistic_regression.pkl")
#model — stores your trained Logistic Regression classifier.

# Confirm that both files were loaded successfully
print("TF-IDF vectorizer loaded successfully!")
print("ML model loaded successfully!")

