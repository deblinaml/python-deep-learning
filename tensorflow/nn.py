import numpy as np 
import pandas as pd 
import torch 
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data 
from torch.autograd import Variable
training_set = pd.read_csv('ml-100k/u1.base', delimiter='\t')
training_set = np.array(training_set, dtype = 'int')
test_set = pd.read_csv('ml-100k/u1.test', delimiter='\t')
test_set= np.array(test_set, dtype= 'int')
nb_users = int(max(max(training_set[:,0]),max(test_set[:,0])))
nb_mov = int(max(max(training_set[:,1]), max(test_set[:,1])))

################################################################
'''Converting the data in a line'''
################################################################

def convert(data):
    new_data = []
    for id_users in range (1,nb_users +1):
        id_mov = data[:,1][data[:,0] == id_users]
        id_rat = data[:,2][data[:,0] == id_users]
        rats = np.zeros(nb_mov)
        
