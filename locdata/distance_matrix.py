#!/usr/bin/python3
# -*- coding: utf-8 -*-

data = ['commuting_relations_ORP_4_2019.csv',
        'commuting_relations_ORP_5_2019.csv',
        'commuting_relations_ORP_6_2019.csv'
        ]

import numpy as np
import pandas as pd

pop = pd.read_csv('population.csv')

def create_matrix(d):
    l = len(pop)
    m = np.matrix([[0]*l]*l)
    for i in range(l): # row index
        dest_id = pop.iloc[i].id
        destinations = d[d['destinationLocation.id'] == dest_id]
        for index, row in destinations.iterrows():
            j = pop[pop['id'] == row['sourceLocation.id']].index[0] # There can be only one!
            m[i, j] = row['count']
    return m

def save_matrix(m, file_name):
    from rpy2.robjects import r, numpy2ri
    numpy2ri.activate()
    r.assign("dm", m)
    r("save(dm, file='%s')" % file_name)
    # for Python 2
    #a = np.array(m, dtype='int64')
    #ro = numpy2ri.numpy2ri(a)
    #r.assign("dm", ro)
    #r("save(dm, file='%s')" % file_name)

mats = []
for i in range(len(data)):
    fn = 'dist_matrix_%d' % (i+4) + '.Rdata'
    print("Creating distance matrix %d" % (i+1))
    m = create_matrix(pd.read_csv(data[i]))
    print("Saving distance matrix %d" % (i+1))
    save_matrix(m, fn)
    mats.append(m)
    
m = sum(mats)*1.0/3.0
save_matrix(m, 'dist_matrix_Q2.Rdata')
