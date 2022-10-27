# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:29:29 2022

@author: shilaaa
"""

data_nilai = {
    'A': 4.0,
    'A-': 3.75,
    'B+': 3.5,
    'B': 3.0,
    'B-': 2.75,
    'C+': 2.5,
    'C': 2.0,
    'C-': 1.75,
    'D': 1.50,
    'E': 1.25
}

total = []
bobot = input('Masukkan bobot nilai (pisahkan dengan spasi): ').upper().split()
def hitung_rata(data_nilai, bobot):
    for i in bobot:
        if i == 'A':
            total.append(data_nilai['A'])
        elif i == 'A-':
            total.append(data_nilai['A-'])
        elif i == 'B+':
            total.append(data_nilai['B+'])
        elif i == 'B':
            total.append(data_nilai['B'])
        elif i == 'B-':
            total.append(data_nilai['B-'])
        elif i == 'C+':
            total.append(data_nilai['C+'])
        elif i == 'C':
            total.append(data_nilai['C'])
        elif i == 'C-':
            total.append(data_nilai['C-'])
        elif i == 'D':
            total.append(data_nilai['D'])
        elif i == 'E':
            total.append(data_nilai['E'])
    return sum(total)/len(total)


print(hitung_rata(data_nilai, bobot))
