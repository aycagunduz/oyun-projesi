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

flag_frame_paths = [
    "assets/flag/flag_frame_1.png",
    "assets/flag/flag_frame_2.png",
    "assets/flag/flag_frame_3.png",
    "assets/flag/flag_frame_4.png",
    "assets/flag/flag_frame_5.png",
    "assets/flag/flag_frame_6.png",
    "assets/flag/flag_frame_7.png",
    "assets/flag/flag_frame_8.png",
    "assets/flag/flag_frame_9.png",
    "assets/flag/flag_frame_10.png",
]
flag_frames = [pygame.transform.scale(pygame.image.load(p), (60, 90)) for p in flag_frame_paths]
flag_frame_index = 0
flag_animation_speed = 0.2

def draw_frame(surface):
    if current_level_index == 1:
        
        for x in range(0, WIDTH, TILE_SIZE):
            surface.blit(frame_tile_image_level2, (x, 0))
            surface.blit(frame_tile_image_level2, (x, HEIGHT - 20))

        for y in range(0, HEIGHT, TILE_SIZE):
            surface.blit(pygame.transform.rotate(frame_tile_image_level2, 90), (0, y))
            surface.blit(pygame.transform.rotate(frame_tile_image_level2, -90), (WIDTH - 20, y))
    elif current_level_index == 0 :
        
        for x in range(0, WIDTH, TILE_SIZE):
            surface.blit(frame_tile_image, (x, 0))
            surface.blit(frame_tile_image, (x, HEIGHT - 20))
        for y in range(0, HEIGHT, TILE_SIZE):
            surface.blit(pygame.transform.rotate(frame_tile_image, 90), (0, y))
            surface.blit(pygame.transform.rotate(frame_tile_image, -90), (WIDTH - 20, y))

def draw_extra_tiles():
    global extra_tile_platforms  
    extra_tile_platforms = []    

    for i in range(2):
        x = 6 * TILE_SIZE + i * TILE_SIZE
        y = HEIGHT - 11 * TILE_SIZE
        screen.blit(extra_tile_image, (x, y))
        extra_tile_platforms.append(pygame.Rect(x, y, TILE_SIZE, 1))

    for i in range(2):
        x = (15 - 2 + i) * TILE_SIZE
        y1 = HEIGHT - 13 * TILE_SIZE
        y2 = HEIGHT - 7 * TILE_SIZE
        screen.blit(extra_tile_image, (x, y1))
        extra_tile_platforms.append(pygame.Rect(x, y1, TILE_SIZE, TILE_SIZE))
        screen.blit(extra_tile_image, (x, y2))
        extra_tile_platforms.append(pygame.Rect(x, y2, TILE_SIZE, TILE_SIZE))

def draw_tunnel_platform(plat):
    rows = max(1, plat.height // TILE_SIZE)  
    cols = max(1, plat.width // TILE_SIZE)

    for row in range(rows):
        for col in range(cols):
            if plat.x == 0 and plat.y == HEIGHT - 3 * TILE_SIZE and row == 1 and col == 1:
                tile = tunnel_fill_image 
            elif row == 0:
                tile = tunnel_top_image 
            else:
                tile = tunnel_fill_image  
            screen.blit(tile, (plat.x + col * TILE_SIZE, plat.y + row * TILE_SIZE))

def show_start_screen():
    background = pygame.image.load("assets/background/start screen.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT - 180, 300, 80)

    main_text = font.render("PLAY", True, (255, 255, 255))
    shadow_text = font.render("PLAY", True, (0, 0, 0))

    while True:
        screen.blit(background, (0, 0))
        button_surface = pygame.Surface((button_rect.width, button_rect.height), pygame.SRCALPHA)
        button_surface.fill((255, 105, 180, 0)) 
        screen.blit(button_surface, button_rect.topleft)

        text_rect = main_text.get_rect(center=button_rect.center)
        shadow_rect = text_rect.copy()
        shadow_rect.x += 2  
        shadow_rect.y += 2  

        screen.blit(shadow_text, shadow_rect)  
        screen.blit(main_text, text_rect)      # 

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

        clock.tick(FPS)
def show_character_selection_screen():
    global selected_character_index

    selecting = True
    current_frame_index = 0
    animation_speed = 0.2

    while selecting:
        screen.fill(BLACK)
        title_text = font.render("Karakter Seçimi!", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

        for idx, frameset in enumerate(character_sets):
            frame = frameset["run"][int(current_frame_index) % len(frameset["run"])]
            big_frame = pygame.transform.scale(frame, (80, 80)) 
            frame_x = WIDTH // 5 * (idx + 1) - frame.get_width() // 2
            frame_y = HEIGHT // 2 - frame.get_height() // 2
            screen.blit(big_frame, (frame_x, frame_y))

            if idx == selected_character_index:
                pygame.draw.rect(screen, RED, (frame_x - 5, frame_y - 5, big_frame.get_width() + 10, big_frame.get_height() + 10), 3)

        info_text = font.render("<- / -> ile seç, Enter ile onayla", True, WHITE)
        screen.blit(info_text, (WIDTH // 2 - info_text.get_width() // 2, HEIGHT - 100))

        pygame.display.flip()
        clock.tick(FPS)

        current_frame_index += animation_speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_character_index = (selected_character_index - 1) % len(character_sets)
                elif event.key == pygame.K_RIGHT:
                    selected_character_index = (selected_character_index + 1) % len(character_sets)
                elif event.key == pygame.K_RETURN:
                    selecting = False

def draw_darkness_overlay(player_rect):
    darkness_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    darkness_surface.fill((0, 0, 0, 220)) 

    light_radius = 150 
    light_center = (player_rect.centerx, player_rect.centery)

    pygame.draw.circle(darkness_surface, (0, 0, 0, 0), light_center, light_radius)

    screen.blit(darkness_surface, (0, 0))



levels = [
{  
    "platforms": [
    pygame.Rect(3 * TILE_SIZE, HEIGHT - 4 * TILE_SIZE, 5 * TILE_SIZE, 10),
    pygame.Rect(9 * TILE_SIZE, HEIGHT - 7 * TILE_SIZE, 5 * TILE_SIZE, 10),
    pygame.Rect(15 * TILE_SIZE, HEIGHT - 10 * TILE_SIZE, 5 * TILE_SIZE, 10),
    ],
    "platform_movements": [
        None,
        None,
        {"direction": 1, "speed": 2, "range": (3 * TILE_SIZE, 20 * TILE_SIZE)},  
    ],
    "fruits": [
        pygame.Rect(4 * TILE_SIZE, HEIGHT - 5 * TILE_SIZE, 30, 30),
        pygame.Rect(10 * TILE_SIZE, HEIGHT - 8 * TILE_SIZE, 30, 30),
        pygame.Rect(16 * TILE_SIZE, HEIGHT - 11 * TILE_SIZE, 30, 30),
    ],
    "enemies": [
        pygame.Rect(5 * TILE_SIZE, HEIGHT - 5 * TILE_SIZE, 40, 40),
        pygame.Rect(11 * TILE_SIZE, HEIGHT - 8 * TILE_SIZE, 40, 40),
    ],
    "enemy_ranges": [
        (3 * TILE_SIZE, 7 * TILE_SIZE),
        (9 * TILE_SIZE, 13 * TILE_SIZE),
    ]
},

{  
    "platforms": [ 
        pygame.Rect(0, HEIGHT - 5* TILE_SIZE , 10 * TILE_SIZE, 20* TILE_SIZE),  
        pygame.Rect(15 * TILE_SIZE, HEIGHT - 7 * TILE_SIZE, 10 * TILE_SIZE , 2 * TILE_SIZE),  
        
        pygame.Rect(0, HEIGHT - 11 * TILE_SIZE, 6 * TILE_SIZE, 2 * TILE_SIZE), 
        pygame.Rect(15 * TILE_SIZE, HEIGHT - 13 * TILE_SIZE, 7 * TILE_SIZE, 2 * TILE_SIZE)
    ],
    "walls": [
        pygame.Rect(20 * TILE_SIZE, HEIGHT - 3 * TILE_SIZE, 10, 2 * TILE_SIZE),
        pygame.Rect(10 * TILE_SIZE, HEIGHT - 5 * TILE_SIZE, 10, 4 * TILE_SIZE),
    ],
    "fruits": [
        pygame.Rect(1 * TILE_SIZE, HEIGHT - 6 * TILE_SIZE - 40, 30, 30),  
        pygame.Rect(3 * TILE_SIZE, HEIGHT - 6 * TILE_SIZE - 40, 30, 30),  
        pygame.Rect(5 * TILE_SIZE, HEIGHT - 6 * TILE_SIZE - 40, 30, 30),  
        pygame.Rect(13 * TILE_SIZE, HEIGHT - 8 * TILE_SIZE - 40, 30, 30), 
        pygame.Rect(15 * TILE_SIZE, HEIGHT - 8 * TILE_SIZE - 40, 30, 30), 
        pygame.Rect(17 * TILE_SIZE, HEIGHT - 8 * TILE_SIZE - 40, 30, 30), 
        pygame.Rect(16 * TILE_SIZE, HEIGHT - 13 * TILE_SIZE - 40, 30, 30),
        pygame.Rect(18 * TILE_SIZE, HEIGHT - 13 * TILE_SIZE - 40, 30, 30),
    ],
   "enemies": [
        pygame.Rect(15 * TILE_SIZE, HEIGHT - 8 * TILE_SIZE, 40, 40),  
        pygame.Rect(15 * TILE_SIZE, HEIGHT - 13 * TILE_SIZE - 40, 40, 40),
    ],
    "enemy_ranges": [
        (15 * TILE_SIZE, 21 * TILE_SIZE),
        (15 * TILE_SIZE, 21 * TILE_SIZE),  
    ]

} , 
{
    "platforms": [
        pygame.Rect(0, HEIGHT - TILE_SIZE, 22 * TILE_SIZE, TILE_SIZE),  # Alt zemin
        pygame.Rect(2 * TILE_SIZE, HEIGHT - 6 * TILE_SIZE, 4 * TILE_SIZE, 2 * TILE_SIZE),  
        pygame.Rect(16 * TILE_SIZE, HEIGHT - 6 * TILE_SIZE, 4 * TILE_SIZE, 2 * TILE_SIZE),  
        pygame.Rect(8 * TILE_SIZE, HEIGHT - 10 * TILE_SIZE, 6 * TILE_SIZE, 2 * TILE_SIZE),  
        pygame.Rect(10 * TILE_SIZE, HEIGHT - 14 * TILE_SIZE, 2 * TILE_SIZE, 2 * TILE_SIZE),  
    ],
    "walls": [
        pygame.Rect(11 * TILE_SIZE, HEIGHT - 4 * TILE_SIZE, TILE_SIZE, 2 * TILE_SIZE), 
        pygame.Rect(5 * TILE_SIZE, HEIGHT - 6 * TILE_SIZE, TILE_SIZE, 4 * TILE_SIZE),   
        pygame.Rect(17 * TILE_SIZE, HEIGHT - 6 * TILE_SIZE, TILE_SIZE, 4 * TILE_SIZE),  
    ],
    "fruits": [
        pygame.Rect(3 * TILE_SIZE, HEIGHT - 7 * TILE_SIZE, 30, 30),   
        pygame.Rect(17 * TILE_SIZE, HEIGHT - 7 * TILE_SIZE, 30, 30),  
        pygame.Rect(9 * TILE_SIZE, HEIGHT - 11 * TILE_SIZE, 30, 30),  
        pygame.Rect(11 * TILE_SIZE, HEIGHT - 15 * TILE_SIZE, 30, 30), 
    ],
    "enemies": [
        pygame.Rect(5 * TILE_SIZE, HEIGHT - TILE_SIZE - 55, 80, 80),    
        pygame.Rect(9 * TILE_SIZE, HEIGHT - 10 * TILE_SIZE - 55, 80, 80),  
    ],

    "enemy_ranges": [
        (0, 15 * TILE_SIZE),                     
        (8 * TILE_SIZE, 13 * TILE_SIZE),              
    ],
},
]
def load_level(level_index):
    level_data = levels[level_index]
    platforms = level_data["platforms"]
    walls = level_data.get("walls", [])
    fruits = level_data["fruits"]
    enemies = level_data["enemies"]
    enemy_ranges = level_data["enemy_ranges"]
    platform_movements = level_data.get("platform_movements", [None for _ in platforms])

    if not enemy_ranges and enemies:
        enemy_ranges = []
        for enemy in enemies:
            for plat in platforms:
                if plat.y == enemy.y + enemy.height:  
                    enemy_ranges.append((plat.x, plat.x + plat.width))
                    break
    return platforms, walls, fruits, enemies, enemy_ranges, platform_movements

frame_collision_rects = [
    pygame.Rect(0, 0, WIDTH, 10),                   
    pygame.Rect(0, HEIGHT - 10, WIDTH, 10),          
    pygame.Rect(0, 0, 10, HEIGHT),                 
    pygame.Rect(WIDTH - 10, 0, 10, HEIGHT)          
]
player = pygame.Rect(1 * TILE_SIZE, HEIGHT - 3 * TILE_SIZE, TILE_SIZE, TILE_SIZE)
jump_count = 0
MAX_JUMPS = 2
jump_pressed = False
player_speed = 8
gravity = 1
velocity_y = 0
jumping = False

floor = pygame.Rect(0, HEIGHT - 15, WIDTH, 10)
platforms = [
    pygame.Rect(3 * TILE_SIZE, HEIGHT - 4 * TILE_SIZE, 5 * TILE_SIZE, 10),   
    pygame.Rect(9 * TILE_SIZE, HEIGHT - 7 * TILE_SIZE, 5 * TILE_SIZE, 10),   
    pygame.Rect(15 * TILE_SIZE, HEIGHT - 10 * TILE_SIZE, 5 * TILE_SIZE, 10), 
]

fruits = [
    pygame.Rect(4 * TILE_SIZE, HEIGHT - 5 * TILE_SIZE, 30, 30), 
    pygame.Rect(10 * TILE_SIZE, HEIGHT - 8 * TILE_SIZE, 30, 30), 
    pygame.Rect(16 * TILE_SIZE, HEIGHT - 11 * TILE_SIZE, 30, 30) 
]

total_fruits = len(fruits)
collected_fruits = 0

enemies = [
    pygame.Rect(5 * TILE_SIZE, HEIGHT - 5 * TILE_SIZE, 40, 40),  
    pygame.Rect(11 * TILE_SIZE, HEIGHT - 8 * TILE_SIZE, 40, 40), 
]
enemy_directions = [1, -1]
enemy_range = [
    (3 * TILE_SIZE, 7 * TILE_SIZE),
    (9 * TILE_SIZE, 13 * TILE_SIZE)
]

lives = 3
game_over = False
win = False

double_jump_timer = 0
DOUBLE_JUMP_DELAY = 400  
jump_pressed_time = 0

dj_sound.play(loops=-1)  
show_start_screen()
show_character_selection_screen()

player_right_frames = character_sets[selected_character_index]["run"]
player_left_frames = [pygame.transform.flip(frame, True, False) for frame in player_right_frames]
double_jump_frames = character_sets[selected_character_index]["jump"]
  

current_level_index = 0
platforms, walls, fruits, enemies, enemy_ranges,platform_movements = load_level(current_level_index)
import copy  
original_level_data = copy.deepcopy(levels[current_level_index])
enemy_directions = [1 for _ in enemies]
collected_fruits = 0
total_fruits = len(fruits)
while True:
    
   
    if current_level_index == 2:
        target_platform = platforms[4]  
        flag.x = target_platform.centerx - flag.width // 2
        flag.y = target_platform.top - flag.height
    

    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if restart_button_rect.collidepoint(event.pos):
                lives = 3

                
                levels[current_level_index] = copy.deepcopy(original_level_data)
                platforms, walls, fruits, enemies, enemy_ranges, platform_movements = load_level(current_level_index)

                
                enemy_directions = [1 for _ in enemies]
                player.x, player.y = 1 * TILE_SIZE, HEIGHT - 3 * TILE_SIZE
                collected_fruits = 0
                total_fruits = len(fruits)
                flag.x = WIDTH - 100
                flag.y = HEIGHT - TILE_SIZE - 70

                
                player_frame_index = 0
                carrot_frame_index = 0
                enemy_frame_index = 0
                flag_frame_index = 0

                game_over = False
                win = False
            elif home_button_rect.collidepoint(event.pos):
                lives = 3
                show_start_screen()
                current_level_index = 0

                
                levels[current_level_index] = copy.deepcopy(original_level_data)
                platforms, walls, fruits, enemies, enemy_ranges, platform_movements = load_level(current_level_index)

                enemy_directions = [1 for _ in enemies]
                player.x, player.y = 1 * TILE_SIZE, HEIGHT - 3 * TILE_SIZE
                collected_fruits = 0
                total_fruits = len(fruits)
                flag.x = WIDTH - 100
                flag.y = HEIGHT - TILE_SIZE - 70

                
                player_frame_index = 0
                carrot_frame_index = 0
                enemy_frame_index = 0
                flag_frame_index = 0

                game_over = False
                win = False

            elif next_level_button_rect.collidepoint(event.pos):
                current_level_index += 1
                if current_level_index < len(levels):
                    platforms, walls, fruits, enemies, enemy_ranges, platform_movements = load_level(current_level_index)
                    enemy_directions = [1 for _ in enemies]
                    player.x, player.y = 1 * TILE_SIZE, HEIGHT - 3 * TILE_SIZE
                    collected_fruits = 0
                    total_fruits = len(fruits)
                    game_over = False
                    win = False

                    
                    if current_level_index == 2:
                        flag.x = 17 * TILE_SIZE
                        flag.y = HEIGHT - 3 * TILE_SIZE - flag.height  
                else:
                    win = True

    if game_over:
        screen.fill(BLACK)
        screen.blit(full_game_over_image, (0, 0))

        big_font = pygame.font.Font("assets/font/PixelEmulator3.otf", 80)
        game_over_text = big_font.render("GAME OVER!", True, RED)
        game_over_text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(game_over_text, game_over_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        continue


    if win:
        screen.fill(WHITE)
        win_image = pygame.image.load("assets/background/You win.png")
        win_image = pygame.transform.scale(win_image, (WIDTH, HEIGHT))  
        screen.blit(win_image, (0, 0))

        big_font = pygame.font.Font("assets/font/PixelEmulator3.otf", 80)
        win_text = big_font.render("YOU WIN!", True, WHITE)
        win_text_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(win_text, win_text_rect)
        small_font = pygame.font.Font("assets/font/PixelEmulator3.otf", 30)

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_r:
                        # Oyunu yeniden başlat
                        current_level_index = 0
                        platforms, walls, fruits, enemies, enemy_ranges, platform_movements = load_level(current_level_index)
                        enemy_directions = [1 for _ in enemies]
                        player.x, player.y = 1 * TILE_SIZE, HEIGHT - 3 * TILE_SIZE
                        collected_fruits = 0
                        total_fruits = len(fruits)
                        game_over = False
                        win = False
                        waiting = False  

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed
        player_direction_right = False
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
        player_direction_right = True

    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH
    for i, movement in enumerate(platform_movements):
        if movement:
            plat = platforms[i]
            plat.x += movement["direction"] * movement["speed"]
            if plat.x < movement["range"][0] or plat.x + plat.width > movement["range"][1]:
                movement["direction"] *= -1

    current_time = pygame.time.get_ticks()

    if keys[pygame.K_SPACE]:
        if not jump_pressed:
            if jump_count == 0:
                velocity_y = -18
                jumping = True
                jump_count = 1
                jump_pressed_time = current_time
                jump_sound.play() 
            elif jump_count == 1 and current_time - jump_pressed_time <= DOUBLE_JUMP_DELAY:
                velocity_y = -18
                jumping = True
                jump_count = 2
                jump_sound.play() 
            jump_pressed = True

    else:
        jump_pressed = False

    velocity_y += gravity
    player.y += velocity_y
    if player.colliderect(floor):
        player.y = floor.top - player.height
        velocity_y = 0
        jumping = False
        jump_count = 0
    for plat in platforms:
        if player.colliderect(plat):
            if velocity_y > 0:
                player.y = plat.top - player.height
                velocity_y = 0
                jumping = False
                jump_count = 0
                jump_pressed_time = 0  

            elif velocity_y < 0: 
                player.y = plat.bottom
                velocity_y = 0  
    for border in frame_collision_rects:
        if player.colliderect(border):
          
            if player.right > border.left and player.left < border.left:
                player.right = border.left
            elif player.left < border.right and player.right > border.right:
                player.left = border.right
            if player.top < border.bottom and player.bottom > border.bottom:
                player.top = border.bottom
                velocity_y = 0
            elif player.bottom > border.top and player.top < border.top:
                player.bottom = border.top
                velocity_y = 0
                jumping = False
                jump_count = 0


    for extra_plat in extra_tile_platforms:
        if player.colliderect(extra_plat):
            if velocity_y > 0:
                player.y = extra_plat.top - player.height
                velocity_y = 0
                jumping = False
                jump_count = 0
                jump_pressed_time = 0
            elif velocity_y < 0:
                player.y = extra_plat.bottom
                velocity_y = 0
    for wall in walls:
        if player.colliderect(wall):
            if player.right > wall.left and player.left < wall.left:
                player.right = wall.left
            elif player.left < wall.right and player.right > wall.right:
                player.left = wall.right 

    for i, enemy in enumerate(enemies):
        
        if current_level_index == 1:
            enemy.x += enemy_directions[i] * 4  
        elif current_level_index == 2:
            enemy.x += enemy_directions[i] * 3 
        else:
            enemy.x += enemy_directions[i] * 1  


        if enemy.x < enemy_ranges[i][0] or enemy.x > enemy_ranges[i][1]:
            enemy_directions[i] *= -1


    for enemy in enemies:
        
        distance = ((player.centerx - enemy.centerx) ** 2 + (player.centery - enemy.centery) ** 2) ** 0.5
        if distance < 15:  
            lives -= 1
            pygame.time.delay(1000)
            player.x, player.y = 1 * TILE_SIZE, HEIGHT - 3 * TILE_SIZE
            if lives <= 0:
                game_over = True

    for fruit in fruits[:]:
        if player.colliderect(fruit):
            fruits.remove(fruit)
            collected_fruits += 1

    if not fruits and player.colliderect(flag):
        if current_level_index + 1 < len(levels):
            current_level_index += 1
            platforms, walls, fruits, enemies, enemy_ranges, platform_movements = load_level(current_level_index)
            enemy_directions = [1 for _ in enemies]
            player.x, player.y = 1 * TILE_SIZE, HEIGHT - 3 * TILE_SIZE
            collected_fruits = 0
            total_fruits = len(fruits)
        else:
            win = True
            continue  



    if player.colliderect(flag) and fruits:
        info_text = font.render("Önce tüm meyveleri topla!", True, WHITE)
        screen.blit(info_text, (WIDTH // 2 - info_text.get_width() // 2, HEIGHT // 2 - 50))
    elif player.colliderect(flag) and not fruits:
        current_level_index += 1
        if current_level_index < len(levels):
            platforms, walls, fruits, enemies, enemy_ranges, platform_movements = load_level(current_level_index)
            enemy_directions = [1 for _ in enemies]
            player.x, player.y = 1 * TILE_SIZE, HEIGHT - 3 * TILE_SIZE
            collected_fruits = 0
            total_fruits = len(fruits)
           
        else:
            win = True

    if current_level_index == 1:
        enemy_frame_index += chicken_animation_speed
        if enemy_frame_index >= len(chicken_right_frames):
            enemy_frame_index = 0
    else:
        enemy_frame_index += enemy_animation_speed
        if enemy_frame_index >= len(enemy_right_frames):
            enemy_frame_index = 0


    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        player_frame_index += player_animation_speed
        if player_frame_index >= len(player_right_frames):
            player_frame_index = 0

    if current_level_index == 1:
        carrot_frame_index += apple_animation_speed
        if carrot_frame_index >= len(apple_frames):
            carrot_frame_index = 0
    else:
        carrot_frame_index += carrot_animation_speed
        if carrot_frame_index >= len(carrot_frames):
            carrot_frame_index = 0

    if current_level_index == 1:
        screen.blit(level2_background, (0, 0))
    elif current_level_index == 2:
        screen.blit(dark_background, (0, 0))
    else:
        screen.blit(game_background, (0, 0))
    
    for plat in platforms:
        if current_level_index == 1:
            for row in range(plat.height // TILE_SIZE):
                for col in range(plat.width // TILE_SIZE):
                    if row == 0: 
                        tile = green_tile_image
                    else:  
                        tile = brown_tile_image
                    screen.blit(tile, (plat.x + col * TILE_SIZE, plat.y + row * TILE_SIZE))
        elif current_level_index == 0:  
            for x in range(plat.x, plat.x + plat.width, TILE_SIZE):
                screen.blit(platform_tile_image, (x, plat.y))
        elif current_level_index == 2:
            for col in range(plat.width // TILE_SIZE):
                draw_tunnel_platform(plat)
                    
    draw_frame(screen)

    RIGHT_MARGIN_X = WIDTH - TILE_SIZE + 10
    TOP_MARGIN_Y = TILE_SIZE + 10

    level_text = font.render(f"Level {current_level_index + 1}", True, BLACK)
    level_text_rect = level_text.get_rect(topright=(RIGHT_MARGIN_X - 10, TOP_MARGIN_Y))
    screen.blit(level_text, level_text_rect)

    home_x = RIGHT_MARGIN_X - home_button_image.get_width() - 10

    restart_x = home_x - restart_button_image.get_width() - 10
    screen.blit(home_button_image, (home_x, TOP_MARGIN_Y + 40))
    screen.blit(restart_button_image, (restart_x, TOP_MARGIN_Y + 40))

    next_level_x = restart_x - next_level_button_image.get_width() - 10
    screen.blit(next_level_button_image, (next_level_x, TOP_MARGIN_Y + 40))
    next_level_button_rect.topleft = (next_level_x, TOP_MARGIN_Y + 40)

    home_button_rect.topleft = (home_x, TOP_MARGIN_Y + 40)
    restart_button_rect.topleft = (restart_x, TOP_MARGIN_Y + 40)

    flag_frame_index += flag_animation_speed
    if flag_frame_index >= len(flag_frames):
        flag_frame_index = 0
    screen.blit(flag_frames[int(flag_frame_index)], (flag.x, flag.y))

    if jump_count == 2:
        player_frame_index += player_animation_speed
        if player_frame_index >= len(double_jump_frames):
            player_frame_index = 0
        frame_index = int(player_frame_index)
        screen.blit(double_jump_frames[frame_index], (player.x, player.y))

    


