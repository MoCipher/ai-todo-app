from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class NLPService:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_text(self, text):
        tokens = word_tokenize(text.lower())
        filtered_tokens = [self.lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in self.stop_words]
        return filtered_tokens

    def extract_keywords(self, text):
        tokens = self.preprocess_text(text)
        return list(set(tokens))

    def parse_task_description(self, description):
        keywords = self.extract_keywords(description)
        return {
            'keywords': keywords,
            'original': description
        }