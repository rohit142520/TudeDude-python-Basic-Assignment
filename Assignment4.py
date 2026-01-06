# read a file and handle exception(created by Rohit Gautam)
try:
    with open("file_1",'rt') as fh:
        for line in fh:
            print(line.strip())
except FileNotFoundError:
    print(f" The file which you trying to open does not exists.")
