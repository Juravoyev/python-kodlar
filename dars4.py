"""
2.2 SHART OPERATORLARI. BOSHLANG'ICH BOSQICH. 
"""
import math

# 1 - misol
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# qush_kvadrat = (number1 + number2) ** 2
# kvadrat_qush = number1 ** 2 + number2 ** 2
# if qush_kvadrat > kvadrat_qush:
#     print(f"Qushmasining kvadrati katta. {qush_kvadrat} > {kvadrat_qush}")
# else:
#     print(f"Kvadratlarining qushmasi katta. {kvadrat_qush} > {qush_kvadrat}") 

# 2 - misol
# staj = int(input("Stajni kiriting: "))
# oylik = int(input("Oylik maoshingiz: "))
# if 2 <= staj <= 5:
#     ustama = oylik * 0.02 
# elif 5 < staj <= 10:
#     ustama = oylik * 0.05
# print(f"Umumiy oylik: {oylik + ustama}. Ustama: {ustama}.")

# 3 - misol
# x0 = int(input("x0: "))
# y0 = int(input("y0: "))
# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# A = math.sqrt(pow(x0,2) + pow(y0,2))
# B = math.sqrt(pow(x1,2) + pow(y1,2))
# if A > B:
#     print(f"A({x0},{y0}) nuqta uzoqda joylashgan.")
# elif A == B:
#     print(f"A({x0},{y0}) va B({x1},{y1}) nuqta bir xil uzoqlikda joylashgan.")
# else:
#     print(f"B({x1},{y1}) nuqta uzoqda joylashgan.")

# 4 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a + b > c and a + c > b and b + c > a: 
#     if pow(a,2) + pow(b,2) == pow(c,2) or pow(b,2) + pow(c,2) == pow(a,2) or pow(a,2) + pow(c,2) == pow(b,2):
#         print(f"{a},{b},{c} tomonli to'g'ri burchakli uchburchak.")
#     else:
#         print("To'g'ri burchakli uchburchak emas.")
# else:
#     print("Bunaqa uchburchak mavjud emas.")
# 5- misol
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a > 0:
#     a *= a
# if b > 0:
#     b *= b
# if c > 0:
#     c *= c
# print(a,b,c)

# 6- misol
# x0 = int(input("x0: "))
# y0 = int(input("y0: "))
# if x0 > 0 and y0 > 0:
#     print(f"A({x0},{y0}) nuqta 1 chorakda yotadi.")
# elif x0 > 0 and y0 < 0:
#     print(f"A({x0},{y0}) nuqta 4 chorakda yotadi.")
# elif x0 < 0 and y0 > 0:
#     print(f"A({x0},{y0}) nuqta 2 chorakda yotadi.")
# elif x0 < 0 and y0 < 0:
#     print(f"A({x0},{y0}) nuqta 3 chorakda yotadi.")
# else:
#     print("A(0,0) kordinata boshi")

# 7 - misol
# a1 = int(input("a1 = "))
# b1 = int(input("b1 = "))
# c1 = int(input("c1 = "))
# a2 = int(input("a2 = "))
# b2 = int(input("b2 = "))
# c2 = int(input("c2 = "))
# if (a1 + b1 > c1 and a1 + c1 > b1 and b1 + c1 > a1) and (a2 + b2 > c2 and a2 + c2 > b2 and b2 + c2 > a2):
#     p1 = (a1 + b1 + c1) / 2
#     p2 = (a2 + b2 + c2) / 2
#     s1 = math.sqrt(p1 * (p1 - a1) * (p1 - b1) * (p1 - c1))
#     s2 = math.sqrt(p2 * (p2 - a2) * (p2 - b2) * (p2 - c2))
#     if s1 > s2:
#         print(f"{a1},{b1},{c1} tomonli uchburchak yuzasi katta. S = {s1}")
#     else:
#         print(f"{a2},{b2},{c2} tomonli uchburchak yuzasi katta. S = {s2}")
# else:
#     print("Mavjud bo'lmagan uchburchakni kiritdingiz.")


# 8 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a > 0:
#     a = pow(a,3)
# else:
#     a = 0
# if b > 0:
#     b = pow(b,3)
# else:
#     b = 0
# if c > 0:
#     c = pow(c,3)
# else:
#     c = 0
# print(a,b,c)

# 9 - misol
# n = int(input("n = "))
# if n % 10 == 0:
#     print("Ha")
# else:
#     print("Yo'q")

# 10 - misol
# x = int(input("x = "))
# y = int(input("y = "))
# if x > 0 and y > 0:
#     print("Ha 1 chorakda yotadi.")
# else:
#     print("Yuq 1 chorakda yotmaydi.")

# 11 - misol
# summa = int(input("Kredit summasi: "))
# muddat = int(input("Nechchi yilga(0.5/1): "))
# if muddat == 0.5:
#     yillik = summa * 1.06
# elif muddat == 1:
#     yillik = summa * 1.08
# print(f"{yillik / 12} so'mdan oyiga buladi.")

# 12 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# kvadrat_ayir = abs(a ** 2 - b ** 2)
# ayir_kvadrat = (a - b) ** 2
# if kvadrat_ayir > ayir_kvadrat:
#     print(f"Kvadratlarining ayirmasi katta. {kvadrat_ayir} > {ayir_kvadrat}")
# else:
#     print(f"Ayirmasining kvadrati katta. {ayir_kvadrat} > {kvadrat_ayir}")

# 13 - misol
# x0 = int(input("x0: "))
# y0 = int(input("y0: "))
# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# A = math.sqrt(pow(x0,2) + pow(y0,2))
# B = math.sqrt(pow(x1,2) + pow(y1,2))
# if A > B:
#     print(f"B({x1},{y1}) nuqta yaqinda joylashgan.")
# elif A == B:
#     print(f"A({x0},{y0}) va B({x1},{y1}) nuqta bir xil uzoqlikda joylashgan.")
# else:
#     print(f"A({x0},{y0}) nuqta yaqinda joylashgan.")

# 14 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a + b > c and a + c > b and b + c > a: 
#     if  a == b == c:
#         print(f"{a},{b},{c} teng tomonli uchburchak.")
#     else:
#         print("Teng tomonli uchburchak emas.")
# else:
#     print("Bunaqa uchburchak mavjud emas.")

# 15 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if pow(a,2) + pow(b,2) == pow(c,2) or pow(b,2) + pow(c,2) == pow(a,2) or pow(a,2) + pow(c,2) == pow(b,2):
#     print(f"{a},{b},{c} sonlari Pifagor uchligini tashkil qila oladi")
# else:
#     print(f"{a},{b},{c} sonlar Pifagor uchligini tashkil qila olmaydi")

# 16 - misol
# doira_yuzi = math.pi * 25
# kvadrat_yuzi = 100
# r = math.sqrt(doira_yuzi / math.pi)
# a = math.sqrt(kvadrat_yuzi)
# if r == (a / 2):
#     print("Doira kvadrat ichga chizilgan bo'la oladi.")
# elif r == (math.sqrt(2) * a) / 2:
#     print("Doira kvadratga tashqi chizilgan.")
# else:
#     print("Doira va kvadart kesishmaydi.")

# 17 - misol
# time = float(input("Joriy vaqtni kiriting(0/23): "))
# if time < 12:
#     print(f"{time} am.")
# elif time >= 12 and time < 24:
#     print(f"{time} pm.")
# else:
#     print("Xato vaqt.")

# 18 - misol
# n = int(input("Son: "))
# if n % 2 == 0 or n % 10 == 7:
#     print("Bu son juft yoki 7 bilan tugaydi.")
# else:
#     print("Juft ham emas 7 bilan ham tugamaydi.")


"""
O`rta bosqich
"""

# 1 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# N = (abs(a) + abs(b)) / 2
# M = math.sqrt(abs(a) * abs(b))
# print(N , M)


# 2 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a + b > c and a + c > b and b + c > a: 
#     if  a == b or b == c or a == c:
#         print(f"{a},{b},{c} teng yonli uchburchak.")
#     else:
#         print("Teng yonli uchburchak emas.")
# else:
#     print("Bunaqa uchburchak mavjud emas.")


# 3 - misol
# year = int(input("Yilni kiriting(eramizdan avvalgi yillar - bilan(-2000/2000)):\n"))
# if year < 0:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(f"Eramizdan avvalgi {year} kabisa yili.")
#     else:
#         print(f"Eramizdan avvalgi {year} yil.")
# elif year == 0:
#     print("0")
# else:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(f"Eramizdagi {year} kabisa yili.")
#     else:
#         print(f"Eramizdagi {year} yil.")

# 4 - misol
# price = int(input("Price: "))
# if price > 100_000:
#     print(f"{price} 10% chegirma bilan:{price * 0.9}.")
# else:
#     print(f"{price} narx")

# 5 - misol
# height = float(input("Bo'yingizni kiriting: "))
# weight = float(input("Vazningizni kiriting: "))
# k = height % 100
# if k - 10 <= weight <= k + 10:
#     print("Siz ideal vaznga egasiz.")
# elif weight < k - 10:
#     print("Siz ozg'inroqsiz.")
# elif weight > k + 10:
#     print("Siz semizroqsi.")

# 6 - misol
# question = input("Pyhonni kim yaratgan?\nA) Ilon Mask\nB) Guido van Rossum\nC) Pavel Durov\n>>>")
# if question == 'B':
#     print("To'g'ri javob")
# else:
#     print("Xato!")

# 7 - misol
# price = int(input("Price: "))
# if price > 500:
#     price = 0.95 * price
# if price > 1000:
#     price = 0.9 * price
# print(price)

# 8 - misol
# mounth = int(input("Son kiriting(1,12): "))
# if mounth == 1:
#     print("Yanvar")
# elif mounth == 2:
#     print("Fevral")
# elif mounth == 3:
#     print("Mart")
# elif mounth == 4:
#     print("Aprel")
# elif mounth == 5:
#     print("May")
# elif mounth == 6:
#     print("Iyun")
# elif mounth == 7:
#     print("Iyul")
# elif mounth == 8:
#     print("Avgust")
# elif mounth == 9:
#     print("Sentabr")
# elif mounth == 10:
#     print("Oktabr")
# elif mounth == 11:
#     print("Noyabr")
# elif mounth == 12:
#     print("Dekabr")
# else:
#     print("Xato!")


# 9 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a < b < c:
#     print(f"O'rtacha: {b}")
# elif c < b < a:
#     print(f"O'rtacha {b}")
# elif b < a < c:
#     print(f"O'rtacha {a}")
# elif c < a < b:
#     print(f"O'rtacha {a}")
# elif b < c < a:
#     print(f"O'rtacha {c}")
# elif a < c < b:
#     print(f"O'rtacha {c}")
# else:
#     print("O'ratacha yagona son yo'q.")

# 10 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a < b and a < c:
#     print(f"{a} kichik son.")
# elif b < a and b < c:
#     print(f"{b} kichik son.")
# elif c < a and c < b:
#     print(f"{c} kichik son.")
# else:
#     print("Yagona kichik son yuq.")

# 11 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a + b > c and a + c > b and b + c > a: 
#     if pow(a,2) + pow(b,2) == pow(c,2) or pow(b,2) + pow(c,2) == pow(a,2) or pow(a,2) + pow(c,2) == pow(b,2):
#         print(f"{a},{b},{c} tomonli to'g'ri burchakli uchburchak.")
#     else:
#         print("To'g'ri burchakli uchburchak emas.")
# else:
#     print("Bunaqa uchburchak mavjud emas.")

# 12 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# if a > b:
#     if a % b == 0:
#         print(f"Ha {b} {a} ni bo'luvchisi bo'la oladi.")
#     else:
#         print("Yo'q")
# elif a == b:
#     print("Bu sonlar teng")
# else:
#     if b % a == 0:
#         print(f"Ha {a} {b} ni bo'luvchisi bo'la oladi.")
#     else:
#         print("Yo'q")

# 13 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# Na = (a + b + c) / 3
# if abs(a) > Na and abs(b) > Na and abs(c) > Na:
#     print("Sonlarning moduli katta")
# else:
#     print("Modullari katta emas")

# 14 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a == b and b == c:
#     print("Hammasi teng")
# elif a >= b and a >= c:
#     print(f"{a} katta son")
# elif b >= a and b >= c:
#     print(f"{b} katta son")
# elif c >= a and c >= b:
#     print(f"{c} katta son")

# 15 - misol
# a = int(input("Sonni kiriting: "))
# yuz = (a // 100) % 10
# print(f"Yuzlik xonasi:{yuz}")

# 16 - misol
# x = float(input("x = "))
# if x <= 0:
#     x = -x
# elif 0 < x < 2:
#     x = x ** 2
# else:
#     x = 4
# print(x)


"""
Yuqori bosqich
"""
# 1 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# D = b ** 2 - 4 * a * c
# if D > 0:
#     x1 = (- b - math.sqrt(D)) / (2 * a)
#     x2 = (- b + math.sqrt(D)) / (2 * a)
#     print(f"x1 = {x1}, x2 = {x2}")
# elif D == 0:
#     x = (- b) / (2 * a)
#     print(f"x = {x}")
# else:
#     print("Yechim mavjud emas!")


# 2 - misol
# ikki_xonali = int(input("Ikki xonali son kiriting: "))
# a = int(input("Qidirgan raqam: "))
# if ikki_xonali % 10 == 5 or ikki_xonali // 10 == 5:
#     print("5 raqami bor")
# else:
#     print("5 raqami yuq")
# if ikki_xonali % 10 == a or ikki_xonali // 10 == a:
#     print(f"{a} raqami bor.")
# else:
#     print(f"{a} raqami yuq")

# 3 - misol
# ikki_xonali = int(input("son = "))
# if (ikki_xonali % 10 == 3 or ikki_xonali // 10 == 3) and (ikki_xonali % 10 == 7 or ikki_xonali // 10 == 7):
#     print("3 va 7 raqami bor")
# else:
#     print("3 va 7 raqami yuq")
# if (ikki_xonali % 10 == 4 or ikki_xonali // 10 == 4) and (ikki_xonali % 10 == 8 or ikki_xonali // 10 == 8) or (ikki_xonali % 10 == 9 or ikki_xonali // 10 == 9):
#     print("4 va 8 bor yoki 9")
# else:
#     print("4 8 9 lar ishtirok etmagan")

# 4 - misol
# palindrom = int(input("4 xonali son kiriting: "))
# a = palindrom // 1000
# b = (palindrom // 100) % 10
# c = (palindrom // 10) % 10
# d = palindrom % 10
# if a == d and b == c:
#     print("Palindrom son.")
# else:
#     print("Palindrom emas.")

# 5 - misol
# son = int(input("6 xonali son kiriting: "))
# a = son // 100_000
# b = (son // 10_000) % 10
# c = (son // 1000) % 10
# d = (son // 100) % 10
# e = (son // 10) % 10
# f = son % 10
# if a + b + c == d + e + f:
#     print("Omadli son.")
# else:
#     print("Omadli son emas.")

# 6 - misol
# def get_day(x):
#     if x == 0:
#         return "Yakshanba"
#     elif x == 1:
#         return "Dushanba"
#     elif x == 2:
#         return "Seshanba"
#     elif x == 3:
#         return "Chorshanba"
#     elif x == 4:
#         return "Payshanba"
#     elif x == 5:
#         return "Juma"
#     elif x == 6:
#         return "Shanba"
# day = int(input("(1 - 365) oraliqdan son tanlang: "))
# if 0 < day <= 31 and 0 <= day % 7 <= 6:
#     print(f"{day} - yanvar - {get_day(day % 7)}")
# elif day <= 59 and 0 <= day % 7 <= 6:
#     print(f"{day} - fevral - {get_day(day % 7)}")
# elif day <= 90 and 0 <= day % 7 <= 6:
#     print(f"{day} - mart - {get_day(day % 7)}")
# elif day <= 120 and 0 <= day % 7 <= 6:
#     print(f"{day} - aprel - {get_day(day % 7)}")
# elif day <= 151 and 0 <= day % 7 <= 6:
#     print(f"{day} - may - {get_day(day % 7)}")
# elif day <= 182 and 0 <= day % 7 <= 6:
#     print(f"{day} - iyun - {get_day(day % 7)}")
# elif day <= 213 and 0 <= day % 7 <= 6:
#     print(f"{day} - iyul - {get_day(day % 7)}")
# elif day <= 243 and 0 <= day % 7 <= 6:
#     print(f"{day} - avgust - {get_day(day % 7)}")
# elif day <= 274 and 0 <= day % 7 <= 6:
#     print(f"{day} - sentabr - {get_day(day % 7)}")
# elif day <= 304 and 0 <= day % 7 <= 6:
#     print(f"{day} - oktabr - {get_day(day % 7)}")
# elif day <= 334 and 0 <= day % 7 <= 6:
#     print(f"{day} - noyabr -{get_day(day % 7)}")
# elif day <= 365 and 0 <= day % 7 <= 6:
#     print(f"{day} - dekabr - {get_day(day % 7)}")
# else:
#     print("Xato!")

# 7 - misol
# son = int(input("Sonni kiriting: "))
# a = son // 100
# b = (son // 10) % 10
# c = son % 10
# if a + b + c >= 10:
#     print("Raqamlari yig'indisi 2 xonali son bo'la oladi.")
# else:
#     print("2 xonali son bo'la olmaydi.")
# if a * b * c >= 1000:
#     print("Raqamlari kupaytmasi 4 xonali son bo'la oladi.")
# else:
#     print("Raqamlari kupaytmasi 4 xonali son bo'la olmaydi.")

# 8 - misol
# son = int(input("4 xonali son kiriting: "))
# b = int(input("b sonni kiriting: "))
# a = son // 1000
# b1 = (son // 100) % 10
# c = (son // 10) % 10
# d = son % 10
# if a * b1 * c * d > b:
#     print("Raqamlari kupaytmasi b dan katta.")
# else:
#     print("Katta emas b dan")
# if (a + b1 + c + d) % 3 == 0:
#     print("Ha 3 ga karrali")
# else:
#     print("Yuq karrali emas.")

# 9 - misol
# son = int(input("3 xonali son kiriting: "))
# a = son // 100
# b = (son // 10) % 10
# c = son % 10
# if a == b == c:
#     print("Barcha raqamlari teng")
# elif a == b or b == c or a == c:
#     print("Ha orasida raqamlari bir xillari bor.")
# else:
#     print("Hammasi har xil.")

# 10 - misol
# son = int(input("4 xonali son kiriting: "))
# a = son // 1000
# b = (son // 100) % 10
# c = (son // 10) % 10
# d = son % 10
# if (a + b) == (c + d):
#     print("Teng")
# else:
#     print("Teng emas")
# if (a + b + c + d) % 7 == 0:
#     print("7 ga karrali")
# else:
#     print("7 ga karrali emas")

# 11 - misol
# son = int(input("4 xonali son kiriting: "))
# a1 = int(input("a = "))
# a = son // 1000
# b = (son // 100) % 10
# c = (son // 10) % 10
# d = son % 10
# if (a * b * c * d) % a == 0:
#     print(f"{a1} ga karrali")
# else:
#     print(f"{a1} ga karrali emas")
# if (a * b * c * d) % 3 == 0:
#     print("3 ga karrali")
# else:
#     print("3 ga karrali emas")



