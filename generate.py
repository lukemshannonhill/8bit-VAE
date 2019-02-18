import os
import torch
from interpolation import interpolation

path = '2019_02_18_18_20_55'
temp = None
seconds = 3
name = "test_sample"
score_type = "seprsco"
data_path = '24_12_seprsco_train_no_pad'

#n2 = 4173
n1= 66337
#n1 = 4173
#n2 = 2953
#n2 = 2953
#n2 = 33614#
#n1 =  2953
#n1 = 0
n2 = 33614
#generate_nes_score(path, seconds, name, temp, score_type)

"""
Good songs:

(4173, 2953)
(4463, 4173, 10)
(4463, 39000, 20)
(66337, 33614, 10)
"""
with torch.no_grad():
    interpolation(data_path, path, temp, seconds, name,
                song_id1 = n1, song_id2 = n2, n_steps = 10)
