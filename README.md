# id3organize
Python utility for organizing MP3s from their metadata

### Usage 
id3organize uses [eyed3](https://github.com/nicfit/eyeD3) to read ID3 tags.

Run `pip install eyed3` first

Then run `python id3organize.py input_root output_root`

### Notes
MP3s in `input_root` and its subdirectories will be moved to directories in `output_root` according to the following scheme:

Source: `input_root/[...subdirectories]/somefile.mp3`

Destination: `output_root/artist_name/album_name/somefile.mp3`

Note that empty subdirectories from input_root will not be removed.
