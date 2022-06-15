# Program Python untuk mencetak semua 
# kombinasi dengan panjang tertentu

print(20*"==")
print("Program Membuat Kombinasi dalam 1 Angka")
print(20*"==")

from itertools import combinations 

r = input("masukkan nilai r elemen dari banyaknya angka : ")
comb = combinations(input("masukkan angka urutan yang ingin di kombinasi (tanpaspasi) : "), int(r))

# Print semua kombinasi
for i,comb in enumerate(list(comb), 1):
    print(i)
    print(f'cara {i} = {comb}')
