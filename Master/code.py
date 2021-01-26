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
        menu_scene()

def menu_scene():
    # this function is the menu scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("sprites_and_background.bmp")

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("Big Brain Studios")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)
    
    # sets the background to image 0 in the image Bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
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
    
    # prepare sound
    damage_sound = open("damage.wav", 'rb')
    boop_sound = open("boop.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # for score
    score = 0
    
    score_text = stage.Text(width= 70, height = 14)
    score_text.clear()
    score_text.cursor(85, 0)
    score_text.move(1,1)
    score_text.text("Score: {0:05n}".format(score))


    def show_note():
        # this function takes a note from off the screen and moves it on screen
        for note_number in range(len(notes)):
            if notes[note_number].x < 0:
                lane_picked = randint(1, 4)
                notes[note_number].move(lane_picked * SPRITE_SIZE + constants.SPRITE_SIZE, constants.OFF_TOP_SCREEN)
                break

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("sprites_and_background.bmp")

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # sets the background to image 0 in the image Bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(sprites_and_background, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    # places the lanes on-screen
    for x_location in range(2, 5):
        for y_location in range(constants.SCREEN_GRID_Y - 1):
            background.tile(x_location, y_location, 7)

    # places target pads
    background.tile(2, y_location, 1)
    background.tile(3, y_location, 2)
    background.tile(4, y_location, 3)
    background.tile(5, y_location, 4)
    
    # places the rest of the screen
    for x_location in range(6, constants.SCREEN_GRID_Y):
        for y_location in range(constants.SCREEN_GRID_Y):
            background.tile(x_location, y_location, 8)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [score_text] + [background]
    # render the background and initial location of sprite list
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # A button to fire
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        # B button
        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
                
        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        # update game logic
        # play sound if A was just button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            # fire a laser, if we have enough power (have not used up all the lasers)
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x,ship.y)
                    sound.play(pew_sound)
                    break

        # each frame moves the lasers that have been fired up
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x,
                                          lasers[laser_number].y -
                                            constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)

        # each frame move the aliens down, that are on the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x,
                                          aliens[alien_number].y +
                                            constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    show_alien()
                    score -= 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0,0)
                    score_text.move(1,1)
                    score_text.text("Score: {0}".format(score))

        # each frame check if any of the lasers are touching any of the aliens
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                         lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                                         aliens[alien_number].x + 1, aliens[alien_number].y,
                                         aliens[alien_number].x + 15, aliens[alien_number].y + 15,):
                            # you hit an alien
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1,1)
                            score_text.text("Score: {0}".format(score))

        # each frame, check if any aliens are touching the space ship
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                if stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                                 aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                                 ship.x, ship.y,
                                 ship.x + 15, ship.y + 15):
                    # alien hit the ship
                    sound.stop()
                    sound.play(crash_sound)
                    time.sleep(3.0)
                    game_over_scene(score)

        # redraw Sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    splash_scene()



