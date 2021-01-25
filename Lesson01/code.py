#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on November 2020
# This program is the "Space Aliens" program on the Pybadge

# lesson 01 - Hello world

import ugame
import stage


def game_scene():
    # this function is the main game game_scene

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    
    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()

    # repeat forever, game loop
    while True:
        pass #  just a placeholder for now


if __name__ == "__main__":
    game_scene()
