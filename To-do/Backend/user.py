'''
Created on Oct 24, 2020

@author: Linda and Ileen
'''
class User:
    ''' Constructor: takes in an username, level, exp, password, quests, past quests, 
            profile image, and profile images of the specific user
        Please give us the images in order of evolution; for instance 1. pichu, 2. pikachu 3. raichu'''
    def __init__(self, username, password,  image, images, level = 1, exp = 0, quests = [], past = []):
        self.username = username
        self.password = password
        self.image = image
        self.images = images
        self.level = level
        self.exp = exp
        self.quests = quests
        self.past = past
  
    
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
    
    '''Returns the user's past quests'''
    def get_past(self):
        return self.past
    
    '''Returns the user's password'''
    def get_password(self):
        return self.password
    
    '''Returns the user's image'''
    def get_image(self):
        return self.image
    
    '''Returns the user's images'''
    def _get_images(self):
        return self.images;
    
    '''Changes the image to the correct image of the user's level'''
    def change_image(self):
        self.image = self.images[self.level - 1]
    
    '''Levels up the user to a max of level 3'''
    def level_up(self):
        if self.level < 3:
            self.level += 1;
            self.change_image();
        
    '''Increase exp after completing task'''
    def increase_exp(self, exp_gain):
        self.exp += exp_gain
    
    '''level down the user to a min of level 1'''
    def level_down(self):
        if self.level > 1:
            self.level -= 1;
            self.change_image();
        
    '''Decrease exp after completing task'''
    def decrease_exp(self, exp_loss):
        self.exp -= exp_loss
    
    '''Add a quest to the user's quests'''
    def add_quest(self,q):
        self.quests.append(q)
    
    '''Removes a quest from the user's past quests and add it to quests and subtract exp'''
    def undo_quest(self, q):
        exp_loss = q.get_exp()
        q.change_status()
        self.past.remove(q)
        self.add_quest(q);
        self.decrease_exp(exp_loss)
        
    '''Remove a quest from the user's quest and add it to past quests and add exp'''
    def remove_quest(self, q):
        exp_gain = q.get_exp()
        q.change_status()
        self.past.append(q)
        self.quests.remove(q)
        self.increase_exp(exp_gain)
    
    '''Delete the quest'''
    def delete_quest(self, q):
        self.quests.remove(q)
    

    
    
    
