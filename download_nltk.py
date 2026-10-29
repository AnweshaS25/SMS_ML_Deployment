import nltk

# Download the English stopwords dataset
# Required by preprocess.py during SMS prediction
nltk.download("stopwords", raise_on_error=True)

print("NLTK stopwords downloaded successfully!")



#What does this file do?
#- Imports the NLTK library.
#- Downloads the stopwords dataset.
#- Reports success after the download.
#- Raises an error if the download fails, so deployment doesn't silently continue with missing data.
#Later, we'll configure our cloud deployment process to run this script before starting FastAPI.
#We don't need to run the script locally because our stopwords are already installed.