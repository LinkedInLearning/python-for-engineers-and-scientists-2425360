#!/usr/bin/env python3

import argparse
import json
import os

import numpy as np
import scipy.interpolate
import matplotlib.mlab as mlab
import matplotlib.pyplot as pp

import h5py


def whiten(strain, sampling=4096, bandpass=[20,350]):
    # compute the spectrum
    psd, psd_freqs = mlab.psd(strain, NFFT=sampling*4, Fs=sampling)

    # max out the spectrum outside the bandpass
    psd[(psd_freqs < bandpass[0]) | (psd_freqs > bandpass[1])] = np.max(psd)
    
    dt = 1/sampling

    # compute the real FFT and the corresponding frequencies
    strain_fft = np.fft.rfft(strain)
    fft_freqs = np.fft.rfftfreq(len(strain), dt)

    # interpolate the spectrum to the FFT frequencies
    psd_fft = scipy.interpolate.interp1d(psd_freqs, psd)(fft_freqs)
    
    # whiten and transform back to real space
    whitened = np.fft.irfft(strain_fft / np.sqrt(psd_fft) * np.sqrt(2*dt))
    
    return whitened


parser = argparse.ArgumentParser(description='Download JSON and 4Hz HDF files for GWOSC event id.')

parser.add_argument('id', metavar='id',               help='GWOSC id (e.g., GW150914-v3)')
parser.add_argument('-C', metavar='dir', default='.', help='input/output folder')

args = parser.parse_args()


# load the JSON event file again
jsondict = json.load(open(os.path.join(args.C, args.id + '.json'), 'rb'))
eventdict = jsondict['events'][args.id]

# load the HDF strain files
h1file = h5py.File(os.path.join(args.C, f'H1-{args.id}.hdf5'), 'r')
l1file = h5py.File(os.path.join(args.C, f'L1-{args.id}.hdf5'), 'r')

# get the strain datasets
h1strain = h1file['strain/Strain']
l1strain = l1file['strain/Strain']

# build the time axis from the H1 Strain dataset attributes
h1attrs = h1strain.attrs
gpstime = h1attrs['Xstart'] + h1attrs['Xspacing'] * np.arange(h1attrs['Npoints'])

# define a window around the event
tevent = eventdict['GPS']
around = (gpstime > tevent - 0.1) & (gpstime < tevent + 0.1)

# plot the time series together, reversing L1; add a descriptive title
pp.figure(figsize=(12,3))
pp.plot(gpstime[around] - tevent,  whiten(h1strain)[around])
pp.plot(gpstime[around] - tevent, -whiten(l1strain)[around])
pp.title(f"{args.id}: {eventdict['mass_1_source']} + {eventdict['mass_2_source']} Msun")

# save to a PNG image file
pp.savefig(os.path.join(args.C, args.id + '.png'))
