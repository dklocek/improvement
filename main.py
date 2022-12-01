import os
import sys

def exiting(exit_number):
    exit_message_list = [
        "Sorry too much files, max 5 files allowed \
        \n Usage: pycat file1 \n pycat file1 file2  \
        \n ... \
        \n pycat file1 file 2 file3 file4 file5",
        "At least one file doesn't exist or to less permissions. Exiting...."
    ]
    exit(exit_message_list[exit_number])

def verify_and_prepare_paths():
    if len(sys.argv) > 6:
        exiting(0)

    file_paths = []    

    for i in range(1, len(sys.argv)):
        if not os.path.isfile(sys.argv[i]):
            print(sys.argv[i], "doesn't exist")
            exiting(1)
        else:
            file_paths.append(sys.argv[i])

    return file_paths

def cat():
    file_paths = verify_and_prepare_paths()

    for path in file_paths:
        with open(path, 'r') as file:
            for line in file:
                print(line.strip())
    exit()

if __name__ == "__main__":
    cat()    
