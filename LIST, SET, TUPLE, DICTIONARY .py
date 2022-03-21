#LIST

#Membuat contoh list
nama_list = ['nilai1', 'nilai2', 'nilai3', 'nilai4', 'nilai5']

#Menampilkan List menggunakan perulangan
for i in nama_list:
  print(i)

i = 0
while i < len(nama_list):
  print(nama_list[i])
  i += 1

#Mengupdate nilai dalam List
nama_list = ['nilai1', 'nilai2', 'nilai3', 'nilai4', 'nilai5']
print('\nSebelum diupdate')
print(nama_list)

nama_list[0] = 'nilai6'
print('\nSetelah di update')
print(nama_list)

#Menghapus nilai yang ada dalam List

del nama_list[0]
print('\nNilai setelah dihapus dengan del')
print(nama_list)

nama_list.remove('nilai2')
print('\nNilai setelah dihapus dengan remove')
print(nama_list)

nama_list.pop()
print('\nNilai setelah dihapus dengan pop')
print(nama_list)

#Menambahkan Nilai kedalam List
nama_list.append('Nilai7')
print('\nList setelah ditambahkan Nilai menggunakan append')
print(nama_list)

nama_list.extend(['nilai8', 'nilai9', 'nilai10'])
print('\nList setelah ditambahkan Nilai menggunakan extend')
print(nama_list)

nama_list.insert(0, 'nilai1')
print('\nList setelah ditambahkan Nilai menggunakan insert')
print(nama_list)

#SET
#Membuat contoh Set
telepon = {'nokia', 'oppo', 'vivo', 'microsoft', 'google'}
#Menampilkan Set dengan menggunakan perulangan
for i in telepon:
    print(i)
#Mengupdate salah satu Nilai dari Set
telepon = list(telepon)
telepon[0] = 'xiaomi'
telepon = set(telepon)
print(telepon)
#Menghapus salah satu Nilai dari Set
telepon = list(telepon)
telepon.pop()
telepon = set(telepon)
print(telepon)
#Menambahkan Nilai kedalam Set
telepon = list(telepon)
telepon.insert(2, 'rog')
telepon = set(telepon)
print(telepon)


#TUPLE
#Membuat contoh Tuple
badan = ('gemuk', 'kurus', 'tinggi', 'pendek', 'tegak')
#Menampilakan Tuple menggunakan perulangan
for x in badan:
    print(x)

x = 0
while x < len(badan):
    print(badan[x])
    x += 1
    
#Mengupdate Nilai didalam Tuple
badan = ('gemuk', 'kurus', 'tinggi', 'pendek', 'tegak')
print('\nSebelum di update')
print(badan)

badan = list(badan)
badan[0] = 'bulat'
badan = tuple(badan)
print(badan)

#Menghapus Nilai dari Tuple
badan = list(badan)
del badan[-1]
badan = tuple(badan)
print(badan)

badan = list(badan)
badan.remove('tinggi')
badan = tuple(badan)
print(badan)

badan = list(badan)
badan.pop()
badan = tuple(badan)
print(badan)

#Menambahkan Nilai kedalam Tuple
badan = list(badan)
badan.append('lonjong')
badan = tuple(badan)
print(badan)

badan = list(badan)
badan.extend(['bungkuk', 'gembrot'])
badan = tuple(badan)
print(badan)

badan = list(badan)
badan.insert(2, 'tinggi kurus')
badan = tuple(badan)
print(badan)

#DICTIONARY

#Membuat contoh Dictionary
motor = {
'yamaha soul':'gesit',
'warna':'abu abu',
'keluaran':'2014',}

#Menampilkan Dictionary menggunakan perulangan
for i in motor.items():
    print(i)

for i in motor:
    print(i)

#Mengupdate Nilai pada Dictionary
motor ['warna'] = 'biru'
print(motor)

#Menghapus Nilai pada Dictionary
motor.pop('keluaran')
print(motor)

#Menamba Nilai pada Dictionary
motor['anak muda'] = '19'
print(motor)
