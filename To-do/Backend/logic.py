'''
Created on Oct 24, 2020

@author: Linda and Ileen
'''
from user import User
from quest import Quest

def sign_up(username, password, usernames, pokemon, evolutions):
    # checking if username is in usernames
    
    if username not in usernames:
        usernames[username] = User(username, password, pokemon, evolutions)
        return True
    else:
        return False

def login(username, password, usernames):
    # user input for username and password

    if username in usernames:
        if usernames[username].get_password() == password:
            return True
        else:
            return False
    else:
        return False

def exp_level(username, usernames):
    # iterate from first to current level adding up exp points
    exp_needed = 0
    
    us = usernames[username]
    
    for i in range(1, us.get_level() + 1):
        exp_needed += i * 100

    return exp_needed
        
    
def complete_quest(username, q, usernames):
    # removing completed quests
    
    us = usernames[username]
    us.remove_quest(q)

    total_exp = exp_level(username, usernames)

    # leveling up when exp amount reached high enough
    if us.get_exp() >= total_exp:
        us.level_up()

def uncomplete_quest(username, q, usernames):
    # changing completed quests to uncomplete
    
    us = usernames[username]
    us.undo_quest(q)

    total_exp = exp_level(username, usernames)

    # leveling down when exp amount reached low enough
    if us.get_exp() < total_exp:
        us.level_down()

def make_quest(username, description, label, usernames):
    us = usernames[username]

    reward = 10

    if label == 'hard':
        reward = 20
        
    elif label == 'medium':
        reward = 15

    # creating quest instance called task
    task = Quest(description, reward)

    # appending task to quest list
    us.add_quest(task)

