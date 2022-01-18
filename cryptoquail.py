# CryptoQuail Block Cipher
from itertools import cycle
import math

def rail_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])
def encode(plaintext, rails):
    p = rail_pattern(rails)
    return ''.join(sorted(plaintext, key=lambda i: next(p)))
def decode(ciphertext, rails):
    p = rail_pattern(rails)
    indexes = sorted(range(len(ciphertext)), key=lambda i: next(p))
    result = [''] * len(ciphertext)
    for i, c in zip(indexes, ciphertext):
        result[i] = c
    return ''.join(result)
######

def text2number(string__, x):
    return (int.from_bytes(string__.encode(), "little") % x) + 2

def modEncrypt(msg, key):
    return "".join([chr((ord(msg[i]) + ord(key[i % len(key)])) %  256) for i in range(len(msg))])
def modDecrypt(cip, key):
    return "".join([chr((ord(cip[i]) + (256 - ord(key[i % len(key)]))) % 256)for i in range(len(cip))])


######

def xor(s, k):
    return "".join([chr(ord(f) ^ ord(k[i%len(k)])) for i, f in enumerate(s)])

######

def split(seq):
    n = 12 # block length is 12
    datas = []
    while seq:
        datas.append(seq[:n])
        seq = seq[n:]
    return datas

def pad(e):
    if len(e) == 12: return e
    else:
        return e + (chr(0) * (12 - len(e))) 
######

def encrypt(string, key):
    string = chr(len(string)) + string
    string = modEncrypt(string, key)
    ciphertext = ""
    odometer = [1, 2, 3, 4]
    blocks = split(string)
    key1 = key[12:24]
    key = key[:12]
    for block in blocks:
        block = pad(block)
        if odometer[0] == 1:
            for i in range(4): 
                block = modEncrypt(block, key)
                block = xor(block, key)
        elif odometer[1] == 1:
            for i in range(3):
                block = xor(block, key)
                block = modEncrypt(block, key)
        elif odometer[2] == 1:
            for i in range(2):
                block = xor(block, key1)
                block = modEncrypt(block, key1)
        elif odometer[3] == 1:
            block = modEncrypt(block, key1)
            block = xor(block, key1)
        odometer = odometer[1:] + [odometer[0]]
        ciphertext = ciphertext + block
    ciphertext = encode(ciphertext, text2number(key, 12))
    return xor(ciphertext, chr(text2number(key1, 127)) + chr(text2number(key, 127)))

def decrypt(cipher, key):
    string = ""
    odometer = [1, 2, 3, 4]
    key1 = key[12:24]
    key = key[:12]
    cipher = xor(cipher, chr(text2number(key1, 127)) + chr(text2number(key, 127)))
    cipher = decode(cipher, text2number(key, 12))
    blocks = split(cipher)
    for block in blocks:
        if odometer[1] == 1:
            for i in range(3):
                block = modDecrypt(block, key)
                block = xor(block, key)
        elif odometer[0] == 1:
            for i in range(4):
                block = xor(block, key)
                block = modDecrypt(block, key)
        elif odometer[3] == 1:
            block = xor(block, key1)
            block = modDecrypt(block, key1)
        elif odometer[2] == 1:
            for i in range(2):
                block = modDecrypt(block, key1)
                block = xor(block, key1)
        odometer = odometer[1:] + [odometer[0]]
        string = string + block
    final = list(modDecrypt(string, key + key1).rstrip())
    char = ord(final.pop(0))
    return "".join(final[:char])
if __name__ == "__main__":
    a = encrypt("The quick brown fox jumped over the lazy dogs.", "abcdefghijkl12345678!@#$")
    print(a)
    b = decrypt(a, "abcdefghijkl12345678!@#$")
    print(b)
