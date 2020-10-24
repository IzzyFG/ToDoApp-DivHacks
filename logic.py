'''
Created on Oct 24, 2020

@author: Linda and Ileen
'''

import user
import quest

usernames = {}


def sign_up(username, password):
    # checking if username is in usernames
    if username not in usernames:
        usernames[username] = user.User(username, password)

    else:
        return 'Username already taken'

def login(username, password):
    # user input for username and password

    if username in usernames:
        if user.User.get_password() == password:
            return True
        else:
            return False
    else:
        return False

def exp_level(username):
    # iterate from first to current level adding up exp points
    exp_needed = 0
    
    user = usernames[username]
    
    for i in range(1, user.User.get_level() + 1):
        exp_needed += i * 100

    return exp_needed
        
        
        
    
    
def complete_quest(username, q):
    # removing completed quests
    
    user = usernames[username]
    user.User.remove_quest(q)

    total_exp = exp_level(username)

    # leveling up when exp amount reached
    if user.User.get_exp() >= total_exp:
        user.User.level_up()


def make_quest(username, description, label):
    user = usernames[username]

    reward = 10

    if label == 'hard':
        reward = 50
        
    elif label == 'medium':
        reward = 25

    # creating quest instance called task
    task = quest.Quest(description, reward)

    # appending task to quest list
    user.User.add_quest(task)
    
    
    
    
    
    
    
    
    
    
