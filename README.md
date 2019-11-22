# arbolitomics

This is a script meant to run off a Raspberry Pi connected to a LED strip to make it scroll colors according to a DNA sequence. I wrote it to make Xmas lights (displaying Pine DNA sequences).

The hardware setup is taken from this [tutorial](https://dordnung.de/raspberrypi-ledstrip/ws2812). As in that setup, the script uses the [rpi-ws281x-python](https://github.com/rpi-ws281x/rpi-ws281x-python) library.

Some TODOs:

- [ ] Add error-checking and other robustness methods.
- [ ] Add different viz modes (e.g. introns at lower brightness, start/stop codons flashing).
- [ ] Add on-screen preview mode.
- [ ] ...
