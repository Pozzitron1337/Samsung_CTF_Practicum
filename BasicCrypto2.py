import math

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

p=1680613444652105838344133706142211604381500993652031705380909307238347587888162431490921255465344239
q=2143532995881162829855694296384103840144300960388531553947710050014176459461784664429637761367242287
c=1921902980210977295270519710634709719343372281625129194637780159651252905527903923450045434239794433327822136581724693103107581315471305119544244907185643235873825200596556268483571243342863955690176
e=65537
fn=(p-1)*(q-1)
e_inv=modinv(e,fn)
print("e inverse : ",e_inv)
d=e_inv%fn
print("Euler function(p*q) : ",fn)
print("d :",d)
m=GornerShemePower(c,d,p*q)
hex_m=hex(m).split('x')[-1]
print("Hex is : ",hex_m)
flag=bytes.fromhex(hex_m).decode('ASCII')
print(flag)

