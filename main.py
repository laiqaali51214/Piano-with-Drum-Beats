import pygame
import keys
from pygame import mixer # audio management
# from matplotlib import colors

pygame.init() # initializing pygame modules
# Initializing the mixer
pygame.mixer.init()
pygame.mixer.set_num_channels(50) # 50 simultaneous audios

large_font = pygame.font.Font('files/calibrib.ttf', 90)
semi_large_font = pygame.font.Font('files/calibrib.ttf', 36)
medium_font = pygame.font.Font('files/calibrib.ttf', 30)
small_font = pygame.font.Font('files/calibrib.ttf', 18)
real_small_font = pygame.font.Font('files/calibrib.ttf', 12)
fps = 60 # frames per second for window resolution
timer = pygame.time.Clock()
WIDTH = 52 * 35 # 1820
HEIGHT = 640
window = pygame.display.set_mode([WIDTH, HEIGHT])
white_sounds = []
black_sounds = []
active_whites = []
active_blacks = []

# octaves
left_oct = 4
right_oct = 5

left_hand = keys.left_hand
right_hand = keys.right_hand
piano_notes = keys.piano_notes
white_notes = keys.white_notes
black_notes = keys.black_notes
black_labels = keys.black_labels

for i in range(len(white_notes)):
    white_sounds.append(mixer.Sound(f'files\\audios\\{white_notes[i]}.wav'))

for i in range(len(black_notes)):
    black_sounds.append(mixer.Sound(f'files\\audios\\{black_notes[i]}.wav'))

pygame.display.set_caption("Piano")


def draw_button(screen, color, x, y, width, height, text, text_color, font):
    pygame.draw.rect(screen, color, (x, y, width, height), 100, 8)

    font = pygame.font.Font(None, font)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width // 2, y + height // 2)
    screen.blit(text_surface, text_rect)
    return text_rect  # Return button's rect for click detection


def draw_piano(whites, blacks):
    white_rects = []

    # 52 white keys
    for i in range(52):
        rect = pygame.draw.rect(window, 'light blue', [i * 35, HEIGHT - 300, 35, 300], 0, 2)
        white_rects.append(rect)
        pygame.draw.rect(window, 'black', [i * 35, HEIGHT - 300, 35, 300], 2, 2)
        key_label = small_font.render(white_notes[i], True, 'black')
        window.blit(key_label, (i * 35 + 3, HEIGHT - 20))

    # Add a button below the piano keys
    button_x = 1100
    button_y = 250
    button_width = 100
    button_height = 50
    button_color = 'steel blue'  # Choose your button color
    button_text = "Anthem"
    button_text_color = 'white'  # Choose text color
    button_font_size = 30

    button_x2 = 1300
    button_y2 = 250
    button_text2 = "Believer"

    global button_anthem, button_believer
    button_anthem = draw_button(window, button_color, button_x, button_y,
                                button_width, button_height, button_text, button_text_color, button_font_size)

    button_believer = draw_button(window, button_color, button_x2, button_y2,
                                  button_width, button_height, button_text2, button_text_color, button_font_size)
    skip_count = 0
    last_skip = 2
    skip_track = 2
    black_rects = []

    # 36 black keys
    for i in range(36):
        rect = pygame.draw.rect(window, 'dark blue', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 0, 2)
        for q in range(len(blacks)):
            if blacks[q][0] == i:
                if blacks[q][1] > 0:
                    pygame.draw.rect(window, 'red', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 2, 2)
                    blacks[q][1] -= 1

        key_label = real_small_font.render(black_labels[i], True, 'white')
        window.blit(key_label, (25 + (i * 35) + (skip_count * 35), HEIGHT - 120))
        black_rects.append(rect)
        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1

    for i in range(len(whites)):
        if whites[i][1] > 0:
            j = whites[i][0]
            # pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
            pygame.draw.rect(window, 'red', [j * 35, HEIGHT - 100, 35, 100], 2, 2)
            whites[i][1] -= 1



    return white_rects, black_rects, whites, blacks


def draw_hands(right_octave, left_octave, right_side, left_side):
    # left side
    text = small_font.render(left_side[0], True, 'black')
    window.blit(text, ((left_octave * 245) - 165, HEIGHT - 90))
    text = small_font.render(left_side[2], True, 'black')
    window.blit(text, ((left_octave * 245) - 130, HEIGHT - 90))
    text = small_font.render(left_side[4], True, 'black')
    window.blit(text, ((left_octave * 245) - 95, HEIGHT - 90))
    text = small_font.render(left_side[5], True, 'black')
    window.blit(text, ((left_octave * 245) - 60, HEIGHT - 90))
    text = small_font.render(left_side[7], True, 'black')
    window.blit(text, ((left_octave * 245) - 25, HEIGHT - 90))
    text = small_font.render(left_side[9], True, 'black')
    window.blit(text, ((left_octave * 245) + 10, HEIGHT - 90))
    text = small_font.render(left_side[11], True, 'black')
    window.blit(text, ((left_octave * 245) + 45, HEIGHT - 90))
    text = small_font.render(left_side[1], True, 'white')
    window.blit(text, ((left_octave * 245) - 148, HEIGHT - 195))
    text = small_font.render(left_side[3], True, 'white')
    window.blit(text, ((left_octave * 245) - 113, HEIGHT - 195))
    text = small_font.render(left_side[6], True, 'white')
    window.blit(text, ((left_octave * 245) - 43, HEIGHT - 195))
    text = small_font.render(left_side[8], True, 'white')
    window.blit(text, ((left_octave * 245) - 8, HEIGHT - 195))
    text = small_font.render(left_side[10], True, 'white')
    window.blit(text, ((left_octave * 245) + 27, HEIGHT - 195))

    # right side
    text = small_font.render(right_side[0], True, 'black')
    window.blit(text, ((right_octave * 245) - 165, HEIGHT - 90))
    text = small_font.render(right_side[2], True, 'black')
    window.blit(text, ((right_octave * 245) - 130, HEIGHT - 90))
    text = small_font.render(right_side[4], True, 'black')
    window.blit(text, ((right_octave * 245) - 95, HEIGHT - 90))
    text = small_font.render(right_side[5], True, 'black')
    window.blit(text, ((right_octave * 245) - 60, HEIGHT - 90))
    text = small_font.render(right_side[7], True, 'black')
    window.blit(text, ((right_octave * 245) - 25, HEIGHT - 90))
    text = small_font.render(right_side[9], True, 'black')
    window.blit(text, ((right_octave * 245) + 10, HEIGHT - 90))
    text = small_font.render(right_side[11], True, 'black')
    window.blit(text, ((right_octave * 245) + 45, HEIGHT - 90))
    text = small_font.render(right_side[1], True, 'white')
    window.blit(text, ((right_octave * 245) - 148, HEIGHT - 195))
    text = small_font.render(right_side[3], True, 'white')
    window.blit(text, ((right_octave * 245) - 113, HEIGHT - 195))
    text = small_font.render(right_side[6], True, 'white')
    window.blit(text, ((right_octave * 245) - 43, HEIGHT - 195))
    text = small_font.render(right_side[8], True, 'white')
    window.blit(text, ((right_octave * 245) - 8, HEIGHT - 195))
    text = small_font.render(right_side[10], True, 'white')
    window.blit(text, ((right_octave * 245) + 27, HEIGHT - 195))


def draw_title_bar():
    instruction_text = semi_large_font.render('Instructions:', True, 'black')
    window.blit(instruction_text, (WIDTH - 800, 30))
    instruction_text1 = medium_font.render('Press Right Arrow for High Notes', True, 'black')
    window.blit(instruction_text1, (WIDTH - 800, 80))
    instruction_text2 = medium_font.render('Press Left Arrow for Low Notes', True, 'black')
    window.blit(instruction_text2, (WIDTH - 800, 120))
    instruction_text3 = medium_font.render('Press Space to stop drums', True, 'black')
    window.blit(instruction_text3, (WIDTH - 800, 160))
    instruction_text3 = medium_font.render('Click on song to play drums', True, 'black')
    window.blit(instruction_text3, (WIDTH - 800, 200))

    # logo
    img = pygame.transform.scale(pygame.image.load('files/logo.png'), [250, 250])
    window.blit(img, (300, -30))
    title_text = large_font.render('Piano!', True, 'white')
    window.blit(title_text, (318, 198))
    title_text = large_font.render('Piano!', True, 'black')
    window.blit(title_text, (320, 200))


running = True
while running:
    left_mapping = {'I': f'C{left_oct}',
                 '9': f'C#{left_oct}',
                 'O': f'D{left_oct}',
                 '0': f'D#{left_oct}',
                 'P': f'E{left_oct}',
                 'Z': f'F{left_oct}',
                 'S': f'F#{left_oct}',
                 'X': f'G{left_oct}',
                 'D': f'G#{left_oct}',
                 'C': f'A{left_oct}',
                 'F': f'A#{left_oct}',
                 'V': f'B{left_oct}'}

    right_mapping = {'B': f'C{right_oct}',
                  'H': f'C#{right_oct}',
                  'N': f'D{right_oct}',
                  'J': f'D#{right_oct}',
                  'M': f'E{right_oct}',
                  ',': f'F{right_oct}',
                  'L': f'F#{right_oct}',
                  '.': f'G{right_oct}',
                  ';': f'G#{right_oct}',
                  '/': f'A{right_oct}',
                  '\'': f'A#{right_oct}',
                  '\\': f'B{right_oct}'}
    timer.tick(fps)
    window.fill('sky blue')

    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)
    draw_hands(right_oct, left_oct, right_hand, left_hand)
    draw_title_bar()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            black_key = False
            for i in range(len(black_keys)):
                if black_keys[i].collidepoint(event.pos):
                    black_sounds[i].play(0, 1000)
                    black_key = True
                    active_blacks.append([i, 30])
            for i in range(len(white_keys)):
                if white_keys[i].collidepoint(event.pos) and not black_key:
                    white_sounds[i].play(0, 3000)
                    active_whites.append([i, 30])
        if event.type == pygame.TEXTINPUT:
            if event.text.upper() in left_mapping:
                if left_mapping[event.text.upper()][1] == '#':
                    index = black_labels.index(left_mapping[event.text.upper()])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                else:
                    index = white_notes.index(left_mapping[event.text.upper()])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])
            if event.text.upper() in right_mapping:
                if right_mapping[event.text.upper()][1] == '#':
                    index = black_labels.index(right_mapping[event.text.upper()])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                else:
                    index = white_notes.index(right_mapping[event.text.upper()])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])


        sound = None

        # Check for keyboard events

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_anthem.collidepoint(mouse_pos):
                sound = pygame.mixer.Sound('files\\audios\\anthem.wav')  # Load your audio file
                sound.set_volume(0.2)
                sound.play()  # Play the loaded sound
                pygame.time.delay(5000)
            if button_believer.collidepoint(mouse_pos):
                sound = pygame.mixer.Sound('files\\audios\\believer.wav')  # Load your audio file
                sound.set_volume(0.5)
                sound.play()  # Play the loaded sound
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:  # Change to the key you want to use
                pygame.mixer.init()  # Initialize the mixer
                if sound is not None:
                    sound.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.pause()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if right_oct < 8:
                    left_oct +=1
                    right_oct += 1
            if event.key == pygame.K_LEFT:
                if right_oct > 0:
                    left_oct -=1
                    right_oct -= 1

    pygame.display.flip()
pygame.quit()