'''
Write A Python Program To Check Extension Of A File, 
If File Extension Is “.mp3” Then Display A Message. 
“This File Is Not Allowed”
'''
import os

def check_file_extension(file_path):
    file_extension = os.path.splitext(file_path)[1]
    if file_extension == ".mp3":
        print("This file is not allowed.")
    else:
        print("File extension is allowed.")

if __name__=="__main__":
    file_path = "path/to/file.mp3"
    check_file_extension(file_path)
