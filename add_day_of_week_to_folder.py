import os
os.chdir("C:\\study\\voice")
#os.chdir("C:\\Users\\user\\Google Drive\\re\\ining")
path = os.getcwd()
from datetime import datetime
def get_day_of_week(date_str):
    try:
        if len(date_str) != 8 or not date_str.startswith('20'):
            raise ValueError("Invalid date format")
        date = datetime.strptime(date_str, '%Y%m%d')
        day_of_week = date.weekday()
        days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Satur', 'Sun']
        return days_of_week[day_of_week]
    except ValueError as e:
        return str(e)

files = os.listdir(path)
folders = [f for f in files if not os.path.isfile(path + '/' + f)]  # Filtering only the folders.

for folder in folders:
    date_string = folder
    dayOfWeek = get_day_of_week(date_string)
    new_folder = date_string + "_" + dayOfWeek
    os.rename(folder, new_folder)
