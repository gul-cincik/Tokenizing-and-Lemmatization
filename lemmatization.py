import nltk
sentence = "Alan Mathison Turing was an English mathematician, " \
           "computer scientist, logician, cryptanalyst, philosopher, and theoretical biologist ." \
           "Turing was highly influential in the development of theoretical computer science, " \
           "providing a formalisation of the concepts of algorithm and computation with the Turing machine, " \
           "which can be considered a model of a general-purpose computer ."

chars = [',', '.', '’']
for i in chars:
    sentence = sentence.replace(i, '')

tokens = nltk.word_tokenize(sentence)

#Lemmatizer1
import gensim
from gensim.utils import lemmatize
gensim_lemmas = lemmatize(sentence)
print(gensim_lemmas)

#Lemmatizer2
from nltk.stem.lancaster import LancasterStemmer
word_stemmer = LancasterStemmer()

stem_list = []
for w  in tokens:
    stems = word_stemmer.stem(w)
    stem_list.append(stems)
print(stem_list)