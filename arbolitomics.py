#!/usr/bin/env python3
#
# Arbolitomics: Script to drive a LED-Strip to light up
# according to a DNA sequence.
#
# Author: Wladimir Labeikovsky (wladimir.labeikovsky@cuanschutz.edu)
#
# Hardware setup cribbed from https://dordnung.de/raspberrypi-ledstrip/ws2812
# Software setup cribbed from https://github.com/rpi-ws281x/rpi-ws281x-python
#
# First idea was to read off the complete genomic sequence of the Xmas Tree (Picea abies)
# https://www.ncbi.nlm.nih.gov/genome/11155?genome_assembly_id=367163
#
# For this prototype we'll content ourselves with the sequence of its chloroplast genome
# https://www.ncbi.nlm.nih.gov/nuccore/NC_021456.1
#
# Steps:
# - Downloaded FASTA file from NCBI (sequence.fasta)
# - Remove header line from FASTA file
# - Run the awk command below to remove newlines:
#   awk '/^>/ { print (NR==1 ? "" : RS) $0; next } { printf "%s", $0 } END { printf RS }' sequence.fasta > dna.fasta
#

# Libraries
import time
import argparse
from rpi_ws281x import PixelStrip, Color

# LED Strip Configuration
# Model used: AL-WS2812B-150BK-WP
LED_COUNT = 150       # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create LED Strip Object
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

# Function to clear strip
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

# Testing addresing
sequence = "CTGTGGTGTGCACGCACACAGAGACCAGGGGTCAACCTTAGGTCTTGTTCCAAAGAGCTGTTACCTTGCATTCTTTCTAAATTATGTCGGTTCTCCGGTGAGTTTTTACAGGTAGATAATACATTCTGGTTACCTTCTTCCCAGCAGTAC"

A_color = [0,0,255] # Blue for Adenine
T_color = [255,255,0] # Yellow for Thymine
G_color = [0,255,0] # Green for Guanine
C_color = [255,0,0] # Red for Cytosine

# Main loop
strip.begin() # Make sure to call before other functions
for n in range(LED_COUNT):
    if sequence[n]=='A':
        strip.setPixelColor(n, Color(A_color[0],A_color[1],A_color[2]))
    elif sequence[n]=='T':
        strip.setPixelColor(n, Color(T_color[0],T_color[1],T_color[2]))
    elif sequence[n]=='G':
        strip.setPixelColor(n, Color(G_color[0],G_color[1],G_color[2]))
    elif sequence[n]=='C':
        strip.setPixelColor(n, Color(C_color[0],C_color[1],C_color[2]))
strip.show()

input("Press any key to clean and quit")
colorWipe(strip,Color(0,0,0),10)
        
