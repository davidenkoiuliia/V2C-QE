#!/usr/bin/env python
from main import *

datafile='v2c_bands.dat.gnu'
fermi = 15
symmetryfile='final_bands.out'
bool_shift_efermi= True
fig, ax = plt.subplots()

#bndplot(datafile,fermi,symmetryfile,ax)
bndplot(datafile,fermi,symmetryfile,ax,shift_fermi=0,\
color='black',linestyle='solid',name_k_points=['G','M','K','G'],legend='V2C')


#fig.savefig("test.png")
plt.show()