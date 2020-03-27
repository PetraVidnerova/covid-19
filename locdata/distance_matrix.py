#!/usr/bin/python3
# -*- coding: utf-8 -*-

data = ['commuting_relations_ORP_10_2018.csv',
        'commuting_relations_ORP_11_2018.csv',
        'commuting_relations_ORP_12_2018.csv',
        'commuting_relations_ORP_01_2019.csv',
        'commuting_relations_ORP_02_2019.csv',
        'commuting_relations_ORP_03_2019.csv',
        'commuting_relations_ORP_04_2019.csv',
        'commuting_relations_ORP_05_2019.csv',
        'commuting_relations_ORP_06_2019.csv',
        'commuting_relations_ORP_07_2019.csv',
        'commuting_relations_ORP_08_2019.csv',
        'commuting_relations_ORP_09_2019.csv',
        'commuting_relations_ORP_10_2019.csv',
        'commuting_relations_ORP_11_2019.csv',
        'commuting_relations_ORP_12_2019.csv']

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

def save_matrix(m, file_name, matrix_name="dm"):
    from rpy2.robjects import r, numpy2ri
    numpy2ri.activate()
    # for Python 2
    #a = np.array(m, dtype='int64')
    #ro = numpy2ri.numpy2ri(a)
    r.assign(matrix_name, m)
    r("save(%s, file='%s')" % (matrix_name, file_name))

def dist_matrix(cr): # input is str with path to commuting_relations csv file
    fn = 'dist_matrix' + cr[19:-3] + 'Rdata'
    print("Creating distance matrix %s" % fn)
    m = create_matrix(pd.read_csv(cr))
    print("Saving distance matrix %s" % fn)
    save_matrix(m, fn, matrix_name='dm' + cr[19:-4])
    return m

dist_matrix('commuting_relations_ORP_09_2018.csv')

def quarter(q, data):
    mats = []
    for cr in data: # cr is filename that contains the date
        m = dist_matrix(cr)
        mats.append(m)
        
    m = sum(mats)*1.0/3.0
    name = 'dist_matrix_ORP_Q' + str(q) + '_' + cr[-8:-4]
    mname = 'dm_ORP_Q' + str(q) + '_' + cr[-8:-4] 
    save_matrix(m, name + '.Rdata', matrix_name=mname)
    
quarter(4, data[:3])
quarter(1, data[3:6])
quarter(2, data[6:9])
quarter(3, data[9:12])
quarter(4, data[12:15])
