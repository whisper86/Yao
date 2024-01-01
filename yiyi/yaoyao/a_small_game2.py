#!/usr/bin/python

import pygame
from pygame.locals import *

def main():
    # 初始化 screen
    pygame.init()
    screen = pygame.display.set_mode((150, 50))
    pygame.display.set_caption('Basic Pygame program')

    # 填充背景
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # 显示一些文本
    font = pygame.font.Font(None, 36)
    text = font.render("Hello", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # 把所有东西blit到screen上
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # 事件循环
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
	main()
