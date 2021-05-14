import os
import shutil

# Create the dirs in case they don't exist
def Create_Dirs_If_Neccesary(Dir, Dirs: list):
    for i in range(len(Dirs)):
     if not os.path.exists(Dir + Dirs[i]):
        os.mkdir(Dir + Dirs[i])

# Order the files in the download dir. In Every loop iteration the function cheks if the file extension is in the extension list.
# If it's found it will move the file to the corresponding dir within the download dir, otherwise the files will go to the "OTHERS" dir
def Order_Files_In_Dir(Files: list, Dir, Dirs: list, Extensions: list):
  for file in Files:
    extension = os.path.splitext(file)
    FoundExtension = False
    for ext in range(len(Extensions)):
        if isinstance(Extensions[ext], list) and extension[1] in Extensions[ext]:
                    shutil.move(Dir+file, Dir+Dirs[ext], copy_function=shutil.copy2)
                    FoundExtension = True
                    break
        elif Extensions[ext] == extension[1]:
            shutil.move(Dir+file, Dir+Dirs[ext], copy_function=shutil.copy2)
            FoundExtension = True
            break
    if not FoundExtension and os.path.isfile(Dir+file):
        shutil.move(Dir+file, Dir+Dirs[11], copy_function=shutil.copy2)

Extensions = [
              [".jpg", ".jpeg", ".png", ".ico", ".gif"],
              ".pdf", 
              [".docx", ".doc"], 
              ".pptx", 
              [".mp3", ".ogg"], 
              ".mp4", 
              [".exe", ".msi"], 
              [".rar", ".zip"], 
              ".xlsx",
              ".txt",
              ".html",
              ]

# These will be the new dirs in which the files will be organized
DirNames = ["IMAGES", 
            "PDF", 
            "WORD", 
            "POWER POINT", 
            "AUDIO Mp3", 
            "VIDEOS", 
            ".EXE FILES", 
            "COMPRESSED FILES",
            "EXCEL",
            "TEXT FILES",
            "WEB SITES",
            "OTHERS"
            ]

Dir = r"C:/Users/HP/Downloads/"
Files = os.listdir(r"C:/Users/HP/Downloads")
Create_Dirs_If_Neccesary(Dir, DirNames)
Order_Files_In_Dir(Files, Dir, DirNames, Extensions)