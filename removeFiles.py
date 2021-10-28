import os
import shutil
import time


def main():
    deletedFolderCount = 0
    deletedFileCount = 0
    path = "Path to Delete"
    days = 30
    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):
        for rootFolder, folders, files in os.walk(path):
            if seconds >= getFileOrFolder(rootFolder):
                removeFolder(rootFolder)
                deletedFolderCount += 1
                break
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolder, folder)
                    if seconds >= getFileOrFolder(folderPath):
                        removeFolder(folderPath)
                        deletedFolderCount += 1
                for file in files:
                    filePath = os.path.join(rootFolder, file)
                    if seconds >= getFileOrFolder(filePath):
                        removeFile(filePath)
                        deletedFileCount += 1
        else:
            if seconds >= getFileOrFolder(path):
                removeFile(path)
                deletedFileCount += 1
    else:
        print(f'"{path}" is not found')
        deletedFileCount += 1

    print(f"Total folders deleted: {deletedFolderCount}")
    print(f"Total files deleted: {deletedFileCount}")


def removeFolder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    else:
        print(f"Unable to delete the " + path)


def removeFile(path):
    if not os.remove(path):
        print(f"{path} is removed successfully")
    else:
        print("Unable to delete the " + path)


def getFileOrFolder(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()