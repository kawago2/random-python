# Program Python untuk mencetak semua 
# permutasi menggunakan fungsi dari library python 

print(20*"==")
print("Program Membuat Permutasi dalam 1 Angka")
print(20*"==")

from itertools import permutations 

r = input("masukkan nilai r elemen dari banyaknya angka : ")

mut = permutations(input("masukkan angka yang ingin di mutasi (tanpaspasi) : "), int(r))

# Print semua permutasi 
for i,mut in enumerate(list(mut), 1):
    print(f'cara {i} = {mut}')
