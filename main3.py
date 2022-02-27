def reliability(password):
    if (len(password) >= 8 and \
            any(i.islower() for i in password) and \
            any(i.upper() for i in password) and \
            any(i.isdigit() for i in password)):
        return True
    else:
        return False

userpassword = input('Введите пароль')
answer = reliability(userpassword)
if answer == True:
    print("Ваш пароль надежный")
else:
    print("Ваш пароль ненадежный")