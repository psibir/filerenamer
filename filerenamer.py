
# rename multiple files in a directory or folder
# Warning: this script will rename all files in the directory

import os

def warn():
    input("This script will rename all files in the directory.\nPress any key to continue...")

def main():
    # get the path of the directory
    folder = input("Enter the absolute path of the directory containing the files you wish to rename: \n")
    new_base = input("Enter the desired file name base: ")
    count = 0
    for filename in os.listdir(folder):
        ext = os.path.splitext(filename)[1]
        newname = new_base + str(count) + ext
        oldname = os.path.join(folder, filename)
        newname = os.path.join(folder, newname)
        os.rename(oldname, newname)
        count += 1

warn()

if __name__ == '__main__':
    main()


