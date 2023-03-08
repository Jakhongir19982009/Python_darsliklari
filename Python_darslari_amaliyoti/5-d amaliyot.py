# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:10:12 2023

@author: Jakhongir Tuychiev
"""
# Quyidagi o'zgaruvchilarni yarating: 
    
# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor" 
# viloyat="Samarqand"
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang.
# Va avvalgi mashqni takrorlang.
print("Iltimos quyidagi ma'lumotlarni kiriting:")
kocha = input("Ko'changiz?  ")
mahalla = input("Mahallangiz?  ")
tuman = input("Sizning tumaningiz?  ")
viloyat = input("Viloyatingiz?  ")
print(f"\n{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
print(f"\n{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati.")

# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
manzil = f"""
{kocha} ko'chasi, 
{mahalla} mahallasi, 
{tuman} tumani, 
{viloyat} viloyati."""

# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
manzil_2 = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil_2.title())
print(manzil_2.upper())
print(manzil_2.lower())
print(manzil_2.capitalize())

# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
print(manzil.lower())
print(manzil.upper())
print(manzil.capitalize())
print(manzil.title())

