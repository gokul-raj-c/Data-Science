try:
    f=open("C:\\Users\\Gokul\\OneDrive\\Desktop\\Suii\\index.txt","r")
    x=f.read()
    print(x)
except FileNotFoundError:
    print("file not found")
