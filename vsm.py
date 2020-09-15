from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import math
import os
import sys

# NOTED: test baru untuk kasus setiap dokumen tidak ada term yang sama
# NOTED: misal telur ada di DOC3 2x tetap dihitung 1x


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
# idf masih menghitung kalau term setiap dokumen >1 maka dihitung banyaknya
def invers_dokumen_frekuensi(term_list):
    idf = []
    z = dokumen_frekuensi(collection_term(term_list))
    for x in z:
        for a in x:
            idf.append({a:math.log10((len(term_list)/x.get(a)))})
    return idf

# PEMBOBOTAN TERM SETIAP DOKUMEN
# mencari vektor dengan key yang sama kemudian dikali dengan df per doc
def weighting_term(vektor, term_idf):
    for x in term_idf:
        for y in x:
            for z in vektor:
                if z.get(y) and x.get(y):
                    z[y] = z.get(y) * x.get(y)

    # MENGKUADRATKAN IDF SETIAP TERM
    # update nilai vektor menjadi kuadratnya
    vektor_kuadrat = vektor
    for x in vektor_kuadrat:
        for y in x:
            x[y] = (math.pow(x.get(y),2))

    # MENJUMLAHKAN IDF DALAM SATU DOC
    jumlah_per_doc = []
    for x in vektor_kuadrat:
        jumlah_per_doc.append(sum(x.values()))

    
    # AKAR VEKTOR KUADRAT
    akar_jumlah_per_doc = []
    for x in jumlah_per_doc:
        akar_jumlah_per_doc.append(math.sqrt(x))

    # ARRAY HASIL (DICT)
    result = {
        'total_per_doc':jumlah_per_doc,
        'vektor_term':vektor,
        'vektor_kuadrat':vektor_kuadrat,
        'vektor_akar':akar_jumlah_per_doc
    }
    return result


# FUNGSI MAIN
def main():
    # DOKUMEN KORPUS
    dokumen_list = []
    dokumen_list.append('nasi goreng lezat dan sehat')
    dokumen_list.append('NASI organik enak lebih lezat dari anorganik')
    dokumen_list.append('nasi goreng biasa disajikan dengan telur')
    dokumen_list.append('telur ayam kampung lebih sehat dari negeri')

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
    print('================== idf ==============')
    term_idf = invers_dokumen_frekuensi(kata_baku)
    print(term_idf)

    print('================== weighting ==============')
    vektor = vectorizer(kata_baku)
    weight_term_perdoc = (weighting_term(vektor, term_idf))
    print(weight_term_perdoc['vektor_term'])

    print('================== vektor kuadrat ==============')
    print(weight_term_perdoc['vektor_kuadrat'])


    print('================== jumlah bobot per doc ==============')
    jumlah_bobot = weight_term_perdoc['total_per_doc']
    print(jumlah_bobot)

    print('================== akar jumlah bobot per doc ==============')
    print(weight_term_perdoc['vektor_akar'])

    # print('dump\n ', weight_term_perdoc['dump'])

    
    # for x in vektor:
    #     print(x)
    #     print(sum(x.values()))
            

    # for x in term_idf:
    #     z = 0
    #     for y in x:
    #         # print(y,x.get(y))
    #         print(z, y, term_idf[z].get(y))
    #         z = z+1
    # sys.exit()

    # for x in vektor:
    #     # print(x)
    #     z = 0
    #     for y in x:
    #         # print(y, (x.get(y) * 2))
    #         if(term_idf[z].get(y) != None):
    #             print(y,x.get(y) * term_idf[z].get(y))
    #         z += 1
    #     print('---')
if __name__ == "__main__":
    main()


