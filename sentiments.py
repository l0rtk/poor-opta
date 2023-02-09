import re
from helpers import get_synonyms,get_antonyms,get_word_forms


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


def sentiment_syns_ants_forms(text,pos,neg):
    """
        checking for synonyms,antonyms and forms of the pos and neg keywords
    """
    punc_free = re.sub(r'[^\w\s]', ' ', text.lower())
    
    positives = [w.lower() for w in pos]
    negatives = [w.lower() for w in neg]
    
    #pos and negs synonyms 
    pos_syns = [syn.lower() for word in pos for syn in get_synonyms(word)]
    neg_syns = [syn.lower() for word in neg for syn in get_synonyms(word)]

    pos_forms = [form.lower() for word in pos for form in get_word_forms(word)]
    neg_forms = [form.lower() for word in neg for form in get_word_forms(word)]
    
    splitted = punc_free.split()
    
    caught_positives, caught_negatives = [],[]
    
    positive_synonyms,negative_synonyms = [],[]
    positive_forms,negative_forms = [],[]
    
    for word in splitted:
        # checking words
        if word in positives and word not in caught_positives:
            caught_positives.append(word)
        elif word in negatives and word not in caught_negatives:
            caught_negatives.append(word)
                
        # checking synonyms
        elif word in pos_syns and word not in positive_synonyms:
            positive_synonyms.append(word)
        elif word in neg_syns and word not in negative_synonyms:
            negative_synonyms.append(word)
            
        #checking forms
        elif word in pos_forms and word not in positive_forms:
            positive_forms.append(word)
        elif word in neg_forms and word not in negative_forms:
            negative_forms.append(word)

    all_positives = list(set(caught_positives + positive_synonyms + positive_forms))
    all_negatives = list(set(caught_negatives + negative_synonyms + negative_forms))
    
    return {'caught_pos': caught_positives,
            'caught_neg': caught_negatives,
            'positive_synonyms': positive_synonyms,
            'negative_synonyms': negative_synonyms,
            'positive_forms': positive_forms,
            'negative_forms': negative_forms,
            'all_positives': all_positives,
            'all_negatives': all_negatives}