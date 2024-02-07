# -*- coding: utf-8 -*-
"""sentiment_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/151l1cCIIA_h0ZBssnueWqNUFVm3As99e
"""

!pip install --upgrade pip
!apt-get install -y libxml2-dev libxslt-dev
!pip install newspaper3k

!pip install nltk
import nltk
nltk.download('punkt')

from textblob import TextBlob
from newspaper import Article

url='https://en.wikipedia.org/wiki/Suicide_in_India'
article= Article(url)

article.download()
article.parse()
article.nlp()

text=article.summary
print(text)

blob=TextBlob(text)
sentiment= blob.sentiment.polarity  #-1 to 1
print(sentiment)