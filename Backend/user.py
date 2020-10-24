'''
Created on Oct 24, 2020

@author: Linda and Ileen
'''

class User:
    ''' Constructor: takes in an username, level, exp, password, and quests of the specific user'''
    def __init__(self, username, password, level = 1, exp = 0, quests = []):
        self.username = username
        self.level = level
        self.exp = exp
        self.quests = quests
        self.password = password
    
    '''Returns the user's username'''
    def get_username(self):
        return self.username
    
    '''Returns the user's level'''
    def get_level(self):
        return self.level
    
    '''Returns the user's exp'''
    def get_exp(self):
        return self.exp
    
    '''Returns the user's quests'''
    def get_quests(self):
        return self.quests
    
    '''Returns the user's password'''
    def get_password(self):
        return self.password
    
    '''Add a quest to the user's quests'''
    def add_quest(self,q):
        self.quests.append(q)
    
    '''Remove a quest from the user's quest and add exp'''
    def remove_quest(self, q):
        exp_gain = q.getExp()
        self.quests.remove(q)
        self.increase_exp(exp_gain)
        
    
    '''Levels up the user'''
    def level_up(self):
        self.level += 1;
        
    '''Increase exp after completing task'''
    def increase_exp(self, exp_gain):
        self.exp += exp_gain
    
    
    
