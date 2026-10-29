import nltk
from pathlib import Path

# Create an NLTK data folder inside the project
nltk_data_path = Path(__file__).resolve().parent / "nltk_data"
nltk_data_path.mkdir(parents=True, exist_ok=True)

# Download the English stopwords dataset
# Required by preprocess.py during SMS prediction
nltk.download(
    "stopwords", 
    download_dir="/opt/render/nltk_data",
    raise_on_error=True
)

# Verify that the downloaded stopwords can be loaded
nltk.data.path.insert(0, str(nltk_data_path))

from nltk.corpus import stopwords

print("Stopwords available:", len(stopwords.words("english")))

#print("NLTK stopwords downloaded successfully!")



#What does this file do?
#- Imports the NLTK library.
#- Downloads the stopwords dataset.
#- Reports success after the download.
#- Raises an error if the download fails, so deployment doesn't silently continue with missing data.
#Later, we'll configure our cloud deployment process to run this script before starting FastAPI.
#We don't need to run the script locally because our stopwords are already installed.