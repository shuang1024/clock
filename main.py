import datetime

import pygame
pygame.init()

WIDTH, HEIGHT = 800, 800
FPS = 60

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")

def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def main():
    clock = pygame.time.Clock()

    clock_img = pygame.image.load("clock.png")
    second_img = pygame.image.load("second.png")
    minute_img = pygame.image.load("minute.png")
    hour_img = pygame.image.load("hour.png")

    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        time = list(map(int, list(map(float, str(datetime.datetime.now()).split(" ")[1].split(":")))))
        time[0] %= 12

        display.blit(clock_img, (0, 0))
        display.blit(rot_center(hour_img, 360 - (30*time[0] + time[1]//2)), (0, 0))
        display.blit(rot_center(minute_img, 360 - (time[1]*6 + time[2]//10)), (0, 0))
        display.blit(rot_center(second_img, 360 - (time[2]*6)), (0, 0))


main()