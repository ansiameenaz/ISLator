import re
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Basic stopword and time word lists
STOPWORDS = {
    'a', 'an', 'the', 'is','as', 'are', 'was', 'were', 'am', 'do', 'does',
    'did', 'to', 'of', 'and', 'in', 'on', 'at', 'for', 'with', 'very'
}

TIME_WORDS = {'now', 'today', 'tomorrow', 'yesterday'}

def preprocess(text):
    """
    Lowercase and remove punctuation.
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.split()

def remove_stopwords(tokens):
    """
    Remove common stopwords that are not needed for glossing.
    """
    return [word for word in tokens if word not in STOPWORDS]

def lemmatize(tokens):
    """
    Lemmatize words to their base verb form (e.g., 'drinking' → 'drink').
    """
    return [lemmatizer.lemmatize(word, pos='v') for word in tokens]

def reorder(tokens):
    """
    Move time-related words to the front of the gloss sequence.
    """
    time = [w for w in tokens if w in TIME_WORDS]
    rest = [w for w in tokens if w not in TIME_WORDS]
    return time + rest

def gloss(text):
    """
    Full glossing pipeline: preprocess, remove stopwords, lemmatize, reorder.
    Returns a list of lowercase gloss words.
    """
    tokens = preprocess(text)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize(tokens)
    tokens = reorder(tokens)
    return tokens  # lowercase for JSON and video file matching
