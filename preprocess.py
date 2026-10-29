import string
import re
import nltk
from nltk.corpus import stopwords

# Download the English stopword list if it is not already installed
#nltk.download("stopwords", quiet=True)

# Create a set of English stopwords
stop_words = set(stopwords.words("english"))


# Define a function to clean an SMS message
def preprocess_message(text):

    # Convert the message to lowercase
    text = text.lower()

    # Remove punctuation characters
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Remove English stopwords
    text = " ".join(
        word for word in text.split()
        if word not in stop_words
    )

    # Replace repeated whitespace with a single space
    text = re.sub(r"\s+", " ", text)

    # Remove leading and trailing whitespace
    text = text.strip()

    # Return the cleaned message
    return text

#TESTING CODE
# Create a sample SMS message
#message = "Congratulations! You WON a FREE prize!!!"

# Clean the SMS message
#cleaned_message = preprocess_message(message)

# Display the cleaned message
#print("Original:", message)
#print("Cleaned:", cleaned_message)