import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const
import scipy.integrate as integrate
pdos_data = np.loadtxt('v2c.phdos')

frequencies = pdos_data[:, 0]*2.998*1e10
dos = pdos_data[:, 1]

k_B = const.Boltzmann
hbar = const.hbar

omega_D = max(frequencies)

N_three = integrate.simps(dos, frequencies)
N_A = const.N_A
Theta_D = (hbar * omega_D) / k_B
def debye_integrand(x):
    return (x**4 * np.exp(x)) / ((np.exp(x) - 1)**2)
temperatures = np.linspace(1, 500, 100)
Cv = []
for T in temperatures:
    integral, _ = integrate.quad(debye_integrand, 0, Theta_D/T)
    Cv_value = N_A*(3*N_three * k_B * (T/Theta_D)**3 * integral)/N_three
    Cv.append(Cv_value)
plt.figure(figsize=(10, 6))
plt.plot(temperatures, Cv, label='Heat Capacity (Cv)', color='r')
plt.xlabel('Temperature (K)')
plt.ylabel('Heat Capacity (J/K*mol)')
plt.legend()
plt.grid(True)
plt.show()
print(N_three)