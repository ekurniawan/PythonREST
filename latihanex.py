def convert(i):
    try:
        x=int(i)
        print("Conversion berhasil ! x={}".format(x))
    except (ValueError,TypeError) as e:
        print("Kesalahan: {}".format(str(e)))
        x=-1
    return x

def LuasSegitiga(alas,tinggi):
    if alas<=0:
        raise ValueError("Alas tidak boleh bernilai 0")
    if tinggi<=0:
        raise ValueError("Tinggi tidak boleh bernilai 0")
    return 0.5*alas*tinggi

def Hitung(alas,tinggi):
    try:
        hasil = LuasSegitiga(alas,tinggi)
        print("Hasil: {}".format(hasil))
    except ValueError as e:
        print("Kesalahan: {}".format(str(e)))



