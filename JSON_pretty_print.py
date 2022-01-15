
import json
import pprint

with open('data/raw_traveller_data.json', 'r') as json_file:
    data = json.load(json_file)

    #pprint.pprint(just_read_in)
    #print

    for traveller in data:
        pprint.pprint(traveller)
        print()
        print()