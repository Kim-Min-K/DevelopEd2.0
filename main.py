import pygame
import os
import pygame.font
import random


def main():
    pygame.init()

    display_surface = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu")

    display_surface = pygame.display.get_surface()

    game = Game(display_surface)

    game.play()

    pygame.quit()


class Game:

    def __init__(self, surface):

        self.surface = surface
        self.bg_color = pygame.Color("black")
        self.font_color = pygame.Color("white")
        self.fps = 60
        self.game_clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True


        self.button_streak = 0
        self.just_scored = False

        self.highlighted = 0
        self.highlighted_color = "red"
        self.difficulty = "Easy"
        self.difficulty_set = False
        self.start_game = False
        # start = list[0], easy = list[1], medium = list[2], hard = list[3]
        # used when drawing text
        self.highlighted_list = [self.highlighted_color,"black","black","black"]

        self.buttons = []
        self.current_button = 0
        self.red_button = Red_Button(surface)
        self.buttons.append(self.red_button)
        self.blue_button = Blue_Button(surface)
        self.buttons.append(self.blue_button)
        self.green_button = Green_Button(surface)
        self.buttons.append(self.green_button)
        self.yellow_button = Yellow_Button(surface)
        self.buttons.append(self.yellow_button)
        self.twist_switch = Twist_Switch(surface)
        self.buttons.append(self.twist_switch)
        self.push_switch = Push_Switch(surface)
        self.buttons.append(self.push_switch)

        self.time_left = 60.0

    def play(self):
        while True:
            if not self.start_game:     # have not started the game yet
                self.main_menu()
            self.handle_events()
            self.check_if_scored()
            self.draw()
            if self.continue_game:
                if not self.difficulty_set:   # first entrance into game

                    self.set_difficulty()
                self.update()
                self.decide_continue()
            else:                              # game ended, restart the game
                self.continue_game = True
                self.start_game = False
            self.game_clock.tick(self.fps)

    def check_if_scored(self):
        if self.just_scored == True:
            pass
    
    def handle_events(self):
        events = pygame.event.get() # needs to be called or crashes

    


    def draw(self):
        self.surface.fill(self.bg_color)
        self.red_button.draw()
        self.draw_time()
        pygame.display.update()

    def main_menu(self):
        while not self.start_game:
            self.menu_handler()
            self.draw_menu()
            self.game_clock.tick(self.fps)

    def menu_handler(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            elif event.type == pygame.KEYDOWN:  ############ REMOVE for actual implementation
                if event.key == pygame.K_p:        # enter pressed  

                    if self.highlighted == 0:
                        self.start_game = True
                    elif self.highlighted == 1:
                        self.difficulty = "Easy"
                    elif self.highlighted == 2:
                        self.difficulty = "Medium"
                    else:
                        self.difficulty = "Hard"

                elif event.key == pygame.K_w:                         # down pressed
                    for i in range(len(self.highlighted_list)):
                        self.highlighted_list[i] = "black"
                    self.highlighted -= 1
                    if self.highlighted == -1:                             # looped around
                        self.highlighted = 3
                    self.highlighted_list[self.highlighted] = self.highlighted_color

                elif event.key == pygame.K_s:                         # up pressed
                    for i in range(len(self.highlighted_list)):       # set all colors to black
                        self.highlighted_list[i] = "black"
                    self.highlighted += 1
                    self.highlighted = self.highlighted % 4                # looped around
                    self.highlighted_list[self.highlighted] = self.highlighted_color   # set word to highlight

    # enter once per game to set difficulty variables
    def set_difficulty(self):
        if self.difficulty_set == False:        # set difficutly to on first entrance
            self.difficulty_set = True
            if self.difficulty == "Easy":
                self.time_left = 60.0
            elif self.difficulty == "Medium":
                self.time_left = 45.0
            elif self.difficulty == "Hard":
                self.time_left = 5.0

    def draw_menu(self):
        self.surface.fill(self.bg_color)
        font_size = 80
        font = pygame.font.SysFont("",font_size)  

        start = font.render("Start",True,self.font_color,self.highlighted_list[0]) 
        easy = font.render("Easy",True,self.font_color,self.highlighted_list[1]) 
        medium = font.render("Medium",True,self.font_color,self.highlighted_list[2]) 
        hard = font.render("Hard",True,self.font_color,self.highlighted_list[3]) 
        current_difficulty = font.render("Current Difficulty: "+ self.difficulty,True,self.font_color,self.bg_color) 

        self.surface.blit(start,(300,120)) 
        self.surface.blit(easy,(300,250)) 
        self.surface.blit(medium,(300,380)) 
        self.surface.blit(hard,(300,510)) 
        self.surface.blit(current_difficulty,(300,640))   

        pygame.display.update()

    def draw_time(self):
        font_size = 80
        font = pygame.font.SysFont("",font_size)
        timer_text = font.render(str(round(self.time_left,1)),True,self.font_color,self.bg_color)
        streak_text = font.render(str(self.button_streak),True,self.font_color,self.bg_color)

        timer_location = (1100,0)
        self.surface.blit(timer_text,timer_location)
        self.surface.blit(streak_text,(0,0))


    def update(self):
        self.time_left -= 1/60


    def decide_continue(self):
        if self.time_left < 0:   # add an input to go back to start, auto does it atm
            self.surface.fill(self.bg_color)
            self.continue_game = False
            self.difficulty_set = False



class Red_Button():

    def __init__(self,surface):
        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/4 + 40,self.surface.get_height()/10)
        try:
            self.blue_button_img = pygame.image.load(os.path.join('Assets', 'RedButton.png'))
        except:
            self.blue_button_img = pygame.image.load('/home/logan/Project/DevelopEd2.0/Assets/RedButton.png')

    # draw the button image to the center of the screen
    def draw(self):
        self.surface.blit(self.red_button_img, self.center)

class Blue_Button():

    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/4 + 40,self.surface.get_height()/10)
        try:
            self.blue_button_img = pygame.image.load(os.path.join('Assets', 'BlueButton.png'))
        except:
            self.blue_button_img = pygame.image.load('/home/logan/Project/DevelopEd2.0/Assets/BlueButton.png')
        self.blue_button_img = pygame.transform.scale(self.blue_button_img, (550,550))

    def draw(self):
        self.surface.blit(self.blue_button_img, self.center)

class Green_Button():

    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/4 + 40,self.surface.get_height()/10)
        try:
            self.green_button_img = pygame.image.load(os.path.join('Assets', 'GreenButton.png'))
        except:
            self.blue_button_img = pygame.image.load('/home/logan/Project/DevelopEd2.0/Assets/GreenButton.png')
        self.green_button_img = pygame.transform.scale(self.green_button_img, (550,550))

    def draw(self):
        self.surface.blit(self.green_button_img, self.center)

class Yellow_Button():

    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/4 + 40,self.surface.get_height()/10)
        try:
            self.yellow_button_img = pygame.image.load(os.path.join('Assets', 'YellowButton.png'))
        except:
            self.blue_button_img = pygame.image.load('/home/logan/Project/DevelopEd2.0/Assets/YellowButton.png')
        self.yellow_button_img = pygame.transform.scale(self.yellow_button_img, (550,550))

    def draw(self):
        self.surface.blit(self.yellow_button_img, self.center)

class Twist_Switch():

    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/4 + 40,self.surface.get_height()/10)
        try:
            self.twist_switch_img = pygame.image.load(os.path.join('Assets', 'TwistSwitch.png'))
        except:
            self.blue_button_img = pygame.image.load('/home/logan/Project/DevelopEd2.0/Assets/TwistSwitch.png')
        self.twist_switch_img = pygame.transform.scale(self.twist_switch_img, (550,550))

    def draw(self):
        self.surface.blit(self.twist_switch_img, self.center)
class Push_Switch():

    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/4 + 40,self.surface.get_height()/10)
        try:
            self.push_switch_img = pygame.image.load(os.path.join('Assets', 'PushSwitch.png'))
        except:
            self.blue_button_img = pygame.image.load('/home/logan/Project/DevelopEd2.0/Assets/PushSwitch.png')
        self.push_switch_img = pygame.transform.scale(self.push_switch_img, (550,550))

    def draw(self):
        self.surface.blit(self.push_switch_img, self.center)
main()
