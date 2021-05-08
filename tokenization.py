
"""Task 1. The results must be listed by applying at least 2 different tokenizers and
2 different lemmatizers representing the Tokenization and Lemmatization processes."""

#Tokenizer1
import nltk
data = "General relativity also known as the general theory of relativity ,  \
       is the geometric theory of gravitation published by Albert Einstein in 1915  \
       and is the current description of gravitation in modern physics . "

chars = [',', '.', '’']
for i in chars:
    data = data.replace(i, '')


tokens = nltk.word_tokenize(data)
print(tokens)


#Tokenizer2
from nltk.tokenize import MWETokenizer
mwe_tokens = MWETokenizer([('General', 'relativity'), ('general', 'theory', 'of', 'relativity'),
                           ('geometric', 'theory'), ('Albert', 'Einstein'), ('modern', 'physics')])
tokens2 = mwe_tokens.tokenize(data.split())
print(tokens2)

