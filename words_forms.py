import pandas as pd

df = pd.read_csv('words.csv')
words = {}
# Only for words that have adjective,comparative and superlative forms
for index in range(len(df['Adjective'])):
    words[df["Adjective"][index]] = [ df["Adjective"][index], df["Comparative"][index], df["Superlative"][index] ]
    words[df["Comparative"][index]] = [ df["Adjective"][index],df["Comparative"][index], df["Superlative"][index]]
    words[df["Superlative"][index]] = [ df["Adjective"][index],df["Comparative"][index], df["Superlative"][index]]
