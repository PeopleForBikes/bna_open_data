# -*- coding: utf-8 -*-
"""
Modified on Tuesday Nov 9 2021

@author: rebec
"""

import requests
import pandas as pd

path = ''

#Pull files from AWS 
def pullzip(url, filename):
    # Pull from website
    r = requests.get(url)
    # Save to file
    filename = filename.replace("/", "_") 
    open(path + filename, 'wb').write(r.content)

# Use results file for job ID
bna_results = pd.read_csv(path + 'city_ratings_2021_v14.csv')
bna_results.sort_values(by='City', inplace=True)

for x in bna_results.uuid:
    try:
        url = 'https://s3.amazonaws.com/production-pfb-storage-us-east-1/results/' + x + '/neighborhood_ways.zip'
        filename = bna_results[bna_results.uuid == x].City + bna_results[bna_results.uuid == x].State + '_neighborhood_ways.zip'
        pullzip(url, filename.values[0])
    except (ValueError, TypeError):
        print(bna_results[bna_results.uuid == x].City + bna_results[bna_results.uuid == x].State + 'has no Job ID')
        pass
