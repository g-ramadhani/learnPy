#Quiz Game with Python

print("===========================")
print("Selamat Datang di Game Quiz")
print("===========================")

playing=input("Apakah Anda Ingin Bermain ? Ya/Tidak\n")

if playing.lower() != "ya" :
    print("Baiklah, Sampai Jumpa Semoga Harimu Menyenangkan.")
    quit()
else:
    nama=input("Siapa Nama Anda ? ")

print("Baiklah "+nama+", Mari Bermain Quiz !!!")
print("===========================")

score=0

answer=input("Apa Nama Ibu Kota Jawa Barat ? ")
if answer.lower() == "bandung" :
    print("Benar !")
    score += 1
else:
    print("Salah :(")

answer=input("Siapakah Presiden Indonesia Pertama ? ")
if answer.lower() == "soekarno" :
    print("Benar !")
    score += 1
else:
    print("Salah :(")

answer=input("Apa Kepanjangan RAM ? ")
if answer.lower() == "random access memory" :
    print("Benar !")
    score += 1
else:
    print("Salah :(")

answer=input("Berat Sama Dipikul, Ringan sama Di")
if answer.lower() == "jinjing" :
    print("Benar !")
    score += 1
else:
    print("Salah :(")

answer=input("Apa Kepanjangan dari SIM ? ")
if answer.lower() == "surat izin mengemudi" :
    print("Benar !")
    score += 1
else:
    print("Salah :(")

print("Terima Kasih Telah Bermain "+nama+", kamu menjawab "+str(score)+" pertanyaan dengan benar")

rounding=round(score/5*100,2)

print("Nilaimu adalah "+str(rounding))