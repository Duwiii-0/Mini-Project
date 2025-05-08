
# List 1: Pertanyaan Pilihan Ganda (Tema Geografi Mudah)
pertanyaan = [
    "Gunung tertinggi di Indonesia adalah?",
    "Pulau terbesar di Indonesia adalah?",
    "Benua terbesar di dunia adalah?",
    "Ibukota negara Malaysia adalah?",
    "Laut yang memisahkan Pulau Sumatera dan Jawa adalah?",
    "Danau terbesar di Indonesia adalah?",
    "Negara tetangga Indonesia di sebelah utara adalah?",
    "Sungai Amazon terdapat di benua apa?",
    "Ibukota Provinsi Jawa Tengah adalah?",
    "Negara dengan jumlah pulau terbanyak di dunia adalah?"
]

# List 2: Jawaban Pilihan Ganda (1 benar, 3 pengecoh)
pilgan = [
    ["A. Gunung Merapi", "B. Gunung Rinjani", "C. Gunung Kerinci", "D. Gunung Jaya Wijaya"],   # D
    ["A. Jawa", "B. Kalimantan", "C. Sumatera", "D. Sulawesi"],                                # B
    ["A. Afrika", "B. Amerika", "C. Asia", "D. Eropa"],                                        # C
    ["A. Bangkok", "B. Kuala Lumpur", "C. Manila", "D. Hanoi"],                                # B
    ["A. Laut Jawa", "B. Selat Malaka", "C. Selat Sunda", "D. Laut Banda"],                    # C
    ["A. Danau Toba", "B. Danau Maninjau", "C. Danau Sentani", "D. Danau Poso"],               # A
    ["A. Singapura", "B. Malaysia", "C. Australia", "D. Filipina"],                            # B
    ["A. Asia", "B. Amerika Selatan", "C. Afrika", "D. Australia"],                            # B
    ["A. Bandung", "B. Semarang", "C. Yogyakarta", "D. Solo"],                                 # B
    ["A. Indonesia", "B. Jepang", "C. Filipina", "D. Kanada"]                                  # A
]

kunci = ["D", "B", "C", "B", "C", "A", "B", "B", "B", "A"]  # Kunci jawaban

score = 0 # Inisialisasi skor
# salah
# nilai

for x in range(10):
    print("=======================================")
    print(f"soal ke {x+1} : {pertanyaan[x]}")
    print(pilgan[x][0])
    print(pilgan[x][1])
    print(pilgan[x][2])
    print(pilgan[x][3])
    jawaban = input("Pilih jawabanmu (A/B/C/D) = ").upper()
    
    if jawaban == kunci[x]:
        print(" ")
        print("Jawabanmu benar")
        score += 1
        input("klik enter untuk melanjutkan")
    else:
        print("Jawabanmu salah")
        input("klik enter untuk melanjutkan")
        # jawaban yang benar apa
    
input("klik enter untuk melihat hasil!")

# cek nilai