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

    
    apple_frame_paths = [
        f"assets/fruits/apple/apple_frame_{i+1}.png" for i in range(17)
    ]

    apple_frames = []
    for p in apple_frame_paths:
        img = pygame.image.load(p).convert_alpha()
        img = pygame.transform.scale(img, (50, 50))  
        apple_frames.append(img)

   
    char1_run_frames = slice_sprite_sheet("assets/characters/mask dude/Run (32x32).png", 32, 32, 6)
    char1_jump_frames = slice_sprite_sheet("assets/characters/mask dude/Double Jump (32x32).png", 32, 32, 6)

   
    char2_run_frames = slice_sprite_sheet("assets/characters/ninja frog/Run2(32x32).png", 32, 32, 12)
    char2_jump_frames = slice_sprite_sheet("assets/characters/ninja frog/Double Jump2 (32x32).png", 32, 32, 6)

    
    char3_run_frames = slice_sprite_sheet("assets/characters/pink man/Run 3(32x32).png", 32, 32, 6)
    char3_jump_frames = slice_sprite_sheet("assets/characters/pink man/Double Jump 3(32x32).png", 32, 32, 6)

    
    char4_run_frames = slice_sprite_sheet("assets/characters/virtual guy/Run4(32x32).png", 32, 32, 12)
    char4_jump_frames = slice_sprite_sheet("assets/characters/virtual guy/Double Jump 4(32x32).png", 32, 32, 6)
    character_sets = [
        {"run": char1_run_frames, "jump": char1_jump_frames},
        {"run": char2_run_frames, "jump": char2_jump_frames},
        {"run": char3_run_frames, "jump": char3_jump_frames},
        {"run": char4_run_frames, "jump": char4_jump_frames},
    ]

    selected_character_index = 0  
    font = pygame.font.Font("assets/font/PixelEmulator3.otf", 30)
    extra_tile_image = pygame.image.load("assets/terrains/tile_0_18.png")
    extra_tile_image = pygame.transform.scale(extra_tile_image, (TILE_SIZE, TILE_SIZE))
    game_over_image = pygame.image.load("assets/background/game over.png")
    full_game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))
    restart_button_image = pygame.transform.scale(pygame.image.load("assets/button/reload.png"), (40, 40))
    restart_button_rect = pygame.Rect(WIDTH - 150, 50, 40, 40)
    next_level_button_image = pygame.transform.scale(pygame.image.load("assets/button/next_level.png"), (40, 40))
    next_level_button_rect = pygame.Rect(WIDTH - 200, 50, 40, 40)
    dark_background = pygame.image.load("assets/background/Pink.png")
    dark_background = pygame.transform.scale(dark_background, (WIDTH, HEIGHT))
    home_button_image = pygame.transform.scale(pygame.image.load("assets/button/home.png"), (40, 40))
    home_button_rect = pygame.Rect(WIDTH - 100, 50, 40, 40)
    frame_tile_image = pygame.image.load("assets/terrains/tile_0_1.png")
    frame_tile_image = pygame.transform.scale(
        pygame.image.load("assets/terrains/tile_0_1.png"),
        (TILE_SIZE, 20)
    )
    frame_tile_image_level2 = pygame.image.load("assets/terrains/tile_8_0.png")
    frame_tile_image_level2 = pygame.transform.scale(frame_tile_image_level2, (TILE_SIZE, 20))
    new_enemy_run_frames = slice_sprite_sheet("assets/animals/new_animal/Run (84x38).png", 84, 38, 8)
    new_enemy_run_frames = [pygame.transform.scale(frame, (60, 60)) for frame in new_enemy_run_frames]
    new_enemy_left_frames = [pygame.transform.flip(frame, True, False) for frame in new_enemy_run_frames]
    strawberry_frame_paths = [f"assets/fruits/strawberry/Strawberry.png"]
    strawberry_frames = slice_sprite_sheet(strawberry_frame_paths[0], 32, 32, 17)
    strawberry_frames = [pygame.transform.scale(frame, (70, 60)) for frame in strawberry_frames]
    PLATFORM_HEIGHT = 10  
    platform_tile_image = pygame.transform.scale(
        pygame.image.load("assets/terrains/Grey Off.png"),
        (TILE_SIZE, PLATFORM_HEIGHT)
    )
    player_frames_paths = [
        "assets/characters/virtual guy/sprite_1.png",
        "assets/characters/virtual guy/sprite_2.png",
        "assets/characters/virtual guy/sprite_3.png",
        "assets/characters/virtual guy/sprite_4.png",
        "assets/characters/virtual guy/sprite_5.png",
        "assets/characters/virtual guy/sprite_6.png",
        "assets/characters/virtual guy/sprite_7.png",
        "assets/characters/virtual guy/sprite_8.png",
        "assets/characters/virtual guy/sprite_9.png",
        "assets/characters/virtual guy/sprite_10.png",
        "assets/characters/virtual guy/sprite_11.png",
        "assets/characters/virtual guy/sprite_12.png",
    ]
    player_right_frames = [pygame.transform.scale(pygame.image.load(p), (40, 40)) for p in player_frames_paths]
    player_left_frames = [pygame.transform.flip(frame, True, False) for frame in player_right_frames]

    player_frame_index = 0
    player_animation_speed = 0.5

except pygame.error as e:
    print(f"Görseller yüklenemedi: {e}")
    pygame.quit()
    sys.exit()
    jump_sound = pygame.mixer.Sound("assets\sound\jump_01.wav")
dj_sound = pygame.mixer.Sound("assets\sound\dj.ogg")

jump_sound.set_volume(1.0) 
dj_sound.set_volume(0.3) 
flag = pygame.Rect(WIDTH - 100, HEIGHT - TILE_SIZE - 70, 60, 90)

player_direction_right = True

carrot_frame_index = 0
carrot_animation_speed = 0.15  
carrot_frames = pineapple_frames 

apple_animation_speed = 0.3  


enemy_right_frames_paths = [
    "assets/animals/rabbit/rabbit_sprite_1.png",
    "assets/animals/rabbit/rabbit_sprite_3.png",
    "assets/animals/rabbit/rabbit_sprite_4.png",
    "assets/animals/rabbit/rabbit_sprite_5.png",
    "assets/animals/rabbit/rabbit_sprite_6.png",
    "assets/animals/rabbit/rabbit_sprite_7.png",
    "assets/animals/rabbit/rabbit_sprite_8.png",
    "assets/animals/rabbit/rabbit_sprite_10.png",
    "assets/animals/rabbit/rabbit_sprite_11.png",
    "assets/animals/rabbit/rabbit_sprite_12.png",
]
enemy_right_frames = [pygame.transform.scale(pygame.image.load(p), (40, 40)) for p in enemy_right_frames_paths]

enemy_left_frames_paths =[ 
    "assets/animals/rabbit/flipped_rabbit_sprites/flipped_rabbit_sprite_1.png",
    "assets/animals/rabbit/flipped_rabbit_sprites/flipped_rabbit_sprite_3.png",
    "assets/animals/rabbit/flipped_rabbit_sprites/flipped_rabbit_sprite_4.png",
    "assets/animals/rabbit/flipped_rabbit_sprites/flipped_rabbit_sprite_5.png",
    "assets/animals/rabbit/flipped_rabbit_sprites/flipped_rabbit_sprite_6.png",
    "assets/animals/rabbit/flipped_rabbit_sprites/flipped_rabbit_sprite_7.png",
    "assets/animals/rabbit/flipped_rabbit_sprites/flipped_rabbit_sprite_8.png",
    "assets/animals/rabbit/flipped_rabbit_sprites/flipped_rabbit_sprite_10.png",
    "assets/animals/rabbit/flipped_rabbit_sprites/flipped_rabbit_sprite_11.png",
    "assets/animals/rabbit/flipped_rabbit_sprites/flipped_rabbit_sprite_12.png",
]
enemy_left_frames = [pygame.transform.scale(pygame.image.load(p), (40, 40)) for p in enemy_left_frames_paths]
enemy_frame_index = 0
enemy_animation_speed = 0.15


chicken_right_frames_paths = [
f"assets/animals/chicken/chicken_frame_{i+1}.png" for i in range(1, 10)
]
chicken_right_frames = [pygame.transform.scale(pygame.image.load(p), (40, 40)) for p in chicken_right_frames_paths]
chicken_left_frames =[pygame.transform.flip(frame, True, False) for frame in chicken_right_frames]
chicken_animation_speed = 0.4  

