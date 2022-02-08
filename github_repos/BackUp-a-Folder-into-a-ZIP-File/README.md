# _BackUp-a-Folder-into-a-ZIP-File_

## ___About___
A simple python script to zip required folder.

Stores the snapshot of your work folder based on number of times you run this program

This creates a new Zip file with the same name and the snapshot number of the work folder

This is like creating git commits except that each time you create a new zip folder with the changes you made

Takes the folder path as the input and does the job for you😄😄

# ___Description___

## usage
    python zipFolder.py -p <folderPath> -se <True/False> -me <True/False>

  Arguemnts     | Description
:-------------: | -------------
-p              | Folder path that needs to be zipped, ex: F:\videos\web_dev (web_dev  folder need to be zipped)
-se             | boolean value (__*default value is True*__), this is to display files that caused error in zipping these files, these files are showed after the completion
-me             | boolean value (__*by default it copies the files to the error directory*__), this is to **move** the files to the error folder if these files are creating error while zipping them

**If there is any error in zipping the files, then a new folder under the name "Error-in-Zipping-Files" is created in the parent directory and the files are moved to this folder**

# _Modules Used_ 

- [os](https://docs.python.org/3/library/os.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [zipfile](https://docs.python.org/3/library/zipfile.html)
- [argparse](https://docs.python.org/3/library/argparse.html)

# **_Happy Learning_**
