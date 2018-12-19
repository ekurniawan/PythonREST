from myhelper import HitungLuasSegitiga,HitungLuasLingkaran
from latihan2 import fetch_words

hasil = HitungLuasSegitiga(12,34)
luasLing = HitungLuasLingkaran(22)
hasil_word = fetch_words()

def main():
    print("Hasil :"+ str(hasil))
    print("Luas Lingkaran :" + str(luasLing))
    print(hasil_word)


