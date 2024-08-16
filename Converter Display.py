import pygame
import pyvidplayer2

width, height = 192, 192

pygame.init()
screen = pygame.display.set_mode((width, height), pygame.HIDDEN)

while True:
    screen.fill((0, 0, 0))
    pygame.display.update()

    try:
        video = pyvidplayer2.Video(input('File: '))
    except Exception as e:
        print(e)
        continue

    try:
        f = open(f'{video.name}({width}-{height}).tcvd', 'xb')
    except Exception as e:
        print(e)
        continue

    video.resize((width, height))
    video.mute()

    while video.active:
        video.draw(screen, (0, 0), force_draw=True)
        pygame.display.update()
        for gy in range(0, height, 8):
            for x in range(0, 6):
                for y in range(0, 8):
                    f.write(bytes([i for j in [screen.get_at((x + 6 * i, y + gy))[:3] for i in range(width // 6)] for i in j]))
    f.close()

pygame.quit()
