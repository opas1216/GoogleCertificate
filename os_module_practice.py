import os
import datetime

# os.remove("novel.txt")

print(os.path.exists("finished_masterpiece.txt"))
print(os.path.exists("sample.txt"))
print(os.path.getsize("sample.txt"))
print(os.path.getsize("guests.txt"))
print(os.path.getmtime("sample.txt"))
print(os.path.abspath("sample.txt"))
print(os.path.dirname(os.path.abspath("sample.txt")))
print(os.path.dirname("sample.txt"))
timestamp = os.path.getmtime("sample.txt")
print(datetime.datetime.fromtimestamp(timestamp))
print(os.getcwd())

if not os.path.exists("test"):
    os.makedirs("test")
    os.chdir("test")
    print("Current path = {}".format(os.path.abspath("test")))
    print("getcwd = {}".format(os.getcwd()))
else:
    print("Folder test already exist")
    print("Remove test folder")
    for delete_file in os.listdir("test"):
        print(f"File {delete_file}, abspath = {os.path.abspath(delete_file)}")
        os.remove(os.path.abspath(delete_file))
        print("Delete file {}".format(delete_file))
    os.rmdir("test")
    print("Generate a new folder named test")
    os.mkdir("test")
    print("change the current position to the directory test")
    os.chdir("test")
    print("The current position is {}".format(os.getcwd()))