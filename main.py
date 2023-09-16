import pygame


def main():
    pygame.init()

    pygame.display.set_mode((1280, 720))

    pygame.display.set_caption('Bop-It')

    w_surface = pygame.display.get_surface()

    game = Game(w_surface)

    game.play()

    pygame.quit()


class Game:

    def __init__(self, surface):

        self.surface = surface
        self.bg_color = pygame.Color("black")

        self.fps = 1
        self.game_clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

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
        pass

    def draw(self):
        self.surface.fill(self.bg_color)
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


main()