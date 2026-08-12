#file handling

f=open("C:\\Users\\Gokul\\OneDrive\\Desktop\\Suii\\index.txt","r")    # "r" mode of operation 
# inside open the first argument is the file path, second argument is the model of operation

# x=f.read()
# print(x)  # full contents

# a=f.readline()   # only one line 
# print(a)
# b=f.readline()
# print(b)

c=f.readlines()
print(c)    #['Suuuuuiiiiiii\n', 'meeesssiiiiii\n', 'kylian dictator']  give as a list