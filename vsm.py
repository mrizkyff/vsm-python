from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import math
import os
import sys


# TOTAL DOKUMEN
def jumlah_dokumen(dokumen):
    return len(dokumen)


# CASE FOLDING
def case_folding(dokumen):
    dokumen = [doc.lower() for doc in dokumen]
    return dokumen



# PROSES TOKENISASI
# tokenizer = RegexpTokenizer(r'[a-zA-Z]+')

def main():
    # DOKUMEN KORPUS
    dokumen_list = []
    dokumen_list.append('NASI organik rasa lebih lezat dari anorganik')
    dokumen_list.append('nasi goreng biasa disajikan dengan telur')
    dokumen_list.append('telur ayam kampung lebih sehat dari telur ayam negeri')
    dokumen_list.append('nasi goreng lezat dan sehat')

    print(jumlah_dokumen(dokumen_list))
    print(case_folding(dokumen_list))
    

if __name__ == "__main__":
    main()


