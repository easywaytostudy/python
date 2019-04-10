import os

class fileHandling:
    def __init__(self):
        f = open("demofile.txt", "w")
        f.write("Woops! I have deleted the content!")
        f.close()

    def __del__(self):
        if os.path.exists("demofile.txt"):
            os.remove("demofile.txt")
        else:
            print("The file does not exits")

    #########################################
    #       Python File Handling            #
    #########################################

    # File handling is an important part of any application.
    # Python has several functions for creating, reading, updating, and deleteing files.


    # Open a File
    # The key function for working with files in Python is the open() function.

    # The open() function takes two parameters; filename, and mode.

    # There are four different methods (modes) for opening a file:

    # r - Read - Default value. Opens a file for reading, error if the file does not exist
    # a - Append - Opens a file for appending, creates the file if it does not exist
    # w - Write - Opens a file for writing, creates the file if it does not exist
    # x - Create - Creates the specified file, returns an error if the file exist
    # In addition you can specify if the file should be handled as binary or text mode:

    # t- Text - Default value. Text mode
    # b - Binary - Binary mode (e.g. images)

    ############  open a file  ############

    # To open a file for reading it is enough to specify the name of the file:
    def open_file(self):
        file = open('demofile.txt')
        # The code above is the same as:
        file = open('demofile.txt', 'rt')

    # Because r for read, and t for text are the default values, you do not need to specify them.
    # Note: Make sure the file exist, or else you will get an error.

    ############  Read a File  ############

    # The read() method is used to read files.
    # Before read a file you must open it using open() function.
    def read_file(self):
        f = open("demofile.txt", "r")
        print(f.read())
        f.close()

    ############  Read Only Parts of the File  ############

    # By default the read() method returns the whole text, but you can also specify how many character you want to return:
    def read_only_part_of_the_file(self):
        f = open("demofile.txt", "r")
        print(f.read(12))
        f.close()


    ############  Read Lines  ############

    # You can return one line by using the readline() method:
    def read_lines(self):
        f = open("new.py", "r")
        print(f.readline())
        print(f.readline())
        f.close()
    # By calling readline() two times, you can read the two first lines.


    ############  Write File  ############

    # To write to an existing file, you must add a parameter to the open() function:

    # a - Append - will append to the end of the file
    # w - Write - will overwrite any existing content

    def append_data(self):
        f = open("demofile.txt", "a")
        f.write("Now the file has one more line!")
        f.close()

    # The w method will overwrite the entire file.


    ############  Delete Files  ############
    # To delete a file, you must import the OS module, and run its os.remove() function:


    def remove_file(self):
        if os.path.exists("demofile.txt"):
            os.remove("demofile.txt")
        else:
            print("The file does not exits")


if __name__ == '__main__':
    file = fileHandling()                     # write/create a file(__init__)
    # file.open_file()                        # open a file
    # file.read_file()                        # read a file
    # file.read_only_part_of_the_file()       # read only part of the file
    # file.read_lines()                       # read some lines of the file
    # file.append_data()                      # append the data in a file
    # file.remove_file()                      # remove file if exists
