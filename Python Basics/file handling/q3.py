# f=open("C:\\Users\\Gokul\\OneDrive\\Desktop\\Suii\\index2.pdf","x") # "x" - creating a new file

try:
    f=open("C:\\Users\\Gokul\\OneDrive\\Desktop\\Suii\\index3.pdf","x")
    print("file created")
except FileExistsError:
    print("file already exist")
