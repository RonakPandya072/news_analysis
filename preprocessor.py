from newsapi import NewsApiClient
import json
import requests
import pandas as pd
import nltk

from bs4 import BeautifulSoup

from nltk.tokenize import sent_tokenize

#for text analysis
import textstat

#for text classification, polarity and sensitivity
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

#for polarity and sentiment
from textblob import TextBlob

c_name = ['South Africa','Australia','India','Canada','United States','New Zealand']
c_code=['za','au','in','ca','us','nz']
countries = {}
for i in range(len(c_name)):
  countries[c_name[i]] = c_code[i]

img_link = {"in":"https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/188px-Flag_of_India.svg.png","za":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Flag_of_South_Africa.svg/250px-Flag_of_South_Africa.svg.png",
            "au":"https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Flag_of_Australia_%28converted%29.svg/188px-Flag_of_Australia_%28converted%29.svg.png", "ca":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Canada_%28Pantone%29.svg/188px-Flag_of_Canada_%28Pantone%29.svg.png",
            "us":"https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/250px-Flag_of_the_United_States.svg.png", "nz":"https://upload.wikimedia.org/wikipedia/commons/thu…New_Zealand.svg/188px-Flag_of_New_Zealand.svg.png"}

def content(country_name):
  newsapi = NewsApiClient(api_key='35fc59cb365640dfb9370cf33f3f7556')
  url = ('https://newsapi.org/v2/top-headlines?'
         'country='+str(country_name)+'&'
         'apiKey=35fc59cb365640dfb9370cf33f3f7556'
         )
  response = requests.get(url)
  data = json.loads(response.content)
  title, author, description, url_, urlToimg, date_time, content, name = [], [], [], [], [], [], [], []
  for i in range(10):
    name.append(data['articles'][i]['source']['name'])
    title.append(data['articles'][i]['title'])
    author.append(data['articles'][i]['author'])
    description.append(data['articles'][i]['description'])
    url_.append(data['articles'][i]['url'])
    urlToimg.append(data['articles'][i]['urlToImage'])
    date_time.append(data['articles'][i]['publishedAt'])
    content.append(data['articles'][i]['content'])
  return title, author, description, url_, urlToimg, date_time, content, name


def search(query):
    newsapi = NewsApiClient(api_key='35fc59cb365640dfb9370cf33f3f7556')
    url = ('https://newsapi.org/v2/everything?'
           'q='+query+'&'
            'from=2022-05-05&to=2021-05-05&sortBy=popularity&'
            'apiKey=35fc59cb365640dfb9370cf33f3f7556'
           )
    response = requests.get(url)
    data = json.loads(response.content)
    title, author, description, url_, urlToimg, date_time, content, name = [], [], [], [], [], [], [], []
    for i in range(10):
        name.append(data['articles'][i]['source']['name'])
        title.append(data['articles'][i]['title'])
        author.append(data['articles'][i]['author'])
        description.append(data['articles'][i]['description'])
        url_.append(data['articles'][i]['url'])
        urlToimg.append(data['articles'][i]['urlToImage'])
        date_time.append(data['articles'][i]['publishedAt'])
        content.append(data['articles'][i]['content'])
    return title, author, description, url_, urlToimg, date_time, content, name

def get_data(link):
    r=requests.get(link)
    r.encoding = 'utf-8'
    html = r.text
    soup = BeautifulSoup(html,'html.parser')
    text = soup.get_text()
    clean_text = text.replace("\n", " ")
    clean_text = text.replace("/", " ")
    clean_text = ''.join([c for c in clean_text if c != "\'"])
    sentence = sent_tokenize(clean_text)
    return clean_text, sentence



#text statistics
def ease_reading(text):
    return textstat.flesch_reading_ease(text)

def grade_level(text):
    return textstat.text_standard(text, float_output=False)

def smogindex(text):
    return textstat.smog_index(text)

def ari(text):
    return textstat.automated_readability_index(text)

def reading_time(text):
    return textstat.reading_time(text, ms_per_char=14.69)

def syllable_count(text):
    return textstat.syllable_count(text)

def lexicon_count(text):
    return textstat.lexicon_count(text, removepunct=True)

def sentence_count(text):
    return textstat.sentence_count(text)

def char_count(text):
    return textstat.char_count(text, ignore_spaces=True)

def letter_count(text):
    return textstat.letter_count(text, ignore_spaces=True)

def polly_syllable_count(text):
    return textstat.polysyllabcount(text)

def monosyllable_count(text):
    textstat.monosyllabcount(text)

#Text classification
def classification(text):
    blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
    return blob.sentiment

#sentiment
def sentiment(sentence):
    textblob_sentiment = []
    for s in sentence:
        txt = TextBlob(str(s))
        a = txt.sentiment.polarity
        b = txt.sentiment.subjectivity
        textblob_sentiment.append([s, a, b])
    df_textblob = pd.DataFrame(textblob_sentiment, columns=['Sentence', 'Polarity', 'Subjectivity'])
    return df_textblob

#word frequency and word cloud
def word_frequency(text):
    tokenizer = nltk.tokenize.RegexpTokenizer('\w+')
    tokens = tokenizer.tokenize(text)
    words = []
    for word in tokens:
        words.append(word.lower())
    stopwords = nltk.corpus.stopwords.words('english')
    words_new = []
    for word in words:
        if word not in stopwords:
            words_new.append(word)
    freq_dist = nltk.FreqDist(words_new)
    return  freq_dist

#wordcloud
def word_cloud(text):
    tokenizer = nltk.tokenize.RegexpTokenizer('\w+')
    tokens = tokenizer.tokenize(text)
    words = []
    for word in tokens:
        words.append(word.lower())
    stopwords = nltk.corpus.stopwords.words('english')
    words_new = []
    for word in words:
        if word not in stopwords:
            words_new.append(word)
    return words_new




