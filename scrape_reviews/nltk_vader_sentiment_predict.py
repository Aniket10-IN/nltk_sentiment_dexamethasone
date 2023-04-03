import pandas as pd
import string
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


df = pd.read_csv('comments.csv')
print(df.shape)

# Remove punctuation
def remove_punct(text):
    return ("".join([i for i in text if i not in string.punctuation]))

df['remove_punc'] = df['comments'].apply(lambda x: remove_punct(x))

# lowering text and converting dtype to string from object
df['remove_punc'] = df['remove_punc'].astype(str)
df['remove_punc'] = df['remove_punc'].apply(lambda x: x.lower())


#word tokenization
df['remove_punc'] = df['remove_punc'].apply(lambda x: nltk.word_tokenize(x))


# removing stopwords
stopwords = nltk.corpus.stopwords.words('english')
def remove_stopwords(text):
    return([i for i in text if i not in stopwords])

df['remove_punc'] = df['remove_punc'].apply(lambda x: remove_stopwords(x))

# stemming
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

def stemming(text):
    stem_text = [porter_stemmer.stem(word) for word in text]
    return stem_text

df['clean_comm'] = df['remove_punc'].apply(lambda x: stemming(x))

#converting list to string 
df['text_string'] = df['clean_comm'].apply(lambda x: ' '.join([item for item in x]))

df = df.drop(columns = ['comments', 'remove_punc', 'clean_comm'], axis = 1)

#applying nltk sentiment analyzer
analyzer = SentimentIntensityAnalyzer()
def sentiment_analyzer(text):
    return (analyzer.polarity_scores(text)['compound'])
    
df['polarity'] = df['text_string'].apply(lambda x: sentiment_analyzer(x))

# adding a new column with labels of positve, negative and neutral sentiments
def categorise_sentiment(sentiment, neg_threshold=-0.05, pos_threshold=0.05):
    """ categorise the sentiment value as positive (1), negative (-1) 
        or neutral (0) based on given thresholds """
    if sentiment < neg_threshold:
        label = 'negative'
    elif sentiment > pos_threshold:
        label = 'positive'
    else:
        label = 'neutral'
    return label


df['polarity_roundup'] = df['polarity'].apply(lambda x: categorise_sentiment(x))

print(df['polarity_roundup'].value_counts())