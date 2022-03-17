
import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents=[]
        self.balls_remove=[]
        for key,value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
 
    
    def draw (self, number):
        if number>len(self.contents):
            return self.contents
        else:
      
            for i in range (number):
                ball_choice=random.choice(self.contents)
                self.contents.remove(f'{ball_choice}')
                self.balls_remove.append(ball_choice)    
            
            return self.balls_remove
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range (num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        success = True
        for key in expected_balls.keys():
            if balls.count(key) < expected_balls[key]:
                success = False
                break
        if success:
            count += 1

    return count / num_experiments