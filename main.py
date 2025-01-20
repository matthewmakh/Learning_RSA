from Crypto.Util.number import getPrime

def EA(num1, num2):
    if num2 > num1:
        num1, num2 = num2, num1
    while True:
        if num1%num2==0:
            return num2
        elif num1%num2==1:
            return 1


        remainder = num1%num2
        num1 = num2
        num2 = remainder

        #print(f'{num1} mod {num2} = {num1%num2}')

def EEA(num1,num2):
    #extended euclidean algo
    if num2 == 0:
        return num1, 1, 0
    gcd, x1, y1 = EEA(num2, num1 % num2)
    x = y1
    y = x1 - (num1 // num2) * y1
    return gcd, x, y

def mod_inverse(e, r):
    gcd, x, _ = EEA(e, r)
    if gcd != 1:
        raise ValueError("e and r must be coprime to calculate modular inverse.")
    return x % r

def OPhi(num):
    count = 0
    for i in range(1,num):
        if EA(num, i) == 1:
            count+=1

    return count

'''def mod_inverse(e, r):
    if EA(e, r) == 1:
        return((e ** (OPhi(r) - 1) % r))
    else:
        print("Cannot calculate mod inverse")'''


def RSA_encrypt(m,e,n):
    #return (m**e) % n
    # changed to this for efficiency
    return pow(m,e,n)

def RSA_decrypt(c,d,n):
    #return((c**d) %n)
    # changed to this for efficiency
    return pow(c,d,n)


p = getPrime(2048)
q = getPrime(2048)
e = 65537
n = p*q
r = (p-1)*(q-1)
d = mod_inverse(e,r)

message = getPrime(128)

print(RSA_encrypt(message,e,n))
print(RSA_decrypt(RSA_encrypt(message,e,n),d,n))