import copy
import random
class Hat:
    # the ** in kwargs packs and unpacks the values to be value, key pairs in the self.balls dictionary
    def __init__(self, **kwargs):
        self.balls ={**kwargs}

    def __str__(self):
        return str(self.balls)
    
    # very happy about the if statement layer, verified functionality
    def draw(self, draws):
        balls_instance = self.balls
        drawn_balls = {}
        if draws >= sum(balls_instance.values()):
            return balls_instance
        while draws > 0:
            drawn_ball = random.choice(list(balls_instance.keys()))
            if drawn_ball in balls_instance and balls_instance[drawn_ball] > 0:
                balls_instance[drawn_ball] -= 1
                if drawn_ball in drawn_balls:
                    drawn_balls[drawn_ball] += 1
                else:
                    drawn_balls[drawn_ball] = 1
                draws -= 1
            else:
                continue
        return drawn_balls

    
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_of_matches = 0
    for i in range(num_experiments):
        hat_copy= copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        if balls_drawn == expected_balls:
            num_of_matches += 1
        else:
            continue
    probability = num_of_matches/num_experiments
    
    return probability

test_hat = Hat(red=3, blue=2)
drawn_balls = test_hat.draw(2)
print(str(drawn_balls))