import pygame
import sys
import os

pygame.init()
pygame.mixer.init()
# Pencere ve boyutlar

TILE_SIZE = 40
WIDTH, HEIGHT = 22 * TILE_SIZE, 18 * TILE_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platform Oyunu")
clock = pygame.time.Clock()
FPS = 60

# Renkler

BROWN = (150, 75, 0)
RED = (200, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
extra_tile_platforms = []

def slice_sprite_sheet(sheet_path, frame_width, frame_height, frame_count):
    sheet = pygame.image.load(sheet_path).convert_alpha()
    frames = []
    for i in range(frame_count):
        frame = sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        frame = pygame.transform.scale(frame, (40, 40))
        frames.append(frame)
    return frames
