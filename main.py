import pickle
import time

import keyboard
import pygame

import aple
import snake

pygame.init()
pygame.display.set_caption('SNAKE')
font = pygame.font.Font('freesansbold.ttf', 32)

screen = pygame.display.set_mode((600, 600))
SNAKE_COLOR = [0, 255, 0]
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
game_over = font.render('Game   Over', True, (255, 255, 255))
game_rect = game_over.get_rect()
last_high = font.render(f"High Score: {pickle.load(open('high_score.p', 'rb'))}", True, (255, 255, 255))
last_high_rect = last_high.get_rect()
space_to_play = font.render('press space to play', True, (255, 255, 255))
center = (width // 2, height // 2)
space_rect = space_to_play.get_rect()
space_rect.center = (width // 2, height // 2 + 50)
last_high_rect.center = center
game_rect.center = center
ROW_LENGTH = 40
COL_LENGTH = height / width * ROW_LENGTH
SNAKE_SIZE = width // ROW_LENGTH
START_Y = ROW_LENGTH // 2 * SNAKE_SIZE
START_X = COL_LENGTH // 2 * SNAKE_SIZE
SNAKE_VEL = SNAKE_SIZE
PULSE = 300
OUTLINE = 3
INIT_LENGTH = 5


def main():
    global SNAKE_VEL
    while True:
        screen.blit(last_high, last_high_rect)
        screen.blit(space_to_play, space_rect)
        pygame.display.update()
        while not keyboard.is_pressed(' '):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

        red = aple.Apple()
        snek = snake.Snake(START_X, START_Y)
        pulse = PULSE
        hold_x = 0
        hold_y = -SNAKE_VEL
        score = 0
        waited = False

        running = True
        while running:

            if snek.dead:
                snek.velx, snek.vely, SNAKE_VEL = 0, 0, 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            try:
                if keyboard.is_pressed('w') and snek.vely <= 0:
                    hold_y = -SNAKE_VEL
                    hold_x = 0
                if keyboard.is_pressed('a') and snek.velx <= 0:
                    hold_x = -SNAKE_VEL
                    hold_y = 0
                if keyboard.is_pressed('s') and snek.vely >= 0:
                    hold_x = 0
                    hold_y = SNAKE_VEL
                if keyboard.is_pressed('d') and snek.velx >= 0:
                    hold_x = SNAKE_VEL
                    hold_y = 0
            except:
                pass

            if pulse == 0:
                screen.fill([0, 0, 0])
                pulse = PULSE

                if snek.dead:
                    dump = snek.update(red)
                    if not waited:
                        time.sleep(1)
                        waited = True
                    if len(snek.units) > 0:
                        snek.units.remove(snek.units[-1])
                    else:
                        running = False
                else:
                    snek.velx = hold_x
                    snek.vely = hold_y
                    if snek.update(red):
                        red = aple.Apple()
                        score += 1
                    red.show()
            else:
                pulse -= 1

            pygame.display.update()

        screen.blit(game_over, game_rect)
        pygame.display.update()
        time.sleep(3)

        with open('high_score.p', 'rb') as f:
            if score > pickle.load(f):
                screen.fill([0, 0, 0])
                new_high_score = font.render('New High Score!', True, (255, 255, 255))
                high_score = font.render(str(score), True, (255, 255, 255))
                score_rect = new_high_score.get_rect()
                score_rect.center = center
                screen.blit(new_high_score, score_rect)
                score_rect.center = (width // 2 + 100, height // 2 + 50)
                screen.blit(high_score, score_rect)
                pygame.display.update()
                with open('high_score.p', 'wb') as fi:
                    pickle.dump(score, fi)

        screen.fill([0, 0, 0])
        play_again = font.render('Press space to play again', True, (255, 255, 255))
        again_rect = play_again.get_rect()
        again_rect.center = center
        screen.blit(play_again, again_rect)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            if keyboard.is_pressed(' '): break

        SNAKE_VEL = SNAKE_SIZE





if __name__ == '__main__':
    main()
