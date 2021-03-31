from ursina import *
import random
window.title = 'Trial'
app = Ursina()
score = Text(text='Score: '+str(0), scale=0.05, origin=(0, -19))
'''example of inheriting Entity'''

class Player(Entity):
    dead= False
    def __init__(self, **kwargs):
        super().__init__()
        self.model='cube'
        self.color = color.blue
        self.scale_y = 0.1
        self.scale_x = 0.1
        self.scale_z = 0.1
        self.player_body = []
        self.score= 0
        Food()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):
        if key == 'space':
            self.animate_x(2, duration=1)
    def update(self):
        if held_keys['d']:
            try:
                for i in self.player_body:
                    i.x= self.x -(i.num_pos/10)
                    i.y = self.y
            except Exception as e:
                print(e)
        elif held_keys['a']:
            try:
                for i in self.player_body:
                    i.x= self.x +(i.num_pos/10)
                    i.y = self.y
            except Exception as e:
                print(e)
        elif held_keys['s']:
            try:
                for i in self.player_body:
                    i.x= self.x
                    i.y = self.y + (i.num_pos/10)
            except Exception as e:
                print(e)
        elif held_keys['w']:
            try:
                for i in self.player_body:
                    i.x= self.x
                    i.y = self.y - (i.num_pos/10)
            except Exception as e:
                print(e)
        self.x += held_keys['d'] * time.dt * 1
        self.x -= held_keys['a'] * time.dt * 1
        self.y  += held_keys['w'] * time.dt * 1
        self.y -= held_keys['s'] * time.dt *1
        if self.x >= 6.8:
            for i in self.player_body:
                i.enabled= False
                del i 
            self.enabled = False
            score.origin = (0,0)
            score.text= "Game Over! You scored: "+ str(self.score)
            score.scale = 0.03
            close_game_button.visible =True
            reset_game_button.visible = True
            del self
            Player.dead = True

        elif self.x <= -6.6:
            for i in self.player_body:
                i.enabled= False
                del i 
            self.enabled = False
            score.origin = (0,0)
            score.text= "Game Over! You scored: "+ str(self.score)
            score.scale = 0.03
            close_game_button.visible =True
            reset_game_button.visible = True
            del self
            Player.dead = True

        elif self.y >= 5.6:
            for i in self.player_body:
                i.enabled= False
                del i 
            self.enabled = False
            score.origin = (0,0)
            score.text= "Game Over! You scored: "+ str(self.score)
            score.scale = 0.03
            close_game_button.visible =True
            reset_game_button.visible = True
            del self
            Player.dead = True

        elif self.y <= -5.3:
            for i in self.player_body:
                i.enabled= False
                del i 
            self.enabled = False
            score.origin = (0,0)
            score.text= "Game Over! You scored: "+ str(self.score)
            score.scale = 0.03
            close_game_button.visible =True
            reset_game_button.visible = True
            del self
            Player.dead = True

        try:
            if round(self.x-0.1) == round(Food.current_x_pos) and round(self.y-0.1) == round(Food.current_y_pos):
                Food.current_food.end = True
                self.score +=1
                score.text= 'Score: '+ str(self.score)
                Body.amount = self.score
                self.player_body.append(Body(self.score, self.x, self.y))
                Food()
        except Exception as e:
            print(e)
class Body(Entity):
    amount = 0
    def __init__(self, num_pos, x, y):
        super().__init__()
        self.model = 'cube'
        self.color =color.green
        self.scale_y = 0.1 
        self.scale_x = 0.1
        self.scale_z = 0.1
        self.num_pos= num_pos
        self.x = x-(self.num_pos/10)
        self.y =y

    def update(self):
        self.x += held_keys['d'] * time.dt * 1
        self.x -= held_keys['a'] * time.dt * 1
        self.y  += held_keys['w'] * time.dt * 1
        self.y -= held_keys['s'] * time.dt *1
        
class Food(Entity):
    current_x_pos=0
    current_y_pos = 0
    current_food =None
    def __init__(self, x=None, y=None, **kwargs):
        super().__init__()
        self.model = 'cube'
        self.color = color.red
        self.scale_y = 0.1
        self.scale_x =0.1
        self.scale_z = 0.1
        self.end= False
        if x == None:
            self.x = random.uniform(-6,6)
        else:
            self.x=x
        if y==None:
            self.y = random.uniform(-5,5)
        else:
            self.y =y
        Food.current_x_pos = self.x
        Food.current_y_pos =self.y
        Food.current_food = self
        for key, value in kwargs.items():
            setattr(self, key, value)
    def update(self):
        if self.end == True:
            self.enabled = False
            del self
        if Player.dead == True:
            self.enabled=False
            del self
def play_again():
    close_game_button.visible =False
    reset_game_button.visible = False
    print('Starting again')
    Player.dead= False
    Player(x=-1)
    score.text = "Score: "+ str(0)
    score.origin=(0, -19)
    score.scale = 0.05
def close_game():
    print('Ending')
    close_game_button.visible =False
    reset_game_button.visible = False
    application.quit()
window.exit_button.enabled = True
close_game_button = Button(text='End Game', origin=(1, 2), text_color=color.white, color=color.red, scale=0.005)
reset_game_button =Button(text='Keep Playing', origin=(-1, 2), text_color=color.white, color=color.green, scale=0.005)
close_game_button.visible =False
close_game_button.text_entity.scale = 0.6
reset_game_button.visible = False
reset_game_button.text_entity.scale = 0.6
close_game_button.on_click=close_game
reset_game_button.on_click=play_again
player = Player(x=-1)
app.run() 