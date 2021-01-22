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

    # prepare sound
    whoosh_sound = open("whoosh.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(whoosh_sound)
    
    
    def game_scene():
    # this function is the main game game_scene
    
    # define sound
    damage_sound = open("damage.wav", 'rb')
    boop_sound = open("boop.wav", 'rb')
    
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
