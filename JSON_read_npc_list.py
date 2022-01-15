import json, pprint

with open('data/raw_traveller_data.json', 'r') as file_in:
    npc_list = json.load(file_in)

print(npc_list)
print()

# print(book['STR'])
# print(book['Jeff'])
# print()

# print(book['Tom']['phone'])
# print()

print(type(npc_list))
print()

for traveller in npc_list:
    pprint.pprint(traveller['Traveller_Name'])
    #print()