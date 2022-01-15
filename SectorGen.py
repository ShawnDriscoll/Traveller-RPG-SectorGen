#
#   Python 3.9 Sector Generator
#
########################################################

"""
SectorGen 0.0.1 Beta
-----------------------------------------------------------------------

This program generates sectors using rules from
Mongoose Traveller 1st Edition and Traveller5.
"""

from colorama import init
from colorama import Fore, Back, Style

init() # initialize colorama

from gtts import gTTS
import pyttsx3
#import win32com.client as win32
import sys
#sys.path.append('C:\Users\Shonner\Documents\My Files\Python Programs\Mongoose Traveller')
from random import randint
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#import PyQt5.QtMultimedia as MM
import time
from mainwindow import Ui_MainWindow
from aboutdialog import Ui_aboutDialog
from rpg_tools.PyDiceroll import roll
import os
import logging
import csv
import json

__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'
__app__ = 'SectorGen 0.0.1 (Beta)'
__version__ = '0.0.1b'

engine = pyttsx3.init()

reg_voice_path = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\'

voice = {'US Zira':     {'Name': 'TTS_MS_EN-US_ZIRA_11.0',
                         'Rate': -50,
                         'Volume': 0.0},
         'US David':    {'Name': 'TTS_MS_EN-US_DAVID_11.0',
                         'Rate': -60,
                         'Volume': 0.0}
        }

voices = ['Muted', 'Google', 'US Zira', 'US David']

speaker = 'US Zira'

rate = engine.getProperty('rate')
engine.setProperty('rate', rate + voice[speaker]['Rate'])
volume = engine.getProperty('volume')
engine.setProperty('volume', volume + voice[speaker]['Volume'])
engine.setProperty('voice', reg_voice_path + voice[speaker]['Name'])


class aboutDialog(QDialog, Ui_aboutDialog):
    def __init__(self):
        super().__init__()
        log.info('PyQt5 aboutDialog initializing...')
        self.setWindowFlags(Qt.Drawer | Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.aboutOKButton.clicked.connect(self.acceptOKButtonClicked)
        log.info('PyQt5 aboutDialog initialized.')
        
    def acceptOKButtonClicked(self):
        log.info('PyQt5 aboutDialog closing...')
        self.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        log.info('PyQt5 MainWindow initializing...')
        self.setupUi(self)
        self.genButton.clicked.connect(self.generateSector)
        self.actionGen.triggered.connect(self.generateSector)
        self.actionAbout_SectorGen.triggered.connect(self.actionAbout_triggered)
        self.actionQuitProg.triggered.connect(self.actionQuitProg_triggered)

        #   Options

        self.hydro_calc_method = 'Based on Atmosphere'
        self.hydroBox.addItem('Based on Atmosphere')
        self.hydroBox.addItem('Based on Size')
        self.hydroBox.setCurrentIndex(0)
        self.hydroBox.currentIndexChanged.connect(self.hydroBox_changed)

        self.world_chance_method = '1d6 >= 4'
        self.world_chanceBox.addItem('1d6 >= 4')
        self.world_chanceBox.addItem('1d6 >= 5')
        self.world_chanceBox.addItem('1d6 >= 6')
        self.world_chanceBox.setCurrentIndex(0)
        self.world_chanceBox.currentIndexChanged.connect(self.world_chanceBox_changed)
        self.world_chance = int(self.world_chance_method[7])
        #print(self.world_chance)

        self.popAboutDialog = aboutDialog()
        
        #   UPP Code Table

        self.hex_code = ['0', '1', '2', '3', '4', '5', '6',
                         '7', '8', '9', 'A', 'B', 'C', 'D',
                         'E', 'F', 'G', 'H', 'J', 'K',
                         'L', 'M', 'N', 'P', 'Q', 'R',
                         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.core_code = ['A', 'B', 'C', 'D',
                          'E', 'F', 'G', 'H',
                          'I', 'J', 'K', 'L',
                          'M', 'N', 'O', 'P']
    
    #   World Data Tables

        self.world_temperature_dm = [0, 0, -2, -2, -1, -1, 0, 0, 1, 1, 2, 6, 6, 2, -1, 2]
        self.size_value =           [  2,   2,   1,   1,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]
        self.atmosphere_value =     [  1,   1,   1,   1,   0,   0,   0,   0,   0,   0,   1,   1,   1,   1,   1,   1]
        self.hydro_value =          [  1,   0,   0,   0,   0,   0,   0,   0,   0,   1,   2,   0,   0,   0,   0,   0]
        self.population_value =     [  0,   1,   1,   1,   1,   1,   0,   0,   1,   2,   4,   0,   0,   0,   0,   0]
        self.government_value =     [  1,   0,   0,   0,   0,   1,   0,   2,   0,   0,   0,   0,   0,  -2,  -2,   0]
        self.minimum_TL =           [  8,   8,   5,   5,   3,  -1,  -1,   3,  -1,   3,   8,   9,  10,   5,   5,   8]
    
        self.world_starport_class = [' ', ' ', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'E', 'E', 'X']
        self.starport_value =       [  0,   0,   6,   6,   6,   4,   4,   2,   2,   0,   0,   0,  -4]
        
        self.gas_giant_quantity =      [' ', ' ', '1', '1', '2', '2', '3', '3', '4', '4', '4', '5', '5']
        self.planetoid_belt_quantity = [' ', ' ', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '3']

    #   Sound Tables

        self.V   = 1
        self.CV  = 2
        self.VC  = 3
        self.CVC = 4
        self.CC  = 5
        
        self.ic_sound = ['b','br','c','ch','d','g',
                         'h','j','k','l','m','p',
                         'r','s','st','sh',
                         't','v','w','z']
        self.ic_freq = [28,12,20,16,27,9,20,20,13,
                        28,24,27,24,30,13,25,
                        20,6,16,4]
        
        self.v_sound = ['a','e','i','o','u']
        self.v_freq = [16,20,10,7,3]
    
        self.mc_sound = ['g','lt','ns','nst','ls','ll','nn']
        self.mc_freq = [20,3,18,16,18,4,3]
    
        self.fc_sound = ['ch','ck','d','dy','dyne',
                         'hl','li','la','le','ler',
                         'nn','m','man','ma','mer','ny',
                         'me','n','nas','ne','ng',
                         'ner','nor','nie',
                         'rie','rlie','rly','rie','rt',
                         'ry','sa','sha','nshi','nski','son',
                         'nson','th','ta','ti','t','v',
                         'za','ue','than',
                         'lam','lis','lus','ton','tis','tus',
                         'love','se','nter','ll']
        self.fc_freq = [6,13,22,12,3,3,3,10,6,10,7,
                        25,10,4,13,12,5,27,11,4,14,13,17,7,6,5,5,6,3,
                        21,10,3,8,3,20,9,14,10,16,11,8,6,8,10,7,6,5,7,7,4,
                        4,12,5,4]
        
        for i in range(len(self.ic_sound)):
            log.debug(self.ic_sound[i] + ' ' + str(self.ic_freq[i]))
        
        for i in range(len(self.v_sound)):
            log.debug(self.v_sound[i] + ' ' + str(self.v_freq[i]))
            
        for i in range(len(self.mc_sound)):
            log.debug(self.mc_sound[i] + ' ' + str(self.mc_freq[i]))

        for i in range(len(self.fc_sound)):
            log.debug(self.fc_sound[i] + ' ' + str(self.fc_freq[i]))
    
        self.syllable_type = [self.V,self.V,self.V,self.V,self.V,self.V,self.V,self.V,
                              self.VC,self.VC,self.VC,self.VC,
                              self.CV,self.CV,self.CV,self.CV,
                              self.CVC,self.CVC,self.CVC,self.CVC,self.CVC,self.CVC,
                              self.CC,self.CC]
        #print self.syllable_type
        log.info('PyQt5 MainWindow initialized.')
            
    def pick_sound(self):
        if self.s_type == self.V:
            self.sound = self.v_sounds[randint(1, len(self.v_sounds)) - 1]
        if self.s_type == self.CV:
            self.sound = self.ic_sounds[randint(1, len(self.ic_sounds)) - 1] + self.v_sounds[randint(1, len(self.v_sounds)) - 1]
        if self.s_type == self.VC:
            self.sound = self.v_sounds[randint(1, len(self.v_sounds)) - 1] + self.fc_sounds[randint(1, len(self.fc_sounds)) - 1]
        if self.s_type == self.CVC:
            self.sound = self.ic_sounds[randint(1, len(self.ic_sounds)) - 1] + self.v_sounds[randint(1, len(self.v_sounds)) - 1] \
            + self.fc_sounds[randint(1, len(self.fc_sounds)) - 1]
        if self.s_type == self.CC:
            self.sound = self.mc_sounds[randint(1, len(self.mc_sounds)) - 1]

    def generateSector(self):
        
        if not os.path.exists('data'):
            os.mkdir('data')

        csv_file_out = open('data/raw_sector_data.csv', 'w', newline='')
        csv_writer = csv.writer(csv_file_out)
        csv_writer.writerow(['Location', 'World_Name', 'Starport', 'Size', 'Atmosphere', 'Hydrographics', 'Population', 'Government', 'Law_Level', 'Tech_Level', 'Trade_Codes', 'Travel_Code', 'Base', 'Pop_M', 'Belts', 'Gas_giants', 'Allegiance', 'Stellar_Data'])
        
        json_file_out = open('data/raw_sector_data.json', 'w')
        world_list = []

        self.main_world_tech_level = -1
        self.main_world_travel_code = ''
        self.highest_skill_level = 0

        worlds_rolled = 0

        for hex_loc in range(1280):

            if roll('1d6') >= self.world_chance:

                self.main_world_type_and_government_DM = 0

                self.ic_sounds = []
                for i in range(len(self.ic_freq)):
                    for j in range(self.ic_freq[i]):
                        self.ic_sounds.append(self.ic_sound[i])
                self.v_sounds = []
                for i in range(len(self.v_freq)):
                    for j in range(self.v_freq[i]):
                        self.v_sounds.append(self.v_sound[i])
                self.mc_sounds = []
                for i in range(len(self.mc_freq)):
                    for j in range(self.mc_freq[i]):
                        self.mc_sounds.append(self.mc_sound[i])
                self.fc_sounds = []
                for i in range(len(self.fc_freq)):
                    for j in range(self.fc_freq[i]):
                        self.fc_sounds.append(self.fc_sound[i])
                        
    #             print self.ic_sounds
    #             print
    #             print self.v_sounds
    #             print
    #             print self.mc_sounds
    #             print
    #             print self.fc_sounds
                    
            #   Get World Name
        
                proper = False
                while not(proper):
                    temp = self.CC
                    while temp == self.CC:
                        temp = self.syllable_type[randint(1, len(self.syllable_type)) - 1]
                    self.s_type = temp
                    self.pick_sound()
                    self.word = self.sound
                    building = True
                    while building:
                        syllable = self.syllable_type[randint(1, len(self.syllable_type)) - 1]
                        while temp == self.CC and (syllable == self.CV or syllable == self.CVC or syllable == self.CC):
                            syllable = self.syllable_type[randint(1, len(self.syllable_type)) - 1]
                        while temp == self.V and (syllable == self.V or syllable == self.VC):
                            syllable = self.syllable_type[randint(1, len(self.syllable_type)) - 1]
                        while temp == self.CV and (syllable == self.V or syllable == self.VC):
                            syllable = self.syllable_type[randint(1, len(self.syllable_type)) - 1]
                        while temp == self.VC and (syllable == self.CV or syllable == self.CVC or syllable == self.CC):
                            syllable = self.syllable_type[randint(1, len(self.syllable_type)) - 1]
                        while temp == self.CVC and (syllable == self.CV or syllable == self.CVC or syllable == self.CC):
                            syllable = self.syllable_type[randint(1, len(self.syllable_type)) - 1]
                        if temp == self.VC or temp == self.CVC:
                            building = False
                        else:
                            self.s_type = syllable
                            self.pick_sound()
                            self.word += self.sound
                            temp = syllable

                    if len(self.word) > 3 and len(self.word) < 14:
                        proper = True

                self.main_world_name = chr(ord(self.word[0]) - 32) + self.word[1:len(self.word)]
        
            #   Roll for Main World Location

                self.hex_grid_col = randint(1, 32)
                self.hex_grid_row = randint(1, 40)
                
                #self.main_world_location = self.core_code[(self.hex_grid_col - 1) / 8 + ((self.hex_grid_row - 1) / 10) * 4]
                self.main_world_location = ''
                
                if self.hex_grid_col < 10:
                    self.main_world_location += '0' + self.hex_code[self.hex_grid_col]
                else:
                    self.main_world_location += str(self.hex_grid_col)

                if self.hex_grid_row < 10:
                    self.main_world_location += '0' + self.hex_code[self.hex_grid_row]
                else:
                    self.main_world_location += str(self.hex_grid_row)    

            #   Roll for Main World Size

                self.main_world_size = roll('2D6-2')                        

            #   Roll for Main World Atmosphere

                self.main_world_atmosphere = roll('2D6-7') + self.main_world_size
                if self.main_world_atmosphere < 0:
                    self.main_world_atmosphere = 0
                if self.main_world_atmosphere > 15:
                    self.main_world_atmosphere = 15

            #   Roll for Main World Hydrographics

                if self.hydro_calc_method == 'Based on Atmosphere':
                    self.main_world_hydrographics = roll('2D6-7') + self.main_world_atmosphere
                else:
                    self.main_world_hydrographics = roll('2D6-7') + self.main_world_size
                    
                if self.main_world_hydrographics < 0:
                    self.main_world_hydrographics = 0
                if self.main_world_hydrographics > 10:
                    self.main_world_hydrographics = 10

            #   Add DMs

                if self.main_world_size < 2:
                    self.main_world_hydrographics = 0
                    
                if self.main_world_atmosphere < 2 or \
                        self.main_world_atmosphere == 10 or \
                        self.main_world_atmosphere == 11 or \
                        self.main_world_atmosphere == 12:
                            self.main_world_hydrographics += -4
                    
                if self.main_world_hydrographics < 0:
                    self.main_world_hydrographics = 0

            #   Roll for Main World Population

                #self.main_world_population = roll('2D6-2')
                #self.main_world_population = roll('4D4-4')
                
                self.main_world_population = roll('2d6-2')
                if self.main_world_population == 10:
                    self.main_world_population = roll('2d6+3')

            #   Roll for Main World Government

                if self.main_world_population > 0:
                    self.main_world_government = roll('2D6-7') + self.main_world_population
                    if self.main_world_government < 0:
                        self.main_world_government = 0
                    if self.main_world_government > 15:
                        self.main_world_government = 15
        
                    if self.main_world_government == 10 or \
                        self.main_world_government == 12 or \
                        self.main_world_government == 5 or \
                        self.main_world_government == 3:
                        self.main_world_type_and_government_DM = 1
                else:
                    self.main_world_government = 0

            #   Roll for Law Level

                if self.main_world_population > 0:
                    self.main_world_law_level = roll('2D6-7') + self.main_world_government
                    if self.main_world_law_level < 0:
                        self.main_world_law_level = 0
                    if self.main_world_law_level > 18:
                        self.main_world_law_level = 18
                else:
                    self.main_world_law_level = 0
                    
            #   Roll for Starport    
            
                self.main_world_starport = roll('2D6')
            
            #   Roll for Technology Level

                if self.main_world_population > 0:
                    self.main_world_tech_level = roll('1D6')
            
            #   Add DMs
            
                    self.main_world_tech_level += self.starport_value[self.main_world_starport]
                    self.main_world_tech_level += self.size_value[self.main_world_size]
                    self.main_world_tech_level += self.atmosphere_value[self.main_world_atmosphere]
                    self.main_world_tech_level += self.hydro_value[self.main_world_hydrographics]
                    self.main_world_tech_level += self.population_value[self.main_world_population]
                    self.main_world_tech_level += self.government_value[self.main_world_government]
            
            #   Adjust Minimum TL for Environmental Limits
            
                    if self.minimum_TL[self.main_world_atmosphere] != -1:
                        if self.main_world_tech_level < self.minimum_TL[self.main_world_atmosphere]:
                            self.main_world_tech_level = self.minimum_TL[self.main_world_atmosphere]
                
                    if self.main_world_tech_level < 0:
                        self.main_world_tech_level = 0
                    if self.main_world_tech_level > 20:
                        self.main_world_tech_level = 20

                else:
                    self.main_world_tech_level = 0
                
            #   Calculate Travel Code
            
                self.main_world_travel_code = ''
                if (self.main_world_atmosphere >= 10 or (self.main_world_government == 0 or self.main_world_government == 7 \
                        or self.main_world_government == 10) or (self.main_world_law_level == 0 or self.main_world_law_level >= 9)) and roll('d6') == 6:
                        self.main_world_travel_code = '      A'
            
            #   Lookup Trade Code(s)
            
                self.trade_index = 0
                self.main_world_trade_code = ['  ','  ','  ','  ','  ','  ', '  ', '  ', '  ', '  ']
                self.main_world_trade_class = ['  ','  ','  ','  ','  ','  ', '  ', '  ', '  ', '  ']
                if self.main_world_atmosphere >= 4 \
                                and self.main_world_atmosphere <= 9 \
                                and self.main_world_hydrographics >= 4 \
                                and self.main_world_hydrographics <= 8 \
                                and self.main_world_population >= 5 \
                                and self.main_world_population <= 7:
                    self.main_world_trade_code[self.trade_index] = 'Ag'
                    self.main_world_trade_class[self.trade_index] = 'Agricultural'
                    self.trade_index += 1
                if (self.main_world_atmosphere == 2 \
                                or self.main_world_atmosphere == 3 \
                                or self.main_world_atmosphere == 10 \
                                or self.main_world_atmosphere == 11) \
                                and self.main_world_hydrographics >= 1 \
                                and self.main_world_hydrographics <= 5 \
                                and self.main_world_population >= 3 \
                                and self.main_world_population <= 6 \
                                and self.main_world_law_level >= 6 \
                                and self.main_world_law_level <= 9:
                    self.main_world_trade_code[self.trade_index] = 'Px'
                    self.main_world_trade_class[self.trade_index] = 'Prison'
                    self.main_world_travel_code = '      A'
                    self.trade_index += 1
                if self.main_world_size == 0 \
                                and self.main_world_atmosphere == 0 \
                                and self.main_world_hydrographics == 0:
                    self.main_world_trade_code[self.trade_index] = 'As'
                    self.main_world_trade_class[self.trade_index] = 'Asteroid'
                    self.trade_index += 1
                if self.main_world_population == 0 \
                                and self.main_world_government == 0 \
                                and self.main_world_law_level == 0:
                    self.main_world_trade_code[self.trade_index] = 'Ba'
                    self.main_world_trade_class[self.trade_index] = 'Barren'
                    if roll('1D6') > 2:
                        self.main_world_tech_level = 0
                    self.trade_index += 1
                if self.main_world_starport >= 2 and self.main_world_starport <= 4:
                    if roll('1D3') == 1:
                        self.main_world_trade_code[self.trade_index] = 'Cp'
                        self.main_world_trade_class[self.trade_index] = 'Subsector Capital'
                        self.trade_index += 1
                if self.main_world_population >=5 \
                                and self.main_world_population <= 10 \
                                and self.main_world_government == 6 \
                                and self.main_world_law_level >= 0 \
                                and self.main_world_law_level <= 3:
                    self.main_world_trade_code[self.trade_index] = 'Cy'
                    self.main_world_trade_class[self.trade_index] = 'Colony'
                    self.trade_index += 1
                if self.main_world_atmosphere >= 2 \
                                and self.main_world_hydrographics == 0:
                    self.main_world_trade_code[self.trade_index] = 'De'
                    self.main_world_trade_class[self.trade_index] = 'Desert'
                    self.trade_index += 1
                if self.main_world_atmosphere >= 11 \
                                and self.main_world_hydrographics >= 1:
                    self.main_world_trade_code[self.trade_index] = 'Fl'
                    self.main_world_trade_class[self.trade_index] = 'Fluid Oceans'
                    self.trade_index += 1
                if self.main_world_size >= 6 \
                                and self.main_world_size <= 8 \
                                and (self.main_world_atmosphere == 5 \
                                or self.main_world_atmosphere == 6 \
                                or self.main_world_atmosphere == 8) \
                                and self.main_world_hydrographics >= 5 \
                                and self.main_world_hydrographics <= 7:
                    self.main_world_trade_code[self.trade_index] = 'Ga'
                    self.main_world_trade_class[self.trade_index] = 'Garden'
                    self.main_world_type_and_government_DM = 1
                    self.trade_index += 1
                if self.main_world_population >= 9:
                    self.main_world_trade_code[self.trade_index] = 'Hi'
                    self.main_world_trade_class[self.trade_index] = 'High Population'
                    self.main_world_type_and_government_DM = 1
                    self.trade_index += 1
    #             if self.main_world_tech_level >= 12:
    #                 self.main_world_trade_code[self.trade_index] = 'Ht'
    #                 self.main_world_trade_class[self.trade_index] = 'High Tech'
    #                 self.main_world_type_and_government_DM = 1
    #                 self.trade_index += 1
                if self.main_world_atmosphere >= 0 \
                                and self.main_world_atmosphere <= 1 \
                                and self.main_world_hydrographics >= 1:
                    self.main_world_trade_code[self.trade_index] = 'Ic'
                    self.main_world_trade_class[self.trade_index] = 'Ice-Capped'
                    self.trade_index += 1
                if (self.main_world_atmosphere >= 0 \
                                and self.main_world_atmosphere <= 2 \
                                or self.main_world_atmosphere == 4 \
                                or self.main_world_atmosphere == 7 \
                                or self.main_world_atmosphere == 9) \
                                and self.main_world_population >= 9:
                    self.main_world_trade_code[self.trade_index] = 'In'
                    self.main_world_trade_class[self.trade_index] = 'Industrial'
                    self.main_world_type_and_government_DM = 1
                    self.trade_index += 1
                if self.main_world_population >= 1 \
                                and self.main_world_population <= 3:
                    self.main_world_trade_code[self.trade_index] = 'Lo'
                    self.main_world_trade_class[self.trade_index] = 'Low Population'
                    self.trade_index += 1
    #             if self.main_world_tech_level <= 5:
    #                 self.main_world_trade_code[self.trade_index] = 'Lt'
    #                 self.main_world_trade_class[self.trade_index] = 'Low Tech'
    #                 self.trade_index += 1
                if self.main_world_atmosphere >= 0 \
                                and self.main_world_atmosphere <= 3 \
                                and self.main_world_hydrographics >= 0 \
                                and self.main_world_hydrographics <= 3 \
                                and self.main_world_population >= 6:
                    self.main_world_trade_code[self.trade_index] = 'Na'
                    self.main_world_trade_class[self.trade_index] = 'Non-Agricultural'
                    self.trade_index += 1
                if self.main_world_population <= 6:
                    self.main_world_trade_code[self.trade_index] = 'Ni'
                    self.main_world_trade_class[self.trade_index] = 'Non-Industrial'
                    self.trade_index += 1
                if self.main_world_atmosphere >= 2 \
                                and self.main_world_atmosphere <= 5 \
                                and self.main_world_hydrographics >= 0 \
                                and self.main_world_hydrographics <= 3:
                    self.main_world_trade_code[self.trade_index] = 'Po'
                    self.main_world_trade_class[self.trade_index] = 'Poor'
                    self.trade_index += 1
                if (self.main_world_atmosphere == 6 \
                                or self.main_world_atmosphere == 8) \
                                and self.main_world_population >= 6 \
                                and self.main_world_population <= 8:
                    self.main_world_trade_code[self.trade_index] = 'Ri'
                    self.main_world_trade_class[self.trade_index] = 'Rich'
                    self.main_world_type_and_government_DM = 1
                    self.trade_index += 1
                if self.main_world_hydrographics == 10 \
                                and self.main_world_atmosphere >= 1 \
                                and self.main_world_atmosphere <= 9:
                    self.main_world_trade_code[self.trade_index] = 'Wa'
                    self.main_world_trade_class[self.trade_index] = 'Water World'
                    self.trade_index += 1
                if self.main_world_atmosphere == 0:
                    self.main_world_trade_code[self.trade_index] = 'Va'
                    self.main_world_trade_class[self.trade_index] = 'Vacuum'
                    self.trade_index += 1
                if self.main_world_government + self.main_world_law_level >= 30:
                    self.main_world_trade_code[self.trade_index] = 'Fo'
                    self.main_world_trade_class[self.trade_index] = 'Forbidden'
                    self.trade_index += 1
                    self.main_world_travel_code = '      R'
                
            #   Any bases? Naval? Research, etc?
            
                self.base = ''
                if self.world_starport_class[self.main_world_starport] == 'A':
                    if roll('2D6') >= 8:
                        self.base = 'N'
                    elif roll('2D6') >= 10:
                        self.base = 'S'
                    elif roll('2D6') >= 8:
                        self.base = 'R'
                if self.world_starport_class[self.main_world_starport] == 'B':
                    if roll('2D6') >= 8:
                        self.base = 'N'
                    elif roll('2D6') >= 8:
                        self.base = 'S'
                    elif roll('2D6') >= 8:
                        self.base = 'R'
                if self.world_starport_class[self.main_world_starport] == 'C':
                    if roll('2D6') >= 8:
                        self.base = 'S'
                    elif roll('2D6') >= 10:
                        self.base = 'R'
                    elif roll('2D6') >= 8:
                        self.base = 'W'
                if self.world_starport_class[self.main_world_starport] == 'D':
                    if roll('2D6') >= 7:
                        self.base = 'S'
            
            #   Population Multiplier?
            
                if roll('1D6') > 3:
                    self.population_multiplier = roll('1D6-1')
                    while self.population_multiplier == 5:
                        self.population_multiplier = roll('1D6-1')
                else:
                    self.population_multiplier = roll('1D6+4')
                    while self.population_multiplier == 10:
                        self.population_multiplier = roll('1D6+4')
                if self.population_multiplier < 1:
                    self.population_multiplier = 1
            
            #   Planetoid Belts?
            
                self.planetoid_belts = '0'
                if roll('2D6') >= 8:
                    self.planetoid_belts = self.planetoid_belt_quantity[roll('2D6')]
                    
            
            #   Gas Giants?
            
                self.gas_giants = '0'
                if roll('2D6') >= 5:
                    self.gas_giants = self.gas_giant_quantity[roll('2D6')]
            
            #   Allegiance?
            
                self.allegiance = 'Im'
                temp = roll('D100')
                if temp > 50:
                    self.allegiance = 'Cs'
                if temp > 80:
                    self.allegiance = 'Na'
                if temp > 90:
                    self.allegiance = 'Va'
                if temp > 94:
                    self.allegiance = 'So'
                if temp > 97:
                    self.allegiance = 'As'
                if temp == 100:
                    self.allegiance = 'Zh'
                
            #   System Nature
            
                sn = [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3]
                primary_star_type =   [' ', ' ', 'A', 'M', 'M', 'M', 'M', 'M', 'K', 'G', 'F', 'F', 'F']
                companion_star_type = [' ', ' ', 'A', 'F', 'F', 'G', 'G', 'K', 'K', 'M', 'M', 'M', 'M']
                star_size = [' ', ' ', 'II', 'III', 'IV', 'V', 'V', 'V', 'V', 'V', 'V', 'VI', 'D']
                self.stellar_data = ''
                star_count = sn[roll('2D6')]
                if self.main_world_atmosphere >= 4 and self.main_world_atmosphere <= 9 \
                        or self.main_world_population >= 8:
                    star_DM = 4
                else:
                    star_DM = 0
                star_rolled = roll('2D6') + star_DM
                if star_rolled > 12:
                    star_rolled = 12
                previous_star_rolled = star_rolled
                self.stellar_data += primary_star_type[star_rolled]
                if roll('1D6') > 3:
                    classification = roll('1D6-1')
                    while classification == 5:
                        classification = roll('1D6-1')
                else:
                    classification = roll('1D6+4')
                    while classification == 10:
                        classification = roll('1D6+4')
                self.stellar_data += str(classification)
                star_rolled = roll('2D6') + star_DM
                if star_rolled > 12:
                    star_rolled = 12
                star_size_rolled = star_size[star_rolled]
                if (self.stellar_data == 'K5' or self.stellar_data == 'M9') \
                        and star_size_rolled == 'IV':
                    star_size_rolled = 'V'
                if (self.stellar_data == 'B0' or self.stellar_data == 'F4') \
                        and star_size_rolled == 'IV':
                    star_size_rolled = 'V'
                self.stellar_data += ' ' + star_size_rolled
                previous_star_size_rolled = star_rolled
                star_count += -1
                if star_count > 1:
                    star_rolled = roll('2D6') + previous_star_rolled
                    if star_rolled > 12:
                        star_rolled = 12
                    companion_data = companion_star_type[star_rolled]
                    if roll('1D6') > 3:
                        classification = roll('1D6-1')
                        while classification == 5:
                            classification = roll('1D6-1')
                    else:
                        classification = roll('1D6+4')
                        while classification == 10:
                            classification = roll('1D6+4')
                    companion_data += str(classification)
                    star_rolled = roll('2D6') + previous_star_size_rolled
                    if star_rolled > 12:
                        star_rolled = 12
                    star_size_rolled = star_size[star_rolled]
                    if (companion_data == 'K5' or companion_data == 'M9') \
                            and star_size_rolled == 'IV':
                        star_size_rolled = 'V'
                    if (companion_data == 'B0' or companion_data == 'F4') \
                            and star_size_rolled == 'IV':
                        star_size_rolled = 'V'
                    self.stellar_data += ' ' + companion_data + ' ' + star_size_rolled

            # Print name

                if roll('D100') > 95:
                    self.main_world_name = self.world_starport_class[self.main_world_starport] + \
                                            self.hex_code[self.main_world_size] + \
                                            self.hex_code[self.main_world_atmosphere] + \
                                            self.hex_code[self.main_world_hydrographics] + \
                                            self.hex_code[self.main_world_population] + \
                                            self.hex_code[self.main_world_government] + \
                                            self.hex_code[self.main_world_law_level] + '-' + \
                                            self.hex_code[self.main_world_tech_level]
                    
                self.main_world_trade_codes = ''
                self.main_world_trade_classes = ''
                for i in range(self.trade_index):
                    self.main_world_trade_codes += ' ' + self.main_world_trade_code[i]
                    self.main_world_trade_classes += self.main_world_trade_class[i] + ', '
                
            # Print Main World

                print(self.main_world_name + ' (%s   %s%s%s%s%s%s%s-%s %s%s)' % (self.main_world_location, \
                                self.world_starport_class[self.main_world_starport], \
                                self.hex_code[self.main_world_size], self.hex_code[self.main_world_atmosphere], \
                                self.hex_code[self.main_world_hydrographics], self.hex_code[self.main_world_population], \
                                self.hex_code[self.main_world_government], self.hex_code[self.main_world_law_level], \
                                self.hex_code[self.main_world_tech_level], self.main_world_trade_codes, self.main_world_travel_code))
                
                worlds_rolled += 1

                csv_writer.writerow([self.main_world_location,
                                    self.main_world_name,
                                    self.world_starport_class[self.main_world_starport],
                                    self.hex_code[self.main_world_size],
                                    self.hex_code[self.main_world_atmosphere],
                                    self.hex_code[self.main_world_hydrographics],
                                    self.hex_code[self.main_world_population],
                                    self.hex_code[self.main_world_government],
                                    self.hex_code[self.main_world_law_level],
                                    self.hex_code[self.main_world_tech_level],
                                    self.main_world_trade_codes[1:],
                                    self.main_world_travel_code[len(self.main_world_travel_code) - 1:len(self.main_world_travel_code)],
                                    self.base,
                                    self.population_multiplier,
                                    self.planetoid_belts,
                                    self.gas_giants,
                                    self.allegiance,
                                    self.stellar_data])
                
                trav_rec = {}
                
                trav_rec['Location'] = self.main_world_location
                trav_rec['World_Name'] = self.main_world_name
                trav_rec['Starport'] = self.world_starport_class[self.main_world_starport]
                trav_rec['Size'] = self.hex_code[self.main_world_size]
                trav_rec['Atmosphere'] = self.hex_code[self.main_world_atmosphere]
                trav_rec['Hydrographics'] = self.hex_code[self.main_world_hydrographics]
                trav_rec['Population'] = self.hex_code[self.main_world_population]
                trav_rec['Government'] = self.hex_code[self.main_world_government]
                trav_rec['Law_Level'] = self.hex_code[self.main_world_law_level]
                trav_rec['Tech_Level'] = self.hex_code[self.main_world_tech_level]
                trav_rec['Trade_Codes'] = self.main_world_trade_codes[1:]
                trav_rec['Travel_Code'] = self.main_world_travel_code[len(self.main_world_travel_code) - 1:len(self.main_world_travel_code)]
                trav_rec['Base'] = self.base
                trav_rec['Pop_M'] = self.population_multiplier
                trav_rec['Belts'] = self.planetoid_belts
                trav_rec['Gas_Giants'] = self.gas_giants
                trav_rec['Allegiance'] = self.allegiance
                trav_rec['Stellar_Data'] = self.stellar_data

                world_list.append(trav_rec)

                #log.info(self.full_name + ' was generated.')

        #log.info(self.full_name + ' matches criteria.')
        #json.dump(world_list, json_file_out, indent=4, ensure_ascii=True)
        json.dump(world_list, json_file_out, ensure_ascii=True)

        csv_file_out.close()
        json_file_out.close()

        print('Worlds rolled:', worlds_rolled)

    def hydroBox_changed(self):
        self.hydro_calc_choices = ['Based on Atmosphere', 'Based on Size']
        self.hydro_calc_method = self.hydro_calc_choices[self.hydroBox.currentIndex()]
        print(self.hydro_calc_method)
        log.info("'" + self.hydro_calc_method + "'" + ' was selected.')

    def world_chanceBox_changed(self):
        self.world_chance_choices = ['1d6 >= 4', '1d6 >= 5', '1d6 >= 6']
        self.world_chance_method = self.world_chance_choices[self.world_chanceBox.currentIndex()]
        self.world_chance = int(self.world_chance_method[7])
        print(self.world_chance)
        print(self.world_chance_method)
        log.info("'" + self.world_chance_method + "'" + ' was selected.')

    def actionAbout_triggered(self):
        log.info(__app__ + ' show about...')
        self.popAboutDialog.show()

    def actionQuitProg_triggered(self):
        log.info(__app__ + ' quiting...')
        log.info(__app__ + ' DONE.')
        self.close()


if __name__ == '__main__':
    
    log = logging.getLogger('SectorGen')
    log.setLevel(logging.DEBUG)

    if not os.path.exists('Logs'):
        os.mkdir('Logs')
    
    fh = logging.FileHandler('Logs/SectorGen.log', 'w')
 
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s',
                                  datefmt = '%a, %d %b %Y %H:%M:%S')
    fh.setFormatter(formatter)
    log.addHandler(fh)
    
    log.info('Logging started.')
    log.info(__app__ + ' starting...')
    
    trange = time.localtime()
    if trange[0] > 2022 or trange[1] > 13:
        
        log.warning('Beta time period has expired!')
        
        print()
        print(Fore.RED + Style.BRIGHT + __app__, 'EXPIRED.')
        print(Style.RESET_ALL)
        print()
        print(__author__)
        print()
        s = input('Press ENTER: ')
        log.info(__app__ + ' stopping...')
        
        print('OK')
        
        log.info(__app__ + ' stopped.')
    else:
        print()
        print('Thank you for giving', __app__, 'a try.')
        vernum, release = roll('info')
        print('This program uses', release)
        print()
        print('----------------------------')
        print(__author__)
        print()
        
        log.info(__app__ + ' started, and running...')
        
        app = QApplication(sys.argv)
        
        #Use print(QStyleFactory.keys()) to find a setStyle you like, instead of 'Fusion'

        # app.setStyle('Fusion')
        
        # darkPalette = QPalette()
        # darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
        # darkPalette.setColor(QPalette.WindowText, Qt.white)
        # darkPalette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
        # darkPalette.setColor(QPalette.Base, QColor(42, 42, 42))
        # darkPalette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
        # darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
        # darkPalette.setColor(QPalette.ToolTipText, Qt.white)
        # darkPalette.setColor(QPalette.Text, Qt.white)
        # darkPalette.setColor(QPalette.Disabled, QPalette.Text, QColor(127, 127, 127))
        # darkPalette.setColor(QPalette.Dark, QColor(35, 35, 35))
        # darkPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
        # darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
        # darkPalette.setColor(QPalette.ButtonText, Qt.white)
        # darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
        # darkPalette.setColor(QPalette.BrightText, Qt.red)
        # darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
        # darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        # darkPalette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80))
        # darkPalette.setColor(QPalette.HighlightedText, Qt.white)
        # darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, QColor(127, 127, 127))
        
        mainApp = MainWindow()
        mainApp.show()
        
        # app.setPalette(darkPalette)

        CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
        #print(CURRENT_DIR)
        
        app.exec_()