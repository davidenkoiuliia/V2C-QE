import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np
# load data
energy, dos, idos = np.loadtxt('v2cdos.dat', unpack=True)

# make plot
plt.figure(figsize = (12, 6))
plt.plot(energy, dos, linewidth=0.75, color='red')
plt.yticks([])
plt.xlabel('Energy (eV)')
plt.ylabel('DOS (states/ev)')
plt.axvline(x=6.642, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.xlim(10, 19)
plt.ylim(0, )
plt.fill_between(energy, 0, dos, where=(energy < 6.642), facecolor='red', alpha=0.25)
plt.show()