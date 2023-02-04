import os
import shutil

source = r"C:\Users\Sehran Khatib\Downloads\project 112"
destination = r"C:\Users\Sehran Khatib\Downloads\project 112\documents"

list_of_files = os.listdir(source)
print(list_of_files)

# Move All Image files from Main Folder to Another Folder
for x in list_of_files:

    name, extension = os.path.splitext(x)
    print(name)
    print(extension)

    if extension == '':
        continue
    if extension in ['.ppt', '.docx', '.pdf', '.txt']:

        path1 = source + '/' + x                              
        path2 = destination + '/'                            
        path3 = destination + '/' +  x 
        
        print("path1 " , path1)
        print("path2 " , path2)
        print("path3 ", path3)

        # Check if Folder/Directory Path Exists Before Moving
        # Else make a NEW Folder/Directory Then Move
        if os.path.exists(path2):
          print("Moving " + x + ".....")
          shutil.move(path1, path3)

        else:
          os.mkdir(path2)
          print("Moving " + x + ".....")
          shutil.move(path1, path3)