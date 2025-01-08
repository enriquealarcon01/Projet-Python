import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Get the list of stopwords (english)
stop_words = set(stopwords.words('english'))

# Add spanish stopwords
stop_words.update(set(stopwords.words('spanish')))

# Add french stopwords
stop_words.update(set(stopwords.words('french')))

# Add custom stopwords
custom_stopwords = {'oh', 'na', 'yeah', 'uh', 'ah', 'la', 'ooh', 'hey', 'ha', 'woah', 'ayy', 'doo', 'wo', 'ca'}
stop_words.update(custom_stopwords)

def tokenize_lyrics_with_stopwords(lyrics):
    """
    Tokenize the lyrics and remove stopwords.
    """
    # Tokenize the lyrics
    words = word_tokenize(lyrics)
    
    # Remove stopwords
    words = [word.lower() for word in words if word.isalnum()]
    
    return words

def tokenize_lyrics(lyrics):
    """
    Tokenize the lyrics and remove stopwords.
    """
    # Tokenize the lyrics
    words = word_tokenize(lyrics)
    
    # Remove stopwords
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    
    return words

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(lyrics):
    """
    Analyze the sentiment of the lyrics.
    """
    # Join the list of words into a single string
    text = " ".join(lyrics)
    
    # Analyze the sentiment
    sentiment = analyzer.polarity_scores(text)
    
    return sentiment