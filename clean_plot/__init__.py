__version__ = "0.0.12"
from .utils import download_nltk_dep
try:
    from nltk.corpus import stopwords
    STOPWORDS = set(stopwords.words('english'))
except:
    print('Downloading dependencies')
    download_nltk_dep()
