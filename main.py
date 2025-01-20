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
def OPhi(num):
    count = 0
    for i in range(1,num):
        if EA(num, i) == 1:
            count+=1

    return count

def mod_inverse(e, r):
    if EA(e, r) == 1:
        return((e ** (OPhi(r) - 1) % r))
    else:
        print("Cannot calculate mod inverse")

def RSA_encrypt(m,e,n):
    return (m**e) % n

def RSA_decrypt(c,d,n):
    return((c**d) %n)


p = 11
q = 3
n = p*q
r = (p-1)*(q-1)
e = 3
d = mod_inverse(e,r)

print(RSA_encrypt(7,e,n))
print(RSA_decrypt(RSA_encrypt(7,e,n),d,n))