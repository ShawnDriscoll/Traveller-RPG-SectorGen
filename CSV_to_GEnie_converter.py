
import csv
import operator

print()
print('Generating a GEnie file, while deleting any duplicate hexes found...')
print()

with open('data/raw_sector_data.csv', 'r') as CSV_file_in:
    reader = csv.reader(CSV_file_in, delimiter=',')

    header = next(reader)  # The first line is the header
    #print(header)

    #sort = sorted(reader, key=operator.itemgetter(2,3,4,5,6,7,8,9,10)) # UWP
    #sort = sorted(reader, key=operator.itemgetter(1)) # World_Name
    sort = sorted(reader, key=operator.itemgetter(0)) # location

    sector_name = 'sector'
    
with open('data/GEnie_' + sector_name + '_data.txt', 'w') as GEnie_file_out:

    total_duplicates = 0
    total_count = 0
    total_used = 0

    dup_location = ''

    column_headers = sector_name + '''
 1-13: Name
15-18: HexNbr
20-28: UWP
   31: Bases
33-47: Codes & Comments
   49: Zone
52-54: PBG
56-57: Allegiance
59-74: Stellar Data

....+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8
'''
    GEnie_file_out.write(column_headers)

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
            detail_line = row[1]
            while len(detail_line) < 14:
                detail_line += ' '
            #detail_line += row[0][1:]
            detail_line += row[0] + ' ' + row[2] + row[3] + row[4] + row[5] + row[6] + row[7] + row[8] + '-' + row[9] + '  ' + row[12]
            while len(detail_line) < 32:
                detail_line += ' '
            detail_line += row[10]
            while len(detail_line) < 48:
                detail_line += ' '
            detail_line += row[11]
            while len(detail_line) < 51:
                detail_line += ' '
            detail_line += row[13] + row[14] + row[15] + ' ' + row[17] + ' ' + row[18]
            
            print(detail_line)
            
            GEnie_file_out.write(detail_line + '\n')
            total_used += 1
        total_count += 1
        dup_location = row[0]
    
print()
print('Total Count:', total_count)
print('Total Duplicates:', total_duplicates)
print('Total Used:', total_used)

