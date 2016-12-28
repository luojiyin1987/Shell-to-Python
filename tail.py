with open("test.txt") as f:
    line = f.readline()
    while line:
        print line
        line = f.readline()
