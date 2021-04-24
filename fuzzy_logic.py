import pandas as pd

URLCSV = "https://raw.githubusercontent.com/arfan21/fuzzy-logic/main/restoran.csv"
dataRestoran = pd.read_csv(URLCSV)
print(dataRestoran)

# skala 1 - 100
# Pelayanan Jelek (Trapesium)
batasBawahJelekPelayanan = 20.0
batasAtasJelekPelayanan = 50.0
# Pelayanan Sedang (Segitiga)
batasBawahSedangPelayanan = 40.0
batasTengahSedangPelayanan = 65.0
batasTengahSedangPelayanan = 65.0
batasAtasSedangPelayanan = 90.0
# Pelayanan Bagus (Trapesium)
batasBawahBagusPelayanan = 80.0
batasAtasBagusPelayanan = 100.0

# skala 1 - 10
# Makanan Tidak Enak (Trapesium)
batasBawahTidakEnakMakanan = 3.0
batasAtasTidakEnakMakanan = 5.0
# Makanan Sedang (Segitiga)
batasBawahSedangMakanan = 4.0
batasTengahSedangMakanan = 6.5
batasTengahSedangMakanan = 6.5
batasAtasSedangMakanan = 9.0
# Makanan Enak (Trapesium)
batasBawahEnakMakanan = 8.0
batasAtasEnakMakanan = 10.0


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
        return 'besar', 1.0


def makananTidakEnak(x):
    if (x >= 0 and x <= batasBawahTidakEnakMakanan):
        return 'kecil', 1.0
    elif (x > batasBawahTidakEnakMakanan and x <= batasAtasTidakEnakMakanan):
        return 'kecil', ((batasAtasTidakEnakMakanan-x)/(batasAtasTidakEnakMakanan-batasBawahTidakEnakMakanan))


def makananSedang(x):
    if (x >= batasBawahSedangMakanan and x <= batasTengahSedangMakanan):
        return 'sedang',  ((x-batasBawahSedangMakanan)/(batasTengahSedangMakanan - batasBawahSedangMakanan))
    elif (x > batasTengahSedangMakanan and x <= batasAtasSedangMakanan):
        return 'sedang', ((batasAtasSedangMakanan-x)/(batasAtasSedangMakanan-batasTengahSedangMakanan))


def makananEnak(x):
    if (x >= batasBawahEnakMakanan and x <= batasAtasEnakMakanan):
        return 'besar',  ((x-batasBawahEnakMakanan)/(batasAtasBagusPelayanan-batasBawahEnakMakanan))
    elif (x > batasAtasEnakMakanan):
        return 'besar', 1.0
