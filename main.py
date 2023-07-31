import os
os.chdir("C:\\study\\voice")
path = os.getcwd()
print(path)
import mutagen
from mutagen.mp3 import MP3

files = os.listdir(path)
files = [f for f in files if os.path.isfile(path+'/'+f)] #Filtering only the files.
tmp_folder = path + "\\tmp"
if not os.path.exists( tmp_folder ):
    os.mkdir( tmp_folder )

for file in files:
    start_indsex = file.index("_") + 1
    date_string = file[start_indsex : start_indsex + 6]
    date_folder = path +  "\\" + date_string
    if not os.path.exists(date_folder):
        os.mkdir(date_folder)
    source_file = path + "\\" + file

    duration = MP3(source_file)
    if duration.info.length > 40:
        end_path = date_folder
    else:
        end_path = tmp_folder
        
    dest_file = end_path + "\\" + file[2:-7]
    dest_file += str(int(duration.info.length/60 + 0.5))    + file[-4:]
    print("mvoing " + path + "\\" + file + " to " + dest_file )
    os.rename(path + "\\" + file, dest_file)
