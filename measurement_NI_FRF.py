
import numpy as np
import matplotlib.pyplot as plt
from functions.measurement_NI import measurement_NI
from functions.SynchSweptSine import SynchSweptSine


""" Parameters """
Dev = 'Dev8'        # name of the NI device
fs = 96000          # sampling frequency [Hz]
filename = 'data_microphone.npz'  # name of the file


""" Generate a Swept-sine signal"""
f1 = 5                      # start frequency [Hz]
f2 = 30e3                   # end frequency [Hz]
T = 8                       # time length of the swept-sine [s]
A = 0.5                     # amplitude

# note that 'sss' is an object.
sss = SynchSweptSine(f1=f1, f2=f2, T=T, fs=fs)
out_signal = A*np.concatenate((sss.signal, np.zeros(int(0.5*fs))))

""" Measurement using a National Instruments device  """
y = measurement_NI(out_signal, fs, Dev, iepe=[False])

# Extract signals from measured data (voltage)
u = np.array(y)

""" calculate the FRF and the frequency axis """
U = sss.getFRF(u, N_samples=fs)
f_axis = sss.f_axis(Npts=fs)


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


""" Save the measured data to a file """
np.savez(filename, f_axis=f_axis, fs=fs, U=U, u=u)


plt.show()
