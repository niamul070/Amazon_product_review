import pandas as pd
import gzip
import nltk
import nltk.data
import string
from nltk.corpus import stopwords
import re, csv, yaml, enchant
from nltk.corpus import wordnet
from nltk.metrics import edit_distance
from nltk.tokenize import WordPunctTokenizer
import numpy as np

replacement_patterns = [
	(r'won\'t', 'will not'),
	(r'can\'t', 'cannot'),
	(r'i\'m', 'i am'),
	(r'ain\'t', 'is not'),
	(r'(\w+)\'ll', '\g<1> will'),
	(r'(\w+)n\'t', '\g<1> not'),
	(r'(\w+)\'ve', '\g<1> have'),
	(r'(\w+)\'s', '\g<1> is'),
	(r'(\w+)\'re', '\g<1> are'),
	(r'(\w+)\'d', '\g<1> would'),
]

def replace(text):
    s=text
    for (pattern,repl) in patterns:
        s=re.sub(pattern,repl,s)
    return

def parse(path):
    g=gzip.open(path,'rb')
    for l in g:
        yield eval(l)
        
def getDF(path):
    i=0
    df={}
    for d in parse(path):
        df[i]=d
        i+=1
    return pd.DataFrame.from_dict(df,orient='index')
df=getDF('reviews_Musical_Instruments_5.json.gz')
df.columns
i=0
word_punct_tokenizer=WordPunctTokenizer()
punct = list(string.punctuation)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']

filt3=[]
uniq=[]
i=0
for index,rows in df.iterrows():
    reviews=rows['reviewText']
    reviews=reviews.lower()
    tokens=nltk.word_tokenize(reviews)
    tokens2=word_punct_tokenizer.tokenize(reviews)
    filter=[word for word in tokens2 if word not in stopwords.words('english')]
    post=nltk.pos_tag(filter)
    filt2=[x[0] for x in post if x[1] in ('NN','JJ','RB')]
    for items in filt2:
        filt3.append(items)
    #print(reviews)
    #print('\n')
    i+=1
    if(i>10261):
        i=0
        break
    

for m in filt3:
    if m not in uniq:
        uniq.append(m)
        

freq_dist=nltk.FreqDist(w.lower() for w in filt3)
list(freq_dist.keys())[:100]


def features(top_words):    
    features = {}
    word_set = set(all_words)
    for w in top_words:
        features["w_%s" % w] = (w in word_set)
    return features

featuresets=[]
all_words=filt3


for index,rows in df.iterrows():
    reviews=rows['reviewText']
    reviews=reviews.lower()
    tokens=word_punct_tokenizer.tokenize(reviews)
    feats=features(top_words)
    rating=rows['overall']
    tup=(feats,rating)
    featuresets.append(tup)
    
feats2=np.zeros(shape=(df.shape[0],len(uniq)))
for inx,rows in df.iterrows():
    reviews=rows['reviewText']
    reviews=reviews.lower()
    tokens=word_punct_tokenizer.tokenize(reviews)
    ratings=rows['overall']
    for tks in tokens:
        if(tks in uniq):
            col=uniq.index(tks)
            feats2[inx,col]=1           
