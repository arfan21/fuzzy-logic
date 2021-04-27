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
    maksBaik = 0.0
    maksBiasa = 0.0
    maksBuruk = 0.0
    fuzzyPelayanan = pelayanan(Pelayanan)
    fuzzyMakanan = makanan(Makanan)
    print(f"fuzzyfikasi pelayanan -> {fuzzyPelayanan}")
    print(f"fuzzyfikasi makanan -> {fuzzyMakanan}")
    for i in fuzzyPelayanan:
        for j in fuzzyMakanan:
            hasilInference = inference(i[0], j[0])

            print(f"hasil inference -> {hasilInference}")

            if (hasilInference == 'baik'):
                if (maksBaik < min(i[1], j[1])):
                    maksBaik = min(i[1], j[1])
            if (hasilInference == 'biasa'):
                if (maksBiasa < min(i[1], j[1])):
                    maksBiasa = min(i[1], j[1])
            if (hasilInference == 'buruk'):
                if (maksBuruk < min(i[1], j[1])):
                    maksBuruk = min(i[1], j[1])
            print(
                f"maks buruk : {maksBuruk} -- maks biasa : {maksBiasa} -- maks baik : {maksBaik}")
    return ('buruk', maksBuruk), ('biasa', maksBiasa), ('baik', maksBaik)


# defuzzifikasi dengan metode sugeno

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

    for i, row in dataRestoran.head(10).iterrows():
        print(f"id -> {row['id']}")

        pelayananValue = row['pelayanan'].astype(float)
        makananValue = row['makanan'].astype(float)
        arr_sugeno = nilaiInference(pelayananValue, makananValue)

        print(f"nilai inference : {arr_sugeno}")

        defuzzyResult = defuzzy(
            arr_sugeno[0][1], arr_sugeno[1][1], arr_sugeno[2][1])

        print(f"defuzzy result : {arr_sugeno}\n")

        temp.append(defuzzyResult)

    # find best resto
    bestResto = findBestResto(temp)

    # menulis hasil peringkat ke excel
    df_bestResto = pd.DataFrame(bestResto, columns=['id resto', 'nilai'])

    print("\n")
    print(df_bestResto)

    idResto = df_bestResto.loc[:, 'id resto']
    xlsFile = pd.DataFrame(idResto)
    xlsFile.to_excel('peringkat_tes.xlsx', index=False)


if __name__ == "__main__":
    main()