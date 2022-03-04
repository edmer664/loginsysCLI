auth_user = ""
auth_date = ""
auth_name = ""


def logout():
    global auth_user
    global auth_name
    global auth_date
    auth_date = ""
    auth_name = ""
    auth_user = ""
    print("Successfully LogOut.")


def login(user, password):
    with open('userCredentials.txt', 'r') as f:
        for line in f:
            if line.split(';')[0] == user and line.split(';')[1] == password:
                global auth_name
                auth_name = line.split(';')[2] + " " + line.split(';')[3]
                global auth_user
                auth_user = line.split(';')[0]
                global auth_date
                auth_date = line.split(';')[4]
                print(f"Welcome, {auth_name}!")
                return True
    return False


def retrieve_user():
    return {
        'username': auth_user,
        'name': auth_name,
        'date': auth_date,
    }
