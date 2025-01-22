import os, shutil

pathinput = input('Input file: ')

path = (r"{pathinput}")

file_name = os.listdir(path)

folder_names = ['PNG files', 'MP4 files', 'MP3 files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs((path + folder_names[loop]))


for file in file_name:
    if ".mp3" in file and not os.path.exists(path + "/MP3 files/" +  file):
        shutil.move(path + file, path + "/MP3 files/" +  file)
    if ".png" in file and not os.path.exists(path + "/PNG files/" + file):
        shutil.move(path + file, path + "/PNG files/" +  file)
    if ".mp4" in file and not os.path.exists(path + "/MP4 files/" + file):
        shutil.move(path + file, path + "/MP4 files/" +  file)

else:
    print("Some files didn't move")