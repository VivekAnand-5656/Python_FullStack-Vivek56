f = open("myfile.txt")

# lines = f.readlines()
# print(type(lines))
# print(lines)

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()


f.close()

# ------- Please Write here all methods of file handling --------
