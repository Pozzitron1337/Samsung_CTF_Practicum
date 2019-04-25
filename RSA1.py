import math
#NOT SOLVED!
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
#(a**n)%m
def GornerShemePower(a,n,m):
    b=1
    k=int(math.log(n,2)+1)
    r = 2 ** (k)
    for i in range(0,k):
        b=b*b%m
        r=r>>1
        if (n & r):
            b=(b*a)%m
    return b

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

cyphertext='DxeXbit2wwqqOD7w57dC8iTj7oS9Osf+dDdjDtsfGXUbyZcr ES9EUAYPB6KcjqbucUcF9Xa+AyDc1bTLQdr6sfyo2Jw+X6 swej1YJHm2lQ46kNzIMwYPznwVmNtJQZStKMOoVSS8n WUMa5+KT3g21U2e+yqLOlLZBaPo7Z/bIDQ='
e = 16
N = 0x5f750e1b6fea81d8fe21acbcfdde68ae205d033ba1000d5f5564272bf49df1c6a41dc66f9f1ceb2cb749dc76aaab73e752ad0c4f85028403cfb79d004a063ca9042b9561fdddb8214ee2222013fe65e7705e9c146fa9d6bc9e3fd9ec39e0d10a69d2dbc4fca1ece87fe790fbfd9841e77f76971b7a0664e18daddc11b2df2a27
print("modulus: ", N)
phi = N - 1
print("phi: ", phi)
e_inverse = modinv(e+1, phi)
print("e inverse: ", e_inverse)
d =#e_inverse % phi
print("d is:", d)

decimal_cyphertext=''
for letter in cyphertext:
    decimal_cyphertext = decimal_cyphertext+str(ord(letter))

decimal_cyphertext=int(decimal_cyphertext)
print("cyphertext: ", decimal_cyphertext)
message = GornerShemePower(decimal_cyphertext, d, phi)
print("message: ", message)
