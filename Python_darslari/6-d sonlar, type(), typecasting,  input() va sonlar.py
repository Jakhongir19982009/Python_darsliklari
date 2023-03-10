# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 17:35:34 2023

@author: Jakhongir Tuychiev
"""

                        # Integers - BUTUN SONLAR

# Integer - butun sonlar. Python dasturlash tilida butun sonlar va manfiy sonlar
# ustida arifmetik amallar bajarsa bo'ladi.
a = 2
b = 3.5
c = a+b
print(c)


                        # UZUN SONLARNI KIRITISH

d = 36_550_358  # ko'p xonali sonlarni (_) belgisi orqali guruhlab yozish m-n.
e = 7_597_834_792


                        # Floats - O'NLIK SONLAR

# floats - o'nlik sonlar. Floating point numbers - ning qisqartmasidir.
# Ma'nosi "suzuvchi nuqtali sonlar".
pi = 3.14159
radius = 10 
diametr = 2*radius
print("Aylana uzunligi ", pi*diametr, "ga teng.")


                        # BUTUN SONDAN O'NLIK SONGA

# Butun sonni butun songa bo'lganda ham o'nlik son paydo bo'ladi.
a = 20
b = 40
c = b/a
print(c) 

# Butun va o'nlik sonlar orasidagi barcha arifmetik amallar natijasi o'nlik son bo'ladi.
a = 2
b = 3.0
print(a+b)
print(a*b)
print(a**b)
print(2*(a+b))
print("Yer kurrasida ", e, "ga yaqin odam yashaydi.")


                            # KONSTANTA

# Konstant qiymatni pythonda bildirish uchun o'zgaruvchilar nomi katta harflar bilan
# yozish qabul qilingan.
PI = 3.14159
DOIM = 'internet'


                    # BIR NECHA O'ZGARUVCHIGA QIYMAT BERISH

# bir nechta o'zgaruvchilarga qiymat berish uchun o'zgaruvchilar va qiymatlar orasi
# (,) bilan ajratib yoziladi.
x , y , z = 15 , -8 , 6.75
print(x , z)
print(x , y , z)


                            # TYPECASTING

# typecasting - o'zgaruvchilarning turini o'zgartirish. str() , int() , float().
ism = 'Jakhongir'
yosh = 25
xabar = ism + ' ' + str(yosh) + ' yoshda.'

print(xabar)
print(f"{ism} {yosh} yoshda")


                        # O'ZGARUVCHI TURINI TEKSHIRISH

#   foydalanuvchidan tug'ilgan yilini so'raymiz
t_yili = input("Tug'ilgan yilingizni kiriting: ")
#   o'zgaruvchini int()ga aylantiramiz
t_yili = int(t_yili)
#   foydalanuvchi yoshini hisoblaymiz
yoshi = 2023 - t_yili
#   foydalanuvchi yoshini konsolga chiqaramiz
print("Siz " + str(yoshi) + " yoshda ekansiz")

# THE END