import pygame


def main():
    pygame.init()

    pygame.display.set_mode((500, 400))
    pygame.display.set_caption('Bop-It')

    w_surface = pygame.display.get_surface()

    game = Game(w_surface)

    game.play()

    pygame.quit()


class Game:

    def __init__(self, surface):

        self.surface = surface
        self.bg_color = pygame.Color("black")

        self.fps = 60
        self.game_clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

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

        pygame.display.update()

    def update(self):
        pass

    def decide_continue(self):
        pass


main()