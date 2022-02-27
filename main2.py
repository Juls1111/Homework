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


print(password())
