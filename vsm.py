from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import math
import os
import sys


def load_dokumen(dokumen):
    
    return dokumen_list


# TOTAL DOKUMEN
def jumlah_dokumen(dokumen):
    return len(dokumen)


# CASE FOLDING MENJADI LOWERCASE
def case_folding(dokumen):
    dokumen = [doc.lower() for doc in dokumen]
    return dokumen


# PROSES TOKENISASI MENJADI TERM
def tokenisasi(tot_docs,dokumen):
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    term_list = []
    for i in range(tot_docs):
        term_list.append(tokenizer.tokenize(dokumen[i]))
    return term_list


# HAPUS STOPWORD
def hapus_stop_words(tot_docs, token_list):
    stopwordslist = (sorted(stopwords.words('indonesian')))
    clean_term_list = []
    for i in range(tot_docs):
        temp_list = []
        temp_list = [x for x in token_list[i] if x not in stopwordslist]
        clean_term_list.append(temp_list)
    return clean_term_list


# STEMING MENJADI KATA BAKU
def stemming(tot_docs, token_list):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    base_clean_term_list = []
    for i in range(tot_docs):
        temp_list = []
        temp_list = [stemmer.stem(x) for x in token_list[i] ]
        base_clean_term_list.append(temp_list)
    return base_clean_term_list



def main():
    # DOKUMEN KORPUS
    dokumen_list = []
    dokumen_list.append('NASI organik rasa lebih lezat dari anorganik')
    dokumen_list.append('nasi goreng biasa disajikan dengan telur')
    dokumen_list.append('telur ayam kampung lebih sehat dari telur ayam negeri')
    dokumen_list.append('nasi goreng lezat dan sehat')

    # print(jumlah_dokumen(dokumen_list))
    # print(case_folding(dokumen_list))
    token_list = tokenisasi(jumlah_dokumen(dokumen_list),case_folding(dokumen_list))
    clean_term = hapus_stop_words(jumlah_dokumen(dokumen_list), token_list)
    print(clean_term)
    kata_baku = stemming(jumlah_dokumen(dokumen_list), clean_term)
    print(kata_baku)

if __name__ == "__main__":
    main()


