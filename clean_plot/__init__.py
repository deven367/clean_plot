__version__ = "0.0.7"
from .core import *
from .trial import *
from .functions import *
from .feature_extractor import *
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
