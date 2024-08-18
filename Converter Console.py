import pygame
import pyvidplayer2

width, height = 80, 24

pygame.init()
screen = pygame.display.set_mode((width, height), pygame.HIDDEN)

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    pygame.display.update()

    try:
        video = pyvidplayer2.Video(input('File: '))
    except Exception as e:
        print(e)
        continue

    try:
        f = open(f'{video.name}.tcvc', 'xb')
    except Exception as e:
        print(e)
        continue

    video.resize((width, height))
    video.mute()

    while video.active:
        video.draw(screen, (0, 0), force_draw=True)
        pygame.display.update()
        for y in range(24):
            for x in range(0, 80, 2):
                f.write(bytes([*screen.get_at((x, y))[:3], *screen.get_at((x + 1, y))[:3]]))
        clock.tick(video.frame_rate)
    f.close()

    print(f'Recommended tick/sec: {round(960 * video.frame_rate)}')

pygame.quit()
