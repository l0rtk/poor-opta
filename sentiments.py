import re
import nltk
from nltk.corpus import wordnet

def dummy_sentiment(text,pos,neg):
    punc_free = re.sub(r'[^\w\s]', ' ', text.lower())
    pos_low = [w.lower() for w in pos]
    neg_low = [w.lower() for w in neg]
    splitted = punc_free.split()
    negatives, positives = [],[]
    
    for word in splitted:
        if word in pos_low:
            positives.append(word)
        elif word in neg_low:
            negatives.append(word)
    return { 'positives' : positives,'pos_count' : len(positives), 'negatives' : negatives, 'neg_count' : len(negatives) }


def get_antonyms(word):
    antonyms = []
    for syn in wordnet.synsets("good"):
        for l in syn.lemmas():
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return antonyms

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets("good"):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms