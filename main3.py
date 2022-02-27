def reliability(password):
    if (len(password) >= 8 and \
            any(i.islower() for i in password) and \
            any(i.isupper() for i in password) and \
            any(i.isdigit() for i in password)):
        return True
    else:
        return False

userpassword = input('Введите пароль')

if reliability(userpassword):
    print("Ваш пароль надежный.")
else:
    print("Ваш пароль ненадежный.")
