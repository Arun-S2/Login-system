def id(email):
    condition = 0
    i1 = 0
    i2 = 0

    for x in email:
        if x == "@":
            i1 = email.index(x)
        elif x == ".":
            i2 = email.index(x)
    if i1 != 0 or i2 != 0:
        condition += 1
    if i2 > (i1 + 1):
        condition += 1
    else:
        condition += 0

    import string
    low = [x for x in string.ascii_lowercase]

    if email[0] in low:
        condition += 1

    if condition == 3:
        return True
    else:
        return False


def pas(password):
    condition = 0

    if len(password) > 5 and len(password) < 16:
        condition += 1

    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in password:
        if x in num:
            condition += 1
            break

    import string
    upper = [x for x in string.ascii_uppercase]
    for x in password:
        if x in upper:
            condition += 1
            break

    lower = [x for x in string.ascii_lowercase]
    for x in password:
        if x in lower:
            condition += 1
            break

    for x in password:
        if x not in num:
            if x not in upper:
                if x not in lower:
                    condition += 1
                    break

    if condition == 5:
        return True
    else:
        return False


def register():
    print('Register process')
    email = input('Create your username (E-mail ID):')
    if not id(email):
        print('Enter a valid E-mail ID!')
        register()
    elif email in d:
        print('Email ID already exist,Enter a new email ID')
        register()
    else:
        password = input('Create your password :')
        if pas(password):
            d.append(email)
            f.append(password)
            print('registered successfully!')
            update()
            return True

        elif not pas(password):
            print('Enter a valid password :')
            register()


def login():
    print('Login process')
    username = input('Enter your username :')
    if username in d:
        password = input('Enter your password :')
        ind = d.index(username)
        if password == f[ind]:
            print('login success')
            print(f'Hi ,{username}, Welcome to Guvi! ')
        else:
            print('Incorrect password!')
            reset()
    else:
        print("username doesn't exist!")
        basic()


db = open('login_details.txt', 'r')
d = []
f = []
for i in db:
    a, b = i.split(',')
    b = b.strip()
    d.append(a)
    f.append(b)

def reset():
    x = input('Login | Forgotpassword :')
    if x == 'Forgotpassword':
        username = input('Enter your username :')
        if username in d:
            password = input('Enter your password :')
            ind = d.index(username)
            if pas(password) == True:
                f[ind] = password
                update()
                print('Your password changed successfully')
            else:
                print('Invalid password!!!')
                reset()
        else:
            print("Invalid username!")
            reset()
    elif x == 'Login':
        login()
    else:
        print('Invalid input!!!')
        reset()

def update():
    db = open('login_details.txt', 'w')
    for x in range(len(d)):
        db.write(d[x] + ',' + f[x] + '\n')


def basic():
    initial = input('Register | Login :')

    if initial == "Register":
        if register() == True:
            basic()

    elif initial == "Login":
        login()

    else:
        print('Enter a valid input!')
        basic()


basic()

