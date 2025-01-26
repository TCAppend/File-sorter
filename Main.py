import os, shutil

folder_names = ['IMAGE files', 'VIDEO files', 'MP3 files', 'GIF files']

def Scanner():
    for loop in range(0,4):
        if not os.path.exists(path_sorted + folder_names[loop]):
            print(path_sorted + folder_names[loop])
            os.makedirs((path_sorted + folder_names[loop]))
            
        

def File_creation():
    for file in file_name:
        if ".mp3" in file and not os.path.exists(path_sorted + "/MP3 files/" +  file):
            shutil.move(path_sorted + file, path_sorted + "/MP3 files/" +  file)
        if ".png" in file and not os.path.exists(path_sorted + "/IMAGE files/" + file):
            shutil.move(path_sorted + file, path_sorted + "/IMAGE files/" +  file)
        if ".mp4" in file and not os.path.exists(path_sorted + "/VIDEO files/" + file):
            shutil.move(path_sorted + file, path_sorted + "/VIDEO files/" +  file)
        if ".webp" in file and not os.path.exists(path_sorted + "/VIDEO files/" + file):
            shutil.move(path_sorted + file, path_sorted + "/VIDEO files/" +  file)
        if ".gif" in file and not os.path.exists(path_sorted + "/GIF files/" + file):
            shutil.move(path_sorted + file, path_sorted + "/GIF files/" +  file)
        if ".jpeg" in file and not os.path.exists(path_sorted + "/IMAGE files/" + file):
            shutil.move(path_sorted + file, path_sorted + "/IMAGE files/" +  file)
        if ".jpg" in file and not os.path.exists(path_sorted + "/IMAGE files/" + file):
            shutil.move(path_sorted + file, path_sorted + "/IMAGE files/" +  file)



try:
    print('Tc'''+'s Totally original file sorter')
    print('Just place the address by copying and pasting it here')
    print('NOTE: if youre going to sort an outside local disk, you should place "/" at the end, otherwise it wont work....')
    Filedirectory = input('Input file directory: ')
    #replace 'Filedirectory' to your prefered address here if you wanna do it manually(dont forget to include '\' in the end of the link)
    path_sorted = Filedirectory 
    file_name = os.listdir(path_sorted)
    Scanner()
    File_creation()
except:
    print('Error, Didnt sort the files.... please insert the appropriate syntax(like actually reading the NOTE)')