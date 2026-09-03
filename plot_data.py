import matplotlib.pyplot as plt
import numpy as np

""" Parameters """
filename = 'data_microphone.npz'  # name of the file

with np.load(filename) as data:
    f_axis = data['f_axis']         # frequency axis [Hz]
    fs = data['fs']                 # sampling frequency [Hz]
    U = data['U']                   # voltage spectrum [V]
    u = data['u']                   # voltage signal [V]


""" Plot the results """
fig, ax = plt.subplots()
ax.semilogx(f_axis, 1000*np.abs(U))
ax.set_xlim(20, 20e3)
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Voltage Magnitude [mV]')
ax.set_title('Microphone Voltage spectrum')
ax.grid(True)

fig, ax = plt.subplots()
ax.plot(1000*u)
ax.set_xlabel('Samples [-]')
ax.set_ylabel('Voltage [mV]')
ax.set_title('Microphone Voltage signal')
ax.grid(True)



plt.show()
