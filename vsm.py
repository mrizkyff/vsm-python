from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import math
import os
import sys


# KOLEKSI SELURUH TERM, tidak ada term yang sama
def collection_term(term_list):
    term_collective = []
    for x in range(len(term_list)):
        for term in term_list[x]:
            term_collective.append(term)
    return term_collective



# CASE FOLDING MENJADI LOWERCASE
def case_folding(dokumen):
    dokumen = [doc.lower() for doc in dokumen]
    return dokumen


# PROSES TOKENISASI MENJADI TERM
def tokenisasi(dokumen):
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    term_list = []
    for i in range(len(dokumen)):
        term_list.append(tokenizer.tokenize(dokumen[i]))
    return term_list


# HAPUS STOPWORD
def hapus_stop_words(token_list):
    stopwordslist = (sorted(stopwords.words('indonesian')))
    clean_term_list = []
    for i in range(len(token_list)):
        temp_list = []
        temp_list = [x for x in token_list[i] if x not in stopwordslist]
        clean_term_list.append(temp_list)
    return clean_term_list


# STEMING MENJADI KATA BAKU
def stemming(token_list):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    base_clean_term_list = []
    for i in range(len(token_list)):
        temp_list = []
        temp_list = [stemmer.stem(x) for x in token_list[i] ]
        base_clean_term_list.append(temp_list)
    return base_clean_term_list


# def frekuensi_doc(token_list):
#     dict_doc = []
#     for term in token_list:
#         dict_doc.append()


# MEMBUAT VECTOR DOKUMEN
def vectorizer(base_clean_term_list):
    vector = []
    for i in range(len(base_clean_term_list)):
        temp_dict = {}
        temp_dict = {x:base_clean_term_list[i].count(x) for x in base_clean_term_list[i] }
        vector.append(temp_dict)
    return vector



# MENGHITUNG DOKUMEN FREKUENSI SETIAP TERM (DF)
def dokumen_frekuensi(koleksi_term):
    df = []
    temp = list(dict.fromkeys(koleksi_term))
    for counter in temp:
        df.append({counter:koleksi_term.count(counter)})
    return df


# MENGHITUNG INVERS DOKUMEN FREKUENSI (IDF)
def invers_dokumen_frekuensi(term_list):
    idf = []
    z = dokumen_frekuensi(collection_term(term_list))
    for x in z:
        for a in x:
            idf.append({a:math.log10((len(term_list)/x.get(a)))})
    return idf


# FUNGSI MAIN
def main():
    # DOKUMEN KORPUS
    dokumen_list = []
    dokumen_list.append('NASI organik terasa lebih lezat dari anorganik')
    dokumen_list.append('nasi goreng biasa disajikan dengan telur')
    dokumen_list.append('telur ayam kampung lebih sehat dari negeri')
    dokumen_list.append('nasi goreng lezat dan sehat')

    # print(jumlah_dokumen(dokumen_list))
    # print(case_folding(dokumen_list))
    # tot_dokumen = len(dokumen_list);
    token_list = tokenisasi(case_folding(dokumen_list))
    clean_term = hapus_stop_words(token_list)
    print(clean_term)
    kata_baku = stemming(clean_term)
    print(kata_baku)
    print('================== term ==============\n',collection_term(kata_baku))
    print('================== df ==============\n',dokumen_frekuensi(collection_term(kata_baku)))
    print('================== idf ==============\n',invers_dokumen_frekuensi(kata_baku))
    # print('---------- vector ----------')
    # vektor = vectorizer(kata_baku) 
    # for x in vektor:
    #     print(x)

if __name__ == "__main__":
    main()


