
import csv
import operator

print()
print('Generating a WBS file, while deleting any duplicate hexes found...')
print()

with open('data/raw_sector_data.csv', 'r') as CSV_file_in:
    reader = csv.reader(CSV_file_in, delimiter=',')

    header = next(reader)  # The first line is the header
    #print(header)

    #sort = sorted(reader, key=operator.itemgetter(2,3,4,5,6,7,8,9,10)) # UWP
    #sort = sorted(reader, key=operator.itemgetter(1)) # World_Name
    sort = sorted(reader, key=operator.itemgetter(0)) # location

    sector_filename = ''
    while sector_filename == '':
        sector_filename = input('Enter sector name for this data: ')
        if sector_filename != '':
            sector_filename = sector_filename.replace(' ', '_')
            print()
    
with open('data/' + sector_filename + '.WBS', 'w') as WBS_file_out:

    total_duplicates = 0
    total_count = 0
    total_used = 0

    dup_location = ''

    column_headers = '''WBS File Format (V1.1.0)
------------------------

Hex Location    = 00 - 03
World Name      = 06 - 19
UWP Code        = 22 - 30
Trade Code      = 33 - 43
PBG Code        = 47 - 49
Base Code       = 52
Allegiance Code = 55 - 56
Satellite Code  = 59
Stellar Details = 62 - 81

00000000001111111111222222222233333333334444444444555555555566666666667777777777888
01234567890123456789012345678901234567890123456789012345678901234567890123456789012
'''
    WBS_file_out.write(column_headers)

    # for row in reader:
    for row in sort:
        #           [0]          [1]          [2]       [3]        [4]            [5]            [6]           [7]            [8]          [9]          [10]           [11]         [12]     [13]     [14]       [15]        [16]        [17]          [18]            [19]
        # row = ['Location', 'World_Name', 'Starport', 'Size', 'Atmosphere', 'Hydrographics', 'Population', 'Government', 'Law_Level', 'Tech_Level', 'Trade_Codes', 'Travel_Code', 'Base', 'Pop_M', 'Belts', 'Gas_giants', 'Worlds', 'Allegiance', 'Stellar_Data', 'Temperature']
        #if row[3] >='0' and row[6] >= '0': # Asteroids
        #if row[24] >= 'G': # nobles
        #if 'Oc' in row[10] or 'Wa' in row[10]: # ocean worlds
        #if row[6] >= 'E': # population
        if row[0] == dup_location:
            print('DUPLICATE LOCATION FOUND AT ' + row[0] + '!')
            total_duplicates += 1
        else:
            detail_line = row[0] + '  ' + row[1]
            while len(detail_line) < 22:
                detail_line += ' '
            detail_line += row[2] + row[3] + row[4] + row[5] + row[6] + row[7] + row[8] + '-' + row[9] + '  '
            tc = row[10]
            if len(tc) > 12:
                tc = tc[0:12]
            detail_line += tc
            while len(detail_line) < 47:
                detail_line += ' '
            detail_line += row[13] + row[14] + row[15] + '  ' + row[12]
            while len(detail_line) < 55:
                detail_line += ' '
            detail_line += row[17]
            while len(detail_line) < 62:
                detail_line += ' '
            detail_line += row[18]
                
            print(detail_line)
            
            WBS_file_out.write(detail_line + '\n')
            total_used += 1
        total_count += 1
        dup_location = row[0]
    
print()
print('Total Count:', total_count)
print('Total Duplicates:', total_duplicates)
print('Total Used:', total_used)

