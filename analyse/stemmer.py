from nltk.stem.porter import *  # import des porter stemmers
from nltk.stem.snowball import GermanStemmer

class Stemmer:
    @staticmethod
    def get_stems(list):
        stemmer = GermanStemmer()  # erzeugen des Stemmers
        for i in range(0, len(list)):  # durchgehen der uebergebenen liste
            list[i] = stemmer.stem(list[i])  # stemmen der liste
        return list  # rueckgabe der liste

###### Ab Hier nur zum Testen
# b = ['caresses', 'flies', 'dies', 'mules', 'denied',
#    'died', 'agreed', 'owned', 'humbled', 'sized',
#   'meeting', 'stating', 'siezing', 'itemization',
#  'sensational', 'traditional', 'reference', 'colonizer',
# 'plotted', 'wäschewaschen', 'wäscheleine']
# stemer = GermanStemmer()
# for i in b:
#     a = stemer.stem(i)
#     print(a)
