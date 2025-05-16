import pygame
import sys
import os

pygame.init()
pygame.mixer.init()


TILE_SIZE = 40
WIDTH, HEIGHT = 22 * TILE_SIZE, 18 * TILE_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platform Oyunu")
clock = pygame.time.Clock()
FPS = 60


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
try:
    start_screen_background = pygame.image.load("assets/background/Blue.png")
    start_screen_background = pygame.transform.scale(start_screen_background, (WIDTH, HEIGHT))
    game_background = pygame.image.load("assets/background/Blue.png")
    game_background = pygame.transform.scale(game_background, (WIDTH, HEIGHT))
    heart_image = pygame.image.load("assets/heart.png")
    heart_image = pygame.transform.scale(heart_image, (30, 30))
    level2_background = pygame.image.load("assets/background/Yellow.png")
    level2_background = pygame.transform.scale(level2_background, (WIDTH, HEIGHT))
    double_jump_frame_paths = [
        "assets/characters/virtual guy/double_jump_frame_1.png",
        "assets/characters/virtual guy/double_jump_frame_2.png",
        "assets/characters/virtual guy/double_jump_frame_3.png",
        "assets/characters/virtual guy/double_jump_frame_4.png",
        "assets/characters/virtual guy/double_jump_frame_5.png",
        "assets/characters/virtual guy/double_jump_frame_6.png",
    ]
    double_jump_frames = [pygame.transform.scale(pygame.image.load(p), (40, 40)) for p in double_jump_frame_paths]

    tunnel_fill_image = pygame.image.load("assets/terrains/tile_9_7.png")
    tunnel_fill_image = pygame.transform.scale(tunnel_fill_image, (TILE_SIZE, TILE_SIZE))
    tunnel_top_image = pygame.image.load("assets/terrains/tile_8_7.png")
    tunnel_top_image = pygame.transform.scale(tunnel_top_image, (TILE_SIZE, TILE_SIZE))


    green_tile_image = pygame.image.load("assets/terrains/tile_0_7.png")
    green_tile_image = pygame.transform.scale(green_tile_image, (TILE_SIZE, TILE_SIZE))

    brown_tile_image = pygame.image.load("assets/terrains/tile_0_9.png")
    brown_tile_image = pygame.transform.scale(brown_tile_image, (TILE_SIZE, TILE_SIZE))

    pineapple_frame_paths = [
        f"assets/fruits/pineapple/pineapple_{i+1}.png" for i in range(17)
    ]

    pineapple_frames = []
    for p in pineapple_frame_paths:
        img = pygame.image.load(p).convert_alpha()
        img = pygame.transform.scale(img, (50,50))  
        pineapple_frames.append(img)

    