
import pygame
from math import cos, sin
import os
import logging
import sys
from constants import __app__
from constants import __py_version_req__
from constants import *

__version__ = '2.0'
__release__ = '2.0.0b'
__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'

mapper_log = logging.getLogger('mapper')
mapper_log.setLevel(logging.DEBUG)

if not os.path.exists('Logs'):
    os.mkdir('Logs')

fh = logging.FileHandler('Logs/mapper.log', 'w')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s',
                              datefmt = '%a, %d %b %Y %H:%M:%S')
fh.setFormatter(formatter)
mapper_log.addHandler(fh)

mapper_log.info('Logging started.')
mapper_log.info('mapper v' + __version__ + ' started, and running...')

white = (255, 255, 255)
black = (0, 0, 0)
gray = (60, 60, 60)
medium_gray = (120, 120, 120)
green = (0, 255, 0)
red = (255, 0, 0)
yellow  = (255, 255, 0)
orange = (255, 165 ,0)
amber = (255, 191, 0)
blue = (0, 0, 255)
darker_blue = (0, 0, 150)
purple = (255, 0, 255)
cyan = (0,255,255)
light_green = (144, 238, 144)
pink = (255, 105, 180)
dark_green = (100, 190, 100)
light_blue = (135, 206, 250)
gold = (255, 215, 0)
maya_blue = (79, 214, 255)
bright_green = (102, 255, 0)
brown = (150,75,0)
light_purple = (177, 156, 217)
light_red = (255, 102, 102)
lightish_blue = (153, 153, 255)
canary_yellow = (255, 239, 0)
dark_red = (139, 0, 0)
light_brown = (181, 101, 29)
tan = (210, 180, 140)
light_gray = (200, 200, 200)
silver = (192, 192, 192)
rust = (183, 65, 14)
yellow_green = (154, 205, 50)
peach = (255, 229, 180)
pear = (209, 226, 49)
dark_grey = (40, 40, 40)
wood = (193, 154, 107)
maroon = (123, 17, 19)
dark_purple = (48, 25, 52)
white_pink = (171, 39, 79)
deep_purple = (255, 0, 224)
light_pink = (246, 148, 206)

allegiance_color = {'4Wor': purple,
                    '6w': blue,
                    '6w  ': blue,
                    'AkUn': gold,
                    'AlCo': gray,
                    'As': yellow,
                    'As  ': yellow,
                    'AsIf': tan,
                    'AsMw': yellow,
                    'AsOf': yellow,
                    'AsSc': yellow,
                    'AsT0': yellow,
                    'AsT1': yellow,
                    'AsT2': yellow,
                    'AsT3': yellow,
                    'AsT4': yellow,
                    'AsT5': yellow,
                    'AsT6': yellow,
                    'AsT7': yellow,
                    'AsT8': yellow,
                    'AsT9': yellow,
                    'AsTA': gray,
                    'AsTv': yellow,
                    'AsVc': yellow,
                    'AsWc': yellow,
                    'AsXX': yellow,
                    'AU': yellow,
                    'AU  ': yellow,
                    'Bium': yellow,
                    'BlSo': dark_purple,
                    'CA': purple,
                    'CA  ': purple,
                    'CAEM': orange,
                    'CAin': tan,
                    'Ca': yellow,
                    'Ca  ': yellow,
                    'Cl': yellow_green,
                    'Cl  ': yellow_green,
                    'CoLg': tan,
                    'Cr': orange,
                    'Cr  ': orange,
                    'Cs': cyan,
                    'Cs  ': cyan,
                    'CsMP': pink,
                    'CsTw': yellow_green,
                    'CsZh': blue,
                    'DaCf': light_blue,
                    'DeHg': pink,
                    'DeNo': green,
                    'DiGr': cyan,
                    'DiWb': purple,
                    'DoAl': purple,
                    'Ed': purple,
                    'Ed  ': purple,
                    'EsMa': gray,
                    'FCSA': cyan,
                    'FeAl': gray,
                    'FeHe': orange,
                    'Ff': light_green,
                    'Ff  ': light_green,
                    'FlLe': green,
                    'Fj': gray,
                    'Fj  ': gray,
                    'GaFd': red,
                    'GaRp': gray,
                    'GdKa': gold,
                    'GdSt': purple,
                    'GlEm': gray,
                    'GlFe': blue,
                    'GrCo': pink,
                    'Gs': red,
                    'Gs  ': red,
                    'H1': purple,
                    'H1  ': purple,
                    'H2': purple,
                    'H2  ': purple,
                    'H3': purple,
                    'H3  ': purple,
                    'H4': purple,
                    'H4  ': purple,
                    'H5': purple,
                    'H5  ': purple,
                    'H6': purple,
                    'H6  ': purple,
                    'HaCo': red,
                    'Hc': gold,
                    'Hc  ': gold,
                    'HeCo': light_gray,
                    'HoPA': green,
                    'Hp': green,
                    'Hp  ': green,
                    'Hq': green,
                    'Hq  ': green,
                    'Hs': pink,
                    'Hs  ': pink,
                    'Hv': purple,
                    'Hv  ': purple,
                    'HvFd': purple,
                    'Hy': green,
                    'Hy  ': green,
                    'Ia': pink,
                    'Ia  ': pink,
                    'IHPr': pink,
                    'Im': red,
                    'Im  ': red,
                    'ImAp': blue,
                    'ImDa': red,
                    'ImDc': red,
                    'ImDd': red,
                    'ImDg': red,
                    'ImDi': red,
                    'ImDs': red,
                    'ImDv': red,
                    'ImLa': red,
                    'ImLc': blue,
                    'ImLu': darker_blue,
                    'ImSy': blue,
                    'ImVd': blue,
                    'Iz': green,
                    'Iz  ': green,
                    'JaPa': green,
                    'JuHl': blue,
                    'JuNa': pink,
                    'JuRu': dark_green,
                    'K1': green,
                    'K1  ': green,
                    'K2': light_green,
                    'K2  ': light_green,
                    'K3': yellow_green,
                    'K3  ': yellow_green,
                    'K4': green,
                    'K4  ': green,
                    'KaEm': red,
                    'Kc': light_green,
                    'Kc  ': light_green,
                    'KhLe': yellow,
                    'Kk': green,
                    'Kk  ': green,
                    'Kl': green,
                    'Kl  ': green,
                    'Kr': blue,
                    'Kr  ': blue,
                    'KrBu': cyan,
                    'Kx': red,
                    'Kx  ': red,
                    'LaCo': orange,
                    'LeSu': green,
                    'LnRp': cyan,
                    'Lt': purple,
                    'Lt  ': purple,
                    'Lx': light_green,
                    'Lx  ': light_green,
                    'MaCl': gray,
                    'MaEm': pink,
                    'MaPr': pink,
                    'MaUn': gray,
                    'Mi': pink,
                    'Mi  ': pink,
                    'MiCo': red,
                    'MoLo': gold,
                    'MnPr': gray,
                    'Mp': yellow_green,
                    'Mp  ': yellow_green,
                    'Na': white,
                    'Na  ': white,
                    'NaHu': white,
                    'NkCo': light_blue,
                    'Og': light_green,
                    'Og  ': light_green,
                    'Pd': purple,
                    'Pd  ': purple,
                    #'NaXX': purple,
                    'PiFe': blue,
                    'PlLe': pink,
                    'PrBr': purple,
                    'Prot': yellow,
                    'Rc': pink,
                    'Rc  ': pink,
                    'Re': red,
                    'Re  ': red,
                    'ReUn': red,
                    'Rm': green,
                    'Rm  ': green,
                    'SaCo': cyan,
                    'SC': cyan,
                    'SC  ': cyan,
                    'SeFo': yellow_green,
                    'ShRp': cyan,
                    'SlLg': gold,
                    'So': orange,
                    'So  ': orange,
                    'SoBf': blue,
                    'SoCf': orange,
                    'SoCT': blue,
                    'SoBF': blue,
                    'SoFr': blue,
                    'SoHn': blue,
                    'SoKv': blue,
                    'SoNS': blue,
                    'SoQu': blue,
                    'SoRD': blue,
                    'SoRz': blue,
                    'SoWu': blue,
                    'Sp': gold,
                    'Sp  ': gold,
                    'Sr': red,
                    'Sr  ': red,
                    'Ss': red,
                    'Ss  ': red,
                    'StCl': yellow,
                    'SwCf': blue,
                    'SwFW': gray,
                    'Tc': gold,
                    'Tc  ': gold,
                    'Te': tan,
                    'Te  ': tan,
                    'TeCl': green,
                    'Tk': orange,
                    'Tk  ': orange,
                    'Tl': gold,
                    'Tl  ': gold,
                    'TL': gold,
                    'TL  ': gold,
                    'Tn': tan,
                    'Tn  ': tan,
                    'TrBr': green,
                    'TrCo': blue,
                    'TrDo': red,
                    'TY': light_purple,
                    'TY  ': light_purple,
                    'UnGa': gray,
                    'Up': light_gray,
                    'Up  ': light_gray,
                    'V40S': yellow_green,
                    'Va': yellow_green,
                    'Va  ': yellow_green,
                    'VA': yellow_green,
                    'VA  ': yellow_green,
                    'VAkh': yellow_green,
                    'VARC': yellow_green,
                    'VAug': yellow_green,
                    'VAsP': yellow_green,
                    'VB': yellow_green,
                    'VB  ': yellow_green,
                    'VBkA': yellow_green,
                    'VCKd': yellow_green,
                    'VD': yellow_green,
                    'VD  ': yellow_green,
                    'VDeG': yellow_green,
                    'VDzF': peach,
                    'VE': yellow_green,
                    'VE  ': yellow_green,
                    'Ve': yellow_green,
                    'Ve  ': yellow_green,
                    'VF': yellow_green,
                    'VF  ': yellow_green,
                    'VG': yellow_green,
                    'VG  ': yellow_green,
                    'ViCo': orange,
                    'VInL': yellow_green,
                    'VJ': yellow_green,
                    'VJ  ': yellow_green,
                    'VK': yellow_green,
                    'VK  ': yellow_green,
                    'VKfu': yellow_green,
                    'VL': yellow_green,
                    'VL  ': yellow_green,
                    'VNoe': yellow_green,
                    'VOpA': yellow_green,
                    'VOuz': yellow_green,
                    'VP': yellow_green,
                    'VP  ': yellow_green,
                    'VPGa': yellow_green,
                    'VR': yellow_green,
                    'VR  ': yellow_green,
                    'VRrs': yellow_green,
                    'VRuk': yellow_green,
                    'VS': yellow_green,
                    'VS  ': yellow_green,
                    'VSDp': yellow_green,
                    'VSEq': yellow_green,
                    'VThE': yellow_green,
                    'VTzE': yellow_green,
                    'VU': yellow_green,
                    'VU  ': yellow_green,
                    'VUru': yellow_green,
                    'VVar': yellow_green,
                    'VWan': yellow_green,
                    'VWP2': yellow_green,
                    'VX': yellow_green,
                    'VX  ': yellow_green,
                    'VZ': yellow_green,
                    'VZ  ': yellow_green,
                    'WiDe': purple,
                    'Yc' : gray,
                    'Yc  ': gray,
                    'Yt': cyan,
                    'Yt  ': cyan,
                    'ZePr': yellow,
                    'Zh': blue,
                    'Zh  ': blue,
                    'ZhAx': red,
                    'ZhCa': blue,
                    'ZhIN': blue,
                    'ZhIa': blue,
                    'ZhJp': blue,
                    'ZhMe': blue,
                    'ZhSh': blue,
                    'ZyCo': light_pink
                    }

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

text_rotate_degrees = 45

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
window_title = __app__
pygame.display.set_caption(window_title)
window_icon = pygame.image.load('images/shonner_die_alpha.png')
pygame.display.set_icon(window_icon)

agricultural_world = pygame.image.load('images/agricultural_70.png').convert_alpha()
garden_world = pygame.image.load('images/garden_70.png').convert_alpha()
desert_world = pygame.image.load('images/desert_0.png').convert_alpha()
ice_capped_world = pygame.image.load('images/ice_capped_100.png').convert_alpha()
industrial_world = pygame.image.load('images/industrial_0.png').convert_alpha()
non_agricultural_world = pygame.image.load('images/non_agricultural_30.png').convert_alpha()
non_industrial_world = pygame.image.load('images/non_industrial_30.png').convert_alpha()
water_world = pygame.image.load('images/water_100.png').convert_alpha()
fluid_world = pygame.image.load('images/fluid_100.png').convert_alpha()
vacuum_world = pygame.image.load('images/vacuum_0.png').convert_alpha()
asteroid = pygame.image.load('images/asteroid_0.png').convert_alpha()
dieback_world = pygame.image.load('images/dieback_0.png').convert_alpha()
barren_world = pygame.image.load('images/barren_0.png').convert_alpha()
zero_water_world = pygame.image.load('images/zero_water.png').convert_alpha()
generic_10 = pygame.image.load('images/generic_10.png').convert_alpha()
generic_20 = pygame.image.load('images/generic_20.png').convert_alpha()
generic_30 = pygame.image.load('images/generic_30.png').convert_alpha()
generic_40 = pygame.image.load('images/generic_40.png').convert_alpha()
generic_50 = pygame.image.load('images/generic_50.png').convert_alpha()
generic_60 = pygame.image.load('images/generic_60.png').convert_alpha()
generic_70 = pygame.image.load('images/generic_70.png').convert_alpha()
generic_80 = pygame.image.load('images/generic_80.png').convert_alpha()
generic_90 = pygame.image.load('images/generic_90.png').convert_alpha()
generic_100 = pygame.image.load('images/water_100.png').convert_alpha()

world_scale = 4

# for jj in range(11):
#     print 8 + jj*4,
# print

def _planet(surface, color, pos, radius, thickness, world_size, world_atmosphere, world_hydrographics, world_population, world_trade):
    world_image =''
    if world_atmosphere >= 4 and world_atmosphere <= 9 \
                and world_hydrographics >= 4 and world_hydrographics <= 8 \
                and world_population >= 5 and world_population <= 7:
        world_image = agricultural_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if world_size >= 6 \
                and world_size <= 8 \
                and (world_atmosphere == 5 or world_atmosphere == 6 or world_atmosphere == 8) \
                and world_hydrographics >= 5 and world_hydrographics <= 7:
        world_image = garden_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if world_atmosphere >= 2 \
                and world_hydrographics == 0:
        world_image = desert_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if world_atmosphere >= 0 \
                and world_atmosphere <= 1 \
                and world_hydrographics >= 1:
        world_image = ice_capped_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if (world_atmosphere >= 0 \
                and world_atmosphere <= 2 \
                or world_atmosphere == 4 \
                or world_atmosphere == 7 \
                or world_atmosphere == 9) \
                and world_population >= 9:
        world_image = industrial_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if world_atmosphere >= 0 and world_atmosphere <= 3 \
                and world_hydrographics >= 0 and world_hydrographics <= 3 \
                and world_population >= 6:
        world_image = non_agricultural_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if world_population <= 6:
        world_image = non_industrial_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if world_hydrographics == 0:
        world_image = zero_water_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if world_hydrographics == 10 \
                and world_atmosphere >= 1 and world_atmosphere <= 9:
        world_image = water_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if world_atmosphere >= 10 and world_atmosphere <= 12 \
                and world_hydrographics >= 1 and world_hydrographics <= 10:
        world_image = fluid_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if world_atmosphere == 0:
        world_image = vacuum_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if world_size == 0 \
                and world_atmosphere == 0 \
                and world_hydrographics == 0:
        world_image = asteroid
        world_image = pygame.transform.scale(world_image, (24, 24))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if 'Ag' in world_trade:
        world_image = agricultural_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if 'De' in world_trade:
        world_image = desert_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if 'Ba' in world_trade:
        world_image = barren_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if 'Di' in world_trade:
        world_image = dieback_world
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
    if world_image == '':
        world_image = eval('generic_' + str(world_hydrographics * 10))
        world_image = pygame.transform.scale(world_image, (8 + world_size*world_scale, 8 + world_size*world_scale))
        x, y = pos
        w, h = world_image.get_size()
        surface.blit(world_image, (x-w/2, y-h/2))
        #_circle(screen, color, pos, radius, thickness)

def _pixel(surface, color, pos):
    pygame.draw.line(surface, color, pos, pos)

def _circle(surface, color, pos, radius, thickness, see_thru=False):
    if see_thru:
        temp_surf = pygame.Surface((radius*2, radius*2))
        temp_surf.fill(TRANSPARENT)
        temp_surf.set_colorkey(TRANSPARENT)
        pygame.draw.circle(temp_surf, (color[0], color[1], color[2], 120), (radius, radius), radius)
        temp_surf.set_alpha(120)
        surface.blit(temp_surf, (pos[0]-radius, pos[1]-radius, radius*2, radius*2))
    else:
        pygame.draw.circle(surface, color, pos, radius, thickness)

def _rectangle(surface, color, coords, thickness, see_thru=False):
    if see_thru:
        temp_surf = pygame.Surface((coords[2], coords[3]))
        temp_surf.fill(TRANSPARENT)
        temp_surf.set_colorkey(TRANSPARENT)
        pygame.draw.rect(temp_surf, (color[0], color[1], color[2], 120), [0, 0, coords[2], coords[3]])
        temp_surf.set_alpha(120)
        surface.blit(temp_surf, (coords[0], coords[1], coords[2], coords[3]))
    else:
        pygame.draw.rect(surface, color, coords, thickness)
    
def _hexagon(surface, color, pos, radius, thickness, see_thru=False):
    n_sides = 6
    step = 360 / n_sides
    angle = 0
    points = []
    for i in range(n_sides):
        if see_thru:
            x = radius + radius*cos(angle*3.14159265359/180)
            y = radius + radius*sin(angle*3.14159265359/180)
        else:
            x = pos[0] + radius*cos(angle*3.14159265359/180)
            y = pos[1] + radius*sin(angle*3.14159265359/180)
        angle += step
        points.append((x,y))
    if see_thru:
        temp_surf = pygame.Surface((radius*2, radius*2))
        temp_surf.fill(TRANSPARENT)
        temp_surf.set_colorkey(TRANSPARENT)
        pygame.draw.polygon(temp_surf, (color[0], color[1], color[2], 120), points)
        temp_surf.set_alpha(120)
        surface.blit(temp_surf, (pos[0]-radius, pos[1]-radius, radius*2, radius*2))
    else:
        pygame.draw.polygon(surface, color, points, thickness)

def display_map(xx=0, yy=0, zoom=1, grid_style='RECT_grid', zone_style='circled', trade_code=False, see_thru=False, show_loc=True, show_grid=True, subxx=0, subyy=0):
    
    log = logging.getLogger('PyMapGen.mapper')

    # was information for this program asked for?
    if xx == 'info':
        ver = 'mapper, release version ' + __release__ + ' for Python ' + str(__py_version_req__)
        mapper_log.info('Reporting: mapper release version: %s' % __release__)
        return __version__, ver

    mapper_log.debug('Displaying map at ' + str(zoom) + 'X zoom. Style used = ' + grid_style)

    x_zoom = zoom
    y_zoom = zoom
    
    #print 'xx=%d, yy=%d zoom=%d' % (xx,yy, zoom)
    
    screen.fill(black)
    
    voiced_sector_name = 'BLANK'
    sector_names = []
    sectors_filled = []
    voiced_subector_name = 'BLANK'
    subsector_names = []
    
    if zoom < 8:
        for y in range(ROWS//y_zoom):
            for x in range(COLUMNS//x_zoom):
                
                sectors_filled.append(0)
                
        sect_point = 0   
        
        capitals_list = []
        
        for y in range(ROWS//y_zoom):
            for x in range(COLUMNS//x_zoom):
                if zoom == 1:
                    sector_x = x - COLUMNS//2 + xx
                    sector_y = y - ROWS//2 + 1 - yy
                elif zoom == 2:
                    sector_x = x - COLUMNS//4 + xx
                    sector_y = y - ROWS//4 + 1 - yy
                elif zoom == 4:
                    sector_x = x - 1 + xx
                    sector_y = -yy
                
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
                        
                        color = gray
                        pygame.draw.rect(screen, color, (x*32*X_SPACING*x_zoom, y*40*Y_SPACING*y_zoom, 32*X_SPACING*x_zoom, 40*Y_SPACING*y_zoom), DOT_SIZE*zoom)
                        
                        
                        if show_grid:
                            for i in range(32):
                                for j in range(40):
                        
                                    color = gray
                                    
                                    if i // 2 == i / 2.0:
                                        if zoom < 4:
                                            _pixel(screen, color, (i*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom, j*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom))
                                        else:
                                            #_circle(screen, color, (i*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom, j*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom), DOT_SIZE, 0)
                                            if grid_style == 'RECT_grid':
                                                _rectangle(screen, color, [i*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom + 2,
                                                                           j*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom + 2,
                                                                           14,
                                                                           15],
                                                                           DOT_SIZE-1)
                                            elif grid_style == 'HEX_grid_20' or grid_style == 'HEX_grid_18':
                                                _hexagon(screen, color, (i*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom + 9,
                                                                         j*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom + 9),
                                                                         int(grid_style[9:11])//2,
                                                                         1)
                                    else:
                                        if zoom < 4:
                                            _pixel(screen, color, (i*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom, j*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom))
                                        else:
                                            #_circle(screen, color, (i*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom, j*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom), DOT_SIZE, 0)
                                            if grid_style == 'RECT_grid':
                                                _rectangle(screen, color, [i*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom + 2,
                                                                           j*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom + OFFSET*y_zoom + 2,
                                                                           14,
                                                                           15],
                                                                           DOT_SIZE-1)
                                            elif grid_style == 'HEX_grid_20' or grid_style == 'HEX_grid_18':
                                                _hexagon(screen, color, (i*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom + 9,
                                                                         j*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom + 9),
                                                                         int(grid_style[9:11])//2,
                                                                         1)
                        
                        for line in sec_file_in:
                            #print line[:len(line)-1]
                            read_line += 1
                            if read_line == 4:
                                sector_name = line[2:len(line)-1]
                                #print(sector_x, sector_y, (xx, yy))
                                if sector_x == xx and sector_y == -yy:
                                    voiced_sector_name = sector_name
                                #print(sector_name)
                                sector_names.append(sector_name)
                                sectors_filled[sect_point] = 1
                                sect_point += 1
                            if read_line == 5:
                                sector_offset = eval(line[2:len(line)-1])
                                #print(sector_offset, end=' ')
                                #print(sector_offset[0], -sector_offset[1])
                                added_sectors[sector_name] = (sector_offset[0], -sector_offset[1])
                            if line[:3] == 'Hex':
                                name_tab = line.find('Name')
                                allegiance_tab = line.find('A')
                                world_tab = line.find('UWP')
                                pop_m_tab = line.find('PBG')
                                travel_code_tab = line.find('Z')
                            if line[:1] == '-':
                                allegiance_length = line[allegiance_tab:allegiance_tab+6].find(' ')
                            if line[:1] != '#' and line[:1] != '-' and line[:1] != 'H' and len(line) > 3:
                                if int(line[:4]) > 0:
                                    #print(line[allegiance_tab:allegiance_tab+allegiance_length], len(line[allegiance_tab:allegiance_tab+allegiance_length]))
                                    if line[allegiance_tab:allegiance_tab+allegiance_length] not in allegiance_color:
                                        color = white
                                    else:
                                        color = allegiance_color[line[allegiance_tab:allegiance_tab+allegiance_length]]
                                        
                                    hex_x=int(line[0:2]) - 1
                                    hex_y=int(line[2:4]) - 1
    
                                    #population = hex_code[line[world_tab+4]] * int(line[pop_m_tab])
                                    population = hex_code[line[world_tab+4]]
                                    world_name = line[name_tab:name_tab+19].strip()
                                    if hex_x // 2 == hex_x / 2.0:
                                        if world_name == 'Reference' or world_name == 'Capital' \
                                        or world_name == 'Regina' or world_name == 'Vland' \
                                        or world_name == 'Terra' or world_name =='Guaran' \
                                        or world_name == 'Glea' or world_name == 'Kusyu' \
                                        or world_name == 'Zhdant' or world_name == 'Lair':
                                            color = yellow
                                            if zoom == 4:
                                                _circle(screen, color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10 , int(hex_y*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom) + 10), 8, 0)
                                                capitals_list.append((world_name, int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom) + 10))
                                            else:
                                                _circle(screen, color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom), int(hex_y*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom)), 8, 0)
                                                capitals_list.append((world_name, int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom), int(hex_y*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom)))
    #                                     if color == red or color == amber:
    #                                         _circle(screen, color, (hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom, hex_y*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom), DOT_SIZE*population**.5 + 1, 1)
                                        #color = white
                                        if population < 10:
                                            if zoom == 1:
                                                _pixel(screen, color, (hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom, hex_y*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom))
                                            else:
                                                if zoom == 4:
                                                    if line[travel_code_tab] == 'R':
                                                        zone_color = red
                                                        _circle(screen, zone_color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom) + 10), int(zoom+2), 1)
                                                    if line[travel_code_tab] == 'A':
                                                        zone_color = amber
                                                        _circle(screen, zone_color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom) + 10), int(zoom+2), 1)
                                                    _circle(screen, color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom) + 10), int(zoom), 0)
                                                else:
                                                    _circle(screen, color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom), int(hex_y*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom)), 2, 0)
                                        else:
                                            #color = orange
                                            if zoom == 4:
                                                if line[travel_code_tab] == 'R':
                                                    zone_color = red
                                                    _circle(screen, zone_color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom) + 10), int(zoom+2), 1)
                                                if line[travel_code_tab] == 'A':
                                                    zone_color = amber
                                                    _circle(screen, zone_color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom) + 10), int(zoom+2), 1)
                                                _circle(screen, color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom) + 10), int(zoom), 0)
                                            else:
                                                _circle(screen, color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom), int(hex_y*Y_SPACING*y_zoom + y*40*Y_SPACING*y_zoom)), int(zoom*2), 0)
                                    else:
                                        if world_name == 'Reference' or world_name == 'Capital' \
                                        or world_name == 'Regina' or world_name == 'Vland' \
                                        or world_name == 'Terra' or world_name =='Guaran' \
                                        or world_name == 'Glea' or world_name == 'Kusyu' \
                                        or world_name == 'Zhdant' or world_name == 'Lair':
                                            color = yellow
                                            if zoom == 4:
                                                _circle(screen, color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom) + 10), 8, 0)
                                                capitals_list.append((world_name, int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom) + 10))
                                            else:
                                                _circle(screen, color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom), int(hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom)), 8, 0)
                                                capitals_list.append((world_name, int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom), int(hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom)))
    #                                     if color == red or color == amber:
    #                                         _circle(screen, color, (hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom, hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom), DOT_SIZE*population**.5 + 1, 1)
                                        #color = white
                                        if population < 10:
                                            if zoom == 1:
                                                _pixel(screen, color, (hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom, hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom))
                                            else:
                                                if zoom == 4:
                                                    if line[travel_code_tab] == 'R':
                                                        zone_color = red
                                                        _circle(screen, zone_color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom) + 10), int(zoom+2), 1)
                                                    if line[travel_code_tab] == 'A':
                                                        zone_color = amber
                                                        _circle(screen, zone_color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom) + 10), int(zoom+2), 1)
                                                    _circle(screen, color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom) + 10), int(zoom), 0)
                                                else:
                                                    _circle(screen, color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom), int(hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom)), 2, 0)
                                        else:
                                            #color = orange
                                            if zoom == 4:
                                                if line[travel_code_tab] == 'R':
                                                    zone_color = red
                                                    _circle(screen, zone_color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom) + 10), int(zoom+2), 1)
                                                if line[travel_code_tab] == 'A':
                                                    zone_color = amber
                                                    _circle(screen, zone_color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom) + 10), int(zoom+2), 1)
                                                _circle(screen, color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom) + 10, int(hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom) + 10), int(zoom), 0)
                                            else:
                                                _circle(screen, color, (int(hex_x*X_SPACING*x_zoom + x*32*X_SPACING*x_zoom), int(hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + y*40*Y_SPACING*y_zoom)), int(zoom*2), 0)                       
                    
                except IOError:
                    #print 'No ' + sec_filename + '.dat'
                    log.warning("Missing '" + sec_filename + ".dat' file [Warning]")
                    mapper_log.warning("Display Warning! '" + sec_filename + ".dat' is missing.")
                    sect_point += 1

        for i in range(len(capitals_list)):
            world_name_font = pygame.font.SysFont('Eras ITC Demi', 24, False, False)
            world_name_text = world_name_font.render(capitals_list[i][0], True, white)
            screen.blit(world_name_text, [capitals_list[i][1],
                                          capitals_list[i][2]-20])
        #print added_sectors
        #print sector_names
        #print sectors_filled
        saved_sector_list = list(sector_names)
        sector_name_pointer = 0
        
        # rotate sector labels and print them
        sect_point = 0
        for y in range(ROWS//y_zoom):
            for x in range(COLUMNS//x_zoom):
                if sectors_filled[sect_point] == 1:
                    printing = True
                    x_line_spacing = 0
                    y_line_spacing = 0
                    while printing:
                        space_check = sector_names[sector_name_pointer].find(' ')
                        if space_check == -1:
                            font = pygame.font.SysFont('Eras ITC Demi', 26*zoom, False, True)
                            text = font.render(sector_names[sector_name_pointer], True, white)
                            text = pygame.transform.rotate(text, text_rotate_degrees)
                            alpha_img = pygame.Surface(text.get_rect().size, pygame.SRCALPHA)
                            alpha_img.fill((255, 255, 255, 180 + (255-180)//(zoom*3)))
                            text.blit(alpha_img, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                            screen.blit(text, [x*32*X_SPACING*x_zoom + 32*X_SPACING*x_zoom/6 + x_line_spacing, y*40*Y_SPACING*y_zoom + 40*Y_SPACING*y_zoom/6 + y_line_spacing])
                            printing = False
                            sector_name_pointer += 1
                        else:
                            font = pygame.font.SysFont('Eras ITC Demi', 26*zoom, False, True)
                            text = font.render(sector_names[sector_name_pointer][:space_check], True, white)
                            text = pygame.transform.rotate(text, text_rotate_degrees)
                            alpha_img = pygame.Surface(text.get_rect().size, pygame.SRCALPHA)
                            alpha_img.fill((255, 255, 255, 180 + (255-180)//(zoom*3)))
                            text.blit(alpha_img, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                            screen.blit(text, [x*32*X_SPACING*x_zoom + 32*X_SPACING*x_zoom/6 + x_line_spacing, y*40*Y_SPACING*y_zoom + 40*Y_SPACING*y_zoom/6 + y_line_spacing])
                            sector_names[sector_name_pointer] = sector_names[sector_name_pointer][space_check+1:len(sector_names[sector_name_pointer])]
                            x_line_spacing += 20
                            y_line_spacing += 40*zoom
                sect_point += 1
    else:
        #print('subxx=%d, subyy=%d, zoom-8, style=%s' % (subxx,subyy,grid_style))
        
        subsector_list = []
        # Display zoom-8. Two subectors.
        for x in range(2):
            
            sec_filename = 'sec'
                
            if xx < 0:
                sec_filename += '_m'
            else:
                sec_filename += '_p'
            if xx < -9 or xx > 9:
                sec_filename += str(abs(xx))
            else:
                sec_filename += '0' + str(abs(xx))
            
            if -yy < 0:
                sec_filename += '_m'
            else:
                sec_filename += '_p'
            if -yy < -9 or -yy > 9:
                sec_filename += str(abs(-yy))
            else:
                sec_filename += '0' + str(abs(-yy))

            try:
                read_line = 0
                with open('data/' + sec_filename + '.dat', 'r') as sec_file_in:

                    subsector_list = []
                    for line in sec_file_in:
                        #print line[:len(line)-1]
                        if line[:11] == '# Subsector':
                            subsector_list.append(line[15:len(line)-1])

                    #print(subsector_list)
                    #print(subsector_list[subxx + subyy*4], subsector_list[subxx+1 + subyy*4])
                    subsector_names = []
                    subsector_names.append(subsector_list[subxx + subyy*4])
                    subsector_names.append(subsector_list[subxx+1 + subyy*4])
                    #print(subsector_names[x])
                    
                    color = gray
                    pygame.draw.rect(screen, color, (x*512, 0, 512, 703), DOT_SIZE*2)

                    for i in range(8):
                        for j in range(10):
                            
                            parsec_loc = ''
                            p_column = i + (subxx+x)*8 + 1
                            if p_column < 10:
                                parsec_loc += '0' + str(p_column)
                            else:
                                parsec_loc += str(p_column)
                            p_row = j + subyy*10 + 1
                            if p_row < 10:
                                parsec_loc += '0' + str(p_row)
                            else:
                                parsec_loc += str(p_row)
                                
                            color = gray

                            font = pygame.font.SysFont('Eras ITC Demi', 12, False, False)
                            text = font.render(parsec_loc, True, color)
                            
                            if i//2 == i/2.0:
                                if grid_style == 'RECT_grid':
                                    if show_grid:
                                        _rectangle(screen, color, [i*64 + 4 + x*512,
                                                                   j*70.4 + 4,
                                                                   56,
                                                                   63],
                                                                   DOT_SIZE-1)
                                    if show_loc:
                                        screen.blit(text, [i*64 + 22 + x*512, j*70.4 + 7])
                                elif grid_style == 'HEX_grid_40':
                                    if show_grid:
                                        _hexagon(screen, color, (i*64 + 24 + x*512,
                                                                 j*70.4 + 32),
                                                                 int(grid_style[9:11]), 1)
                                    if show_loc:
                                        screen.blit(text, [i*64 + 14 + x*512, j*70.4])
                            else:
                                if grid_style == 'RECT_grid':
                                    if show_grid:
                                        _rectangle(screen, color, [i*64 + 4 + x*512,
                                                                   j*70.4 + 4 + 36,
                                                                   56,
                                                                   63],
                                                                   DOT_SIZE-1)
                                    if show_loc:
                                        screen.blit(text, [i*64 + 22 + x*512, j*70.4 + 7 + 36])
                                elif grid_style == 'HEX_grid_40':
                                    if show_grid:
                                        _hexagon(screen, color, (i*64 + 24 + x*512,
                                                                 j*70.4 + 32 + 36),
                                                                 int(grid_style[9:11]), 1)
                                    if show_loc:
                                        screen.blit(text, [i*64 + 14 + x*512, j*70.4 + 36])
                    
                    color = medium_gray
                            
                    font = pygame.font.SysFont('Eras ITC Demi', 96, False, False)
                    text = font.render(subsector_names[x], True, color)
                    text.set_alpha(180)
                    width = len(subsector_names[x])
                    screen.blit(text, [x*512 + 256 - width*36/2, 100])

                    sec_file_in.seek(0)
                    for line in sec_file_in:
                        read_line += 1
                        if read_line == 4:
                            sector_name = line[2:len(line)-1]
                            #print sector_x, sector_y, (xx, yy)
                            #if sector_x == xx and sector_y == -yy:
                            voiced_sector_name = sector_name
                            #print sector_name
                            #sector_names.append(sector_name)
                            #sectors_filled[sect_point] = 1
                            #sect_point += 1
                        if read_line == 5:
                            sector_offset = eval(line[2:len(line)-1])
                            #print sector_offset,
                            #print sector_offset[0], -sector_offset[1]
                            #added_sectors[sector_name] = (sector_offset[0], -sector_offset[1])
                        if line[:3] == 'Hex':
                            name_tab = line.find('Name')
                            remarks_tab = line.find('Remarks')
                            allegiance_tab = line.find('A')
                            world_tab = line.find('UWP')
                            pop_m_tab = line.find('PBG')
                            travel_code_tab = line.find('Z')
                        if line[:1] == '-':
                            allegiance_length = line[allegiance_tab:allegiance_tab+6].find(' ')
                        if line[:1] != '#' and line[:1] != '-' and line[:1] != 'H' and len(line) > 3:
                            if int(line[:4]) > 0:
                                #print line[allegiance_tab:allegiance_tab+allegiance_length], len(line[allegiance_tab:allegiance_tab+allegiance_length])
                                if line[allegiance_tab:allegiance_tab+allegiance_length] not in allegiance_color:
                                    color = white
                                else:
                                    color = allegiance_color[line[allegiance_tab:allegiance_tab+allegiance_length]]
                                    
                                hex_x=int(line[0:2])
                                hex_y=int(line[2:4])
                                #print hex_x, hex_y
                                if hex_x > (subxx+x)*8 and hex_x <= (subxx+x)*8+8 and hex_y > subyy*10 and hex_y <= subyy*10+10:
                                    
                                    
                                    temp_x = hex_x - 8*(subxx+x)
                                    temp_y = hex_y - 10*subyy
                                    
                                    world_size = hex_code[line[world_tab+1]]
                                    world_atmosphere = hex_code[line[world_tab+2]]
                                    world_hydrographics = hex_code[line[world_tab+3]]
                                    #population = hex_code[line[world_tab+4]] * int(line[pop_m_tab])
                                    world_population = hex_code[line[world_tab+4]]
                                    world_name = line[name_tab:name_tab+19].strip()
                                    world_name_color = white
                                    world_trade = line[remarks_tab:remarks_tab+20]
                                    if 'Cx' in world_trade or 'Cp' in world_trade:
                                        world_name_color = red
                                    if world_population >= 10:
                                        world_name = world_name.upper()
                                    world_name_font = pygame.font.SysFont('Eras ITC Demi', 18, False, False)
                                    world_name_text = world_name_font.render(world_name, True, world_name_color)
                                    world_uwp_font = pygame.font.SysFont('Eras ITC Demi', 14, False, False)
                                    if trade_code:
                                        world_uwp_text = world_uwp_font.render(world_trade, True, white)
                                    else:
                                        world_uwp_text = world_uwp_font.render(line[world_tab:world_tab+9], True, white)
                                    if hex_x // 2 == hex_x / 2.0:
                                        if grid_style == 'RECT_grid':
                                            if line[travel_code_tab] == 'R' or line[travel_code_tab] == 'A':
                                                if line[travel_code_tab] == 'R':
                                                    zone_color = red
                                                if line[travel_code_tab] == 'A':
                                                    zone_color = amber
                                                if zone_style == 'circled':
                                                    _circle(screen, zone_color, (int((temp_x-1)*64 + 33 + x*512),
                                                                                 int((temp_y-1)*70.4) + 70),
                                                                                 int(zoom*3),
                                                                                 1,
                                                                                 see_thru)
                                                else:
                                                    _rectangle(screen, zone_color, [(temp_x-1)*64 + 4 + x*512,
                                                                                    (temp_y-1)*70.4 + 40,
                                                                                    56,
                                                                                    63],
                                                                                    1,
                                                                                    see_thru)
                                            
#                                             _circle(screen, color, (int((temp_x-1)*64 + 33 + x*512),
#                                                                     int((temp_y-1)*70.4) + 70),
#                                                                     int(zoom), 0)
                                            
                                            _planet(screen, color, (int((temp_x-1)*64 + 33 + x*512),
                                                                    int((temp_y-1)*70.4) + 70),
                                                                    int(zoom), 0,
                                                                    world_size, world_atmosphere, world_hydrographics, world_population, world_trade)
                                            
                                            screen.blit(world_name_text, [int((temp_x-1)*64 + 32 - len(world_name)*7/2 + x*512),
                                                                          int((temp_y-1)*70.4) + 46])
                                            screen.blit(world_uwp_text, [int((temp_x-1)*64 + 30 - 25 + x*512),
                                                                         int((temp_y-1)*70.4) + 86])
                                        elif grid_style == 'HEX_grid_40':
#                                         if world_name == 'Reference' or world_name == 'Capital' or world_name == 'Regina' or world_name == 'Vland' or world_name == 'Terra':
#                                             color = yellow
#                                             _circle(screen, color, (int(hex_x*X_SPACING*x_zoom + subxx*32*X_SPACING*x_zoom), int(hex_y*Y_SPACING*y_zoom + subyy*40*Y_SPACING*y_zoom)), 8, 0)
                                            if line[travel_code_tab] == 'R' or line[travel_code_tab] == 'A':
                                                if line[travel_code_tab] == 'R':
                                                    zone_color = red
                                                if line[travel_code_tab] == 'A':
                                                    zone_color = amber
                                                if zone_style == 'circled':
                                                    _circle(screen, zone_color, (int((temp_x-1)*64 + 24 + x*512),
                                                                                 int((temp_y-1)*70.4) + 67),
                                                                                 int(zoom*3),
                                                                                 1,
                                                                                 see_thru)
                                                else:
                                                    _hexagon(screen, zone_color, (int((temp_x-1)*64 + 24 + x*512),
                                                                                  int((temp_y-1)*70.4) + 67),
                                                                                  int(grid_style[9:11]),
                                                                                  1,
                                                                                  see_thru)
                                                             
                                            _planet(screen, color, (int((temp_x-1)*64 + 24 + x*512),
                                                                    int((temp_y-1)*70.4) + 67),
                                                                    int(zoom), 0,
                                                                    world_size, world_atmosphere, world_hydrographics, world_population, world_trade)
    
                                            screen.blit(world_name_text, [int((temp_x-1)*64 + 24 - len(world_name)*7/2 + x*512),
                                                                          int((temp_y-1)*70.4) + 46])
                                            screen.blit(world_uwp_text, [int((temp_x-1)*64 + 24 - 25 + x*512),
                                                                         int((temp_y-1)*70.4) + 86])
                                        
                                    else:
                                        if grid_style == 'RECT_grid':
                                            if line[travel_code_tab] == 'R' or line[travel_code_tab] == 'A':
                                                if line[travel_code_tab] == 'R':
                                                    zone_color = red
                                                if line[travel_code_tab] == 'A':
                                                    zone_color = amber
                                                if zone_style == 'circled':
                                                    _circle(screen, zone_color, (int((temp_x-1)*64 + 33 + x*512),
                                                                                 int((temp_y-1)*70.4) + 37),
                                                                                 int(zoom*3),
                                                                                 1,
                                                                                 see_thru)
                                                else:
                                                    _rectangle(screen, zone_color, [(temp_x-1)*64 + 4 + x*512,
                                                                                    (temp_y-1)*70.4 + 4,
                                                                                    56,
                                                                                    63],
                                                                                    1,
                                                                                    see_thru)
                                            
                                            _planet(screen, color, (int((temp_x-1)*64 + 33 + x*512),
                                                                    int((temp_y-1)*70.4) + 37),
                                                                    int(zoom), 0,
                                                                    world_size, world_atmosphere, world_hydrographics, world_population, world_trade)
                                            
                                            screen.blit(world_name_text, [int((temp_x-1)*64 + 32 - len(world_name)*7/2 + x*512),
                                                                          int((temp_y-1)*70.4) + 12])
                                            screen.blit(world_uwp_text, [int((temp_x-1)*64 + 30 - 25 + x*512),
                                                                         int((temp_y-1)*70.4) + 52])
                                        elif grid_style == 'HEX_grid_40':
#                                         if world_name == 'Reference' or world_name == 'Capital' or world_name == 'Regina' or world_name == 'Vland' or world_name == 'Terra':
#                                             color = yellow
#                                             _circle(screen, color, (int(hex_x*X_SPACING*x_zoom + subxx*32*X_SPACING*x_zoom), int(hex_y*Y_SPACING*y_zoom + OFFSET*y_zoom + subyy*40*Y_SPACING*y_zoom)), 8, 0)
                                            if line[travel_code_tab] == 'R' or line[travel_code_tab] == 'A':
                                                if line[travel_code_tab] == 'R':
                                                    zone_color = red
                                                if line[travel_code_tab] == 'A':
                                                    zone_color = amber
                                                if zone_style == 'circled':
                                                    _circle(screen, zone_color, (int((temp_x-1)*64 + 24 + x*512),
                                                                                 int((temp_y-1)*70.4) + 33),
                                                                                 int(zoom*3),
                                                                                 1,
                                                                                 see_thru)
                                                else:
                                                    _hexagon(screen, zone_color, (int((temp_x-1)*64 + 24 + x*512),
                                                                                  int((temp_y-1)*70.4) + 32),
                                                                                  int(grid_style[9:11]),
                                                                                  1,
                                                                                  see_thru)
                                            
                                            _planet(screen, color, (int((temp_x-1)*64 + 24 + x*512),
                                                                    int((temp_y-1)*70.4) + 33),
                                                                    int(zoom), 0,
                                                                    world_size, world_atmosphere, world_hydrographics, world_population, world_trade)
                                        
                                            screen.blit(world_name_text, [int((temp_x-1)*64 + 24 - len(world_name)*7/2 + x*512),
                                                                          int((temp_y-1)*70.4) + 12])
                                            screen.blit(world_uwp_text, [int((temp_x-1)*64 + 24 - 25 + x*512),
                                                                         int((temp_y-1)*70.4) + 52])

            except IOError:
                #print 'No ' + sec_filename + '.dat'
                log.warning("Missing '" + sec_filename + ".dat' file for viewing subsectors [Warning]")
                mapper_log.warning("Subsector Display Warning! '" + sec_filename + ".dat' is missing.")

    pygame.display.update()
    
    if zoom == 1:
        return voiced_sector_name
    elif zoom == 4:
        return saved_sector_list
    elif zoom == 8:
        return subsector_names
    else:
        return 'RESERVED'

if __name__ == '__main__':
    mapper_log.info('mapper was run without display_map() called.  Help will be sent if needed.')
    print()
    if len(sys.argv) < 2:
        print("     Type 'mapper.py -h' for help")
        print("     Type 'mapper.py -v' for version information")
    elif sys.argv[1] in ['-h', '/h', '--help', '-?', '/?']:
        print('     mapper is a module (containing a display_map function)')
        print('     that needs to be imported by PyMapGen.')
    elif sys.argv[1] in ['-v', '/v', '--version', '-V', '/V']:
        print('     mapper.py version ' + __version__)
    else:
        print("     Type 'mapper.py -h' for help")
        print("     Type 'mapper.py -v' for version information")
