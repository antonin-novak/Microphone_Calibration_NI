# Microphone Electrostatic Calibration - Measurement

This repository contains the measurement code for an **electrostatic calibration
experiment** used to determine the **sensitivity of a microphone as a function of
frequency**.

A swept-sine signal is generated and sent to the microphone (e.g. via
an electrostatic actuator/calibrator), while the microphone's electrical output
(voltage) is recorded using a National Instruments (NI) acquisition device. The
Frequency Response Function (FRF) obtained from the measurement gives the
microphone's voltage response as a function of frequency, which can later be
compared to a theoretical model developed separately (e.g. by students in the lab
session).

## How it works

1. A **swept-sine** signal is generated (`SynchSweptSine` class) that
   sweeps from a start frequency `f1` to an end frequency `f2` over `T` seconds.
2. The signal is played back and simultaneously acquired through an **NI USB-4431**
   device (`measurement_NI` function), which handles the analog output/input tasks.
3. The recorded microphone voltage signal `u` is processed to extract its **Frequency Response Function** (`sss.getFRF`), along with the corresponding
   frequency axis (`sss.f_axis`).
4. Results (frequency axis, sampling frequency, spectrum, and raw signal) are saved
   to a `.npz` file for later analysis.
5. The measured spectrum and raw voltage signal are plotted for a quick visual
   check.

## Repository structure

```
measurement_NI_FRF.py       # Main script: generates the swept-sine, runs the
                             # measurement, computes the FRF and saves/plots results
plot_data.py                 # Loads a saved .npz file and re-plots the results
functions/
    measurement_NI.py         # Handles NI device communication (analog I/O)
    SynchSweptSine.py          # Synchronized swept-sine signal generation and
                                # FRF/impulse-response processing
```

## Requirements

- Python 3
- [NI-DAQmx driver](https://www.ni.com/en/support/downloads/drivers/download.ni-daq-mx.html)
  installed on the machine
- Python packages:
  - `numpy`
  - `matplotlib`
  - `nidaqmx`

Install the Python dependencies with:

```bash
pip install numpy matplotlib nidaqmx
```

## Hardware setup

- **NI USB-4431** (or compatible NI device) connected to the computer.
- Analog output channel `ao0` drives the excitation signal (e.g. to an
  electrostatic actuator/calibrator placed in front of the microphone).
- Analog input channel `ai0` acquires the microphone's voltage output.
- Update the `Dev` variable in [measurement_NI_FRF.py](measurement_NI_FRF.py) to
  match the NI device name as seen in NI-MAX (e.g. `'Dev1'`, `'Dev8'`, ...).

## Usage

1. Connect the NI device and the microphone under test.
2. Set the measurement parameters in [measurement_NI_FRF.py](measurement_NI_FRF.py):
   - `Dev`: NI device name
   - `fs`: sampling frequency [Hz]
   - `f1`, `f2`: start/end frequency of the swept-sine [Hz]
   - `T`: duration of the swept-sine [s]
   - `A`: excitation amplitude
3. Run the measurement:

```bash
python measurement_NI_FRF.py
```

This generates the swept-sine, performs the acquisition, computes the FRF, saves
the results to `data_microphone.npz`, and displays the voltage spectrum and time
signal plots.

4. To re-plot previously saved data without running a new measurement:

```bash
python plot_data.py
```

## Output data

The saved `.npz` file contains:

| Variable | Description |
|----------|--------------|
| `f_axis` | Frequency axis [Hz] |
| `fs`     | Sampling frequency [Hz] |
| `U`      | Microphone voltage spectrum (FRF) [V] |
| `u`      | Raw microphone voltage signal [V] |

Note that microphone sensitivity is **not** included in this data; the voltage
spectrum `U` must be combined with the known excitation level of the electrostatic
calibration setup to obtain the actual sensitivity vs. frequency curve.

## Author

Antonin Novak
