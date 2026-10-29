# Import the saved vectorizer and trained model
from model import tfidf, model

# Import our SMS preprocessing function
from preprocess import preprocess_message


# Define a function to predict whether an SMS is Ham or Spam
def predict_sms(message):

    # Step 1: Preprocess the incoming SMS
    cleaned_message = preprocess_message(message)

    # Step 2: Convert the cleaned SMS into TF-IDF features
    message_tfidf = tfidf.transform([cleaned_message])

    # Step 3: Predict whether the SMS is Ham or Spam
    prediction = model.predict(message_tfidf)[0]

    # Step 4: Get the probability associated with the Spam class
    spam_index = list(model.classes_).index("spam")
    spam_probability = model.predict_proba(message_tfidf)[0][spam_index]

    # Step 5: Return the prediction and probability
    return prediction, spam_probability


#TESTING
# Test the prediction function with a sample SMS
#message = "Congratulations! You WON a FREE prize!!!"

# Get the prediction and Spam probability
#prediction, probability = predict_sms(message)

# Display the results
#print("Prediction:", prediction)
#print("Spam Probability:", round(probability * 100, 2), "%")