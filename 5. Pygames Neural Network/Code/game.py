import pygame
from pipe import PipeCollection
from defs import *

class Game:
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.gameDisplay = pygame.display.set_mode((DISPLAY_W,DISPLAY_H))
        pygame.display.set_caption('Learn to fly')

        self.bgImg = pygame.image.load(BG_FILENAME) #Loading the background
        self.label_font = pygame.font.SysFont("monospace", DATA_FONT_SIZE)

        self.dt = 0
        self.game_time = 0

        self.pipes = PipeCollection(self.gameDisplay)
        self.pipes.create_new_set()



    def update_label(self, data, title, font, x, y, gameDisplay):
        label = font.render('{} {}'.format(title, data), 1, DATA_FONT_COLOR)
        gameDisplay.blit(label, (x, y))
        return y

    def update_data_labels(self, gameDisplay, dt, game_time, font):
        y_pos = 10
        gap = 20
        x_pos = 10
        y_pos = self.update_label(round(1000/dt,2), 'FPS', font, x_pos, y_pos + gap, gameDisplay)
        y_pos = self.update_label(round(game_time/1000,2),'Game time', font, x_pos, y_pos + gap, gameDisplay)

    def draw_objects(self):
        self.gameDisplay.blit(self.bgImg, (0, 0))
        self.update_data_labels(self.gameDisplay, self.dt, self.game_time, self.label_font)
        for pi in self.pipes.pipes:
            pi.draw()

        pygame.display.update() # Update/Render window

    
    def run_game_loop(self):
        while True:

            self.dt = self.clock.tick(FPS)
            self.game_time += self.dt


            #Handle Events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    return
            
            
            #Update Display
            self.draw_objects()
            self.pipes.update(self.dt)