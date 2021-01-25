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
    splash_screen_background = stage.Bank.from_bmp16("splash_screen.bmp")

    # declare background
    background = stage.Grid(splash_screen_background, constants.SCREEN_X,
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

if __name__ == "__main__":
    splash_scene()
