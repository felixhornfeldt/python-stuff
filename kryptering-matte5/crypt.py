letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö"]

def encrypt(msg, c, n):
    msg_arr = [letters.index(i) for i in msg]
    # print(msg_arr)
    crypt_msg = []
    for i in msg_arr:
        crypt_msg.append(i**c % n - 1)
    return crypt_msg
    

def decrypt(msg, d, n):
    decrypt_msg = []
    for i in msg:
        # decrypt_msg.append(letters[i**d % n - 1])
        print(i**d % n - 1)
    return decrypt_msg

# a = encrypt("LÅDANIENBILGÅRRUNTOCHRUNT", 7, 33)
# print(a)
# b = decrypt(a, 3, 33)
# print(b)
# print(decrypt([60,42,207,207,19],77,221))

import random as rm

def bank():
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,1291,1297,1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,1709,1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,1811,1823,1831,1847,1861,1867,1871,1873,1877,1879]
    p = rm.choice(primes)
    q = rm.choice(primes)
    n = p*q
    t = (p-1)*(q-1)
    c = rm.choice(primes)
    # c*d `kongurent` 1 % n
    i = 1
    while True:
        d = i
        if c*d % t == 1:
            break
        # print(d)
        i += 1
        pass

    return [c,d,n]

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö"]

def computer(msg, c, n):
    msg_arr = [letters.index(i) for i in msg]
    # print(msg_arr)
    crypt_msg = []
    for i in msg_arr:
        crypt_msg.append(i**c % n + 1)
    return crypt_msg

import time

t1 = time.clock()
bank_keys = bank()
t2 = time.clock()
print(str(t2-t1)+" s")

t1 = time.clock()
crypt = computer("NAJS", bank_keys[0], bank_keys[2])
print(crypt)
t2 = time.clock()
print(str(t2-t1)+" s")

t1 = time.clock()
print(decrypt(crypt, bank_keys[1],bank_keys[2]))
t2 = time.clock()
print(str(t2-t1)+" s")