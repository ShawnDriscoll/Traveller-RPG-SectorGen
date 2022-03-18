#
#
#   Generate a map from Traveller 5 sector data
#
#####################################################################

"""
PyMapGen 0.1.0 Beta
-------------------

This program displays Traveller 5 sectors and subsectors.

The Traveller game in all forms is owned by Far Future Enterprises.
Copyright 1977 - 2022 Far Future Enterprises.
Traveller is a registered trademark of Far Future Enterprises.
"""

from colorama import init
from colorama import Fore, Back, Style

init() # initialize colorama
import pyttsx3
import pygame
from pygame.locals import *
import time
from mapper import display_map
import os
import logging
from constants import *
from constants import __app__

engine = pyttsx3.init()

reg_voice_path = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\'

voice = {'US Zira':     {'Name': 'TTS_MS_EN-US_ZIRA_11.0',
                         'Rate': -50,
                         'Volume': -0.0},
         'US David':    {'Name': 'TTS_MS_EN-US_DAVID_11.0',
                         'Rate': -60,
                         'Volume': -0.0}
        }

speaker = 'US Zira'  # Your system's default voice will be used if speaker value is not found in registry.

rate = engine.getProperty('rate')
engine.setProperty('rate', rate + voice[speaker]['Rate'])
volume = engine.getProperty('volume')
engine.setProperty('volume', volume + voice[speaker]['Volume'])
engine.setProperty('voice', reg_voice_path + voice[speaker]['Name'])

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
          'Gateway': (3, 0), 'Hlakhoi': (-4, -2), 'Ziafrplians': (-5, 2),
          'Gvurrdon': (-4, 2), 'Foreven': (-5, 1), 'Tuglikki': (-3, 2),
          'Stiatlchepr': (-6, 3), 'Provence': (-2, 2), 'Itvikiastaf': (-5, 3),
          'Tienspevnekr': (-6, 2), 'Zdiedeiant': (-7,3)
          }

XORG_SECTOR, YORG_SECTOR = sector['Core']

__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'
__version__ = '0.1.0b'

#clock = pygame.time.Clock()

def main(voice_muted, grid_style, zone_style, trade_code, see_thru, show_loc, show_grid):
    
    xx = XORG_SECTOR
    yy = YORG_SECTOR
    
    subxx = 0
    subyy = 0
    
    
    x_zoom_in_level_1_matrix = [-2, -1, -1, 0, 0, 1, 1, 2]
    y_zoom_in_level_1_matrix = [-1, 0, 0, 1]
    x_zoom_in_level_2_matrix = [-1, 0, 0, 1]
    y_zoom_in_level_2_matrix = [0, 1]
    
    x_zoom_out_level_2_matrix = [-1, 0, 0, 1]
    y_zoom_out_level_2_matrix = [0, 0]
    x_zoom_out_level_4_matrix = [0, 0]
    y_zoom_out_level_4_matrix = [0]
    
    zoom = 1
    zooming = False
    
    # zoom and draw_style are optional with this call here
    # zoom = 1 to 4 (default is 1)
    # draw_style = 'HEX_grid_18', 'HEX_grid_20', or 'RECT_grid' (default is 'RECT_grid')
    voiced_sector_name = display_map(xx, yy)
    
    if not voice_muted:
        # some text to speak
        if voiced_sector_name != 'BLANK':
            text = 'displaying area near the ' + voiced_sector_name + ' sector'
        else:
            text = 'this area is unexplored'
    
        engine.say(text)
        engine.runAndWait()
    
    still_displaying = True
    
    while still_displaying:
        
        temp_muted = False
        
        event_scanning = True
        
        while event_scanning:
            event = pygame.event.wait()
            #for event in pygame.event.get():
            
            #print event.type
            if event.type == QUIT:
                still_displaying = False
                event_scanning = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x_mouse_down_pos, y_mouse_down_pos = pos
                if event.button == 4:
                    #Zooming in
                    zooming = True
                    if zoom == 1:
                        x_sector_coord = int(x_mouse_down_pos / (32*X_SPACING*zoom))
                        y_sector_coord = int(y_mouse_down_pos / (40*Y_SPACING*zoom))
                        x_location = x_zoom_in_level_1_matrix[x_sector_coord]
                        y_location = y_zoom_in_level_1_matrix[y_sector_coord]
                        xx += x_location
                        yy += -y_location
                    elif zoom == 2:
                        x_sector_coord = int(x_mouse_down_pos / (32*X_SPACING*zoom))
                        y_sector_coord = int(y_mouse_down_pos / (40*Y_SPACING*zoom))
                        x_location = x_zoom_in_level_2_matrix[x_sector_coord]
                        y_location = y_zoom_in_level_2_matrix[y_sector_coord]
                        xx += x_location
                        yy += -y_location
                    elif zoom == 4:
                        x_sector_coord = int(x_mouse_down_pos / (32*X_SPACING*zoom))
                        y_sector_coord = int(y_mouse_down_pos / (40*Y_SPACING*zoom))
                        temp_xx = xx
                        temp_yy = yy
                        xx += x_sector_coord-1
                        subxx = 0
                        subyy = 0
                    elif zoom == 8:
                        pass
                    zoom += 1
                    if zoom == 3:
                        zoom = 4
                    if zoom == 5:
                        zoom = 8
                    event_scanning = False
                    if zoom > 8:
                        zoom = 8
                        event_scanning = True
                elif event.button == 5:
                    #zooming out
                    zooming = True
                    if zoom == 1:
                        pass
                    elif zoom == 2:
                        x_sector_coord = int(x_mouse_down_pos / (32*X_SPACING*zoom))
                        y_sector_coord = int(y_mouse_down_pos / (40*Y_SPACING*zoom))
                        x_location = x_zoom_out_level_2_matrix[x_sector_coord]
                        y_location = y_zoom_out_level_2_matrix[y_sector_coord]
                        xx += x_location
                        yy += -y_location
                    elif zoom == 4:
                        x_sector_coord = int(x_mouse_down_pos / (32*X_SPACING*zoom))
                        y_sector_coord = int(y_mouse_down_pos / (40*Y_SPACING*zoom))
                        x_location = x_zoom_out_level_4_matrix[x_sector_coord]
                        y_location = y_zoom_out_level_4_matrix[y_sector_coord]
                        xx += x_location
                        yy += -y_location
                    elif zoom == 8:
                        xx = temp_xx
                        yy = temp_yy
                    zoom += -1
                    if zoom == 7:
                        zoom = 4
                    if zoom == 3:
                        zoom = 2
                    event_scanning = False
                    if zoom < 1:
                        zoom = 1
                        event_scanning = True                    
                
            elif event.type == pygame.MOUSEBUTTONUP:
                if not zooming:
                    pos = pygame.mouse.get_pos()
                    x_mouse_up_pos, y_mouse_up_pos = pos
                    if zoom == 1:
                        if x_mouse_down_pos == x_mouse_up_pos and y_mouse_down_pos == y_mouse_up_pos:
                            # sector was clicked on
                            x_sector_distance = int(x_mouse_up_pos / (32*X_SPACING*zoom)) - 4
                            y_sector_distance = int(y_mouse_up_pos / (40*Y_SPACING*zoom)) - 1
                            if x_sector_distance != 0 or y_sector_distance != 0:
                                # origin sector was not clicked on
                                xx += x_sector_distance
                                yy += -y_sector_distance
                                event_scanning = False
                        else:
                            # mouse button was dragged
                            x_mouse_distance = x_mouse_up_pos - x_mouse_down_pos
                            y_mouse_distance = y_mouse_up_pos - y_mouse_down_pos
                            columns_moved = int(x_mouse_distance / (32*X_SPACING*zoom+.5))
                            rows_moved = int(y_mouse_distance / (40*Y_SPACING*zoom+.5))
                            
                            if columns_moved != 0 or rows_moved != 0:
                                xx += -columns_moved
                                yy += rows_moved
                                event_scanning = False
                    elif zoom == 2:
                        if x_mouse_down_pos == x_mouse_up_pos and y_mouse_down_pos == y_mouse_up_pos:
                            # sector was clicked on
                            x_sector_distance = int(x_mouse_up_pos / (32*X_SPACING*zoom)) - 2
                            y_sector_distance = int(y_mouse_up_pos / (40*Y_SPACING*zoom))
                            if x_sector_distance <= -2:
                                xx += -1
                            if x_sector_distance >= 1:
                                xx += 1
                            if x_sector_distance >= -1 and x_sector_distance <= 0:
                                if y_sector_distance == 0:
                                    yy += 1
                                else:
                                    yy += -1
                            event_scanning = False
                        else:
                            # mouse button was dragged
                            x_mouse_distance = x_mouse_up_pos - x_mouse_down_pos
                            y_mouse_distance = y_mouse_up_pos - y_mouse_down_pos
                            columns_moved = int(x_mouse_distance / (32*X_SPACING*zoom+.5))
                            rows_moved = int(y_mouse_distance / (40*Y_SPACING*zoom+.5))
                            
                            if columns_moved != 0 or rows_moved != 0:
                                xx += -columns_moved
                                yy += rows_moved
                                event_scanning = False
                            
                    elif zoom == 4:
                        if x_mouse_down_pos == x_mouse_up_pos and y_mouse_down_pos == y_mouse_up_pos:
                            # sector was clicked on
                            x_sector_distance = int(x_mouse_up_pos / (32*X_SPACING*zoom)) - 1
                            y_sector_distance = int(y_mouse_up_pos / (40*Y_SPACING*zoom))
                            if x_sector_distance == 0:
                                xx += 1
                            else:
                                xx += -1
                            event_scanning = False
                        else:
                            # mouse button was dragged
                            x_mouse_distance = x_mouse_up_pos - x_mouse_down_pos
                            y_mouse_distance = y_mouse_up_pos - y_mouse_down_pos
                            columns_moved = int(x_mouse_distance / (32*X_SPACING*zoom+.5))
                            rows_moved = int(y_mouse_distance / (40*Y_SPACING*zoom+.5))
                            
                            if columns_moved != 0 or rows_moved != 0:
                                xx += -columns_moved
                                yy += rows_moved
                                event_scanning = False
                else:
                    zooming = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if zoom == 8:
                        subxx += -1
                        if subxx < 0:
                            subxx = 0
                        else:
                            event_scanning = False
                    else:
                        xx += -1
                        event_scanning = False
                elif event.key == pygame.K_RIGHT:
                    if zoom == 8:
                        subxx += 1
                        if subxx > 2:
                            subxx = 2
                        else:
                            event_scanning = False
                    else:
                        xx += 1
                        event_scanning = False
                elif event.key == pygame.K_UP:
                    if zoom == 8:
                        subyy += -1
                        if subyy < 0:
                            subyy = 0
                        else:
                            event_scanning = False
                    else:
                        yy += 1
                        event_scanning = False
                elif event.key == pygame.K_DOWN:
                    if zoom == 8:
                        subyy += 1
                        if subyy > 3:
                            subyy = 3
                        else:
                            event_scanning = False
                    else:
                        yy += -1
                        event_scanning = False
                elif event.key == pygame.K_m:
                    if not voice_muted:
                        text = 'muting'
                        voice_muted = True
                    else:
                        text = 'vocalizations enabled'
                        voice_muted = False
                    engine.say(text)
                    engine.runAndWait()
                elif event.key == pygame.K_h:
                    temp_muted = True
                    if zoom == 8:
                        grid_style = 'HEX_grid_40'
                    else:
                        if grid_style == 'HEX_grid_20':
                            grid_style = 'HEX_grid_18'
                        else:
                            grid_style = 'HEX_grid_20'
                    event_scanning = False
                elif event.key == pygame.K_r:
                    temp_muted = True
                    grid_style = 'RECT_grid'
                    event_scanning = False
                elif event.key == pygame.K_c:
                    temp_muted = True
                    see_thru = not see_thru
                    event_scanning = False
                elif event.key == pygame.K_z:
                    temp_muted = True
                    if zone_style == 'fixed':
                        zone_style = 'circled'
                    else:
                        zone_style = 'fixed'
                    event_scanning = False
                elif event.key == pygame.K_t:
                    temp_muted = True
                    trade_code = not trade_code
                    event_scanning = False
                elif event.key == pygame.K_l:
                    temp_muted = True
                    show_loc = not show_loc
                    event_scanning = False
                elif event.key == pygame.K_g:
                    temp_muted = True
                    show_grid = not show_grid
                    event_scanning = False
                elif event.key == pygame.K_ESCAPE:
                    still_displaying = False
                    event_scanning = False

#        msElapsed = clock.tick(30)
        
        if not event_scanning and still_displaying:
            
            if zoom == 8:
                if grid_style == 'HEX_grid_18' or grid_style == 'HEX_grid_20':
                    grid_style = 'HEX_grid_40'
                    
            voiced_sector_name = display_map(xx, yy, zoom, grid_style, zone_style, trade_code, see_thru, show_loc, show_grid, subxx, subyy)
            
            if zoom == 8:
                if grid_style == 'HEX_grid_40':
                    grid_style = 'HEX_grid_20'
                    
            if not voice_muted and not temp_muted:
                # some text to speak
                if zoom == 1:
                    if voiced_sector_name != 'BLANK':
                        text = 'displaying area near the ' + voiced_sector_name + ' sector'
                    else:
                        text = 'this area is unexplored'
                elif zoom == 4:
                    if voiced_sector_name == []:
                        text = 'this area is unexplored'
                    elif len(voiced_sector_name) == 2:
                        text = 'displaying both the ' + voiced_sector_name[0] + ' and ' + voiced_sector_name[1] + ' sectors'
                    else:
                        text = 'displaying the ' + voiced_sector_name[0] + ' sector'
                elif zoom == 8:
                    if voiced_sector_name == []:
                        text = 'this area is unexplored'
                    else:
                        text = 'displaying both the ' + voiced_sector_name[0] + ' and ' + voiced_sector_name[1] + ' subsectors'
                if zoom == 1 or zoom == 4 or zoom == 8:
                    #print text
                    engine.say(text)
                    engine.runAndWait()
            
    print('Exiting ' + __app__)
    log.info(__app__ + ' closing...')
    log.info('Logging ended.')
    
    if not voice_muted:
        # some text to speak
        text = 'Exiting ' + __app__

        engine.say(text)
        engine.runAndWait()
    
if __name__ == '__main__':
    
    voice_muted = True
    grid_style = 'RECT_grid'
    zone_style = 'circled'
    trade_code = False
    see_thru = False
    show_loc = True
    show_grid = True
    
    if not voice_muted:
        # some text to speak
        text = 'Starting ' + __app__

        engine.say(text)
        engine.runAndWait()
        
    log = logging.getLogger('PyMapGen')
    log.setLevel(logging.DEBUG)

    if not os.path.exists('Logs'):
        os.mkdir('Logs')
    
    fh = logging.FileHandler('Logs/pymapgen.log', 'w')
 
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s',
                                  datefmt = '%a, %d %b %Y %H:%M:%S')
    fh.setFormatter(formatter)
    log.addHandler(fh)
    
    log.info('Logging started.')
    log.info(__app__ + ' starting...')
    
    trange = time.localtime()
    if trange[0] > 2031 or trange[1] > 12:
        log.info(__app__ + ' EXPIRED.')
        print()
        print(Fore.RED + Style.BRIGHT + __app__, 'EXPIRED.')
        print(Style.RESET_ALL)
        print()
        print(__author__)
        print()
        s = input('Press ENTER: ')
        print("OK")
    else:
        print()
        print('Thank you for giving', __app__, 'a try.')
        print()
        print('This program uses:')
        vernum, release = display_map('info')
        print(release)
        print('Pygame 2.1.0')
        print('SDL 2.0.16')
        print(Fore.RED + Style.BRIGHT)
        if vernum != '1.1':
            print('WARNING! Different version of mapper installed:', vernum)
            log.warning('WARNING! Different version of mapper installed: ' + vernum)
        if pygame.version.vernum != (2, 1, 0):
            print('WARNING! Different version of Pygame installed:', pygame.version.ver)
        if pygame.get_sdl_version() != (2, 0, 16):
            print('WARNING! Different version of SDL installed:', pygame.get_sdl_version())
        if not pygame.image.get_extended():
            print('No extended image file format support for Pygame.' + Style.RESET_ALL)
        else:
            print(Style.RESET_ALL + 'Extended image file format supported for Pygame.')
        print()
        print('----------------------------')
        print(__author__)
        print()
        print('The Traveller game in all forms is owned by Far Future Enterprises.')
        print('Copyright 1977 - 2022 Far Future Enterprises.')
        print('Traveller is a registered trademark of Far Future Enterprises.')
        print()
        
        main(voice_muted, grid_style, zone_style, trade_code, see_thru, show_loc, show_grid)