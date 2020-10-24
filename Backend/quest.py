'''
Created on Oct 24, 2020

@author: Linda and Ileen
'''
class Quest():
    
    '''Construct a Quest with a description, exp, and status'''
    def __init__(self, description = "", exp = 0 , status = False):
        self.description = description
        self.exp = exp
        self.status = status
    
    '''Return the quest's description'''
    def get_description(self):
        return self.description
    
    '''Return the quest's exp'''
    def get_exp(self):
        return self.exp
    
    '''Return the quest's status'''
    def get_status(self):
        return self.status
    
    '''Change status of the quest to True after the user has completing the task'''
    def change_status(self):
        self.status = True