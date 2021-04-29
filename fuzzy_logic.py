import pandas as pd

URLCSV = "https://raw.githubusercontent.com/arfan21/fuzzy-logic/main/restoran.csv"
dataRestoran = pd.read_csv(URLCSV)

# skala 1 - 100
# Pelayanan Jelek (Trapesium)
batasBawahJelekPelayanan = 20.0
batasAtasJelekPelayanan = 50.0
# Pelayanan Sedang (Segitiga)
batasBawahSedangPelayanan = 40.0
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
batasAtasSedangMakanan = 9.0
# Makanan Enak (Trapesium)
batasBawahEnakMakanan = 8.0
batasAtasEnakMakanan = 10.0


# fuzzyfikasi pelayanan

def pelayanan(x):
    hasilPelayanan = []
    if ((x >= 0) and (x <= batasAtasJelekPelayanan)):
        hasilPelayanan.append(pelayananJelek(x))
    if ((x >= batasBawahSedangPelayanan) and (x <= batasAtasSedangPelayanan)):
        hasilPelayanan.append(pelayananSedang(x))
    if ((x >= batasBawahBagusPelayanan) and (x <= batasAtasBagusPelayanan)):
        hasilPelayanan.append(pelayananBagus(x))
    return hasilPelayanan


def pelayananJelek(x):
    if (x >= 0.0 and x <= batasBawahJelekPelayanan):
        return 'jelek', 1.0
    elif (x > batasBawahJelekPelayanan and x <= batasAtasJelekPelayanan):
        return 'jelek', ((batasAtasJelekPelayanan-x)/(batasAtasJelekPelayanan-batasBawahJelekPelayanan))


def pelayananSedang(x):
    if (x >= batasBawahSedangPelayanan and x <= batasTengahSedangPelayanan):
        return 'sedang',  ((x-batasBawahSedangPelayanan)/(batasTengahSedangPelayanan - batasBawahSedangPelayanan))
    elif (x > batasTengahSedangPelayanan and x <= batasAtasSedangPelayanan):
        return 'sedang', ((batasAtasSedangPelayanan-x)/(batasAtasSedangPelayanan-batasTengahSedangPelayanan))


def pelayananBagus(x):
    if (x >= batasBawahBagusPelayanan and x <= batasAtasBagusPelayanan):
        return 'bagus',  ((x-batasBawahBagusPelayanan)/(batasAtasBagusPelayanan-batasBawahBagusPelayanan))
    elif (x > batasAtasBagusPelayanan):
        return 'bagus', 1.0


# fuzzyfikasi makanan

def makanan(x):
    hasilMakanan = []
    if ((x >= 0.0) and (x <= batasAtasTidakEnakMakanan)):
        hasilMakanan.append(makananTidakEnak(x))
    if ((x >= batasBawahSedangMakanan) and (x <= batasAtasSedangMakanan)):
        hasilMakanan.append(makananSedang(x))
    if ((x >= batasBawahEnakMakanan) and (x <= batasAtasEnakMakanan)):
        hasilMakanan.append(makananEnak(x))
    return hasilMakanan


def makananTidakEnak(x):
    if (x >= 0 and x <= batasBawahTidakEnakMakanan):
        return 'tidak enak', 1.0
    elif (x > batasBawahTidakEnakMakanan and x <= batasAtasTidakEnakMakanan):
        return 'tidak enak', ((batasAtasTidakEnakMakanan-x)/(batasAtasTidakEnakMakanan-batasBawahTidakEnakMakanan))


def makananSedang(x):
    if (x >= batasBawahSedangMakanan and x <= batasTengahSedangMakanan):
        return 'sedang',  ((x-batasBawahSedangMakanan)/(batasTengahSedangMakanan - batasBawahSedangMakanan))
    elif (x > batasTengahSedangMakanan and x <= batasAtasSedangMakanan):
        return 'sedang', ((batasAtasSedangMakanan-x)/(batasAtasSedangMakanan-batasTengahSedangMakanan))


def makananEnak(x):
    if (x >= batasBawahEnakMakanan and x <= batasAtasEnakMakanan):
        return 'enak',  ((x-batasBawahEnakMakanan)/(batasAtasBagusPelayanan-batasBawahEnakMakanan))
    elif (x > batasAtasEnakMakanan):
        return 'enak', 1.0


# aturanan inferensi

def inference(pelayanan, makanan):
    # buruk
    if (pelayanan == 'jelek' and makanan == 'tidak enak'):
        return 'buruk'
    if (pelayanan == 'jelek' and makanan == 'sedang'):
        return 'buruk'
    if (pelayanan == 'jelek' and makanan == 'enak'):
        return 'buruk'
    if (pelayanan == 'sedang' and makanan == 'tidak enak'):
        return 'buruk'

    # biasa
    if (pelayanan == 'sedang' and makanan == 'sedang'):
        return 'biasa'
    if (pelayanan == 'bagus' and makanan == 'tidak enak'):
        return 'biasa'
    if (pelayanan == 'bagus' and makanan == 'sedang'):
        return 'biasa'

    # baik
    if (pelayanan == 'sedang' and makanan == 'enak'):
        return 'baik'
    if (pelayanan == 'bagus' and makanan == 'enak'):
        return 'baik'


# mencari nilai inferensi

def nilaiInference(Pelayanan, Makanan):
    minBaik = 0.0
    minBiasa = 0.0
    minBuruk = 0.0
    for i in pelayanan(Pelayanan):
        for j in makanan(Makanan):
            if (inference(i[0], j[0]) == 'baik'):
                if (minBaik < min(i[1], j[1])):
                    minBaik = min(i[1], j[1])
            if (inference(i[0], j[0]) == 'biasa'):
                if (minBiasa < min(i[1], j[1])):
                    minBiasa = min(i[1], j[1])
            if (inference(i[0], j[0]) == 'buruk'):
                if (minBuruk < min(i[1], j[1])):
                    minBuruk = min(i[1], j[1])
    return ('buruk', minBuruk), ('biasa', minBiasa), ('baik', minBaik)


# defuzzifikasi dengan metode Weighted Average

def defuzzy(x, y, z):
    return (x*20) + (y*50) + (z*80) / (x+y+z)


# fungsi untuk mencari 10 restoran terbaik

def findBestResto(dataDefuzzy):
    # mengurutkan hasil defuzzyfikasi
    best = sorted(zip(dataRestoran.id, dataDefuzzy),
                  key=lambda x: x[1], reverse=True)

    # bestResto untuk menampung 10 terbaik restoran
    bestResto = []
    for i in range(10):
        bestResto.append(best[i])
    return bestResto


# main program

def main():
    # temp untuk menampung hasil dari defuzzyfikasi
    temp = []

    for i, row in dataRestoran.iterrows():
        pelayananValue = row['pelayanan'].astype(float)
        makananValue = row['makanan'].astype(float)
        arr_sugeno = nilaiInference(pelayananValue, makananValue)
        defuzzyResult = defuzzy(
            arr_sugeno[0][1], arr_sugeno[1][1], arr_sugeno[2][1])
        temp.append(defuzzyResult)

    # find best resto
    bestResto = findBestResto(temp)

    # menulis hasil peringkat ke excel
    df_bestResto = pd.DataFrame(bestResto, columns=['id resto', 'nilai'])

    print(df_bestResto)

    idResto = df_bestResto.loc[:, 'id resto']
    xlsFile = pd.DataFrame(idResto)
    xlsFile.to_excel('peringkat.xlsx', index=False)


if __name__ == "__main__":
    main()
