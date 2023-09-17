import pygame
import os
import pygame_menu
import pygame.font
from pygame_menu import themes
import random

imgBackground = pygame.image.load("Assets/Background_menu.png")

def main_menu():
    while True:
        print("hello")

def main():
    pygame.init()
    display_surface = pygame.display.set_mode((1280, 720))
    display_surface.blit(imgBackground, (0, 0))
    pygame.display.set_caption("Menu")

    # Menu Page 
    font = pygame.font.Font('freesansbold.ttf',100)
    text = font.render("Welcome!",True, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (200,200)

    display_surface.blit(text, (640,360))
    pygame.display.update()


    w_surface = pygame.display.get_surface()

    game = Game(w_surface)

    main_menu()

    game.play()

    pygame.quit()




def homeScreen():
    pass 


class Game:

    def __init__(self, surface):

        self.surface = surface
        self.bg_color = pygame.Color("black")

        self.fps = 1
        self.game_clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        self.buttons = []

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
        while not self.close_clicked:
            self.handle_events()
            self.draw()
            if self.continue_game:
                self.update()
                self.decide_continue()
            self.game_clock.tick(self.fps)

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True

    def draw(self):
        self.surface.fill(self.bg_color)
        random.choice(self.buttons).draw()
        self.draw_time()
        pygame.display.update()

    def draw_time(self):
        font_size = 80
        font_color = pygame.Color("white")
        font = pygame.font.SysFont("",font_size)
        timer_text = font.render(str(self.time_left),True,font_color,self.bg_color)

        timer_location = (1100,0)
        self.surface.blit(timer_text,timer_location)

    def update(self):
        self.time_left -= 1
        

    def decide_continue(self):
        pass


class Red_Button():

    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/4 + 40,self.surface.get_height()/10)
        self.red_button_img = pygame.image.load(os.path.join('Assets', 'RedButton.jpg'))
        self.red_button_img = pygame.transform.scale(self.red_button_img, (550,550))

    # draw the button image to the center of the screen
    def draw(self):
        self.surface.blit(self.red_button_img, self.center)

class Blue_Button():

    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/4 + 40,self.surface.get_height()/10)
        self.blue_button_img = pygame.image.load(os.path.join('Assets', 'BlueButton.jpg'))
        self.blue_button_img = pygame.transform.scale(self.blue_button_img, (550,550))

    def draw(self):
        self.surface.blit(self.blue_button_img, self.center)

class Green_Button():

    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/4 + 40,self.surface.get_height()/10)
        self.green_button_img = pygame.image.load(os.path.join('Assets', 'GreenButton.jpg'))
        self.green_button_img = pygame.transform.scale(self.green_button_img, (550,550))

    def draw(self):
        self.surface.blit(self.green_button_img, self.center)

class Yellow_Button():

    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/4 + 40,self.surface.get_height()/10)
        self.yellow_button_img = pygame.image.load(os.path.join('Assets', 'YellowButton.jpg'))
        self.yellow_button_img = pygame.transform.scale(self.yellow_button_img, (550,550))

    def draw(self):
        self.surface.blit(self.yellow_button_img, self.center)

class Twist_Switch():

    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/4 + 40,self.surface.get_height()/10)
        self.twist_switch_img = pygame.image.load(os.path.join('Assets', 'TwistSwitch.jpg'))
        self.twist_switch_img = pygame.transform.scale(self.twist_switch_img, (550,550))

    def draw(self):
        self.surface.blit(self.twist_switch_img, self.center)
class Push_Switch():

    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/4 + 40,self.surface.get_height()/10)
        self.push_switch_img = pygame.image.load(os.path.join('Assets', 'PushSwitch.jpg'))
        self.push_switch_img = pygame.transform.scale(self.push_switch_img, (550,550))

    def draw(self):
        self.surface.blit(self.push_switch_img, self.center)
main()
