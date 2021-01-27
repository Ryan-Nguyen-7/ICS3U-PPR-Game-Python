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
    # set the layers; right now, it is just the splah screen
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
    image_bank = stage.Bank.from_bmp16("sprites_and_background.bmp")

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("Big Brain Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)
    
    # sets the background to image 0 in the image Bank
    menu_background = stage.Grid(image_bank, constants.SCREEN_X,
                            constants.SCREEN_Y)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items will show up in order
    game.layers = text + [menu_background]
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

    # prepare sound
    damage_sound = open("damage.wav", 'rb')
    boop_sound = open("boop.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(boop_sound)

    # imports image bank .bmp file
    image_bank = stage.Bank.from_bmp16("sprites_and_background.bmp")

    # sets the background to image 0 in the image Bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    # places the lanes on-screen
    for x_location in range(1, 4):
        for y_location in range(constants.SCREEN_GRID_Y - 1):
            background.tile(x_location, y_location, 7)

    # places target pads
    background.tile(1, y_location, 1)
    background.tile(2, y_location, 2)
    background.tile(3, y_location, 3)
    background.tile(4, y_location, 4)
    
    # places the rest of the screen
    for x_location in range(5, constants.SCREEN_GRID_Y):
        for y_location in range(constants.SCREEN_GRID_Y):
            background.tile(x_location, y_location, 8)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and initial location of sprite list
    game.render_block()

    # repeat forever, game loop
    while True:
        game.tick()

if __name__ == "__main__":
    splash_scene()
