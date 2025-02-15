import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('punkt')
nltk.download("stopwords")

class TextToNum:
    def __init__(self, text):
        self.text = text  # Original text
        self.tokens = []  # Tokenized words
        self.cleaned_text = []  # Final processed words

    def cleaner(self):
        """Removes special characters and converts text to lowercase."""
        self.text = "".join(char.lower() if char.isalnum() or char.isspace() else " " for char in self.text)

    def token(self):
        """Tokenizes the text into words."""
        self.tokens = word_tokenize(self.text)

    def removeStop(self):
        """Removes stopwords from the tokens."""
        stop_words = set(stopwords.words("english"))
        self.cleaned_text = [word for word in self.tokens if word not in stop_words]

    def stemme(self):
        """Applies stemming to the cleaned text."""
        ps = PorterStemmer()
        self.cleaned_text = [ps.stem(word) for word in self.cleaned_text]

    def get_processed_text(self):
        """Returns the final cleaned and stemmed text."""
        return self.cleaned_text
