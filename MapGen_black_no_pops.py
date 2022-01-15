#
#
#   Generate a map from Traveller sector data
#
#####################################################################

from __future__ import with_statement

from colorama import init
from colorama import Fore, Back, Style
from matplotlib.pyparsing import White

init()

from pygame.surface import Surface

hex_code = {'0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15,
            'G': 16,
            'H': 17,
            'J': 18,
            'K': 19,
            'X': 0,
            '?': 0
            }

added_sectors = {}

sector = {'Solomani Rim': (0, -3), 'Old Expanses': (1, -2), 'Fornast': (1, 0),
          'Delphi': (1, -1), 'Drakken': (3, -4), 'Langere': (2, -4),
          'Magyar': (-1, -3), 'Aktifao': (-4, -4), 'Ealiyasiyw': (-3, -2),
          'Corridor': (-2, 1), 'Canopus': (-1, -4), 'Riftspan Reaches': (-4, -1),
          'Core': (0, 0), 'Spinward Marches': (-4, 1), 'Hinterworlds': (2, -2),
          'Aldebaran': (0, -4), 'Leonidae': (3, -2), 'Vland': (-1, 1),
          'Gushemege': (-2, 0), 'Lishun': (0, 1), 'Antares': (1, 1),
          'Zarushagar': (-1, -1), 'Daibei': (-1, -2), 'Ley': (2, 0),
          'Spica': (2, -3), 'Massilia': (0, -1), 'Neworld': (1, -4),
          'Glimmerdrift Reaches': (2, -1), 'Crucis Margin': (3, -1),
          'Alpha Crucis': (1, -3), "Reaver's Deep": (-2, -2),
          "Star's End": (3, 1), 'Iwahfuah': (-3, -3), 'Diaspora': (0, -2),
          'Trojan Reach': (-4, 0), 'Ilelish': (-2, -1), 'Empty Quarter': (2, 1),
          'Dark Nebula': (-2, -3), 'Ustral Quadrant': (-2, -4), 'Phlask': (3, -3),
          'Deneb': (-3, 1), 'Uistilrao': (-3, -4), "Staihaia'yo": (-4, -3),
          'Reft': (-3, 0), 'Verge': (-3, -1), 'Dagudashaag': (-1, 0),
          'Gateway': (3, 0), 'Hlakhoi': (-4, -2)
          }

XORG_SECTOR, YORG_SECTOR = sector['Massilia']

X_SPACING = 4
Y_SPACING = 4.4
# X_SPACING = 8
# Y_SPACING = 10

OFFSET = 2
# OFFSET = 4

DOT_SIZE = 2

ROWS = 6
COLUMNS = 10
# ROWS = 2
# COLUMNS = 4

SCREEN_SIZE = (int(COLUMNS*32*X_SPACING), int(ROWS*40*Y_SPACING))

import pygame
from pygame.locals import *
import time
from rpg_tools.diceroll import roll
import os
import logging

__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'
__app__ = 'MapGen_002b 0.0.1 (Beta)'
__version__ = '0.0.1b'

def pixel(surface, color, pos):
    pygame.draw.line(surface, color, pos, pos)

def circle(surface, color, pos, radius, thickness):
    pygame.draw.circle(surface, color, pos, radius, thickness)

def main():
    pygame.init()
    
    print 'SCREEN_SIZE =', SCREEN_SIZE
    
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    window_title = __app__
    pygame.display.set_caption(window_title)
    window_icon = pygame.image.load('images/shonner_die_alpha.png')
    pygame.display.set_icon(window_icon)
     
    w, h = SCREEN_SIZE 

    clock = pygame.time.Clock()
    
    white = (255,255,255)
    black = (0,0,0)
    gray = (60,60,60)
    green = (0, 255, 0)
    red = (255, 0, 0)
    yellow  = (255, 255, 0)
    orange = (255,165,0)
    amber = (255,191,0)
    blue = (0, 0, 255)
    purple = (255, 0, 255)
    cyan = (0,255,255)
    light_green = (144, 238, 144)
    pink = (255,105,180)
    dark_green = (100, 190, 100)
    light_blue = (135,206,250)
    gold = (255, 215, 0)
    maya_blue = (79, 214, 255)
    bright_green = (102, 255, 0)
    brown = (150,75,0)
    light_purple = (177, 156, 217)
    light_red = (255, 102, 102)
    lightish_blue = (153, 153, 255)
    canary_yellow = (255, 239, 0)
    dark_red = (139,0,0)
    light_brown = (181, 101, 29)
    tan = (210,180,140)
    light_gray = (200, 200, 200)
    silver = (192,192,192)
    rust = (183,65,14)
    yellow_green = (154,205,50)
    peach = (255,229,180)
    pear = (209,226,49)
    dark_grey = (40,40,40)
    wood = (193,154,107)
    maroon = (123,17,19)
    dark_purple = (48,25,52)
    white_pink = (171, 39, 79)
    deep_purple = (255,0,224)
    
    screen.fill(black)
    
    allegiance_color = {'ImDa': gold,
                        'ImDd': rust,
                        'ImDv': light_red,
                        'ImDs': deep_purple,
                        'ImLa': maya_blue,
                        'ImLc': lightish_blue,
                        'ImSy': red,
                        'ImDc': pink,
                        'ImLu': cyan,
                        'ImDg': green,
                        'ImDi': yellow,
                        'LnRp': cyan,
                        'BlSo': dark_purple,
                        'SoCf': orange,
                        'StCl': maroon,
                        'SeFo': white_pink,
                        'AsOf': dark_red,
                        'FlLe': wood,
                        'ZhIN': blue,
                        'VDzF': peach,
                        'MaUn': light_brown,
                        'NaAs': canary_yellow,
                        'NaHu': bright_green,
                        'NaVa': light_purple,
                        'NaXX': light_gray,
                        'JuHl': pear,
                        'JuRu': dark_green,
                        'DaCf': light_green,
                        'SwCf': light_blue,
                        'TrBr': tan,
                        'CsIm': brown,
                        'CsTw': dark_grey,
                        'CsZh': silver,
                        'VAug': yellow_green
                        }

    text_rotate_degrees = 45
    
    sector_names = []
    sectors_filled = []
    
    print
    print 'SECTORS NEARBY:'

#     xx, yy = (XORG_SECTOR, YORG_SECTOR)

    for y in range(ROWS):
        for x in range(COLUMNS):
            
            sectors_filled.append(0)
            
    sect_point = 0        
    for y in range(ROWS):
        for x in range(COLUMNS):
            
            sector_x = x - COLUMNS/2 + XORG_SECTOR
            sector_y = y - ROWS/2 + 1 - 1*YORG_SECTOR
            
            #print sector_x, sector_y,

            sec_filename = 'sec'
            
            if sector_x < 0:
                sec_filename += '_m'
            else:
                sec_filename += '_p'
            if sector_x < -9 or sector_x > 9:
                sec_filename += str(abs(sector_x))
            else:
                sec_filename += '0' + str(abs(sector_x))
            
            if sector_y < 0:
                sec_filename += '_m'
            else:
                sec_filename += '_p'
            if sector_y < -9 or sector_y > 9:
                sec_filename += str(abs(sector_y))
            else:
                sec_filename += '0' + str(abs(sector_y))

            try:
                read_line = 0
                with open('data/' + sec_filename + '.dat', 'r') as sec_file_in:
                    #print sec_filename +'.dat'
                    
                    color = gray
                    pygame.draw.rect(screen, color, (x*32*X_SPACING, y*40*Y_SPACING, 32*X_SPACING, 40*Y_SPACING), DOT_SIZE)
                    
                    for i in range(32):
                        for j in range(40):
                
                            color = gray
                            
                            if i / 2 == i / 2.0:
                                pixel(screen, color, (i*X_SPACING + x*32*X_SPACING, j*Y_SPACING + y*40*Y_SPACING))
                                #pixel(screen, color, (i*X_SPACING + x*32*X_SPACING, j*Y_SPACING + y*40*Y_SPACING), DOT_SIZE, 0)
                            else:
                                pixel(screen, color, (i*X_SPACING + x*32*X_SPACING, j*Y_SPACING + OFFSET + y*40*Y_SPACING))
                                #pixel(screen, color, (i*X_SPACING + x*32*X_SPACING, j*Y_SPACING + OFFSET + y*40*Y_SPACING), DOT_SIZE, 0)
                    
                    for line in sec_file_in:
                        #print line[:len(line)-1]
                        read_line += 1
                        if read_line == 4:
                            sector_name = line[2:len(line)-1]
                            print sector_name,
                            sector_names.append(sector_name)
                            sectors_filled[sect_point] = 1
                            sect_point += 1
                        if read_line == 5:
                            sector_offset = eval(line[2:len(line)-1])
                            print sector_offset,
                            print sector_offset[0], -sector_offset[1]
                            added_sectors[sector_name] = (sector_offset[0], -sector_offset[1])
                        if line[:3] == 'Hex':
                            name_tab = line.find('Name')
                            remarks_tab = line.find('Remarks')
                            allegiance_tab = line.find('A')
                            world_tab = line.find('UWP')
                            pop_m_tab = line.find('PBG')
                            travel_code_tab = line.find('Z')
                        if line[:1] == '-':
                                allegiance_length = line[allegiance_tab:allegiance_tab+6].find(' ')
                        if line[:1] <> '#' and line[:1] <> '-' and line[:1] <> 'H' and len(line) > 3:
                            if int(line[:4]) > 0:
                                print line[allegiance_tab:allegiance_tab+allegiance_length]
                                if line[allegiance_tab:allegiance_tab+allegiance_length] not in allegiance_color:
                                    color = white
                                else:
                                    color = allegiance_color[line[allegiance_tab:allegiance_tab+allegiance_length]]
                                    
                                hex_x=int(line[0:2]) - 1
                                hex_y=int(line[2:4]) - 1

                                #population = hex_code[line[world_tab+4]] * int(line[pop_m_tab])
                                population = hex_code[line[world_tab+4]]
                                
#                                 if line[travel_code_tab] == 'R':
#                                     color = red
#                                 if line[travel_code_tab] == 'A':
#                                     color = amber
                                world_name = line[name_tab:name_tab+19].strip()
                                if hex_x / 2 == hex_x / 2.0:
                                    if world_name == 'Reference' or world_name == 'Capital' or world_name == 'Regina' or world_name == 'Vland' or world_name == 'Terra':
                                        color = yellow
                                        circle(screen, color, (hex_x*X_SPACING + x*32*X_SPACING, hex_y*Y_SPACING + y*40*Y_SPACING), 8, 0)
#                                     if color == red or color == amber:
#                                         circle(screen, color, (hex_x*X_SPACING + x*32*X_SPACING, hex_y*Y_SPACING + y*40*Y_SPACING), DOT_SIZE*population**.5 + 1, 1)
                                    #color = white
                                    if population < 10:
                                        pixel(screen, color, (hex_x*X_SPACING + x*32*X_SPACING, hex_y*Y_SPACING + y*40*Y_SPACING))
                                        #circle(screen, color, (hex_x*X_SPACING + x*32*X_SPACING, hex_y*Y_SPACING + y*40*Y_SPACING), DOT_SIZE*population**.5 + 1, 1)
                                    else:
                                        #color = orange
                                        circle(screen, color, (hex_x*X_SPACING + x*32*X_SPACING, hex_y*Y_SPACING + y*40*Y_SPACING), DOT_SIZE*population**.3 + 1, 0)
                                else:
                                    if world_name == 'Reference' or world_name == 'Capital' or world_name == 'Regina' or world_name == 'Vland' or world_name == 'Terra':
                                        color = yellow
                                        circle(screen, color, (hex_x*X_SPACING + x*32*X_SPACING, hex_y*Y_SPACING + y*40*Y_SPACING), 8, 0)
#                                     if color == red or color == amber:
#                                         circle(screen, color, (hex_x*X_SPACING + x*32*X_SPACING, hex_y*Y_SPACING + OFFSET + y*40*Y_SPACING), DOT_SIZE*population**.5 + 1, 1)
                                    #color = white
                                    if population < 10:
                                        pixel(screen, color, (hex_x*X_SPACING + x*32*X_SPACING, hex_y*Y_SPACING + OFFSET + y*40*Y_SPACING))
                                        #circle(screen, color, (hex_x*X_SPACING + x*32*X_SPACING, hex_y*Y_SPACING + OFFSET + y*40*Y_SPACING), DOT_SIZE*population**.5 + 1, 1)
                                    else:
                                        #color = orange
                                        circle(screen, color, (hex_x*X_SPACING + x*32*X_SPACING, hex_y*Y_SPACING + y*40*Y_SPACING), DOT_SIZE*population**.3 + 1, 0)
                                    
            except IOError:
                #print 'No ' + sec_filename + '.dat'
                sect_point += 1
    
    print added_sectors
    print sector_names
    
    sector_name_pointer = 0
    
    font = pygame.font.SysFont('Eras ITC Demi', 28, False, True)
    
    print sectors_filled
    
    sect_point = 0
    for y in range(ROWS):
        for x in range(COLUMNS):
            if sectors_filled[sect_point] == 1:
                printing = True
                x_line_spacing = 0
                y_line_spacing = 0
                while printing:
                    space_check = sector_names[sector_name_pointer].find(' ')
                    if space_check == -1:
                        #print sector_names[sector_name_pointer]
                        text = font.render(sector_names[sector_name_pointer], True, white)
                        text = pygame.transform.rotate(text, text_rotate_degrees)
                        screen.blit(text, [x*32*X_SPACING + 32*X_SPACING/8 + x_line_spacing, y*40*Y_SPACING + 40*Y_SPACING/8 + y_line_spacing])
                        printing = False
                        sector_name_pointer += 1
                    else:
                        #print sector_names[sector_name_pointer][:space_check]
                        text = font.render(sector_names[sector_name_pointer][:space_check], True, white)
                        text = pygame.transform.rotate(text, text_rotate_degrees)
                        screen.blit(text, [x*32*X_SPACING + 32*X_SPACING/8 + x_line_spacing, y*40*Y_SPACING + 40*Y_SPACING/8 + y_line_spacing])
                        sector_names[sector_name_pointer] = sector_names[sector_name_pointer][space_check+1:len(sector_names[sector_name_pointer])]
                        x_line_spacing += 20
                        y_line_spacing += 40
                #print
            sect_point += 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        


#        msElapsed = clock.tick(30)
         
            
        pygame.display.update()


if __name__ == '__main__':
    
    log = logging.getLogger('MapGen_002b 0.0.1b')
    log.setLevel(logging.DEBUG)

    if not os.path.exists('Logs'):
        os.mkdir('Logs')
    
    fh = logging.FileHandler('Logs/mapgen.log', 'w')
 
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s',
                                  datefmt = '%a, %d %b %Y %H:%M:%S')
    fh.setFormatter(formatter)
    log.addHandler(fh)
    
    log.info('Logging started.')
    log.info(__app__ + ' starting...')
    
    trange = time.localtime()
    if trange[0] > 2021 or trange[1] > 12:
        print
        print Fore.RED + __app__, 'EXPIRED.'
        print Fore.RESET + Back.RESET + Style.RESET_ALL
        print
        print __author__
        print
        s = raw_input('Press ENTER: ')
        print "OK"
    else:
        print
        print 'Thank you for giving', __app__, 'a try.'
        print
        print 'This program uses:'
        vernum, release = roll('info')
        print release
        print 'Pygame 1.9.1release-svn2575'
        print 'SDL 1.2.13'
        print
        if vernum != '2.1.0':
            print Fore.RED + 'WARNING! Different version of roll() installed:', vernum
        if pygame.version.vernum != (1, 9, 1):
            print Fore.RED + 'WARNING! Different version of Pygame installed:', pygame.version.ver
        if pygame.get_sdl_version() != (1, 2, 13):
            print Fore.RED + 'WARNING! Different version of SDL installed:', pygame.get_sdl_version()
        print Fore.RESET + Back.RESET + Style.RESET_ALL
        print
        print '----------------------------'
        print __author__
        print
        
        main()