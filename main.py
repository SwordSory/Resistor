import pygame
from pygame.locals import *
import os

pygame.init()


# Function_to_extract_path
def assets_pather(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


width, height = 1080, 542
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Resistor App")
icon = pygame.image.load(assets_pather("Assets/icon.png"))
pygame.display.set_icon(icon)
font = pygame.font.Font(None, 60)
clock = pygame.time.Clock()

background = pygame.image.load(assets_pather("Assets/display.png"))

# Table
colors = [
    ("Black", 1, 0, 250),
    ("Brown", 10, 1, 100),
    ("Red", 100, 2, 50),
    ((255, 165, 0), 1000, 0, 15),  # Orange
    ("Yellow", 10000, 0, 25),
    ("Green", 100000, 0.5, 20),
    ("Blue", 1000000, 0.25, 10),
    ((238, 130, 238), 0, 0.1, 5),  # Viloet
    ("Gray", 0, 0, 1),
    ("White", 0, 0, 0),
    ((255, 215, 0), 0, 5, 0),  # Gold
    ((224, 224, 224), 0, 10, 0),  # Silver
    ((250, 190, 142), 0, 0, 0),
]  # No Color

# Corresponding_Band
initial_values = [8, 3, 5, 6, 10, 3]

# Clicking_Rects
selection_rectangles = [
    [pygame.Rect(4, 297, 164, 43), False],
    [pygame.Rect(176, 296, 166, 43), False],
    [pygame.Rect(349, 297, 164, 43), False],
    [pygame.Rect(522, 297, 188, 42), False],
    [pygame.Rect(719, 297, 174, 42), False],
    [pygame.Rect(905, 297, 162, 43), False],
]

# Rects_for_diagram
figure_rectangles = [
    (214, 23, 25, 144),
    (285, 28, 25, 134),
    (338, 28, 25, 134),
    (391, 28, 25, 134),
    (462, 28, 25, 134),
    (534, 23, 25, 144),
]


# Rects_for_Choosing_color

band1_checker_rects = [
    [pygame.Rect(825, 0, 200, 20), 0],
    [pygame.Rect(825, 20, 200, 20), 1],
    [pygame.Rect(825, 40, 200, 20), 2],
    [pygame.Rect(825, 60, 200, 20), 3],
    [pygame.Rect(825, 80, 200, 20), 4],
    [pygame.Rect(825, 100, 200, 20), 5],
    [pygame.Rect(825, 120, 200, 20), 6],
    [pygame.Rect(825, 140, 200, 20), 7],
    [pygame.Rect(825, 160, 200, 20), 8],
    [pygame.Rect(825, 180, 200, 20), 9],
    [pygame.Rect(825, 200, 200, 20), 12],
]

band2_3_checker_rects = [
    [pygame.Rect(825, 0, 200, 20), 0],
    [pygame.Rect(825, 20, 200, 20), 1],
    [pygame.Rect(825, 40, 200, 20), 2],
    [pygame.Rect(825, 60, 200, 20), 3],
    [pygame.Rect(825, 80, 200, 20), 4],
    [pygame.Rect(825, 100, 200, 20), 5],
    [pygame.Rect(825, 120, 200, 20), 6],
    [pygame.Rect(825, 140, 200, 20), 7],
    [pygame.Rect(825, 160, 200, 20), 8],
    [pygame.Rect(825, 180, 200, 20), 9],
]

multiplier_checker_rects = [
    [pygame.Rect(825, 0, 200, 20), 0],
    [pygame.Rect(825, 20, 200, 20), 1],
    [pygame.Rect(825, 40, 200, 20), 2],
    [pygame.Rect(825, 60, 200, 20), 3],
    [pygame.Rect(825, 80, 200, 20), 4],
    [pygame.Rect(825, 100, 200, 20), 5],
    [pygame.Rect(825, 120, 200, 20), 6],
]

tolerance_checker_rects = [
    [pygame.Rect(825, 0, 200, 20), 1],
    [pygame.Rect(825, 20, 200, 20), 2],
    [pygame.Rect(825, 40, 200, 20), 5],
    [pygame.Rect(825, 60, 200, 20), 6],
    [pygame.Rect(825, 80, 200, 20), 7],
    [pygame.Rect(825, 100, 200, 20), 10],
    [pygame.Rect(825, 120, 200, 20), 11],
]

temp_coef_checker_rects = [
    [pygame.Rect(825, 0, 200, 20), 0],
    [pygame.Rect(825, 20, 200, 20), 1],
    [pygame.Rect(825, 40, 200, 20), 2],
    [pygame.Rect(825, 60, 200, 20), 3],
    [pygame.Rect(825, 80, 200, 20), 4],
    [pygame.Rect(825, 100, 200, 20), 5],
    [pygame.Rect(825, 120, 200, 20), 6],
    [pygame.Rect(825, 140, 200, 20), 7],
    [pygame.Rect(825, 160, 200, 20), 8],
    [pygame.Rect(825, 180, 200, 20), 12],
]


active_color = (255, 102, 102)
passive_color = (105, 105, 105)
all_status = False
Calculate = True


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == VIDEORESIZE:
            pygame.display.set_mode((width, height))

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if not all_status and event.button == 1:  # activating_Bands

                if selection_rectangles[0][0].collidepoint(mouse_pos):
                    selection_rectangles[0][1] = True
                    all_status = True

                elif selection_rectangles[1][0].collidepoint(mouse_pos):
                    selection_rectangles[1][1] = True
                    all_status = True

                elif selection_rectangles[2][0].collidepoint(mouse_pos):
                    selection_rectangles[2][1] = True
                    all_status = True

                elif selection_rectangles[3][0].collidepoint(mouse_pos):
                    selection_rectangles[3][1] = True
                    all_status = True

                elif selection_rectangles[4][0].collidepoint(mouse_pos):
                    selection_rectangles[4][1] = True
                    all_status = True

                elif selection_rectangles[5][0].collidepoint(mouse_pos):
                    selection_rectangles[5][1] = True
                    all_status = True

            # Working_with_activated_bands
            if selection_rectangles[0][1] and event.button == 1:
                for rect, i in band1_checker_rects:
                    if rect.collidepoint(mouse_pos):
                        initial_values[0] = i
                        selection_rectangles[0][1] = False
                        all_status = False
                        Calculate = True

            elif selection_rectangles[1][1] and event.button == 1:
                for rect, i in band2_3_checker_rects:
                    if rect.collidepoint(mouse_pos):
                        initial_values[1] = i
                        selection_rectangles[1][1] = False
                        all_status = False
                        Calculate = True

            elif selection_rectangles[2][1] and event.button == 1:
                for rect, i in band2_3_checker_rects:
                    if rect.collidepoint(mouse_pos):
                        initial_values[2] = i
                        selection_rectangles[2][1] = False
                        all_status = False
                        Calculate = True

            elif selection_rectangles[3][1] and event.button == 1:
                for rect, i in multiplier_checker_rects:
                    if rect.collidepoint(mouse_pos):
                        initial_values[3] = i
                        selection_rectangles[3][1] = False
                        all_status = False
                        Calculate = True

            elif selection_rectangles[4][1] and event.button == 1:
                for rect, i in tolerance_checker_rects:
                    if rect.collidepoint(mouse_pos):
                        initial_values[4] = i
                        selection_rectangles[4][1] = False
                        all_status = False
                        Calculate = True

            elif selection_rectangles[5][1] and event.button == 1:
                for rect, i in temp_coef_checker_rects:
                    if rect.collidepoint(mouse_pos):
                        initial_values[5] = i
                        selection_rectangles[5][1] = False
                        all_status = False
                        Calculate = True

    screen.blit(background, (0, 0))

    if Calculate:
        if initial_values[0] != 12:
            resistance = (
                initial_values[0] * 100 + initial_values[1] * 10 + initial_values[2]
            ) * colors[initial_values[3]][1]
        else:
            resistance = (
                0 * 100 + initial_values[1] * 10 + initial_values[2]
            ) * colors[initial_values[3]][1]
        tolerance = colors[initial_values[4]][2]

        if initial_values[5] == 12:
            temp_coef = "NA"
        else:
            temp_coef = colors[initial_values[5]][3]

        Calculate = False

    for i, (rect, status) in enumerate(selection_rectangles):
        color = colors[initial_values[i]][0]
        pygame.draw.rect(screen, color, rect)

        if status:
            pygame.draw.rect(screen, active_color, rect, 5)
        else:
            pygame.draw.rect(screen, passive_color, rect, 5)

    for i, rect in enumerate(figure_rectangles):
        color = colors[initial_values[i]][0]
        pygame.draw.rect(screen, color, rect)

    resistance_render = font.render(str(resistance) + " Ω", True, "White")
    tolerance_render = font.render("±" + str(tolerance) + "%", True, "White")
    temp_coef_render = font.render(str(temp_coef), True, "White")

    screen.blit(resistance_render, (200, 380))
    screen.blit(tolerance_render, (200, 440))
    screen.blit(temp_coef_render, (200, 500))

    # Showing_Value_changer_rects
    if selection_rectangles[0][1]:
        for rect, i in band1_checker_rects:
            pygame.draw.rect(screen, colors[i][0], pygame.Rect(rect))
        pygame.draw.rect(screen, passive_color, (825, 0, 200, 220), 5)

    elif selection_rectangles[1][1]:
        for rect, i in band2_3_checker_rects:
            pygame.draw.rect(screen, colors[i][0], pygame.Rect(rect))
        pygame.draw.rect(screen, passive_color, (825, 0, 200, 200), 5)

    elif selection_rectangles[2][1]:
        for rect, i in band2_3_checker_rects:
            pygame.draw.rect(screen, colors[i][0], pygame.Rect(rect))
        pygame.draw.rect(screen, passive_color, (825, 0, 200, 200), 5)

    elif selection_rectangles[3][1]:
        for rect, i in multiplier_checker_rects:
            pygame.draw.rect(screen, colors[i][0], pygame.Rect(rect))
        pygame.draw.rect(screen, passive_color, (825, 0, 200, 140), 5)

    elif selection_rectangles[4][1]:
        for rect, i in tolerance_checker_rects:
            pygame.draw.rect(screen, colors[i][0], pygame.Rect(rect))
        pygame.draw.rect(screen, passive_color, (825, 0, 200, 140), 5)

    elif selection_rectangles[5][1]:
        for rect, i in temp_coef_checker_rects:
            pygame.draw.rect(screen, colors[i][0], pygame.Rect(rect))
        pygame.draw.rect(screen, passive_color, (825, 0, 200, 200), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
