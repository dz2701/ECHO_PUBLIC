import sys
import pygame as pg
import pandas
from t2 import std
from Settings import Setting
import functions as gf
def run_game():
    pg.init()
    pg.display.set_caption("ECHO Settings")
    set = Setting()
    scr = pg.display.set_mode((set.screen_w,set.screen_h))

    while(True):
        gf.check_events(set,scr)



run_game()
