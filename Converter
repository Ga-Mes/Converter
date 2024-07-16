import os
import time
import pygame
import pyvidplayer2

width, height = 192, 192

pygame.init()
screen = pygame.display.set_mode((width, height), pygame.HIDDEN)

while True:
    screen.fill((0, 0, 0))
    pygame.display.update()

    try:
        video = pyvidplayer2.Video(input('\033[97mFile: '))
    except Exception as e:
        print(e)
        continue

    video.resize((width, height))
    video.mute()
    
    try:
        f = open(f'tr//trv//{video.name}.trv', 'xb')
    except Exception as e:
        print(e)
        continue

    while video.active:
        video.draw(screen, (0, 0), force_draw=True)
        pygame.display.update()
        for my in range(0, height, 8):
            for mx in range(0, width, 12):
                for x in range(0, 6):
                    for y in range(0, 8):
                        c1 = screen.get_at((x + mx, y + my))
                        c2 = screen.get_at((x + 6 + mx, y + my))
                        f.write(bytes((*c1, *c2)))
    f.close()

pygame.quit()
