import os  # Mengimpor os untuk clear screen

# Pertanyaan
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

# Pilgan
pilgan = [
    ["A. Gunung Merapi", "B. Gunung Rinjani", "C. Gunung Kerinci", "D. Gunung Jaya Wijaya"],  # D
    ["A. Jawa", "B. Kalimantan", "C. Sumatera", "D. Sulawesi"],                               # B
    ["A. Afrika", "B. Amerika", "C. Asia", "D. Eropa"],                                       # C
    ["A. Bangkok", "B. Kuala Lumpur", "C. Manila", "D. Hanoi"],                               # B
    ["A. Laut Jawa", "B. Selat Malaka", "C. Selat Sunda", "D. Laut Banda"],                   # C
    ["A. Danau Toba", "B. Danau Maninjau", "C. Danau Sentani", "D. Danau Poso"],              # A
    ["A. Singapura", "B. Malaysia", "C. Australia", "D. Filipina"],                           # B
    ["A. Asia", "B. Amerika Selatan", "C. Afrika", "D. Australia"],                           # B
    ["A. Bandung", "B. Semarang", "C. Yogyakarta", "D. Solo"],                                # B
    ["A. Indonesia", "B. Jepang", "C. Filipina", "D. Kanada"]                                 # A
]

# Kunjaw
kunci = ["D", "B", "C", "B", "C", "A", "B", "B", "B", "A"]

# Membersihkan layar 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi menu utama
def tampilkan_menu():
    clear()
    print("\n=======================================")
    print("       KUIS GEOGRAFI INDONESIA")
    print("=======================================")
    print("1. Tentang Kuis Ini")
    print("2. Mulai Kuis")
    print("3. Keluar")
    print("=======================================")
    pilihan = input("Pilih menu (1-3): ")  # Input
    return pilihan

# Deskripsi tentang kuis
def tampilkan_tentang():
    clear()
    print("\n=======================================")
    print("          TENTANG KUIS INI")
    print("=======================================")
    print("Kuis geografi dasar tentang Indonesia")
    print("Dibuat untuk pembelajaran python dasar")
    print("=======================================")
    input("Tekan Enter untuk kembali...")  

# Fungsi memulai kuis
def mulai_kuis(nama):
    clear()
    score = 0  # Inisialisasi skor
    for x in range(10):  
        clear()
        print(f"Soal {x+1}: {pertanyaan[x]}")  # Tampilkan pertanyaan
        for pilihan in pilgan[x]:  # Tampilkan pilihan jawaban
            print(pilihan)
        
        # Validasi jawaban
        while True:
            jawaban = input("Jawaban (A/B/C/D): ").upper()
            if jawaban in ['A', 'B', 'C', 'D']:
                break
            print("Input salah! Harap masukkan A, B, C, atau D")
        
        # Cek jawaban
        if jawaban == kunci[x]:
            print("Jawabanmu benar!")
            score += 1
        else:
            print(f"Jawabanmu salah. Jawaban benar: {kunci[x]}")
        
        if x < 9:
            input("Tekan Enter untuk lanjut...")  

    clear()
    print(f"\nSkor akhir: {score}/10")  # Tampilkan skor akhir
    
    # Ulasan berdasarkan skor
    if score == 10:
        ulasan = "Luar biasa! Kamu menguasai geografi!"
    elif score >= 8:
        ulasan = "Good job! Sudah sangat bagus!"
    elif score >= 5:
        ulasan = "Lumayan, tetap semangat belajar ya!"
    else:
        ulasan = "Ayo belajar lagi, kamu pasti bisa!"

    print(f"{ulasan} Good job, {nama}!")  # Tampilkan 
    input("Tekan Enter untuk kembali ke menu...") 

# Fungsi utama 
def main():
    clear()
    nama = input("Selamat datang! Masukkan nama kamu: ").strip().capitalize()  # Input nama dan format rapi
    while True:
        pilihan = tampilkan_menu()
        if pilihan == "1":
            tampilkan_tentang()
        elif pilihan == "2":
            mulai_kuis(nama)
        elif pilihan == "3":
            print(f"\nTerima kasih, {nama}!")  # Keluar dari program
            break
        else:
            print("Pilihan tidak valid!")  # Validasi input menu

# Menjalankan fungsi main hanya jika file ini dijalankan langsung
if __name__ == "__main__":
    main()