#PERCABANGAN

nilai = 9

if nilai > 7:
	print("sembilan lebih besar dari tujuh")
	
if nilai < 10:
	print("sembilan lebih kecil dari sepuluh")

#CONTOH 2

nilai = 80

if nilai > 75:
	print("Nilai anda adalah A")
	
if nilai < 75:
	print("Nilai anda adalah B")	
	
#CONTOH 3

nama_presiden = input("Nama presiden pertama :")

if nama_presiden == 'Soekarno':
	print("Jawaban anda benar")
	
else:
	print("Jawaban anda salah")
	
#CONTOH 4

umur = input("Berapa umur anda : ")

if int(umur) < 25:
	if int(umur) < 20:
		print("Anda masih sekolah")
		
	else:
		print("Anda sudah bekerja")
		
elif int(umur) > 25:
	if int(umur) <30:
		print("Harusnya Anda menikah")
	else:
		print("Anda sudah punya anak 3")
		
else:
	print("Maaf, jawaban anda salah")