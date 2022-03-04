# =================================================================
# Do not modify this code. This will create the userCredentials.txt

import createFile
from myLogin import login, retrieve_user, logout
from manageData import retrieve, add, delete

# createFile.x()
# =================================================================

current_user = {}


def login_prompt():
    user = input("Username: ")
    if user == ("x" or "X"):
        return "x", ""
    password = input("Password: ")
    return user, password


def action_select():
    print(
        """
        1 - View Friend
        2 - Add Friend
        3 - Delete Friend
        X - Exit
        """)
    s = input("Enter your choice: ")
    if s == "1":
        retrieve()
    elif s == "2":
        add()
    elif s == "3":
        delete()
    elif s == "x" or s == "X":
        logout()


# Hey there, start typing your Python code here...


def main():
    username, password = login_prompt()
    while login(username, password) == False:
        if username == "x":
            print("Goodbye!")
            break
        username, password = login_prompt()
    if username != "x":
        global current_user
        current_user = retrieve_user()
        action_select()


if "__main__" == __name__:
    main()

# ================================================================
# Do not delete or edit this part
# The following code will display the list of friends for each
# user from the textfiles created by your code
# print()
# for x in uname:
#     l = open(x+'.txt', 'r')
#     friends = l.read().split()
#     print(f"{x} friend\'s {friends}")
