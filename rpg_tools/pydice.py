#
#   pydice.py 3.12.0
#
#   Written for Python 3.11.0
#
#   To use this module: from pydice import roll
#
#   Make a dice roll
#
##########################################################

'''
pydice module containing roll()

Usage:
    from pydice import roll
    print(roll('2D6'))

    Will roll two 6-sided dice, returning an integer
'''

from random import random
import os
import logging
import sys

__version__ = '3.12'
__release__ = '3.12.0'
__py_version__ = '3.11.0'
__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'

dice_log = logging.getLogger('pydice')
#dice_log.setLevel(logging.DEBUG)
dice_log.setLevel(logging.WARNING)

if not os.path.exists('Logs'):
    os.mkdir('Logs')

fh = logging.FileHandler('Logs/pydice.log', 'w')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s',
                              datefmt = '%a, %d %b %Y %H:%M:%S')
fh.setFormatter(formatter)
dice_log.addHandler(fh)

dice_log.info('Logging started.')
dice_log.info('roll() v' + __version__ + ' started, and running...')
if sys.version_info[0] < 3 or sys.version_info[1] < 11:
    print('Warning:', sys.version_info[0:3], 'is an older version of Python installed.')
    dice_log.warning('Warning: ' + str(sys.version_info[0:3]) + ' is an older version of Python installed.')
elif sys.version_info[0] > 3 or sys.version_info[1] > 11:
    print('Warning:', sys.version_info[0:3], 'is a newer version of Python installed.')
    dice_log.warning('Warning: ' + str(sys.version_info[0:3]) + ' is a newer version of Python installed.')

number_of_dice = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
simple_dice = ['D2', 'D3', 'D4', 'D5', 'D6', 'D8', 'D10', 'D12', 'D20', 'D30']
traveller5_dice = ['1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D']
fate_dice = ['1DF', '2DF', '3DF', '4DF', '5DF']

__error__ = -9999

def _dierolls(dtype, dcount):
    '''
    Takes two integer arguments:
        dtype (the number of sides for the dice)
        dcount (the number of dice to roll)
    
    and returns an integer value.
    
    This function is for internal use and has no error-checking!    
    '''

    dtotal = 0
    if dcount == 1:
        dice_log.debug('Using %s %d-sided die...' % (number_of_dice[dcount], dtype))
    else:
        if dcount < 11:
            dice_log.debug('Using %s %d-sided dice...' % (number_of_dice[dcount], dtype))
        else:
            dice_log.debug('Using %d %d-sided dice...' % (dcount, dtype))
        
    for i in range(dcount):
        rolled = int(random() * dtype + 1)
        if rolled == 8 or rolled == 11 or rolled == 18 or rolled >= 80 and rolled <= 89:
            dice_log.debug('Rolled an %s' % rolled)
        else:
            dice_log.debug('Rolled a %s' % rolled)
        dtotal += rolled
    return dtotal

def roll(dice='2d6'):
    '''
    The dice types to roll are:\n
    '4dF', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D8', 'D09', 'D10', 'D12', 'D20',
    'D30', 'D099', 'D100', 'D0999', 'D1000', 'D44', 'D66', 'D666', 'D88',
    'DD', 'FLUX', 'GOODFLUX', 'BADFLUX', 'BOON', 'BANE', 'ADVANTAGE',
    'DISADVANTAGE', and also Traveller5's 1D thru 10D rolls

    Some examples are:\n
    roll('D6') or roll('1D6') -- roll one 6-sided die\n
    roll('2D6') -- roll two 6-sided dice\n
    roll('D09') -- roll a 10-sided die (0 - 9)\n
    roll('D10') -- roll a 10-sided die (1 - 10)\n
    roll('D099') -- roll a 100-sided die (0 - 99)\n
    roll('D100') -- roll a 100-sided die (1 - 100)\n
    roll('D66') -- roll for a D66 chart\n
    roll('FLUX') -- a FLUX roll (-5 to 5)\n
    roll('3D6+6') -- add +6 DM to roll\n
    roll('4D4-4') -- add -4 DM to roll\n
    roll('2DD+3') -- roll (2D6+3) x 10\n
    roll('BOON') -- roll 3D6 and keep the higher two dice\n
    roll('4dF') -- make a FATE roll (-4 to 4)\n
    roll('4D') -- make a Traveller5 4D roll\n
    roll('4D6H3') -- roll 4D6 and keep the higher three dice\n
    roll('3D6L2') -- roll 3D6 and keep the lower two dice\n
    roll('info') -- release version of program\n
    roll('2D8 # weapon damage') -- a 2D8 roll with a comment added
    
    An invalid roll will return a -9999 value.
    '''

    log = logging.getLogger('SectorGen.pydice')
    
    # strip out comment if found
    ichar3 = dice.find('#')
    if ichar3 != -1:
        dice_comment = '                    ' + dice[ichar3:len(dice)]
        dice = dice[0:ichar3]
    else:
        dice_comment = ''

    # make inputted string argument upper case, and remove spaces
    dice = str(dice).upper().replace(' ','')
    org_dice = dice
    
    # is this a default dice roll?
    if dice == '':
        dice = '2D6'
        dice_log.debug('Nothing entered. Default ' + dice + ' will be rolled.')

    # was information for this program asked for?
    if dice == 'INFO':
        ver = 'roll(), release version ' + __release__ + ' for Python ' + __py_version__
        dice_log.info('Reporting: roll() release version: %s' % __release__)
        if sys.version_info[0] < 3 or sys.version_info[1] < 11:
            print('Warning:', sys.version_info[0:3], 'is an older version of Python installed.')
            dice_log.warning('Warning: ' + str(sys.version_info[0:3]) + ' is an older version of Python installed.')
        elif sys.version_info[0] > 3 or sys.version_info[1] > 11:
            print('Warning:', sys.version_info[0:3], 'is a newer version of Python installed.')
            dice_log.warning('Warning: ' + str(sys.version_info[0:3]) + ' is a newer version of Python installed.')
        return __version__, ver
    
    # was a test asked for?
    if dice == 'TEST':
        dice_log.info('A 6x6 test was started...')
        roll_chart_6x6 = {}
        data = []
        for i in range(13):
            data.append(0)
        n = 10000
        
        for i in range(6):
            for j in range(6):
                roll_chart_6x6[(i+1, j+1)] = 0
        print()
        print('      6x6 Roll Chart Test')
        print('     1    2    3    4    5    6')
        for i in range(n):
            die1 = _dierolls(6, 1)
            die2 = _dierolls(6, 1)
            roll_chart_6x6[(die1, die2)] += 1
            result = die1 + die2
            data[result] += 1
                
        for i in range(6):
            print(i+1, end=' ')
            for j in range(6):
                print('%4d' % roll_chart_6x6[(i+1, j+1)], end=' ')
            print()
        
        for i in range(6):
            for j in range(6):
                roll_chart_6x6[(i+1, j+1)] = 0
        print()
        print('            6x6 Roll Chart Percentage')
        print('        1       2       3       4       5       6')
        for x in range(13):
            if x > 1:
                for i in range(6):
                    for j in range(6):
                        if (i+1)+(j+1) == x and roll_chart_6x6[(i+1, j+1)] == 0:
                            roll_chart_6x6[(i+1, j+1)] = data[x]
        
        for i in range(6):
            print(i+1, end=' ')
            for j in range(6):
                print('%6.2f%%' % (roll_chart_6x6[(i+1, j+1)] * 100. / n), end=' ')
            print()
        print()
        dice_log.info('6x6 test completed 100%.')
        for x in range(len(data)):
            data[x] = data[x] * 100. / n
        return data[2:13]

    # was a min/max/avg asked for?
    if dice == 'MINMAXAVG':
        rolls_for_test = ['1d1', '1d2', '1d3', '1d4', '1d5', '1d6', '1d8', '1d09', '1d10', '1d12', '1d20', '1d30', '1d099', '1d100',
                  '1df', '2df', '3df', '4df', '5df', 'flux', 'goodflux', 'badflux', 'boon', 'bane', 'advantage', 'disadvantage',
                  '2d4', '3d4', '4d4',
                  '2d6', '3d6', '4d6',
                  '2d8', '3d8', '4d8',
                  '2d09', '3d09', '4d09',
                  '2d10', '3d10', '4d10',
                  '2d12', '3d12', '4d12',
                  '2d20', '3d20', '4d20', '3d6+1', '2d6-2', '2d6-7',
                  '1dd', '2dd', '3dd', '4dd+3', '4d6l3', '3d6h2-2',
                  'd0999', 'd1000', 'd666']

        print()
        print('Using brute force...')
        print()

        total_numbers = 2000

        for i in range(len(rolls_for_test)):
            test_roll = rolls_for_test[i]
            minimum = 100000000
            maximum = -100000000
            total_sum = 0
            for n in range(total_numbers):
                die = roll(test_roll)
                if minimum > die:
                    minimum = die
                if maximum < die:
                    maximum = die
                total_sum += die
            sample = []
            for x in range(10):
                sample.append(roll(test_roll))

            print('Test Roll: %s, Min: %d, Max: %d, Avg: %.1f, ' % (test_roll, minimum, maximum, total_sum / total_numbers) + 'Sample:', sample)

        print()
        print('Increase the value of total_numbers in pydice to improve its precision.')
        print()
        return

    log.debug(dice + ' ' + dice_comment)
    dice_log.debug("Asked to roll '%s':" % dice)

    #get dice modifier
    dice_mod = 0
    
    ichar2 = dice.find('+')
    if ichar2 != -1:
        try:
            dice_mod = int(dice[ichar2:len(dice)])
            dice = dice[:ichar2]
        except ValueError:
            print('[ERROR] Not a valid dice modifier: %s' % dice[ichar2:len(dice)])
            dice_log.error('[ERROR] Not a valid dice modifier: %s' % dice[ichar2:len(dice)])
    else:
        ichar2 = dice.find('-')
        if ichar2 != -1:
            try:
                dice_mod = int(dice[ichar2:len(dice)])
                dice = dice[:ichar2]
            except ValueError:
                print('[ERROR] Not a valid dice modifier: %s' % dice[ichar2:len(dice)])
                dice_log.error('[ERROR] Not a valid dice modifier: %s' % dice[ichar2:len(dice)])

    if dice == 'BOON':
        dice = '3D6H2'
    if dice == 'BANE':
        dice = '3D6L2'
    if dice == 'ADVANTAGE':
        dice = '2D20H1'
    if dice == 'DISADVANTAGE':
        dice = '2D20L1'

    if dice.find('H') == -1 and dice.find('L') == -1:
        # check if a FATE dice roll
        dF_dice = dice
        if dF_dice in fate_dice:
            num_dice = int(dF_dice[0:len(dF_dice) - 2])
            rolled = 0
            for rolls in range(num_dice):
                rolled += _dierolls(3, 1) - 2
            rolled += dice_mod
            dice_log.info("'%s' = %d%s+%d = %d %s" % (dice, num_dice, 'dF', dice_mod, rolled, dice_comment))
            return rolled
    
    # check if FLUX dice are being rolled
    if dice == 'FLUX':
        flux1 = _dierolls(6, 1)
        flux2 = _dierolls(6, 1)
        rolled = flux1 - flux2
        dice_log.info("'%s' = %d - %d = %d %s" % (dice, flux1, flux2, rolled, dice_comment))
        return rolled

    elif dice == 'GOODFLUX':
        flux1 = _dierolls(6, 1)
        flux2 = _dierolls(6, 1)
        if flux1 < flux2:
            rolled = flux2 - flux1
            dice_log.info("'%s' = %d - %d = %d %s" % (dice, flux2, flux1, rolled, dice_comment))
        else:
            rolled = flux1 - flux2
            dice_log.info("'%s' = %d - %d = %d %s" % (dice, flux1, flux2, rolled, dice_comment))
        return rolled

    elif dice == 'BADFLUX':
        flux1 = _dierolls(6, 1)
        flux2 = _dierolls(6, 1)
        if flux1 > flux2:
            rolled = flux2 - flux1
            dice_log.info("'%s' = %d - %d = %d %s" % (dice, flux2, flux1, rolled, dice_comment))
        else:
            rolled = flux1 - flux2
            dice_log.info("'%s' = %d - %d = %d %s" % (dice, flux1, flux2, rolled, dice_comment))
        return rolled

    # check if negative number was entered
    elif dice[0] == '-':
        log.error('Negative dice count found! [ERROR]')
        print('Negative dice count found! [ERROR]')
        dice_log.error("Negative number of dice = '" + dice + "' [ERROR]")
        return __error__

    else:

        if dice.find('H') == -1 and dice.find('L') == -1:

            # check if T5 dice are being rolled
            t5_dice = dice
            if t5_dice in traveller5_dice:
                num_dice = int(t5_dice[0:len(t5_dice) - 1])
                rolled = _dierolls(6, num_dice) + dice_mod
                dice_log.info("Traveller5 '%s' = %d%s+%d = %d %s" % (dice, num_dice, 'D6', dice_mod, rolled, dice_comment))
                return rolled

    # look for H or L in string (for keeping higher or lower dice)
    keep = None
    ichar4 = dice.find('L')
    if ichar4 == -1:
        ichar4 = dice.find('H')
        if ichar4 != -1:
            keep = dice[ichar4:len(dice)]
    else:
        keep = dice[ichar4:len(dice)]
    if keep != None:
        dice = dice[0:len(dice)-2]

    # look for DD in the string (for destructive dice rolls)
    ichar1 = dice.find('DD')
    if ichar1 == -1:
        
        # if not, does the string indicate regular dice for use?
        ichar1 = dice.find('D')
    if ichar1 == 0:
        
        # only one die is being rolled
        num_dice = 1

    if ichar1 != -1:
        if ichar1 != 0:
            
            # is there a number found?
            if dice[0:ichar1].isdigit():
                # how many dice are being rolled?
                num_dice = int(dice[0:ichar1])
            else:
                num_dice = 0
        if num_dice >= 1:

            # what kind of dice are being rolled? D6? D66? etc.
            if ichar2 != -1:
                dice_type = dice[ichar1:ichar2]
            else:
                dice_type = dice[ichar1:len(dice)]

            if dice_type in simple_dice:
                if keep != None:
                    die = []
                    keep_type = keep[0:1]
                    rolls_kept = int(keep[1:2])
                    if rolls_kept <= num_dice:
                        if keep_type == 'H':
                            dice_log.info('%s%s%d: Keeping higher %d %s' % (dice, keep_type, rolls_kept, rolls_kept, dice_comment))
                        else:
                            dice_log.info('%s%s%d: Keeping lower %d %s' % (dice, keep_type, rolls_kept, rolls_kept, dice_comment))
                        for i in range(num_dice):
                            die.append(_dierolls(int(dice_type[1:len(dice_type)]), 1))
                            dice_log.debug("%s = %d %s" % (dice_type, die[i], dice_comment))
                        die_swap = True
                        while die_swap == True:
                            die_swap = False
                            for j in range(len(die) - 1):
                                if keep_type == 'H':
                                    if die[j] < die[j+1]:
                                        temp_die = die[j]
                                        die[j] = die[j+1]
                                        die[j+1] = temp_die
                                        die_swap = True
                                else:
                                    if die[j] > die[j+1]:
                                        temp_die = die[j]
                                        die[j] = die[j+1]
                                        die[j+1] = temp_die
                                        die_swap = True
                        rolled = 0
                        for j in range(rolls_kept):
                            rolled += die[j]
                            dice_log.debug('Keeping: %d' % die[j])
                        rolled += dice_mod
                        dice_log.info('Total roll for %s: %d %s' % (org_dice, rolled, dice_comment))
                        return rolled
                    else:
                        dice = dice + keep_type + str(rolls_kept)
                        dice_log.info('[ERROR] Not enough dice: %s' % dice)
                        print('[ERROR] Not enough dice: %s' % dice)
                        return __error__
                else:
                    rolled = _dierolls(int(dice_type[1:len(dice_type)]), num_dice) + dice_mod
                    dice_log.info("'%s' = %d%s+%d = %d %s" % (dice, num_dice, dice_type, dice_mod, rolled, dice_comment))
                    return rolled
            elif dice_type == 'D1' and num_dice == 1 and dice_mod == 0:
                rolled = int(random() + .5)
                dice_log.info("'%s' = %d%s = %d %s" % (dice, num_dice, dice_type, rolled, dice_comment))
                return rolled
            elif dice_type == 'D44' and num_dice == 1 and dice_mod == 0:
                roll_1 = _dierolls(4, 1)
                roll_2 = _dierolls(4, 1)
                rolled = roll_1 * 10 + roll_2
                dice_log.info("'%s' = %d%s = %d and %d = %d %s" % (dice, num_dice, dice_type, roll_1, roll_2, rolled, dice_comment))
                return rolled
            elif dice_type == 'D66' and num_dice == 1 and dice_mod == 0:
                roll_1 = _dierolls(6, 1)
                roll_2 = _dierolls(6, 1)
                rolled = roll_1 * 10 + roll_2
                dice_log.info("'%s' = %d%s = %d and %d = %d %s" % (dice, num_dice, dice_type, roll_1, roll_2, rolled, dice_comment))
                return rolled
            elif dice_type == 'D88' and num_dice == 1 and dice_mod == 0:
                roll_1 = _dierolls(8, 1)
                roll_2 = _dierolls(8, 1)
                rolled = roll_1 * 10 + roll_2
                dice_log.info("'%s' = %d%s = %d and %d = %d %s" % (dice, num_dice, dice_type, roll_1, roll_2, rolled, dice_comment))
                return rolled
            elif dice_type == 'D666' and num_dice == 1 and dice_mod == 0:
                roll_1 = _dierolls(6, 1)
                roll_2 = _dierolls(6, 1)
                roll_3 = _dierolls(6, 1)
                rolled = roll_1 * 100 + roll_2 * 10 + roll_3
                dice_log.info("'%s' = %d%s = %d and %d and %d = %d %s" % (dice, num_dice, dice_type, roll_1, roll_2, roll_3, rolled, dice_comment))
                return rolled
            elif dice_type == 'D09':
                roll_total = 0
                for rolls in range(num_dice):
                    rolled = (_dierolls(10, 1) - 1)
                    dice_log.debug('Corrected to a roll of %s (because 0-9 values)' % rolled)
                    roll_total += rolled
                roll_total += dice_mod
                dice_log.info("'%s' = %d%s+%d = %d %s" % (dice, num_dice, dice_type, dice_mod, roll_total, dice_comment))
                return roll_total
            elif dice_type == 'D099' and num_dice == 1:
                roll_1 = (_dierolls(10, 1) - 1) * 10
                roll_2 = _dierolls(10, 1) - 1
                rolled = roll_1 + roll_2 + dice_mod
                dice_log.info("'%s' = %d%s+%d = %d and %d + %d = %d %s" % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, dice_mod, rolled, dice_comment))
                return rolled
            elif dice_type == 'D100' and num_dice == 1:
                roll_1 = (_dierolls(10, 1) - 1) * 10
                roll_2 = _dierolls(10, 1)
                rolled = roll_1 + roll_2 + dice_mod
                dice_log.info("'%s' = %d%s+%d = %d and %d + %d = %d %s" % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, dice_mod, rolled, dice_comment))
                return rolled
            elif dice_type == 'D0999' and num_dice == 1:
                roll_1 = (_dierolls(10, 1) - 1) * 100
                roll_2 = (_dierolls(10, 1) - 1) * 10
                roll_3 = _dierolls(10, 1) - 1
                rolled = roll_1 + roll_2 + roll_3 + dice_mod
                dice_log.info("'%s' = %d%s+%d = %d and %d and %d + %d = %d %s" % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, roll_3, dice_mod, rolled, dice_comment))
                return rolled
            elif dice_type == 'D1000' and num_dice == 1:
                roll_1 = (_dierolls(10, 1) - 1) * 100
                roll_2 = (_dierolls(10, 1) - 1) * 10
                roll_3 = _dierolls(10, 1)
                rolled = roll_1 + roll_2 + roll_3 + dice_mod
                dice_log.info("'%s' = %d%s+%d = %d and %d and %d + %d = %d %s" % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, roll_3, dice_mod, rolled, dice_comment))
                return rolled
            elif dice_type == 'DD':
                rolled = (_dierolls(6, num_dice) + dice_mod) * 10
                dice_log.info("'%s' = (%d%s+%d) * 10 = %d %s" % (dice, num_dice, dice_type, dice_mod, rolled, dice_comment))
                return rolled
                                                    
    log.error('Wrong dice type entered! [ERROR]')
    dice_log.error("!!!!!!!!!!!!!!!!!!!!! DICE ERROR! '" + dice + "' is unknown !!!!!!!!!!!!!!!!!!!!!!!!!")
    
    print()
    print("** DICE ERROR! '%s' is unknown **" % dice)
    print("Valid dice rolls are:")
    print("roll('D6') or roll('1D6') -- roll one 6-sided die")
    print("roll('2D6') -- roll two 6-sided dice")
    print("roll('D09') -- roll a 10-sided die (0 - 9)")
    print("roll('D10') -- roll a 10-sided die (1 - 10)")
    print("roll('D099') -- roll a 100-sided die (0 - 99)")
    print("roll('D100') -- roll a 100-sided die (1 - 100)")
    print("roll('D66') -- roll for a D66 chart")
    print("roll('FLUX') -- a FLUX roll (-5 to 5)")
    print("roll('2DD+3') -- roll (2D6+3) x 10")
    print("roll('BOON') -- roll 3D6 and keep the higher two dice")
    print("roll('4D') -- make a Traveller5 4D roll")
    print("roll('4dF') -- make a FATE roll (-4 to 4)")
    print("roll('4D6H3') -- roll 4D6 and keep the higher three dice")
    print("roll('3D6L2') -- roll 3D6 and keep the lower two dice")
    print()
    print("-/+ DMs can be added to rolls:")
    print("roll('3D6+6') -- add +6 DM to roll")
    print("roll('4D4-4') -- add -4 DM to roll")
    print()
    print("roll('info') -- release version of program")
    print()
    print("roll('2D8 # weapon damage') -- a 2D8 roll with a comment added")
    print()
    return __error__

if __name__ == '__main__':
    dice_log.info("pydice was run without 'roll()' called.  Help will be sent if needed.")
    print()
    if len(sys.argv) < 2:
        print('     Type:')
        print("     'pydice.py -h' for help")
        print("     'pydice.py -v' for version")
    elif sys.argv[1] in ['-h', '/h', '--help', '-?', '/?']:
        print('     pydice is a module (containing a roll function)')
        print('     that needs to be imported into Python.')
        print()
        print('     For example:')
        print('     >>> import pydice')
        print("     >>> print(pydice.roll('2d6'))")
        print()
        print('     Or:')
        print('     >>> from pydice import roll')
        print("     >>> print(roll('2d6'))")
        print()
        print()
        print('     But using the CMD prompt:')
        print("     C:\>pydice.py roll('2d6')")
        print()
        print('     Or just:')
        print('     C:\>pydice.py 2d6')
    elif sys.argv[1] in ['-v', '/v', '--version']:
        print('     roll(), release version ' + __release__ + ' for Python ' + __py_version__)
    else:
        dice = ''
        if len(sys.argv) > 2:
            for i in range(len(sys.argv)):
                if i > 0:
                    dice += sys.argv[i]
        else:
            dice = sys.argv[1]
        if "roll('" in dice:
            num = dice.find("')")
            if num != -1:
                dice = dice[6:num]
                dice = str(dice).upper().strip()
                if dice == '':
                    dice = '2D6'
                    dice_log.debug('Default roll was made')
                num = roll(dice)
                if dice != 'TEST' and dice != 'INFO' and dice != 'MINMAXAVG':
                    print("Your '%s' roll is %d." % (dice, num))
                    dice_log.info("The direct call to pydice with '%s' resulted in %d." % (dice, num))
                elif dice == 'INFO':
                    print('roll(), release version ' + __release__ + ' for Python ' + __py_version__)
            else:
                print('Typo of some sort --> ' + dice)
        else:
            dice = str(dice).upper().strip()
            if dice == 'ROLL()':
                dice = '2D6'
                dice_log.debug('Default roll was made')
            num = roll(dice)
            if dice != 'TEST' and dice != 'INFO' and dice != 'MINMAXAVG':
                print("Your '%s' roll is %d." % (dice, num))
                dice_log.info("The direct call to pydice with '%s' resulted in %d." % (dice, num))
            elif dice == 'INFO':
                print('roll(), release version ' + __release__ + ' for Python ' + __py_version__)
