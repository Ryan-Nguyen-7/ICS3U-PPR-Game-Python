#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on January 2021
# This program is the "Prance Prance Rebellion" game on the Pybadge

import ugame
import stage
import time
import random
import supervisor

import constants


def splash_scene():
    # this function is the splash scene
    
    game_scene()
    
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
