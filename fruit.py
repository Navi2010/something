import random

class Fruit:
    def __init__(self):
        self.fruits = {'apple':'red',
                       'orange':'orange',
                       'banana':'yellow',
                       'cucumber':'green'}
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            x = input()
            if x.lower()==color:
                print('correct')
            else:
                print('incorrect')
            option = int(input('enter 0 if you want to play otherwise enter 1: '))
            if option:
                break

print('welcome to the fruit quiz!')
obj = Fruit()
obj.quiz()