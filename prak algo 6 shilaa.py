# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 21:16:20 2022

@author: shilaaa
"""

def bulan():
    print ("menentukan hari dan bulan")
    
while True:
    print ("ketik 0 untuk menghentikan program ini")
    x = int(input("Masukkan bulan ke berapa (1-12)?"))
    if (x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12):
        print ("maka jumlah harinya adalah 31\n") 
    elif (x==2):
        print ("maka jumlah harinya adalah 28\n")
    elif (x==0):
        print ("Terima kasih, see you next .\n")
        break
    else :
        print ("maka jumlah harinya adalah 30\n") 
        
x = bulan
print (x)