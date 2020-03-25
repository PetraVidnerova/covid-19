#!/usr/bin/python3
# -*- coding: utf-8 -*-

typ = 'ORP' # ,ožné hodnoty:  'Kraj', 'Okres', 'ORP', None (to stahne vsechno do jednoho souboru)
SNAPSHOT = 12 # Duben 2019, viz https://api.inovujemesdaty.cz/snapshots.csv
FILE_NAME = 'commuting_relations_4_2019' # příponu csv připojíme automaticky
BASE_URL = 'https://api.inovujemesdaty.cz/commuting_between_locations.csv' 
DOWNLOAD_BY = 10 # stahovat 10 lokací najednou
SLEEP_TIME = 1 # po každém stažení počkat sekundu

import pandas as pd
locations = pd.read_csv('locations.csv')
if typ:
    locations = locations[locations.type == typ]
    
# moc velké
#loc_param = "&".join('location[]=%d' % x for x in locations.id)
#url = BASE_URL + "commuting_age_genders.csv?snapshot=%s&" % SNAPSHOT + loc_param
#print(url) 

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        
def make_url(loc_ids):
    loc_param = "&".join('sourceLocation[]=%d' % x for x in loc_ids)
    return BASE_URL + "?snapshot=%s&" % SNAPSHOT + loc_param
    

import urllib.request
import os, shutil, time
if not os.path.isdir('tmp'):
    os.mkdir('tmp')
i = 1
file_names = []
for loc_ids in chunks(locations.id, DOWNLOAD_BY):
    file_name = 'tmp/' + FILE_NAME + "_%d" % i + '.csv'
    url = make_url(loc_ids)
    print("Stahuji kus cislo %d" % i)
    print("\t id lokaci: %s" % list(loc_ids))
    #print(url)
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    i += 1
    file_names.append(file_name)
    time.sleep(SLEEP_TIME)

print("Merging...")
result = pd.concat((pd.read_csv(f, sep=';') for f in file_names), axis=0, ignore_index=True)
result.to_csv(FILE_NAME + '.csv')
