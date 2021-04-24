import pandas as pd

URLCSV = "https://raw.githubusercontent.com/arfan21/fuzzy-logic/main/restoran.csv"
dataRestoran = pd.read_csv(URLCSV)
print(dataRestoran)

# skala 1 - 100
# Pelayanan Jelek (Trapesium)
batasBawahJelekPelayanan = 20
batasAtasJelekPelayanan = 50
# Pelayanan Sedang (Segitiga)
batasBawahSedangPelayanan = 40
batasTengahSedangPelayanan = 65
batasTengahSedangPelayanan = 65
batasAtasSedangPelayanan = 90
# Pelayanan Bagus (Trapesium)
batasBawahBagusPelayanan = 80
batasAtasBagusPelayanan = 100

# skala 1 - 10
# Makanan Tidak Enak (Trapesium)
batasBawahTidakEnakMakanan = 3
batasAtasTidakEnakMakanan = 5
# Makanan Sedang (Segitiga)
batasBawahSedangMakanan = 4
batasTengahSedangMakanan = 6.5
batasTengahSedangMakanan = 6.5
batasAtasSedangMakanan = 9
# Makanan Enak (Trapesium)
batasBawahEnakMakanan = 8
batasAtasEnakMakanan = 10


def pelayanan(x):
    hasilPelayanan = []
    if ((x >= batasBawahJelekPelayanan) and (x <= batasAtasJelekPelayanan)):
        hasilPelayanan.appenpelayananJelek(x)
    if ((x >= batasBawahSedangPelayanan) and (x <= batasAtasSedangPelayanan)):
        hasilPelayanan.append(pelayananSedang(x))
    if ((x >= batasBawahBagusPelayanan) and (x <= batasAtasBagusPelayanan)):
        hasilPelayanan.append(pelayananBagus(x))
    return hasilPelayanan


def pelayananJelek(x):
    if (x >= 0 and x <= batasBawahJelekPelayanan):
        return 'kecil', 1.0
    elif (x > batasBawahJelekPelayanan and x <= batasAtasJelekPelayanan):
        return 'kecil', ((batasAtasJelekPelayanan-x)/(batasAtasJelekPelayanan-batasBawahJelekPelayanan))


def pelayananSedang(x):
    if (x >= batasBawahSedangPelayanan and x <= batasTengahSedangPelayanan):
        return 'sedang',  ((x-batasBawahSedangPelayanan)/(batasTengahSedangPelayanan - batasBawahSedangPelayanan))
    elif (x > batasTengahSedangPelayanan and x <= batasAtasSedangPelayanan):
        return 'sedang', ((batasAtasSedangPelayanan-x)/(batasAtasSedangPelayanan-batasTengahSedangPelayanan))


def pelayananBagus(x):
    if (x >= batasBawahBagusPelayanan and x <= batasAtasBagusPelayanan):
        return 'besar',  ((x-batasBawahBagusPelayanan)/(batasAtasBagusPelayanan-batasBawahBagusPelayanan))
    elif (x > batasAtasBagusPelayanan):
        return 'besar', 1
