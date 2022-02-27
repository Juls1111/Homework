import random
import secrets

def password():
    m = []
    for i in range(33, 127):
        m.append(chr(i))
    s = random.randint(7, 10)
    password1 = ''
    for j in range(s):
        password1 += secrets.choice(m)
    return password1

def reliability(password):
    if (len(password) >= 8 and \
            any(i.islower() for i in password) and \
            any(i.isupper() for i in password) and \
            any(i.isdigit() for i in password)):
        return True
    else:
        return False

def reliablepassword():
    k=1
    while True:
        p=password()
        if (reliability(p)):
            print("Ваш надежный пароль ", p + ' был сгенерирован с попытки № ', k)
            break
        else:
            k=k+1

print(reliablepassword())
