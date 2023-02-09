import nltk
from nltk.corpus import wordnet
from words_forms import words

def get_antonyms(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            if l.antonyms():
                if l.antonyms()[0].name() not in antonyms:
                    antonyms.append(l.antonyms()[0].name())
    return antonyms

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            if l.name() not in synonyms:
                synonyms.append(l.name())
    return synonyms


def get_word_forms(word):
    try:
        return words[word]
    except KeyError:
        return []