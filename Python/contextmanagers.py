from contextlib import contextmanager

class File():
    def __init__(self, filename, method):

        self.file = open(filename, method)

    def __enter__(self):

        print("Entering")
        return self.file

    def __exit__(self, type, value, traceback):

        print(f"{type}, {value}, {traceback}")
        print("Exiting")
        self.file.close()
        if type == Exception:
            return True

with File("abc.txt", "w") as f:
    f.write("hello")
    
#############################################################

@contextmanager
def file(filename, method):
    print("Entering")
    file = open(filename, method)
    yield file
    file.close()
    print("Exiting")

with file("text.txt", "w") as f:

    print("Middle")
    f.write("hello")
    raise Exception






