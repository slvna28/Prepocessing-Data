# Versi tanpa penjelasan dapat dilihat di clean.py

import pandas as pd
import numpy as np


data = pd.read_csv('diamonds.csv')

# 1
# Memilih 6 kolom pertama dengan memberikan nama kolom yang akan dipilih
# Nama-nama kolom disimpan ke dalam sebuah list
# Kemudian mengakses 'data' menggunakan list sebelumnya sebagai 'key'

kolom = ['carat', 'cut', 'color', 'clarity', 'depth', 'table']
print(data[kolom])

# ----------------------------------------------------------------------

# 2
# Menggunakan property 'dtype' untuk melihat tipe data setiap kolom

print(data.dtypes)

# ----------------------------------------------------------------------

# 3
# Menggunakan fungsi 'describe' untuk melihat summarize dan menggunakan
# argumen 'object' dalam sebuah list pada parameter include untuk melihat
# summarize kolom yang memiliki tipe data 'object'

print(data.describe(include=['object']))

# ----------------------------------------------------------------------

# 4
# Menggunakan kondisi (syarat) tertentu yaitu
# - data['x'] > 5 sebagai length (panjang)
# - data['y'] > 5 sebagai width (lebar)
# - data['depth] > 5 sebagai depth
# semua kondisi itu digabung menggunakan operator bitwise-and (&)
# kemudian mengakses data berdasarkan kondisi diatas sebagai 'key'

# Reference
# bitwise-operator : https://code.tutsplus.com/id/articles/understanding-bitwise-operators--active-11301

print(data[(data['x'] > 5) & (data['y'] > 5) & (data['depth'] > 5)])

# ----------------------------------------------------------------------

# 5
# Sama seperti sebelumnya kita menggunakan kondisi (syarat) yaitu
# - data['cut'] == 'Fair'
# - data['cut'] == 'Good'
# - data['cut'] == 'Premium'
# Semua kondisi itu digabung menggunakan operator bitwise-or (|)
# Referensi sama seperti no. 4

print(data[(data['cut'] == 'Fair') | (data['cut'] == 'Good') | (data['cut'] == 'Premium')]) 

# ----------------------------------------------------------------------

# 6
# Memilih kolom 'cut' kemudian menggunakan fungsi 'describe' untuk melihat summary

print(data['cut'].describe())

# ----------------------------------------------------------------------

# 7
# Menggunakan fungsi 'notna' atau 'notnull' untuk mengganti nilai missing
# menjadi False dan nilai lainnya menjadi True

print(data.notna())

# ----------------------------------------------------------------------

# 8
# Menggunakan fungsi 'dropna' untuk menghapus baris yang memiliki nilai NAN
# bagian optional yaitu menggunakan argumen True pada parameter inplace
# agar output dari fungsi langsung mengubah data original
# Kemdian menggunakan property 'shape' untuk melihat "bentuk" dari data

# Jika tidak menggunakan inplace=True maka syntax menjadi
# data = data.dropna()
# print(data.shape)

data.dropna(inplace=True)
print(data.shape)

# ----------------------------------------------------------------------

# 9
# Menset index data dengan kolom yang ada pada data, menggunakan set_index
# Dan menggunakan fungsi 'reset_index' untuk mereset index datanya

data = data.set_index('color')
data.reset_index()
print(data)

# ----------------------------------------------------------------------

# 10
# Menggunakan 'fillna' pada df1 untuk menggantikan nilai NAN dengan data dari df2

df1 = pd.DataFrame({
    'A': [None, 0, None],
    'B': [3, 4, 5]
})
df2 = pd.DataFrame({
    'A': [1, 1, 3],
    'B': [3, None, 3]
})
df1 = df1.fillna(df2)
print(df1)

# ----------------------------------------------------------------------

# 11
# Menggabungkan data1 dan data2 pada kolom 'key1' menggunakan fungsi merge

data1 = pd.DataFrame({
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
    'P': ['P0', 'P1', 'P2', 'P3'],
    'Q': ['Q0', 'Q1', 'Q2', 'Q3']
})
data2 = pd.DataFrame({
    'key1': ['K0', 'K1', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K0'],
    'R': ['R0', 'R1', 'R2', 'R3'],
    'S': ['S0', 'S1', 'S2', 'S3']
})
data = pd.merge(data1, data2, on='key1')
print(data)

# ----------------------------------------------------------------------

# 12
# Menggunakan fungsi 'groupby' dengan argumen 'school_code' untuk mengelompokkan data
# berdasarkan kolom 'school_code'

student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
grouped = student_data.groupby('school_code')

# ----------------------------------------------------------------------

# 13
# Menggunakan for loop untuk mengecek setiap group dalam data yang telah dikelompokkan
# Kemudian mengambil sebuah group (kelompok) dengan fungsi 'get_group'
# Lalu mencari summarize pada kolom 'age' dan menggunakan 'loc' untuk memilih output apa yang diinginkan
# disini dipilih 'mean', 'min', 'max' sebagai output
# Kemudian memprint setiap data berdasarkan group dan summary-nya

for group in grouped.groups:
    current = grouped.get_group(group)
    summarize = current['age'].describe().loc[['mean', 'min', 'max']]
    print(f'{group}\n{summarize}\n')

# ----------------------------------------------------------------------

# 14
# Pertama-tama menggunakan 'isnull' untuk melihat data yang memiliki nilai NAN, kemudian
# Jumlahkan data yang bernilai True (output dari isnull adalah boolean) menggunakan fungsi 'sum'
# pada fungsi 'sum' digunakan argumen 1 pada parameter 'axis' yang berarti sumbu yang dijumahkan
# axis 1 merupakan baris dan axis 0 adalah kolom
# kemudian kita mengecek jika nilainya dibawah dari 2
# lalu kita mengakses data (df) berdasarkan kondisi yang ada sebagai 'key'

df = pd.DataFrame({
    'ord_no':[np.nan, np.nan, 70002, np.nan, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, np.nan],
    'purch_amt':[np.nan, 270.65, 65.26, np.nan, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, np.nan],
    'ord_date': [np.nan, '2012-09-10', np.nan, np.nan, '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10',
                    '2012-10-10', '2012-06-27', '2012-08-17', np.nan],
    'customer_id':[np.nan, 3001, 3001, np.nan, 3002, 3001, 3001, 3004, 3003, 3002, 3001, np.nan]
})
print(df[df.isnull().sum(axis=1) < 2])

# ----------------------------------------------------------------------

# 15
# Pertama kita memilih kolom yang akan dicari meannya, semua kolom dipakai kecuali tanggal (ord_date)
# Lalu kita menggunakan for loop untuk mengecek setiap kolom yang sudah dipilih
# Untuk setiap kolom:
# - Kita cari mean-nya menggunakan fungsi 'mean'
# - Ganti nilai pada kolom yang bernilai NAN dengan mean
# Penjelasan inplace=True sama seperti sebelumnya

df = pd.DataFrame({
    'ord_no':[70001, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
    'purch_amt':[150.5, np.nan, 65.26, 110.5, 948.5, np.nan, 5760, 1983.43, np.nan, 250.45, 75.29, 3045.6],
    'sale_amt':[10.5, 20.65, np.nan, 11.5, 98.5, np.nan, 57, 19.43, np.nan, 25.45, 75.29, 35.6],
    'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10',
                    '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id':[3002, 3001, 3001, 3003 ,3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],
    'salesman_id':[5002, 5003, 5001, np.nan, 5002, 5001, 5001, np.nan, 5003, 5002, 5003, np.nan]
})

columns = ['ord_no', 'punch_amt', 'sale_amt', 'customer_id', 'salesman_id']

for column in columns:
    mean = df[column].mean()
    df[column].fillna(mean, inplace=True)

print(df)
