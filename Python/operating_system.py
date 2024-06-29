import os

print(f"\n directory is: {os.getcwd()} \n")  # CWD stands for "Current Working Directory"

os.chdir("/Users/sohail/desktop/")  # ch(change) dir(directory)

print(f"\n directory is: {os.getcwd()} \n")
print(os.listdir("/Users/sohail/python/"))  # lists the files in the directory. Default directory is current directory

os.mkdir("Python is back")                        # Creates a new directory
os.mkdir("Testing")
os.mkdir("C++")
os.makedirs("My new battery/new laptop battery")  # Same as "mkdir" but can also create sub-directories
os.makedirs("My new battery/battery testing")

os.rmdir("Testing")                               # Removes the directory
os.rmdir("Python is back")
os.removedirs("My new battery/new laptop battery") 
os.removedirs("My new battery/battery testing")   # Same as "rmdir" but can specifically remove any sub-directories

os.rename("C++", "Best AI lang Python")           # Used to rename a dir with actual name as 1st arg and new name is 2nd arg
os.rmdir("Best AI lang Python")

print(os.stat("/Users/sohail/python/graph.py"))   # Used to look at info of the file
print(os.stat("/Users/sohail/python/graph.py").st_size)

""" If we want to see the entire dir tree and files within the dir, then we can use "os.walk()". It is a generator that yields a tuple
of 3 values as it is walking the dir tree , so for each dir that it sees, it yields the dir path, the dirs within that path and the files
within that path"""

for path, directory, file in os.walk("/Users/sohail/python"):
    print(f"Current path is: {path}")
    print(f"Directories: {directory}")
    print(f"Files: {file}\n")

for key, value in enumerate(os.environ, start=1):  # os.environ returns a dictionary of environment variables 
    print(key, value)

print(os.environ.get("Pycharm")) # Returns the value(i.e. path) of the key provided

# It is very error prone to concatenate paths, here is what we can do

file_path = os.path.join(os.environ.get("Pycharm"), "test.txt")  # It joins both the paths
print(file_path)

print(os.path.basename("YASIN/WAQAS ACCOUNT"))                    # Returns the base name
print(os.path.dirname("YASIN/WAQAS ACCOUNT"))                     # Returns the dir name
print(os.path.split("Test folder/testing"))                       # Returns a tuple of directory name and file name
print(os.path.exists("Test folder/testing"))                      # Returns True if the path provided exists
print(os.path.isdir("Test folder"))                               # Returns True if the provided path is a directory
print(os.path.isfile("Test folder/testing/spacewallpaper.jpg"))   # Returns True if the provided path is a file
print(os.path.splitext("Test folder/testing/spacewallpaper.jpg")) # Returns a tuple of path of file and its extension
