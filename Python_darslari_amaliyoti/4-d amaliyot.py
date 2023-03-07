# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 12:16:53 2023

@author: tuych
"""
# ma'lumotlar
shahar = "Булунгур"
viloyat = 'Samarqand'

# ma'lumotlar
ism = 'Jakhongir'
familiya = "Tuychiyev"
yosh = 25



# (+) matnni qo'shish operatori
ism_sharif = (ism + familiya)
ism_sharif = (ism + ' ' + familiya)
# print("Mening ismim " + ism)



# f"..." f-string operatori. Bir necha matnlar va ma'lumotlarni qo'shuvchi operator.
ism_sharif = f"{ism} {familiya}"
manzil = f"{viloyat} viloyati {shahar}"
# print(ism_sharif)
# print(f"{ism} {familiya}")
# print(f"Assalomu alaykum, mening ismim {ism_sharif}")
# print("Men", ism_sharif, manzil, "shahrida istiqomat qilaman.")
# print(f"Salom, mening ismim {ism} {familiya}. Men {manzil} shahrida istiqomat qilaman.")



# Maxsus belgilar   \t,  \n
# print("Assalomu alaykum!")
# print('Assalomu \talaykum!')
# print("Assalomu \nalaykum!")



# pythonning bir necha methodlari     .upper(), .lower(), .title(), .capitalize().
ism = 'jakhongir'
sharif = 'tuychiev'
ism_sharif = f"{ism} {sharif}"
ism_sharif = ism_sharif.upper()
# print(ism_sharif.upper())
# print(ism_sharif.lower())
# print(ism_sharif.title())
# print(ism_sharif.capitalize())



# pythonning     .strip(), .lstrip(), .rstrip()  methodlari
hello = '     salom       '
# print(hello.lstrip())
# print(hello.rstrip())
# print(hello.strip() + " do'stlar")



# INPUT funksiyasi. Input foydalanuvchidan ma'lumot so'rash uchun funksiya. 
ism = input("Ismingiz nima?\n>>>")
print("Assalomu alaykum, " + ism.title(),)
print("Xush kelibsiz!")