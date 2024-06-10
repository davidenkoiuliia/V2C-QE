import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

# load data
def data_loader(fname):
    import numpy as np

    data = np.loadtxt(fname)
    energy = data[:, 0]
    pdos = data[:, 1]  # ldos col, total contribution for a given orbital

    return energy, pdos

energy, pdos_V = data_loader('atom_C_s.dat')
_, pdos_C = data_loader('atom_C_p.dat')

# make plots
plt.figure(figsize = (8, 4))
plt.plot(energy, pdos_V, linewidth=0.75, color='#006699', label='s-orbital')
plt.plot(energy, pdos_C, linewidth=0.75, color='r', label='p-orbital')
plt.yticks([])
plt.xlabel('Energy (eV)')
plt.ylabel('DOS')
plt.axvline(x= 7.9421, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.xlim(10, 19)
plt.ylim(0, 4)
plt.legend(frameon=False)
plt.show()
