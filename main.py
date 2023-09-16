import pygame
<<<<<<< HEAD
import pygame_menu
import pygame.font
from pygame_menu import themes
#===============
import random
>>>>>>> 4507a2bd0ee47ac24ee3abe4b3998eca9d5aaa9d


def main():
    pygame.init()

    display_surface = pygame.display.set_mode((1280, 720))
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

<<<<<<< HEAD
if __name__ == '__main__':
=======
class Red_Button():
>>>>>>> 4507a2bd0ee47ac24ee3abe4b3998eca9d5aaa9d

<<<<<<< HEAD
    main()
=======
    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/2,self.surface.get_height()/2)
        self.color = pygame.Color("red")

    def draw(self):
        pygame.draw.circle(self.surface,self.color,self.center,self.radius)

class Blue_Button():

    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/2,self.surface.get_height()/2)
        self.color = pygame.Color("blue")

    def draw(self):
        pygame.draw.circle(self.surface,self.color,self.center,self.radius)

class Green_Button():

    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/2,self.surface.get_height()/2)
        self.color = pygame.Color("green")

    def draw(self):
        pygame.draw.circle(self.surface,self.color,self.center,self.radius)

class Yellow_Button():

    def __init__(self,surface):

        self.surface = surface
        self.radius = 80
        self.center = (self.surface.get_width()/2,self.surface.get_height()/2)
        self.color = pygame.Color("yellow")

    def draw(self):
        pygame.draw.circle(self.surface,self.color,self.center,self.radius)
main()
>>>>>>> 4507a2bd0ee47ac24ee3abe4b3998eca9d5aaa9d