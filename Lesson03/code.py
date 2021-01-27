#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on November 2020
# This program is the "Prance Prance Rebellion" game on the Pybadge


import ugame
import stage
import time
import random
import supervisor

import constants

def splash_scene():
    # this function is the splash scene

    # get sound ready
    whoosh_sound = open("whoosh.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(whoosh_sound)

    # image banks for CircuitPython
    splash_screen = stage.Bank.from_bmp16("splash_screen.bmp")

    # sets background
    background = stage.Grid(splash_screen, constants.SCREEN_X,
                            constants.SCREEN_Y)

    # background made up of 16 sprites and their coordinates
    background.tile(3, 2, 0)
    background.tile(4, 2, 1)
    background.tile(5, 2, 2)
    background.tile(6, 2, 3)

    background.tile(3, 3, 4) 
    background.tile(4, 3, 5)
    background.tile(5, 3, 6)
    background.tile(6, 3, 7)

    background.tile(3, 4, 8)
    background.tile(4, 4, 9) 
    background.tile(5, 4, 10)
    background.tile(6, 4, 11)

    background.tile(3, 5, 12)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 15)


    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers; right now, it is just the splash screen
    game.layers = [background]
    # render the background and initial location of sprite list
    game.render_block()

    # repeat forever, game loop
    while True:
        # Wait for 2 seconds
        time.sleep(2.0)
        menu_scene()

def menu_scene():
    # this function is the menu scene

    # image banks for CircuitPython
    image_bank = stage.Bank.from_bmp16("space_aliens.bmp")

    # add text objects
    text = []

    text1 = stage.Text(width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(15, 10)
    text1.text("Big Brain Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text2.move(37, 110)
    text2.text("PRESS START")
    text.append(text2)

    # sets the background to image 0 in the image Bank
    background = stage.Grid(image_bank, constants.SCREEN_X,
                            constants.SCREEN_Y)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items will show up in order
    game.layers = text + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        # Start button -> calls game scene function
        if keys & ugame.K_START != 0:
            game_scene()

    # update game logic
    game.tick() # wait until refresh rate finishes

def game_scene():
    # this function is the main game scene

    # health, score, combo
    text = []

    health = 3
    health_text = stage.Text(width=29, height=14)
    health_text.clear()
    health_text.move(5 * constants.SPRITE_SIZE,0)
    health_text.text("HP: {0}".format(health))
    text.append(health_text)

    score = 0
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.move(5 * constants.SPRITE_SIZE,10)
    score_text.text("Score: {0}".format(score))
    text.append(score_text)

    combo = 0
    combo_text = stage.Text(width=29, height=14)
    combo_text.clear()
    combo_text.move(5 * constants.SPRITE_SIZE,20)
    combo_text.text("Combo: {0}x".format(combo))
    text.append(combo_text)

    # imports image bank .bmp file
    image_bank = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # sets the background to image 0 in the image Bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    # sets randomized starry background
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)

    # sets the lanes
    for x_location in range(1, 5):
        for y_location in range(constants.SCREEN_GRID_Y):
            background.tile(x_location, y_location, 4) # 4th element = straight ship

    # places target pads
    background.tile(1, constants.SCREEN_GRID_Y - 1, 8) # 8th element = chill squid
    background.tile(2, constants.SCREEN_GRID_Y - 1, 8)
    background.tile(3, constants.SCREEN_GRID_Y - 1, 8)
    background.tile(4, constants.SCREEN_GRID_Y - 1, 8)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and initial location of sprite list
    game.render_block()

    # repeat forever, game loop
    while True:
        pass # placeholder

if __name__ == "__main__":
    splash_scene()
