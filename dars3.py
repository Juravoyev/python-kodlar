"""
2.1 Mantiqiy ammallar. BOSHLANG`ICH BOSQICH
"""
# 4 - misol
# A = int(input("A: "))
# x = A % 6 == 0
# print(x)

# 5 - misol
# A = int(input("A: "))
# x = A % 2 == 1
# print(x)

# 9 - misol
# a = int(input("a= "))
# d = a // 100
# x = 1 <= d <= 9
# print(x)


# 10 - misol
# a = int(input("a= "))
# b = int(input("b= "))
# c = int(input("c= "))
# x = (a < 45 and b >= 45 and c >= 45) or (a >= 45 and b < 45 and c >= 45) or (a >= 45 and b >= 45 and c < 45)
# print(x)

# 11 - misol
# a = int(input("a= "))
# x = a % 3 == 0 and a % 10 == 0
# print(x)

# 12 - misol
# A = int(input("A = "))
# x = -137 < A < -51 or 55 < A < 123
# print(x)

# 13 - misol
# X = int(input("X = "))
# Y = int(input("Y = "))
# Z = int(input("Z = "))
# x = (X % 5 == 0 and Y % 5 != 0 and Z % 5 != 0) or (X % 5 != 0 and Y % 5 == 0 and Z % 5 != 0) or (X % 5 != 0 and Y % 5 != 0 and Z % 5 == 0)
# print(x)

# 14 - misol
# X = int(input("X = "))
# Y = int(input("Y = "))
# Z = int(input("Z = "))
# x = (X > 80 and Y <= 80 and Z <= 80) or (X <= 80 and Y > 80 and Z <= 80) or (X <= 80 and Y <= 80 and Z > 80)
# print(x)

# 15 - misol
# A = int(input("A = "))
# x = not(-10 <= A <= -2 or 2 <= A <= 15)
# print(x)

# 16 - misol
# A = int(input("A = "))
# x = 1 <= A // 1000 <= 9 and A != 4999
# print(x)

# 17 - misol
# A = int(input("A = "))
# x = A % 3 == 0 and A % 2 == 0
# print(x)

# 18 - misol
# A = int(input("A = "))
# B = int(input("B = "))
# x = A % 2 == 0 and B % 2 == 0
# print(x)

# 19 - misol
# A = int(input("A = "))
# B = int(input("B = "))
# C = int(input("C = "))
# x = (A % 2 == 1 and B % 2 == 0 and C % 2 == 0) or (A % 2 == 0 and B % 2 == 1 and C % 2 == 0) or (A % 2 == 0 and B % 2 == 0 and C % 2 == 1)
# print(x)

# 20 - misol
# A = int(input("A = "))
# x = A % 3 == 0 and A % 4 != 0
# print(x)


"""
O`RTA BOSQICH
"""
# 1 - misol
# A = int(input("A = "))
# B = int(input("B = "))
# C = int(input("C = "))
# x = A % 3 == 0 and B % 3 == 0 and C % 3 == 0
# print(x)

# 2 - misol
# A = int(input("A = "))
# x = A % 4 == 0 or A % 7 == 0
# print(x)

# A = int(input("A = "))
# x = A % 5 == 0 and A % 10 != 0
# print(x) 

# 3 - misol
# n = int(input("n = "))
# m = int(input("m = "))
# k = int(input("k = "))
# l = int(input("l = "))
# x = n + m > k and n > k and m < l
# print(x)

# 4 - misol
# N = int(input("N = "))
# x = (N % 3 == 0 and N % 9 != 0) or (N % 4 == 0 and N % 5 == 0 and N % 24 == 0)
# print(x)

# 6 - misol
# deposit = int(input("Depozit = "))
# omonat = 1.2 * (deposit * (deposit <= 5000)) or 1.22 * (deposit * (5000 < deposit <= 10000))
# print(omonat)

# 7 - misol
# N = int(input("N = "))
# x = N % 2 == 0 and N % 7 == 0 and N % 11 != 0 and N % 13 != 0
# print(x)

# 8 - misol
# N = int(input("N = "))
# x = N % 3 != 0 and N % 7 == 0 and N % 10 == 0
# print(x)

# 9 -misol
# k = int(input("k = "))
# l = int(input("l = "))
# n = int(input("n = "))
# m = int(input("m = "))
# x = (k == 0 and l > m) or (k < 0 and 2 * l - 3 * n < m)

# 10 - misol
# N = int(input("N = "))
# x = (N % 3 != 0 and N % 7 == 0) or (N % 5 != 0 and N % 4 != 0) or (N % 8 == 0 and N % 11 == 0)
# print(x)

# 11 - misol
# price = int(input("price = "))
# x = 0.95 * (price * (400 <= price < 600)) or 0.9 * (price * (600 <= price < 1000))
# print(x)

# 12 - misol
# k = int(input("k = "))
# l = int(input("l = "))
# m = int(input("m = "))
# n = int(input("n = "))
# x = k + l + m + n > 0 and ((k > 0  and 2 * m > l) or (k < 0 and n > 3 * l))
# print(x)

# 13 - misol
# t = int(input("Suhbat vaqti: "))
# dt = int(input("Suhbat davomiyligi: "))
# s = int(input("Qo'ng'iroq daqiqasining narxi: "))
# d = int(input("Haftaning kuni: "))
# narx = (s * 0.8 * (22 <= t and dt <= 600)) or (s * 0.9 * (6 <= d <= 7))
# print(narx)

# 14 - misol
# X , Y , Z = True , False , True
# x = not (not X and Y) or (X and not Z)
# print(x)

# 15 - misol
# maths = int(input("Maths point: "))
# physics = int(input("Physics point: "))
# it = int(input("IT point: "))
# x = 4 <= maths <= 5 and 4 <= physics <= 5 and 4 <= it <= 5
# print(x)


# 16 - misol
# A = int(input("A = "))
# B = int(input("B = "))
# C = int(input("C = "))
# D = int(input("D = "))
# x = (A % 2 == 0 and B % 2 == 0 and C % 2 != 0 and D % 2 != 0) or (A % 2 == 0 and B % 2 != 0 and C % 2 == 0 and D % 2 != 0) or (A % 2 == 0 and B % 2 != 0 and C % 2 != 0 and D % 2 == 0) or (A % 2 != 0 and B % 2 == 0 and C % 2 == 0 and D % 2 != 0) or (A % 2 != 0 and B % 2 == 0 and C % 2 != 0 and D % 2 == 0) or (A % 2 != 0 and B % 2 != 0 and C % 2 == 0 and D % 2 == 0)
# print(x)

# 17 - misol
# A = int(input("A = "))
# B = int(input("B = "))
# C = int(input("C = "))
# D = int(input("D = "))
# x = (A % 3 == 0 and B % 5 == 0 and C % 5 == 0 and D % 5 == 0) or (A % 5 == 0 and B % 3 == 0 and C % 5 == 0 and D % 5 == 0) or (A % 5 == 0 and B % 5 == 0 and C % 3 == 0 and D % 5 == 0) or (A % 5 == 0 and B % 5 == 0 and C % 5 == 0 and D % 3 == 0)
# print(x)

# 18 - misol
# price = int(input("Price: "))
# x = (0.95 * price * (1000 <= price <= 2000)) or (0.9 * price * (2000 < price <= 5000))
# print(x) 

# 19 - misol
# salary = int(input("Salary: "))
# staj = int(input("Staj: "))
# price = (1.02 * salary * (5 <= staj <= 10)) or (1.1 * salary * (10 < staj <= 20))
# print(price)

# 20 - misol
# X , Y , Z
# X and not (not Y or Z) or Y

# 21 - misol
# staj = int(input("staj: "))
# k = (11 * (staj <= 2)) or (12 * (2 < staj <= 5)) or (13 * (staj > 5))
# print(k)

# 22 - misol
# t = int(input("suhbat vaqti 0 dan 24 soatgacha: "))
# dt = int(input("suhbat davomiyligi daqiqalarda: "))
# s = int(input("qo'ng'iroq daqiqasining narxi: "))
# d = int(input("haftaning kuni 1 dan 7 gacha: "))
# price = (0.9 * dt * s * (t >= 22 and dt <= 600 and 1 <= d < 6)) or (0.85 * dt * s * (t >= 22 and dt < 600 and 6 <= d <= 7))
# print(price)

# 24 - misol
# A , B , C 
# A and not B or not (A or not C)

# 25 - misol
# A = int(input("A = "))
# B = int(input("B = "))
# C = int(input("C = "))
# D = int(input("D = "))
# x = (A % 7 == 0 and B % 2 == 1 and C % 2 == 1 and D % 2 == 1) or (A % 2 == 1 and B % 7 == 0 and C % 2 == 1 and D % 2 == 1) or (A % 2 == 1 and B % 2 == 1 and C % 7 == 0 and D % 2 == 1) or (A % 2 == 1 and B % 2 == 1 and C % 2 == 1 and D % 7 == 0)
# print(x)

# 26 - misol
# N = int(input("N = "))
# x = N % 5 != 0 and N % 6 == 0
# print(x)

# 27 - misol
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# x = a < 0 and b ** 2 - 4 * a * c > 0
# print(x)

# 28 - misol
# uah = int(input("uah = "))
# usd = int(input("usd = "))
# evro = int(input("evro = "))
# x = 1.2 * uah * (uah < 5000)
# y = 1.12 * usd * (usd < 5000)
# z = 1.1 * evro * (evro < 5000)
# print(x , y , z)

# 29 - misol
# A , B , C = True , True , True
# x = not (A and not B) or (A or not C)
# print(x)

# 30 - misol
# A = int(input("A = "))
# B = int(input("B = "))
# C = int(input("C = "))
# D = int(input("D = "))
# x = (A % 5 == 0 and B % 2 == 0 and C % 2 == 0 and D % 2 == 0) or (A % 2 == 0 and B % 5 == 0 and C % 2 == 0 and D % 2 == 0) or (A % 2 == 0 and B % 2 == 0 and C % 5 == 0 and D % 2 == 0) or (A % 2 == 0 and B % 2 == 0 and C % 2 == 0 and D % 5 == 0)
# print(x)

























