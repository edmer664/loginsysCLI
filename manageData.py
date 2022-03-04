from myLogin import retrieve_user
import os

current_user = retrieve_user()


def retrieve():
    try:
        f_list = open('./friends/' + current_user['username']+'.txt', 'r')
        return f_list.readlines()
    except:
        pass


def add():
    try:
        f_list = open('./friends/' + current_user['username']+'.txt', 'a')
        f_list.write(input('Enter friend\'s username: ')+'\n')
    except:
        pass


def delete():
    try:
        f_list = open('./friends/' + current_user['username']+'.txt', 'r')
        f_list = f_list.readlines()
        print(f_list)
        f_list.remove(input('Enter friend\'s username: ')+'\n')
        f_list = open('./friends/' + current_user['username']+'.txt', 'w')
        f_list.write(f_list)
    except:
        pass
