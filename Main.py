import os, shutil

pathinput1 = input('Input file directory: ')


path = pathinput1 + '/'

file_name = os.listdir(path)

folder_names = ['IMAGE files', 'MP4 files', 'MP3 files', 'GIF files']

for loop in range(0,4):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs((path + folder_names[loop]))


for file in file_name:
    if ".mp3" in file and not os.path.exists(path + "/MP3 files/" +  file):
        shutil.move(path + file, path + "/MP3 files/" +  file)
    if ".png" in file and not os.path.exists(path + "/IMAGE files/" + file):
        shutil.move(path + file, path + "/IMAGE files/" +  file)
    if ".mp4" in file and not os.path.exists(path + "/MP4 files/" + file):
        shutil.move(path + file, path + "/MP4 files/" +  file)
    if ".gif" in file and not os.path.exists(path + "/GIF files/" + file):
        shutil.move(path + file, path + "/GIF files/" +  file)
    if ".jpeg" in file and not os.path.exists(path + "/IMAGE files/" + file):
        shutil.move(path + file, path + "/IMAGE files/" +  file)
    if ".jpg" in file and not os.path.exists(path + "/IMAGE files/" + file):
        shutil.move(path + file, path + "/IMAGE files/" +  file)
    

else:
    print("Some files didn't move")