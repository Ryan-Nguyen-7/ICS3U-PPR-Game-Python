#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on November 2020
# This program is the "Space Aliens" program on the Pybadge


import ugame
import stage

def splash_scene():
    # this function is the splash scene

    # image banks for CircuitPython
    splash_screen_background = stage.Bank.from_bmp16("splash_screen.bmp")

    # sets the background to image 0 in the image Bank
    background = stage.Grid(splash_screen_background, constants.SCREEN_X,
                            constants.SCREEN_Y)

    # background made up of 16 sprites and their coordinates
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items will show up in order
    game.layers = [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # calls menu scene
    while True:
        time.sleep(2.0)
        menu_scene()
def game_scene():
    # this function is the main game game_scene
  
    # prepare sound
    damage_sound = open("damage.wav", 'rb')
    boop_sound = open("boop.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # score
    score = 0
    
    score_text = stage.Text(width= 70, height = 14)
    score_text.clear()
    score_text.cursor(85, 0)
    score_text.move(1,1)
    score_text.text("Score: {0:05n}".format(score))

    def show_note():
        # this function takes an alien from off the screen and moves it on screen
        for note_number in range(len(notes)):
            if notes[note_number].x < 0:
                lane = randint(1, 4)
                notes[note_number].move(lane * SPRITE_SIZE, constants.OFF_TOP_SCREEN)
                break

    # image banks for CircuitPython

if __name__ == "__main__":
    splash_scene()
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



