#!/usr/bin/env python3

import argparse
import json
import os

import requests


def get_and_save(url, filename, folder='.'):
    """Utility function to query a URL, dump its content to file, and return the request object."""
    
    target = os.path.join(args.C, filename)
    print(f"Downloading {url} to {target}.")

    r = requests.get(url)
    with open(target, 'wb') as outfile:
        outfile.write(r.content)
    
    return r

        
parser = argparse.ArgumentParser(description='Download JSON and 4Hz HDF files for GWOSC event id.')

parser.add_argument('id', metavar='id',               help='GWOSC id (e.g., GW150914-v3)')
parser.add_argument('-C', metavar='dir', default='.', help='output folder')

args = parser.parse_args()


# get the JSON catalog file (unless we have it already), parse it
try:
    catalog = json.load(open(os.path.join(args.C, 'catalog.json'), 'rb'))
except FileNotFoundError:
    r1 = get_and_save('https://www.gw-openscience.org/eventapi/json/allevents',
                      'catalog.json', args.C)
    catalog = json.loads(r1.text)

# get the JSON event file for the requested ID, write it to disk, and parse it
jsonurl = catalog['events'][args.id]['jsonurl']
r2 = get_and_save(jsonurl, args.id + '.json', args.C)
jsondict = json.loads(r2.text)

# identify HDF strain files, get them, write them to disk
for file in jsondict['events'][args.id]['strain']:
    if (file['duration'] == 32 and file['sampling_rate'] == 4096
                               and file['format'] == 'hdf5'
                               and file['detector'] in ['H1','L1']):
        get_and_save(file['url'], f'{file["detector"]}-{args.id}.hdf5', args.C)
