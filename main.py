import os
os.chdir("C:\\study\\voice")
path = os.getcwd()
print(path)
from datetime import datetime
from mutagen.mp3 import MP3

def get_day_of_week(date_str):
    try:
        date = datetime.strptime(date_str, '%y%m%d')
        day_of_week = date.weekday()
        days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        return days_of_week[day_of_week]
    except ValueError:
        return "Invalid date format"

files = os.listdir(path)
files = [f for f in files if os.path.isfile(path+'/'+f)] #Filtering only the files.

for file in files:
    start_indsex = file.index("_") + 1
    date_string = file[start_indsex : start_indsex + 6]
    dayOfWeek = get_day_of_week(date_string)
    date_folder = path +  "\\" + date_string + "_" + dayOfWeek
    
    if not os.path.exists(date_folder):
        os.mkdir(date_folder)
    source_file = path + "\\" + file

    duration = MP3(source_file)
    if duration.info.length > 1:  # 4 seconds ONLY minimum
        end_path = date_folder

    dest_file = end_path + "\\" + file[2:-7]
    dest_file += str(int(duration.info.length/60 + 0.5))    + file[-4:]
    print("moving " + path + "\\" + file + " to " + dest_file )
    os.rename(path + "\\" + file, dest_file)
