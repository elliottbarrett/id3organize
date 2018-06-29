# id3organize
Python utility for organizing MP3s from their metadata

Usage: python id3organize.py input_root output_root

MP3s in input_root and its subdirectories will be moved to directories in 
output_root according to the following scheme

Source: input_root/[...subdirectories]/somefile.mp3
Destination: output_root/artist_name/album_name/somefile.mp3

Note that empty subdirectories from input_root will not be removed.
