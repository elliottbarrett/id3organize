import os
import sys
import eyed3


HOME_DIR = os.path.expanduser("~")
TEST_INPUT_PATH = HOME_DIR + "/Downloads/"
TEST_OUTPUT_PATH = HOME_DIR + "/Music/"

USAGE_MESSAGE = """id3organize.py - recursively organize mp3s based on id3 metadata

  Usage: python id3organize.py input_root output_root

  MP3s in input_root and its subdirectories will be moved to directories in 
  output_root according to the following scheme

  Source: input_root/[...subdirectories]/somefile.mp3
  Destination: output_root/artist_name/album_name/somefile.mp3
"""
SHORT_HELP_MESSAGE = "Run `python id3organize.py -h` for more info"

def move_mp3(path, filename, output_root):
    source_filepath = path + "/" + filename
    audiofile = eyed3.load(source_filepath)
    
    artist_dir = output_root + audiofile.tag.artist
    album_dir = artist_dir + "/" + audiofile.tag.album
    dest_filepath = album_dir + "/" + filename
    
    if not os.path.exists(artist_dir):
        os.makedirs(artist_dir)

    if not os.path.exists(album_dir):
        os.makedirs(album_dir)

    os.rename(source_filepath, dest_filepath)

def organize_library(input_root, output_root):
    for path, directories, files in os.walk(input_root):
        for file in files:
            if file.endswith(".mp3"):
                move_mp3(path, file, output_root)

# Main program
arguments = sys.argv

if len(arguments) == 2 and arguments[1] in ['-h', '-H']:
    print USAGE_MESSAGE
    sys.exit()

if len(arguments) < 3:
    print "An input and output directory must be supplied."
    print "Run `python id3organize.py -h` for more info"
    sys.exit()

input_root = arguments[1]
output_root = arguments[2]

if not input_root.endswith("/"):
    input_root = input_root + "/"

if not output_root.endswith("/"):
    output_root = output_root + "/"

if not os.path.isdir(input_root):
    print "Error: input root " + input_root + " is not a directory"
    print SHORT_HELP_MESSAGE
    sys.exit()

if not os.path.isdir(output_root):
    print "Error: output root " + output_root + " is not a directory"
    print SHORT_HELP_MESSAGE
    sys.exit()

eyed3.log.setLevel("ERROR")
print "Organizing library, this may take a minute"
organize_library(input_root, output_root)
print "Done!"