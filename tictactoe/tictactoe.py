import pygame
from pygame.locals import *
import sys
from time import sleep

pygame.init()
white = (255, 255, 255)
black = (1, 1, 1)
DISP_X = 300
DISP_Y = 300
font = pygame.font.SysFont("monospace", 24)
player_turn = 0
label = None
game_over = False

o_set = set([])
x_set = set([])
win_set = (
    set([1, 2, 3]), set([4, 5, 6]), set([7, 8, 9]),
    set([1, 4, 7]), set([2, 5, 8]), set([3, 6, 9]),
    set([1, 5, 9]), set([3, 5, 7])
)

screen = pygame.display.set_mode((DISP_X, DISP_Y))
space1 = (DISP_X * 2 / 8, DISP_Y * 2 / 8)
space2 = (DISP_X * 4 / 8, DISP_Y * 2 / 8)
space3 = (DISP_X * 6 / 8, DISP_Y * 2 / 8)
space4 = (DISP_X * 2 / 8, DISP_Y * 4 / 8)
space5 = (DISP_X * 4 / 8, DISP_Y * 4 / 8)
space6 = (DISP_X * 6 / 8, DISP_Y * 4 / 8)
space7 = (DISP_X * 2 / 8, DISP_Y * 6 / 8)
space8 = (DISP_X * 4 / 8, DISP_Y * 6 / 8)
space9 = (DISP_X * 6 / 8, DISP_Y * 6 / 8)


def center_of_space(click_pos):
    """Takes position of a click and returns the location of the center of the
        space along with the space number to store in the player's array."""
    if DISP_X * 1 / 8 < click_pos[0] and click_pos[0] < DISP_X * 3 / 8:
        if DISP_Y * 1 / 8 < click_pos[1] and click_pos[1] < DISP_Y * 3 / 8:
            return (space1, 1)
        elif DISP_Y * 3 / 8 < click_pos[1] and click_pos[1] < DISP_Y * 5 / 8:
            return (space4, 4)
        elif DISP_Y * 5 / 8 < click_pos[1] and click_pos[1] < DISP_Y * 7 / 8:
            return (space7, 7)
    elif DISP_X * 3 / 8 < click_pos[0] and click_pos[0] < DISP_X * 5 / 8:
        if DISP_Y * 1 / 8 < click_pos[1] and click_pos[1] < DISP_Y * 3 / 8:
            return (space2, 2)
        elif DISP_Y * 3 / 8 < click_pos[1] and click_pos[1] < DISP_Y * 5 / 8:
            return (space5, 5)
        elif DISP_Y * 5 / 8 < click_pos[1] and click_pos[1] < DISP_Y * 7 / 8:
            return (space8, 8)
    elif DISP_X * 5 / 8 < click_pos[0] and click_pos[0] < DISP_X * 7 / 8:
        if DISP_Y * 1 / 8 < click_pos[1] and click_pos[1] < DISP_Y * 3 / 8:
            return (space3, 3)
        elif DISP_Y * 3 / 8 < click_pos[1] and click_pos[1] < DISP_Y * 5 / 8:
            return (space6, 6)
        elif DISP_Y * 5 / 8 < click_pos[1] and click_pos[1] < DISP_Y * 7 / 8:
            return (space9, 9)
    else:
        return None


def draw(space_center):
    """Draws 'O' or 'X' on the screen."""
    if player_turn == 0:
        pygame.draw.circle(screen, white, space_center, 25)
        pygame.draw.circle(screen, black, space_center, 23)

    elif player_turn == 1:
        pygame.draw.line(screen, white,
                        (space_center[0] + DISP_X * 1 / 16,
                         space_center[1] + DISP_Y * 1 / 16),
                        (space_center[0] - DISP_X * 1 / 16,
                         space_center[1] - DISP_Y * 1 / 16), 3)
        pygame.draw.line(screen, white,
                        (space_center[0] + DISP_X * 1 / 16,
                         space_center[1] - DISP_Y * 1 / 16),
                        (space_center[0] - DISP_X * 1 / 16,
                         space_center[1] + DISP_Y * 1 / 16), 3)

# draws board
pygame.draw.line(screen, white,
                (DISP_X * 3 / 8, DISP_Y * 1 / 8),
                (DISP_X * 3 / 8, DISP_Y * 7 / 8), 3)
pygame.draw.line(screen, white,
                (DISP_X * 5 / 8, DISP_Y * 1 / 8),
                (DISP_X * 5 / 8, DISP_Y * 7 / 8), 3)
pygame.draw.line(screen, white,
                (DISP_X * 1 / 8, DISP_Y * 3 / 8),
                (DISP_X * 7 / 8, DISP_Y * 3 / 8), 3)
pygame.draw.line(screen, white,
                (DISP_X * 1 / 8, DISP_Y * 5 / 8),
                (DISP_X * 7 / 8, DISP_Y * 5 / 8), 3)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            # Obtains the position of the mouse
            space = pygame.mouse.get_pos()
            space_center_tuple = center_of_space(space)
            if space_center_tuple is not None:
                space_center_loc, space_center_score = space_center_tuple
                draw(space_center_loc)
                player_turn = (player_turn + 1) % 2
                # Stores player's move in array
                if player_turn == 0:
                    o_set.add(space_center_score)
                elif player_turn == 1:
                    x_set.add(space_center_score)

    if player_turn == 0:
        label = font.render("Player Turn: O", 1, white)
    else:
        label = font.render("Player Turn: X", 1, white)

    if len(o_set) + len(x_set) == 9:
        label = font.render("Players tie!", 1, white)
        game_over = True

    for way in win_set:
        if way.issubset(o_set):
            label = font.render("Player X wins!", 1, white)
            game_over = True
        elif way.issubset(x_set):
            label = font.render("Player O wins!", 1, white)
            game_over = True

    screen.fill(black, (50, DISP_Y - 25, 200, 25))
    screen.blit(label, (50, DISP_Y - 25))

    pygame.display.update()

    if game_over:
        sleep(1)
        pygame.quit()
        sys.exit()
