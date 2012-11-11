wooden-fish
===========

One strike, one step. Creates audio files for walking meditation.

A no-frills script, currently less than fifty lines. The script uses a short file containing one strike of a wooden fish (onestrike.wav), a file containing only silence (generated as follows: ffmpeg -f lavfi -i aevalsrc="0::d=60" silence60s.wav), and a short file containing two strikes in rapid succession (twostrikes.wav). The script relies on the sox (http://sox.sourceforge.net/) and ffmpeg (http://ffmpeg.org/) utilities.

An example output is provided: a generated sequence of strike interarrival times 4 sec apart on average, until approximately 300 sec have passed, ending with two strikes in rapid succession. The mean interarrival time and total duration are the free parameters. To avoid anticipation of strikes during the walking meditation, strikes are varied about the mean interarrival time according to an Irwin-Hall distribution that approximates a normal distribution but crucially has zero probability at absolute distance equal to the mean interarrival time.
