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

    #pos and negs antonyms
    pos_ants = [ant.lower() for word in pos for ant in get_antonyms(word)]
    neg_ants = [ant.lower() for word in neg for ant in get_antonyms(word)]
        
    # word forms e.g good - better best
    pos_forms = [form.lower() for word in pos for form in get_word_forms(word)]
    neg_forms = [form.lower() for word in neg for form in get_word_forms(word)]
    
    splitted = punc_free.split()
    
    # caught keywords from pos and negs
    caught_positives, caught_negatives = [],[]
    
    # caught synonyms and antonyms of pos and neg
    positive_synonyms,negative_synonyms = [],[]
    positive_antonyms,negative_antonyms = [],[]
    
    # caught forms of pos and neg
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
        
        # checking antonyms
        elif word in pos_ants and word not in positive_antonyms:
            positive_antonyms.append(word)
        elif word in neg_ants and word not in negative_antonyms:
            negative_antonyms.append(word)
        
        #checking forms
        elif word in pos_forms and word not in positive_forms:
            positive_forms.append(word)
        elif word in neg_forms and word not in negative_forms:
            negative_forms.append(word)
            
    # combining all positives and all negatives together
    all_positives = list(set(caught_positives + positive_synonyms + positive_forms + negative_antonyms))
    all_negatives = list(set(caught_negatives + negative_synonyms + negative_forms + positive_antonyms))
    
    return {'caught_positives': caught_positives,
            'caught_negatives': caught_negatives,
            'positive_synonyms': positive_synonyms,
            'negative_synonyms': negative_synonyms,
            'positive_forms': positive_forms,
            'negative_forms': negative_forms,
            'all_positives': all_positives,
            'all_negatives': all_negatives}