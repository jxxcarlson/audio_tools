# The simplest possible way to generate sound waveformes
# programmatically and store them in a `.wav` file.
#
# SOURCE: https://pypi.org/project/wavio/
#
# You will need to run `pip install wavio` first.
# Then tun `python gen_sound.py` to produce the file `sine.wav`
# On Mac OS, you can run `afplay sine.wav` to listen to the sound.

import numpy as np
import wavio
import time

rate = 44100  # samples per second
T = 3         # sample duration (seconds)
f = 440.0     # sound frequency (Hz)

# t = array of sample times
t = np.linspace(0, T, T*rate, endpoint=False)

# x = array of samples
# Measure the time needed to compute the samples.
start = time.time()
x = np.sin(2*np.pi * f * t)
end = time.time()
print "Sample construction time: ", (end - start)*1000, "ms"


# Measure the time needed to write the file.
start = time.time()
wavio.write("sine.wav", x, rate, sampwidth=3)
end = time.time()
print "File write time: ", (end - start)*1000, "ms"
