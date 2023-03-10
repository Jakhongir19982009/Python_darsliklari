# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 22:51:10 2023

@author: Jakhongir Tuychiev
"""


                            # 1-MISOL

 # foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur.
son = int(input("Istalgan son kiriting:\n>>>"))
print(son, " ning kvadrati ", son**2, " ga teng")
print(son, " ning kubi ", son**3, " ga teng") 


                            # 2-MISOL

# foydalanuvchining yoshini so'rab, uning tu'g'ilgan yilini hisoblab,
# konsolga chiqaruvchi dastur
yosh = int(input("Yoshingiz nechida?\n>>>"))
t_yil = 2023-yosh
print("Siz ", t_yil, " yilda tug'ilgansiz")


                            # 3-MISOL

# foydalanuvchidan ikki son kiritishni so'rab, sonlarning yig'indisi, ayirmasi,
# ko'paytmasi va bo'linmasini chiqaruvchi dastur
a = float(int(input("Birinchi sonni kiriting:")))

b = float(int(input('Ikkinchi sonni kiriting:')))
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")


