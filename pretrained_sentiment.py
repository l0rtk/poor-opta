import numpy as np
from scipy.special import softmax
from transformers import AutoTokenizer, AutoModelForSequenceClassification,AutoConfig

MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)


def get_sentiment(text):
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    
    result = {}
    
    for i in range(scores.shape[0]):
        l = config.id2label[ranking[i]]
        s = scores[ranking[i]]
        result[l] = np.round(float(s), 4)
    if result['positive'] > result['negative'] and result['positive'] > result['neutral']:
        result['output'] = 'POS'
    elif result['negative'] > result['positive'] and result['negative'] > result['neutral']:
        result['output'] = 'NEG'
    else:
        result['output'] = 'NEU'

    return result